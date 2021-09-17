#Muhammad S Ashraf 1763709
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
totalService = 0
print()

print("Davy's auto shop invoice")
print()
if(service1.lower() == 'oil change'):
    print('Service 1: Oil change, $35')
    totalService = totalService + 35
elif(service1.lower() == 'tire rotation'):
    print('Service 1: Tire rotation, $19')
    totalService = totalService + 19
elif(service1.lower() == 'car wash'):
    print('Service 1: Car wash, $7')
    totalService = totalService + 7
elif(service1.lower() == 'car wax'):
    print('Service 1: Car wax, $12')
    totalService = totalService + 12
elif(service1.lower() == '-'):
    print('Service 1: No service')

if(service2.lower() == 'oil change'):
    print('Service 2: Oil change, $35')
    totalService = totalService + 35
elif(service2.lower() == 'tire rotation'):
    print('Service 2: Tire rotation, $19')
    totalService = totalService + 19
elif(service2.lower() == 'car wash'):
    print('Service 2: Car wash, $7')
    totalService = totalService + 7
elif(service2.lower() == 'car wax'):
    print('Service 2: Car wax, $12')
    totalService = totalService + 12
elif(service2.lower() == '-'):
    print('Service 2: No service')
print()

print(f"Total: ${totalService}")