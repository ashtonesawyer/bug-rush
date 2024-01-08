import bugrush

def test_blocked():
	p = bugrush.Puzzle(file="./tests/dumb2x2.bugs")
	assert p.h() == 3

def test_none():
	board = [["-", "-", "-"],
			 ["|", "-", " "],
			 [" ", " ", ">"],
			 ["-", "|", " "]]
	p = bugrush.Puzzle(b=board)
	assert p.h() == 0

def test_fun3x3():
	p = bugrush.Puzzle(file="./tests/fun3x3.bugs")
	assert p.h() == 5

def test_cleared():
	board = [["-", "-", "-"],
			 [">", " ", " "],
			 ["-", "|", " "]]
	p = bugrush.Puzzle(b=board)
	assert p.h() == 2

def test_unsat5x7():
	p = bugrush.Puzzle(file="./tests/unsat5x7.bugs")
	assert p.h() == 18
