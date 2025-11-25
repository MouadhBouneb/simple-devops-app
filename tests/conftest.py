"""
Pytest configuration for ensuring project root is importable.
"""
import os
import sys


def _add_project_root_to_path() -> None:
    """Ensure repository root is on sys.path for module discovery."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


_add_project_root_to_path()

