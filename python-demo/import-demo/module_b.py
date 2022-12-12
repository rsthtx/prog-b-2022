import module_a

def my_sum(lst):
  total = 0
  for n in lst:
    total = module_a.add(total, n)
  return total
  
print(__name__)
if __name__ == "__main__":
  print("testing library functions in module b")
  assert(my_sum([1,2,3]) == 6)
  
  