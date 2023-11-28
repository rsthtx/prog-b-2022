def v3_solutions():

  def create_score_computer(strategy):
    A_char_value = ord("A")
    X_char_value = ord("X")

    def compute(line):
      p1, p2 = line.split(" ")
      i = ord(p1) - A_char_value
      j = ord(p2) - X_char_value
      score = strategy(i,j)
      # print(p1, p2, i, j, score)
      return score
  
    return compute

  # Values of selection
  R, P, S = [1, 2, 3]
  # values of outcomes
  D, W, L = [3, 6, 0]
  score_strategy_A = lambda i, j : [D, W, L][j-i] + [R, P, S][j]
  score_strategy_B = lambda i, j : [S, R, P][(j+i)%3] + [L , D, W][j]

  def create_solver(strategy):
    compute_score = create_score_computer(strategy)
    return lambda lines: sum(compute_score(l) for l in lines)

  solutionA = create_solver(score_strategy_A)
  solutionB = create_solver(score_strategy_B)
  return (solutionA, solutionB)

def v2_solutions():

  # Values of selection
  R, P, S = [1, 2, 3]
  # values of outcomes
  D, W, L = [3, 6, 0]

  score_lookup_A = {f"{p1} {p2}" : [D, W, L][j-i] + [R, P, S][j] for i, p1 in enumerate("ABC") for j, p2 in enumerate("XYZ")}
  score_lookup_B = {f"{p1} {p2}" : [S, R, P][(j+i)%3] + [L , D, W][j] for i, p1 in enumerate("ABC") for j, p2 in enumerate("XYZ")}

  def create_solver(score_lookup):
    def solve(lines):
      return sum(score_lookup[l] for l in lines)
    return solve

  solutionA = create_solver(score_lookup_A)
  solutionB = create_solver(score_lookup_B)
  return (solutionA, solutionB)


def v1_solutions():
  # values
  rock, paper, scissors = [1, 2, 3]
  lose, draw, win = [0, 3, 6]

  def solutionA(lines):
    score_lookup_table = {
      # opponent plays rock
      "A X": draw + rock,
      "A Y": win + paper,
      "A Z": lose + scissors,
      # opponent plays paper
      "B X": lose + rock,
      "B Y": draw + paper,
      "B Z": win + scissors,
      # opponent plays scissors
      "C X": win + rock,
      "C Y": lose + paper,
      "C Z": draw + scissors,
    }

    total_score = 0
    for line in lines:
      total_score += score_lookup_table[line]

    return total_score

  def solutionB(lines):
    score_lookup_table = {
      # opponent plays rock
      "A X": lose + scissors,
      "A Y": draw + rock,
      "A Z": win + paper,
      # opponent plays paper
      "B X": lose + rock,
      "B Y": draw + paper,
      "B Z": win + scissors,
      # opponent plays scissors
      "C X": lose + paper,
      "C Y": draw + scissors,
      "C Z": win + rock,
    }

    return sum(score_lookup_table[line] for line in lines)

  return (solutionA, solutionB)


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines

solutionA, solutionB = v3_solutions()

if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  input_file_name = "input.txt"
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")
