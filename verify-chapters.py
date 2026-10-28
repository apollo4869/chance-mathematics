"""Compatibility entry: technical migration checks, no math/history approval."""
from pathlib import Path
import subprocess,sys
raise SystemExit(subprocess.call([sys.executable,str(Path(__file__).parent/'tools/check-stage1.py')]))
