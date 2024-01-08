# Bug Rush
Ashton Sawyer

## Description
Overall the assignment went pretty well. I referenced the code for the slider game
quite a bit while initially writting the program. I started with BFS and once that was working
I also tried to impliment A\*.

### BFS
Right now BFS is working really well. In my tests, the longest puzzle is unsat5x7.bugs and
it takes just over 2 seconds. When I first wrote it it took about 10 seconds on that puzzle.
I was able to reducde it by profiling with cProfile and optimizing the relevant functions.

### A\*
My A\* is working, as in it gets the correct answer, but it's running very slow and I'm not
entirely sure why. I think it's getting stuck in loops somewhere as it searches because it's
performing _way_ more copies than BFS.

For example, here are some of the stats on some5x7.bugs:

```
For BFS:
		3340463 function calls (3268018 primitive calls) in 1.301 seconds

	Ordered by: cumulative time

	ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	 52351    0.062    0.000    0.845    0.000 /usr/lib/python3.10/copy.py:66(copy)
	 52351    0.034    0.000    0.760    0.000 /u/sawyeras/cs441/bug-rush/bugrush.py:55(__copy__)

For A*:
		35052643 function calls (34594568 primitive calls) in 18.740 seconds

	Ordered by: cumulative time

	ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	457981    0.524    0.000    9.937    0.000 /usr/lib/python3.10/copy.py:66(copy)
	457981    0.273    0.000    9.236    0.000 /u/sawyeras/cs441/bug-rush/bugrush.py:55(__copy__)
```

I think I have a good heuristic, though. It counts the amount of spaces in front of
the goal car + the amount of cars in front of the goal car, and for each of those 
cars, +1 if above and below it is blocked

Ex:

```
----
  |-
>|||
|--|


h = 3 spaces in front
  + 1 unblocked car
  + 4 for 2 blocked cars
  = 7
```

## Running

```
python3 bugrush.py -f FILE [-s SOLVER] [-p]

	--file=FILE, -f=FILE
		Indicate the file to get the puzzle from
	--solver={bfs, astar}, -s={bfs, astar}
		Choose the algorithm with which to solve the puzzle.
		Default is BFS
	--profile, -p
		Profile the code and output the results
```
