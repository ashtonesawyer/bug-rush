import bugrush

def test_dumb2x2():
	p = bugrush.Puzzle("./tests/dumb2x2.bugs")
	assert p.bug == (2, 0)

def test_first5x5():
	p = bugrush.Puzzle("./tests/first5x5.bugs")
	assert p.bug == (3, 0)

def test_unsat3x4():
	p = bugrush.Puzzle("./tests/unsat3x4.bugs") 
	assert p.bug == (2, 0)
	
