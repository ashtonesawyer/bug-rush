import bugrush

def test_dumb2x2():
	p = bugrush.Puzzle(file="./tests/dumb2x2.bugs")
	assert len(p.bfs()) == 3

def test_first5x5():
	p = bugrush.Puzzle(file="./tests/first5x5.bugs")
	assert len(p.bfs()) == 17

def test_fun3x3():
	p = bugrush.Puzzle(file="./tests/fun3x3.bugs")
	assert len(p.bfs()) == 12

def test_fun3x4():
	p = bugrush.Puzzle(file="./tests/fun3x4.bugs")
	assert len(p.bfs()) == 11

def test_hardest3x3():
	p = bugrush.Puzzle(file="./tests/hardest3x3.bugs")
	assert len(p.bfs()) == 15

def test_hardest3x4():
	p = bugrush.Puzzle(file="./tests/hardest3x4.bugs")
	assert len(p.bfs()) == 34

def test_some5x7():
	p = bugrush.Puzzle(file="./tests/some5x7.bugs")
	assert len(p.bfs()) == 42
	

def test_unsat3x4():
	p = bugrush.Puzzle(file="./tests/unsat3x4.bugs")
	assert p.bfs() == None

def test_unsat5x7():
	p = bugrush.Puzzle(file="./tests/unsat5x7.bugs")
	assert p.bfs() == None
	
