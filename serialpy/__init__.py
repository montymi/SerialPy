# __init__.py

from importlib import resources
import tomllib

# Version of the serial-search package
__version__ = "1.0.0"

# Read settings from config file
_cfg = tomllib.loads(resources.read_text("serialpy", "config.toml"))
PRINT = _cfg["settings"]["print"]
