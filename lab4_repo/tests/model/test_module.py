import sys
from pathlib import Path

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))

from module import serve_beer

def test_serve_beer_legal():
  adult = 25
  assert serve_beer(adult) == "Have beer"
 
def test_serve_beer_illegal():
  child = 10
  assert serve_beer(child) == "No beer"