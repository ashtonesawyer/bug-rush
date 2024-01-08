import bugrush

def test_unifinished():
	p = bugrush.Puzzle(file="./tests/dumb2x2.bugs")
	assert p._finished() == False

def test_finished():
	board = [["-", "-", "-"],
			 [" ", "|", "-"],
			 [" ", " ", ">"],
			 ["|", " ", "-"]]
	p = bugrush.Puzzle(b=board)
	assert p._finished() == True


