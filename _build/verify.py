"""Every solution must pass; every stub must fail."""
from __future__ import annotations
import os, subprocess, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = dict(os.environ)
env["PYTHONPATH"] = str(ROOT)
env["PYTHONDONTWRITEBYTECODE"] = "1"

info = tomllib.loads((ROOT / "info.toml").read_text())
bad = []
for item in info["exercises"]:
    name = item["name"]
    ex = ROOT / item["path"]
    sol = ROOT / item["path"].replace("exercises/", "solutions/", 1)

    r = subprocess.run([sys.executable, str(sol)], capture_output=True, text=True,
                       cwd=ROOT, env=env, timeout=30)
    if r.returncode != 0:
        bad.append(f"SOLUTION FAILS {name}\n{r.stderr.strip()[-900:]}")

    r2 = subprocess.run([sys.executable, str(ex)], capture_output=True, text=True,
                        cwd=ROOT, env=env, timeout=30)
    if r2.returncode == 0:
        bad.append(f"STUB PASSES (too easy / nothing to do) {name}")

print(f"checked {len(info['exercises'])} exercises")
if bad:
    print("\n\n".join(bad))
    sys.exit(1)
print("ALL GOOD")
