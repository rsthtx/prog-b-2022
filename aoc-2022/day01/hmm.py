my_list = [6,7,8]

for value in my_list:
  print(value)
  
for idx in range(len(my_list)):
  value = my_list[idx]
  print(idx, ":", value)



for idx, value in enumerate(my_list):
  print(idx, ":", value)
