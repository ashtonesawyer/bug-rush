import bugrush

p = bugrush.Puzzle("./tests/dumb2x2.bugs")

def test_oneMove():
	assert p.moves() == [((1, 1), (1, 0))]

def test_noMoves():
	board = [["-", "-"],
			 ["|", "-"],
			 [">", "-"]]	
	p.board = board
	assert p.moves() == []	

def test_manyMoves():
	board = [["-", "-", "-"],
			 ["|", " ", "-"],
			 [">", "|", " "],
			 ["-", " ", "|"]]
	p.board = board
	assert p.moves() == [((2,1), (1, 1)), ((1,2), (1, 1)), ((3,2), (2,2)), ((2,1), (3, 1)), ((3,0), (3,1))]

	
