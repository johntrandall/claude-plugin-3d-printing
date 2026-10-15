# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Finn Randall
"""Shared helpers for build123d part scripts.

Keeps the part scripts pure geometry: they define shapes, `cadlib` handles
export, reporting and preview.

Three functions:

    save(shape, "name")   -> writes out/name.stl and out/name.step
    render(shape, "name") -> writes name.png, a shaded multi-view sheet
    show(shape)           -> live preview in the ocp_vscode viewer, if running

`out/` is resolved relative to the *calling part script*, so each project
folder keeps its own exports next to its own sources.

STL is what BambuStudio slices. STEP is the editable CAD original -- keep it,
it is the only lossless record of the geometry.
"""

from __future__ import annotations

import sys
from pathlib import Path

from build123d import export_step, export_stl

__all__ = ["save", "render", "show", "FILAMENT_DENSITY", "DEFAULT_MATERIAL"]

# Filament densities in g/cm^3, used only for the rough mass estimate.
FILAMENT_DENSITY = {
    "PLA": 1.24,
    "PETG": 1.27,
    "ABS": 1.04,
    "ASA": 1.07,
    "TPU": 1.21,
}

# PETG by default: PLA is brittle in flexure, which matters for spring clips.
DEFAULT_MATERIAL = "PETG"

# Mesh quality for the STL. Smaller tolerance = finer facets = bigger file.
# 0.01 mm is well below what an 0.4 mm nozzle can resolve.
DEFAULT_TOLERANCE = 0.01
DEFAULT_ANGULAR_TOLERANCE = 0.1

# Views for render(). Each is (label, direction-toward-camera, up-vector).
# Bottom is in the list on purpose: on a part that mates with something, the
# underside is where the geometry that matters usually lives.
#
# "top" and "bottom" are deliberately tilted about 20 deg off the axis rather
# than being true orthographic plan views. Flat shading gives coplanar faces
# the same tone regardless of height, so a feature raised proud of a flat
# face -- an index arrow on a knob lid, a boss, an embossed rib -- vanishes
# completely when viewed straight down. The tilt is enough for its side walls
# to catch the light and for the eye to read the step.
DEFAULT_VIEWS = (
    ("iso", (1.0, -1.1, 0.75), (0.0, 0.0, 1.0)),
    ("front", (0.0, -1.0, 0.05), (0.0, 0.0, 1.0)),
    ("top", (0.22, -0.38, 1.0), (0.0, 1.0, 0.0)),
    ("bottom", (0.22, -0.38, -1.0), (0.0, 1.0, 0.0)),
)

RENDER_COLOR = (214, 222, 232)

# Depth-edge outlining. EDGE_THRESHOLD is a fraction of the model's depth
# along the view axis, so it does not need retuning per part.
EDGE_THRESHOLD = 0.02
EDGE_DARKEN = 0.55


def _caller_dir(depth: int = 2) -> Path:
    """Directory of the script that called into cadlib.

    Walks up the stack past cadlib's own frames so `out/` lands next to the
    part script, not next to this file. Falls back to the current working
    directory when there is no `__file__` (REPL, `python -c`, notebooks).
    """
    frame = sys._getframe(0)
    here = Path(__file__).resolve()
    for _ in range(depth + 8):
        frame = frame.f_back
        if frame is None:
            break
        caller_file = frame.f_globals.get("__file__")
        if not caller_file:
            continue
        path = Path(caller_file).resolve()
        if path != here:
            return path.parent
    return Path.cwd().resolve()


def save(
    shape,
    name: str,
    *,
    material: str = DEFAULT_MATERIAL,
    tolerance: float = DEFAULT_TOLERANCE,
    angular_tolerance: float = DEFAULT_ANGULAR_TOLERANCE,
    out_dir: Path | str | None = None,
):
    """Export `shape` as STL and STEP into `out/` beside the calling script.

    Pass `out_dir` to put them somewhere else -- `out_dir="."` drops them
    straight beside the part script, which is what you want for a small
    project where one folder holding notes, source, renders and STLs beats
    a tidier tree you have to click through to slice something.

    Prints the bounding box (mm), the solid volume (cm^3) and a rough solid
    mass (g). Returns `shape` so calls can be chained.
    """
    base = _caller_dir()
    out_dir = base / "out" if out_dir is None else (base / out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    stl_path = out_dir / f"{name}.stl"
    step_path = out_dir / f"{name}.step"

    export_stl(
        shape,
        str(stl_path),
        tolerance=tolerance,
        angular_tolerance=angular_tolerance,
    )
    export_step(shape, str(step_path))

    bbox = shape.bounding_box()
    size = bbox.size
    volume_cm3 = shape.volume / 1000.0  # build123d volumes are mm^3

    key = material.upper()
    density = FILAMENT_DENSITY.get(key)

    print(f"[{name}]")
    print(f"  bounding box : {size.X:.2f} x {size.Y:.2f} x {size.Z:.2f} mm")
    print(f"  volume       : {volume_cm3:.2f} cm^3")
    if density is None:
        known = ", ".join(sorted(FILAMENT_DENSITY))
        print(f"  mass         : unknown material {material!r} (known: {known})")
    else:
        print(
            f"  mass (solid) : {volume_cm3 * density:.1f} g "
            f"in {key} @ {density} g/cm^3"
        )
        print("                 solid figure only -- infill makes the real print lighter")
    print(f"  stl          : {stl_path}")
    print(f"  step         : {step_path}")

    return shape


def render(
    shape,
    name: str,
    *,
    views=DEFAULT_VIEWS,
    size: int = 640,
    out_dir: Path | None = None,
    tolerance: float = DEFAULT_TOLERANCE,
    angular_tolerance: float = DEFAULT_ANGULAR_TOLERANCE,
):
    """Write `name.png`, a shaded multi-view contact sheet of `shape`.

    A still image you can look at without a viewer running -- the point is to
    catch a geometry mistake before it becomes a print. Writes next to the
    calling script by default, so the image sits beside the notes and Obsidian
    can embed it; pass `out_dir` to put it elsewhere.

    Needs numpy and pillow, both of which come in with build123d's stack.
    Returns the path written, or None if it could not render.

    Deliberately tiny: it tessellates the shape, culls backfaces, and paints
    the triangles far-to-near with one flat tone each. No z-buffer, so
    interpenetrating geometry can flicker -- irrelevant for a watertight
    solid, which is all we ever hand it.
    """
    try:
        import numpy as np
        from PIL import Image, ImageDraw
    except ImportError:
        print("note: numpy/pillow not installed -- skipping render")
        return None

    tris = _triangles(shape, tolerance, angular_tolerance)
    if tris is None or len(tris) == 0:
        print("note: nothing to render")
        return None

    panels = [
        _shade(tris, direction, up, size, np, Image, ImageDraw)
        for _, direction, up in views
    ]
    sheet = Image.new("RGB", (size * len(panels), size), "white")
    for i, panel in enumerate(panels):
        sheet.paste(panel, (i * size, 0))

    target = (out_dir or _caller_dir()) / f"{name}.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target)

    labels = ", ".join(v[0] for v in views)
    print(f"  render       : {target}  ({labels}; {len(tris)} tris)")
    return target


def _triangles(shape, tolerance, angular_tolerance):
    """Tessellate `shape` into an (n, 3, 3) array of triangle vertices."""
    import numpy as np

    from build123d import export_stl

    # Going through a temp STL rather than poking at OCCT's triangulation
    # API keeps this working across build123d versions, and costs nothing
    # at these mesh sizes.
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "r.stl"
        export_stl(
            shape,
            str(path),
            tolerance=tolerance,
            angular_tolerance=angular_tolerance,
        )
        data = path.read_bytes()

    if data[:5] == b"solid" and b"facet" in data[:2000]:  # ASCII STL
        verts, cur = [], []
        for line in data.decode("utf8", "ignore").splitlines():
            parts = line.strip().split()
            if parts[:1] == ["vertex"]:
                cur.append([float(v) for v in parts[1:4]])
                if len(cur) == 3:
                    verts.append(cur)
                    cur = []
        return np.array(verts, dtype=float)

    import struct

    count = struct.unpack("<I", data[80:84])[0]
    dt = np.dtype([("n", "<3f4"), ("v", "<3,3f4"), ("attr", "<u2")])
    arr = np.frombuffer(data[84 : 84 + count * 50], dtype=dt, count=count)
    return arr["v"].astype(float)


def _shade(tris, direction, up, size, np, Image, ImageDraw):
    """Paint one view into a size x size image.

    Rasterises into a real z-buffer and then outlines depth discontinuities.

    The outlining is not decoration. Flat shading colours a facet from its
    normal alone, so two surfaces that are parallel get the same tone no
    matter how far apart they are -- an index arrow standing 1.8 mm proud of
    a flat knob lid becomes literally invisible from above. No light rig
    fixes that, because the normals really are identical. Depth is the only
    thing that distinguishes them, so the depth buffer draws the edges.
    """
    d = np.array(direction, dtype=float)
    d /= np.linalg.norm(d)
    up = np.array(up, dtype=float)

    # Right-handed screen basis: right x up = d, i.e. d points at the viewer.
    # Build it the other way round and every render comes out MIRRORED, which
    # is near-invisible on a symmetric part -- engraved text is the only tell.
    right = np.cross(up, d)
    if np.linalg.norm(right) < 1e-9:  # looking straight along `up`
        up = np.array([0.0, 1.0, 0.0])
        right = np.cross(up, d)
    right /= np.linalg.norm(right)
    up = np.cross(d, right)

    basis = np.stack([right, up, d], axis=1)  # world -> camera
    cam = tris.reshape(-1, 3) @ basis
    lo, hi = cam.min(0), cam.max(0)
    centre = (lo + hi) / 2
    scale = size * 0.86 / max(hi[0] - lo[0], hi[1] - lo[1], 1e-9)
    cam = cam.reshape(-1, 3, 3)

    # Screen Y grows downward, hence the flip.
    xy = (cam[:, :, :2] - centre[:2]) * scale * np.array([1, -1]) + size / 2
    zs = cam[:, :, 2]

    normals = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
    lengths = np.linalg.norm(normals, axis=1)
    lengths[lengths == 0] = 1
    normals /= lengths[:, None]

    light = np.array([0.4, -0.6, 0.7])
    light /= np.linalg.norm(light)
    shade = 0.22 + 0.78 * np.abs(normals @ light)

    zbuf = np.full((size, size), -np.inf)
    sbuf = np.zeros((size, size))
    hit = np.zeros((size, size), dtype=bool)

    facing = normals @ d > 0  # backface cull
    for i in np.nonzero(facing)[0]:
        _raster(xy[i], zs[i], shade[i], zbuf, sbuf, hit, size, np)

    img_f = np.where(hit, sbuf, 0.0)

    # Outline depth discontinuities and the silhouette.
    #
    # Use the SECOND difference, not the first. A surface slanted away from
    # the camera has a large but constant depth gradient, so a first-
    # difference test paints every facet of every curved wall and the render
    # turns into scribble. The second difference is zero across any constant
    # slope and spikes only where the depth actually steps -- which is
    # exactly the raised-feature boundary we are trying to see.
    span = max(hi[2] - lo[2], 1e-9)
    z = np.where(hit, zbuf, np.nan)
    edge = np.zeros((size, size), dtype=bool)
    for ax in (0, 1):
        prev = np.roll(z, 1, axis=ax)
        nxt = np.roll(z, -1, axis=ax)
        lap = np.abs(2.0 * z - prev - nxt)
        edge |= np.nan_to_num(lap, nan=0.0) > span * EDGE_THRESHOLD
    for ax, sh in ((0, 1), (0, -1), (1, 1), (1, -1)):
        edge |= hit & ~np.roll(hit, sh, axis=ax)  # silhouette
    edge &= hit
    img_f = np.where(edge, img_f * EDGE_DARKEN, img_f)

    rgb = np.zeros((size, size, 3), dtype=np.uint8)
    for c in range(3):
        chan = np.where(hit, np.clip(img_f * RENDER_COLOR[c], 0, 255), 255)
        rgb[:, :, c] = chan.astype(np.uint8)
    return Image.fromarray(rgb, "RGB")


def _raster(pts, zs, tone, zbuf, sbuf, hit, size, np):
    """Z-buffered fill of one screen-space triangle."""
    x0 = max(int(np.floor(pts[:, 0].min())), 0)
    x1 = min(int(np.ceil(pts[:, 0].max())) + 1, size)
    y0 = max(int(np.floor(pts[:, 1].min())), 0)
    y1 = min(int(np.ceil(pts[:, 1].max())) + 1, size)
    if x1 <= x0 or y1 <= y0:
        return

    xx, yy = np.meshgrid(
        np.arange(x0, x1) + 0.5, np.arange(y0, y1) + 0.5, indexing="xy"
    )
    (ax, ay), (bx, by), (cx, cy) = pts
    area = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if abs(area) < 1e-12:
        return
    w0 = ((bx - ax) * (yy - ay) - (by - ay) * (xx - ax)) / area
    w1 = ((cx - bx) * (yy - by) - (cy - by) * (xx - bx)) / area
    w2 = 1.0 - w0 - w1
    inside = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
    if not inside.any():
        return

    # Match each weight to the vertex it belongs to. w0 is built from edge
    # A->B so it is the weight of C; w1 is built from B->C so it is the
    # weight of A; w2 is the remainder, the weight of B. Pair them up wrong
    # and depth is interpolated wrong inside every triangle -- which shows up
    # not as obviously broken geometry but as faint seams along the mesh,
    # easily misread as a tessellation artefact.
    z = w1 * zs[0] + w2 * zs[1] + w0 * zs[2]
    sub_z = zbuf[y0:y1, x0:x1]
    win = inside & (z > sub_z)
    if not win.any():
        return
    sub_z[win] = z[win]
    sbuf[y0:y1, x0:x1][win] = tone
    hit[y0:y1, x0:x1][win] = True


def show(shape):
    """Preview `shape` in the ocp_vscode viewer, if one is listening.

    Never raises: a missing package or a viewer that is not running is a
    normal, non-fatal condition when running a part script from a plain
    terminal. Returns True if the shape was handed to a viewer.
    """
    try:
        from ocp_vscode import show as _show

        _show(shape)
        return True
    except ImportError:
        print("note: ocp_vscode not installed -- skipping preview")
    except Exception as exc:  # viewer not running, port busy, etc.
        print(f"note: ocp_vscode viewer unavailable ({exc.__class__.__name__}) -- skipping preview")
    return False
