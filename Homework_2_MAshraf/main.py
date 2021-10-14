userFile = open('inputDates.txt','r')
dates = userFile.readlines()

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

count = 0
for userDate in dates:
  count += 1
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
        if count>0:
          file2 = open('parsedDates.txt','a')
          file2.write(ans + '\n')
          file2.close()
        else:
          file3 = open('parsedDates.txt','w')
          file3.write(ans + '\n')
          file3.close()
        break

  except ValueError:
    continue

userFile.close()