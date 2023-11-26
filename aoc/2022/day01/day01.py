# def solutionA(lines):
  
#   max_calories = 0
#   calories = 0
#   for line in lines:
#     if line == "":
#       max_calories = max(calories, max_calories) 
#       calories = 0
#     else:
#       calories += int(line)
  
#   max_calories = max(calories, max_calories)
#   return max_calories


def solutionA(lines):
  return solve(lines)


def solutionB(lines):
  max_list = [0,0,0]
  return solve(lines, max_list)
  
  
def solve(lines, max_list = [0]):
  calories = 0
  for line in lines:
    if line == "":
      update_max_list(calories, max_list)
      calories = 0
    else:
      calories += int(line)
  
  # make sure the last elf is included
  update_max_list(calories, max_list)
    
  return sum(max_list)

def update_max_list(calories, top_list):
  for idx, value in enumerate(top_list):
    if calories > value:
      top_list.insert(idx, calories)
      top_list.pop()
      break


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  # input_file_name = "input.txt"
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")
