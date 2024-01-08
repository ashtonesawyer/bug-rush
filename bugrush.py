#!/usr/bin/python3

import cProfile, pstats
import sys, heapq, argparse
from copy import copy
from collections import deque
from itertools import chain

# create a deepcopy of the board 
# (faster than lib deepcopy in this case)
def deepcopy(board):
	ret = []
	for row in board:
		r = []
		for square in row:
			r.append(square)
		ret.append(r)
	return ret

class Bstate(object):
	def __init__(self, f, st):
		self.f = f
		self.st = st

	def __eq__(self, other):
		return self.f == other.f
	
	def __lt__(self, other):
		return self.f < other.f

	def state(self):
		return self.st

	def key(self):
		return self.f

class Puzzle(object):
	g = 0
	def __init__(self, file=None, b=None, bug=None):
		if b == None:
			self.board = self._parseBoard(file)
		elif file == None:
			self.board = deepcopy(b)
		else:
			print("Error: No Board")
			exit(-1)

		if bug == None:
			self.bug = self._findBug() #position as (i, j)
		else:
			self.bug = bug
		self.parent = None
		self.moved = None

	def __copy__(self):
		newcopy = Puzzle(b=self.board, bug=self.bug)
		return newcopy

	def __eq__(self, other):
		self.board == other.board

	def __hash__(self):
		# flatten board and hash entire thing
		# leocon.dev/blog/2021/09/how-to-flatten-a-python-list-array-and-which-one-you-should-use/
		return hash(tuple(chain.from_iterable(self.board)))

	# returns list of legal moves
	# moves given as tuples of coords to swap
	def moves(self):
		r = len(self.board)
		c = len(self.board[0])
		moves = []
		for i in range(1, r):
			for j in range(c):
				if self.board[i][j]	== " ": #faster to search spaces than bugs
					if i > 1 and self.board[i-1][j] == "|":
						moves.append(((i-1, j), (i, j)))
					if i+1 < r and self.board[i+1][j] == "|":
						moves.append(((i+1, j), (i, j)))
					if j > 0 and (self.board[i][j-1] == "-" or self.board[i][j-1] == ">"):
						moves.append(((i, j-1), (i, j)))
					if j+1 < c and (self.board[i][j+1] == "-" or self.board[i][j+1] == ">"):
						moves.append(((i, j+1), (i, j))) 
		return moves

	# make the move
	def move(self, move):
		((i, j), (k, l)) = move
		self.board[i][j], self.board[k][l] = self.board[k][l], self.board[i][j]	

		# update bug if it was moved
		if self.board[i][j] == ">":
			self.bug = (i, j)
		elif self.board[k][l] == ">":
			self.bug = (k, l)
		return

	# calc absolute min number of moves to finished
	def h(self):
		(i, j) = self.bug
		width = len(self.board[0])
		total = width - 1 - j  # start with distance from bug to end
		for k in range(j+1, width):
			if self.board[i][k] == "-":
				return None # can't have horizontal cars in front of goal on solveable puzzle
			elif self.board[i][k] == "|":
				total += 2 # assume blocked 
				# subtract extra if blocked not true
				if i+1 < len(self.board):
					if self.board[i-1][k] == " " or self.board[i+1][k] == " ":
						total -= 1
		return total
			
	def bfs(self):
		start = copy(self)
		start.parent = None
		start.moved = None
		visited = {hash(start)}

		queue = deque()
		queue.appendleft(start)

		while queue:
			state = queue.pop()

			possible = state.moves()
			for move in possible:
				child = copy(state)
				child.move(move)

				key = hash(child)
				if key in visited:
					continue


				if child._finished():
					soln = [move]
					while state.parent:
						state = state.parent
						soln.append(state.moved)
					return list(reversed(soln))

				child.parent = state
				child.moved = move
				visited.add(key)
				queue.appendleft(child)

		# no soln
		return None
		
	# find shortest path to soln w/ A*
	def astar(self):
		start = copy(self)
		start.parent = None
		start.moved = None

		visited = {hash(start): start}

		pqueue = []
		start.h = start.h()
		if start.h == None:
			return None
		start.f = start.g + start.h
		heapq.heappush(pqueue, Bstate(start.f, start))

		while pqueue:
			state = heapq.heappop(pqueue).state()

			if state._finished():
				soln = []
				g = state.g
				states = {state}
				while True:
					if state.moved:
						soln.append(state.moved)

					state = state.parent
					if not state.parent:
						break
					assert state not in states
					states.add(state)
					g -= 1
					assert g == state.g
				return list(reversed(soln))
		
			possible = state.moves()
			for move in possible:
				child = copy(state)
				child.move(move)
				
				if child._finished():
					soln = [move]
					g = state.g
					states = {state}
					while True:
						if state.moved:
							soln.append(state.moved)

						state = state.parent
						if not state.parent:
							break
						assert state not in states
						states.add(state)
						g -= 1
					return list(reversed(soln))


				child.g = state.g + 1
				child.h = child.h()
				child.f = child.g + child.h

				hh = hash(child)
				if hh not in visited or visited[hh].f > state.f:
					child.parent = state
					child.moved = move
					visited[hh] = child
					heapq.heappush(pqueue, Bstate(child.f, child))

		return None

	
	def _parseBoard(self, file):
		board = []
		with open(file, "r") as f:
			for row in f:
				squares = []
				for char in row:
					if char != '\n':
						squares.append(char)
				board.append(squares)
		return board

	def _findBug(self):
		for i in range(1, len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] == ">":
					return (i, j)

	def _finished(self):
		(i, j) = self.bug
		if j == len(self.board[0]) - 1:
			return True
		return False 

	def _printBoard(self):
		for i in range(len(self.board)):
			print(*self.board[i], sep="")

def run(args):
	f = args.file
	if f == None:
		print("Invalid Argument Usage", file=sys.stderr)
		print("Usage: python3 bugrush.py -f <file>", file=sys.stderr)
		exit(-1)
	p = Puzzle(file=f)
	
	solver = args.solver
	# astar really slow (2+ mins) for unsat5x7?
	# bfs working well
	if solver == "bfs":
		soln = p.bfs()
	else:
		soln = p.astar()
	print(len(soln)) if soln != None else print("unsat")

def runprofile(args):
	cProfile.run("run(args)", "stats")
	p = pstats.Stats("stats")
	p.sort_stats("cumulative").print_stats()

parser = argparse.ArgumentParser(description="Find the shortest soln to Bug Rush")
parser.add_argument('--file', '-f', type=str, default=None, 
					help='file to read the puzzle from')
solvers = {"bfs", "astar"}
parser.add_argument('--solver', '-s', type=str, choices=solvers, default="bfs",
					help='solver algorithm')
parser.add_argument('--profile', '-p', action='store_true', help='profile the code')

args = parser.parse_args()


if args.profile:
	runprofile(args)
else:
	run(args)


