# agency-poem-01 entry: write the vendored poem to /output/entry.txt.
# Standard library only. Deterministic: the same bytes every run.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poem.txt")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
dst = os.path.join(OUT, "entry.txt")
shutil.copyfile(SRC, dst)
# Verify the copy: the output must be byte-identical to the vendored poem.
assert os.path.getsize(dst) == os.path.getsize(SRC), "copy size mismatch"
with open(SRC, "rb") as f_src, open(dst, "rb") as f_dst:
    assert f_src.read() == f_dst.read(), "copy bytes mismatch"
