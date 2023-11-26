# Advent of code

Julekalender for softwareudviklere

- [Advent of Code 2023](https://adventofcode.com/2023)

Her er de første låger fra sidste års julekalender, så der er lidt at fordrive tiden med, mens vi venter i spænding på 1. december ;-)

### [Advent of code 2022](https://adventofcode.com/2022)

- [Første låge](https://adventofcode.com/2022/day/1)
- [Anden låge](https://adventofcode.com/2022/day/2)
- [Tredje låge](https://adventofcode.com/2022/day/3)
- [Fjerde låge](https://adventofcode.com/2022/day/4)
- [Femte låge](https://adventofcode.com/2022/day/5)

## Hints til løsning
- Log in med github på [Advent of Code](https://adventofcode.com/)
- Lav en ny mappe, f.eks. `day01`
- Til hvert problem er der en stump eksempel input. Gem dette i en fil: `day01/dummy-input.txt`
- Hent dit personlige input data og gem det i en fil på din computer, f.eks. `day01/input.txt`
- Lav `day01/day01.py` i samme mappe som input filen
- Løs opgaven ;-)
- Lav en ny mappe til hver dag i kalenderen for nemt at holde styr på løsninger og input-data til de enkelte dage.

Her er en [stump python kode](template/dayXX.py), der kan bruges som skabelon til starten på en løsning.

```python
def solutionA(lines):
  # TODO: replace with code solving the problem
  return -1 # Dummy result, deliberately wrong


def solutionB(lines):
  # TODO: replace with code solving the problem
  return -2 # Dummy result, deliberately wrong


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

```

## Materiale

- [Automate the Boring Stuff](https://automatetheboringstuff.com/#toc), Al Sweigert
- Install python: [python.org/downloads](https://www.python.org/downloads/)
- [Command line basics](https://getsrevel.github.io/tools/command-line/)
- [Thonny](https://thonny.org/) beginner friendly python editor.