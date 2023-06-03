#test Hello | python app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from src.app import Hello

def test_Hello():
    assert Hello() == "Hello World!"
    
