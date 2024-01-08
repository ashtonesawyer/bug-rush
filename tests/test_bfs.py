import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bugrush

def test_dumb2x2():
	p = bugrush.Puzzle(file="./boards/dumb2x2.bugs")
	assert len(p.bfs()) == 3

def test_first5x5():
	p = bugrush.Puzzle(file="./boards/first5x5.bugs")
	assert len(p.bfs()) == 17

def test_fun3x3():
	p = bugrush.Puzzle(file="./boards/fun3x3.bugs")
	assert len(p.bfs()) == 12

def test_fun3x4():
	p = bugrush.Puzzle(file="./boards/fun3x4.bugs")
	assert len(p.bfs()) == 11

def test_hardest3x3():
	p = bugrush.Puzzle(file="./boards/hardest3x3.bugs")
	assert len(p.bfs()) == 15

def test_hardest3x4():
	p = bugrush.Puzzle(file="./boards/hardest3x4.bugs")
	assert len(p.bfs()) == 34

def test_some5x7():
	p = bugrush.Puzzle(file="./boards/some5x7.bugs")
	assert len(p.bfs()) == 42
	

def test_unsat3x4():
	p = bugrush.Puzzle(file="./boards/unsat3x4.bugs")
	assert p.bfs() == None

def test_unsat5x7():
	p = bugrush.Puzzle(file="./boards/unsat5x7.bugs")
	assert p.bfs() == None
	
