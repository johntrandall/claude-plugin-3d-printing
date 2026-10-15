#!/usr/bin/env bash
# render-previews.sh: headless preview renders of a 3D model (.scad, .stl, .obj, .3mf, .amf)
#
# Part of the 3d-printing-models-and-tools skill. Agents: run this script instead of
# rendering previews "by hand": it burns zero conversation context beyond one Bash call,
# and the PNGs it emits can be Read (as images) or handed to the user directly.
#
# Usage:
#   render-previews.sh <model-file> [outdir]
#
#   <model-file>  .scad rendered directly; mesh formats (.stl/.obj/.3mf/.amf) are
#                 wrapped in a temp import() .scad
#   [outdir]      output directory (default: alongside the input file)
#
# Output: <basename>-preview-{iso,front,side,top}.png  (1600x1200)
#
# Requires: OpenSCAD on PATH (brew install --cask openscad or openscad@snapshot).
# Assumes macOS: if openscad is not on PATH it falls back to
# /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD.

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -20
  exit 2
fi

MODEL="$1"
[[ -f "$MODEL" ]] || { echo "ERROR: no such file: $MODEL" >&2; exit 1; }

OPENSCAD="$(command -v openscad || true)"
[[ -n "$OPENSCAD" ]] || OPENSCAD="/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
[[ -x "$OPENSCAD" ]] || { echo "ERROR: openscad not found (brew install --cask openscad)" >&2; exit 1; }

ABS_MODEL="$(cd "$(dirname "$MODEL")" && pwd)/$(basename "$MODEL")"
OUTDIR="${2:-$(dirname "$ABS_MODEL")}"
mkdir -p "$OUTDIR"
BASE="$(basename "$MODEL")"; BASE="${BASE%.*}"

# Mesh formats get a wrapper .scad that imports them.
EXT="${MODEL##*.}"; EXT="$(echo "$EXT" | tr '[:upper:]' '[:lower:]')"
SRC="$ABS_MODEL"
TMPDIR_WRAP=""
if [[ "$EXT" != "scad" ]]; then
  TMPDIR_WRAP="$(mktemp -d)"
  trap '[[ -n "$TMPDIR_WRAP" ]] && rm -rf "$TMPDIR_WRAP"' EXIT
  SRC="$TMPDIR_WRAP/wrap.scad"
  printf 'import("%s");\n' "$ABS_MODEL" > "$SRC"
fi

# view-name : camera rotation (rx,ry,rz). Translation/distance handled by --viewall --autocenter.
VIEWS=(
  "iso:55,0,25"
  "front:90,0,0"
  "side:90,0,90"
  "top:0,0,0"
)

for v in "${VIEWS[@]}"; do
  NAME="${v%%:*}"; ROT="${v#*:}"
  OUT="$OUTDIR/${BASE}-preview-${NAME}.png"
  # NOTE: no bare --render flag - in current builds it takes an argument and
  # swallows the next token (the input path). Preview-quality render is fine here.
  "$OPENSCAD" -o "$OUT" \
    --imgsize=1600,1200 \
    --camera="0,0,0,${ROT},0" \
    --viewall --autocenter \
    --colorscheme=Cornfield \
    "$SRC" 2>/dev/null \
    || { echo "ERROR: render failed for view '$NAME' (run without 2>/dev/null to debug)" >&2; exit 1; }
  echo "$OUT"
done
