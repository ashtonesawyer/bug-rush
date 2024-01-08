import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bugrush

def test_unifinished():
	p = bugrush.Puzzle(file="./boards/dumb2x2.bugs")
	assert p._finished() == False

def test_finished():
	board = [["-", "-", "-"],
			 [" ", "|", "-"],
			 [" ", " ", ">"],
			 ["|", " ", "-"]]
	p = bugrush.Puzzle(b=board)
	assert p._finished() == True


