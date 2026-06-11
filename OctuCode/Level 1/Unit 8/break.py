print("***** Continue *****")

for x in range(6):
  if x == 3:
    continue
  print(x)
  
print("***** Break *****")

for x in range(6):
  if x == 3:
    print("I have to leave now ...")
    break
  print(x)