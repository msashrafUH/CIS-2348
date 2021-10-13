var = 0
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
while var == 0:
  try:
    userDate = input("Enter the month day, year: ")
  except SyntaxError:
    continue
  if userDate=='-1':
    break

  try:
    arr = userDate.split()
    digit = len(arr)
    if digit!=3:
      continue
    m = arr[0]
    day = arr[1]
    y = arr[2]
    d, comma = day.split(',')

    for x in range(12):
      if userDate.find(months[x])>=0:
        mo = str(x+1)
        ans = mo + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
    continue