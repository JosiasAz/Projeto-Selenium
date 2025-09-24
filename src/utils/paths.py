from pathlib import Path

def project_root() -> Path:
    # src/utils/paths.py -> src -> root
    return Path(__file__).resolve().parents[2]
