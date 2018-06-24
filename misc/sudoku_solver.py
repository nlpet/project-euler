
puzzle1 = [[0,2,6,0,0,0,8,1,0],
		  [3,0,0,7,0,8,0,0,6],
		  [4,0,0,0,5,0,0,0,7],
		  [0,5,0,1,0,7,0,9,0],
		  [0,0,3,9,0,5,1,0,0],
		  [0,4,0,3,0,2,0,5,0],
		  [1,0,0,0,3,0,0,0,2],
		  [5,0,0,2,0,4,0,0,9],
		  [0,3,8,0,0,0,4,6,0]]

puzzle2 = [[0,0,5,0,0,2,0,6,7],
		   [4,0,0,0,8,5,0,0,0],
		   [1,0,8,0,0,0,5,4,0],
		   [0,0,0,5,3,0,0,0,0],
		   [3,0,0,6,0,1,0,0,8],
		   [0,0,0,0,2,9,0,0,0],
		   [0,6,1,0,0,0,7,0,4],
		   [0,0,0,3,1,0,0,0,6],
		   [7,9,0,4,0,0,1,0,0]]

puzzle3 = [[0,0,0,0,7,0,0,0,2],
		   [0,6,3,0,5,2,0,0,0],
		   [9,0,4,1,0,0,7,0,0],
		   [0,0,1,0,0,7,0,5,8],
		   [8,9,0,0,0,6,3,0,0],
		   [0,0,0,4,0,3,0,2,9],
		   [0,1,0,8,6,0,0,0,4],
		   [0,0,5,0,0,0,8,1,3],
		   [0,8,9,0,4,0,0,0,0]]


def define_blocks(sections):
	blocks,currSection,i,j = {},1,0,0
	while sections >= currSection:
		blocks[currSection] = [(i,j),(i,j+1),(i,j+2),(i+1,j),(i+1,j+1),(i+1,j+2),(i+2,j),(i+2,j+1),(i+2,j+2)]
		j += 3
		if j > 8:
			i += 3
			j = 0
		currSection += 1
	return blocks


def find_neighbors(cell,puzzle):
	result = set()
	neighbors = define_blocks(len(puzzle))
	for k,v in neighbors.items(): 
		if cell in v:
			for num in v: result.add(puzzle[num[0]][num[1]])
	for i in range(len(puzzle)):
		result.add(puzzle[cell[0]][i])
		result.add(puzzle[i][cell[1]])
	return result

def solve(puzzle):
	h = l = 0
	zeroes = len([n for p in puzzle for n in p if n == 0])
	while zeroes != 0:
		for h in range(len(puzzle)):
			for l in range(len(puzzle)):
				if puzzle[h][l] == 0: 
					result = list(set([1,2,3,4,5,6,7,8,9]) - set(find_neighbors((h,l),puzzle)))
					if len(result) == 1: 
						puzzle[h][l] = result[0]
						zeroes -= 1
	print('')
	print("Solved")
	for p in puzzle: print(p)

solve(puzzle1)
solve(puzzle2)
solve(puzzle3)
