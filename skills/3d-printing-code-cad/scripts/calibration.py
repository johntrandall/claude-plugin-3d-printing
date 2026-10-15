# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Finn Randall
"""Printer calibration coupon -- measure this before designing any press-fit.

A flat plate carrying four through-holes at nominal 3, 4, 5 and 6 mm, each
labelled with engraved text. Corners are filleted and the top edge chamfered,
so the coupon also shows at a glance how your printer renders those features.

WHY
---
Printed holes always come out undersize. Extrusion width, the thin-wall
compensation in the slicer, and the die-swell of plastic around an inside
corner all eat into the bore. The error is roughly a constant diameter offset,
not a percentage, so one measurement covers every hole you will ever print on
this machine with this filament.

Every press-fit, boss, pin and screw clearance in the other projects depends on
that number. Guessing it costs a whole print each time you are wrong.

WHAT TO MEASURE AFTER PRINTING
------------------------------
1. Print one coupon flat on the bed, in the material you will actually use
   (default PETG), at the layer height and nozzle you will actually use. The
   number is per-material and per-profile -- PLA and PETG do not match.
2. Let it cool fully. Warm plastic still measures large.
3. With calipers, measure each hole across two perpendicular diameters and
   take the smaller. Holes print slightly oval; the smaller number is what a
   pin has to pass through.
4. Record measured minus nominal for each hole in a "Measured shrinkage"
   table in your project notes. The four values should agree within about 0.05 mm.
   If they do not, the smallest hole is the odd one out -- trust the 5 and
   6 mm figures.
5. Also caliper the plate itself against PLATE_LENGTH / PLATE_WIDTH to catch
   any XY scaling error, and the chamfer and corner radius by eye to confirm
   the printer resolves them at all.

The resulting offset is what you add to every nominal hole diameter in later
parts. Re-run this coupon whenever you change filament brand or nozzle.

Run (with cadlib.py one folder above this script, or on sys.path):
    python3 calibration.py
Outputs out/calibration_coupon.{stl,step} beside the script
"""

from __future__ import annotations

import sys
from pathlib import Path

# Part scripts live in a subdirectory; put the project root (one folder up) on
# sys.path so the shared cadlib is importable no matter where the script is
# invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build123d import (  # noqa: E402
    Align,
    Axis,
    BuildPart,
    BuildSketch,
    Circle,
    Locations,
    Mode,
    Plane,
    Rectangle,
    Text,
    chamfer,
    extrude,
    fillet,
)

import cadlib  # noqa: E402

# ---------------------------------------------------------------------------
# PARAMETERS -- everything adjustable lives here. All dimensions in mm.
# ---------------------------------------------------------------------------

PART_NAME = "calibration_coupon"
MATERIAL = "PETG"

# Plate body
PLATE_LENGTH = 74.0          # X extent
PLATE_WIDTH = 24.0           # Y extent
PLATE_THICKNESS = 3.0        # Z extent, thick enough not to warp off the bed
CORNER_RADIUS = 3.0          # fillet on the four vertical corners
TOP_CHAMFER = 0.6            # chamfer around the top face, breaks the edge

# Test holes -- nominal diameters. These are the numbers you compare against.
HOLE_DIAMETERS = (3.0, 4.0, 5.0, 6.0)
HOLE_PITCH = 17.0            # centre-to-centre spacing along X
HOLE_Y = 5.0                 # hole centreline offset from plate centre in Y

# Engraved labels, one under each hole
LABEL_TEXTS = ("3", "4", "5", "6")
LABEL_FONT = "Arial"         # present on every macOS install
LABEL_SIZE = 5.5
LABEL_Y = -6.5               # text centre offset from plate centre in Y
ENGRAVE_DEPTH = 0.6          # sunk into the top face; >= 2 layers at 0.2 mm

# Mesh quality for the exported STL
STL_TOLERANCE = 0.01
STL_ANGULAR_TOLERANCE = 0.1

# ---------------------------------------------------------------------------
# GEOMETRY
# ---------------------------------------------------------------------------


def build_coupon():
    """Return the calibration coupon as a build123d part."""
    n = len(HOLE_DIAMETERS)
    # Centre the row of holes on the plate.
    x_positions = [(i - (n - 1) / 2.0) * HOLE_PITCH for i in range(n)]

    with BuildPart() as coupon:
        # Plate body
        with BuildSketch(Plane.XY):
            Rectangle(PLATE_LENGTH, PLATE_WIDTH)
        extrude(amount=PLATE_THICKNESS)

        # Round the four vertical corners
        fillet(coupon.edges().filter_by(Axis.Z), radius=CORNER_RADIUS)

        # Break the top edge. Done before the holes are cut so only the
        # outer perimeter is chamfered, not the bores.
        top_face = coupon.faces().sort_by(Axis.Z)[-1]
        chamfer(top_face.edges(), length=TOP_CHAMFER)

        # Through-holes. A subtracted sketch of circles is more predictable
        # than the Hole() primitive, which depends on the active workplane.
        with BuildSketch(Plane.XY):
            for x, dia in zip(x_positions, HOLE_DIAMETERS):
                with Locations((x, HOLE_Y)):
                    Circle(radius=dia / 2.0)
        extrude(amount=PLATE_THICKNESS, mode=Mode.SUBTRACT)

        # Engraved labels, sunk into the top face
        with BuildSketch(Plane.XY.offset(PLATE_THICKNESS)):
            for x, label in zip(x_positions, LABEL_TEXTS):
                with Locations((x, LABEL_Y)):
                    Text(
                        label,
                        font_size=LABEL_SIZE,
                        font=LABEL_FONT,
                        align=(Align.CENTER, Align.CENTER),
                    )
        extrude(amount=-ENGRAVE_DEPTH, mode=Mode.SUBTRACT)

    return coupon.part


if __name__ == "__main__":
    part = build_coupon()
    cadlib.save(
        part,
        PART_NAME,
        material=MATERIAL,
        tolerance=STL_TOLERANCE,
        angular_tolerance=STL_ANGULAR_TOLERANCE,
    )
    cadlib.show(part)
