"""Legacy command name; prepares a LOCAL candidate only. Never publishes."""
from pathlib import Path
import subprocess,sys
raise SystemExit(subprocess.call([sys.executable,str(Path(__file__).parent/'build.py')]))
