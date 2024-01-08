import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bugrush

def test_dumb2x2():
	p = bugrush.Puzzle("./boards/dumb2x2.bugs")
	assert p.board == [["-","-"], [" ", "-"], [">", "|"]]

def test_first5x5():
	p = bugrush.Puzzle("./boards/first5x5.bugs")
	ans = [["-", "-", "-", "-", "-"],
		   ["-", "-", "-", " ", "-"],
		   ["|", "-", "-", "-", "|"],
		   [">", "|", "|", "|", "|"],
		   [" ", "-", "-", "-", "-"],
		   ["-", "-", "-", "-", "-"]]
	assert p.board == ans

def test_unsat3x4():
	p = bugrush.Puzzle("./boards/unsat3x4.bugs") 
	ans = [["-", "-", "-", "-"],
		   ["-", " ", " ", "|"],
		   [">", "|", " ", "|"],
		   [" ", "|", "-", "|"]]
	assert p.board == ans
