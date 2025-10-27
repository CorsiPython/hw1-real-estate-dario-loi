"""
Pytest configuration for local imports.

Ensures the project root is on sys.path so tests can import `real_estate`
when running `pytest` directly from the repository root.
"""
from __future__ import annotations

import os
import sys


# Add the repository root (parent of this tests/ folder) to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
