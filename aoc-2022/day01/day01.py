def solutionA(lines):
  max_calories = 0
  
  calories = 0
  for line in lines:
    if not line:
      calories = 0
    else:
      calories += int(line)
      
      if calories > max_calories:
        max_calories = calories
  
  return max_calories

def solutionB(lines):
  top_list = [0,0,0]
  calories = 0
  for line in lines:
    if line == "":
      update_top_list(calories, top_list)
      calories = 0
    else:
      calories += int(line)
  
  # make sure the last elf is included
  update_top_list(calories, top_list)
    
  return sum(top_list)

def update_top_list(calories, top_list):
  for i, cal in enumerate(top_list):
    if calories > cal:
      top_list.insert(i, calories)
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
