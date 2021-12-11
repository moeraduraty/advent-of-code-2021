N_ROWS = 10
N_COLS = 10

def parse_input(file):
  f = open(file, "r")
  text = f.read()
  return [ [ int(n) for n in line ] for line in text.split("\n") ]

def print_grid(grid):
  for row in grid:
    print(''.join([ str(el) for el in row ]))
  print('--')


def simulate(initial_grid, num_steps):
  total_flashes = 0
  grid = initial_grid

  for step in range(num_steps):
    print(step)
    print_grid(grid)
    new_grid = [ row[:] for row in grid ]
    
    flashed = set()
    stack = []
    for r in range(N_ROWS):
      for c in range(N_COLS):
        new_grid[r][c] += 1
        if new_grid[r][c] > 9:
          stack.append((r, c))
          flashed.add((r, c))
          new_grid[r][c] = 0

    num_flashes = 0
    while stack:
      num_flashes += 1
      r, c = stack[-1]
      stack.pop()
      deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
      for delta in deltas:
        d_r, d_c = delta
        n_r = r + d_r
        n_c = c + d_c
        r_inbounds = 0 <= n_r < N_ROWS
        c_inbounds = 0 <= n_c < N_COLS
        neighbor = (n_r, n_c) 
        if r_inbounds and c_inbounds and neighbor not in flashed:
          new_grid[n_r][n_c] += 1
          if new_grid[n_r][n_c] > 9:
            flashed.add(neighbor)
            stack.append(neighbor)
            new_grid[n_r][n_c] = 0
    total_flashes += num_flashes
    grid = new_grid

  return total_flashes


grid = parse_input("input_3.txt")
answer = simulate(grid, 100)
print(answer)
