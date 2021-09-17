#Muhammad S Ashraf 1763709
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(lemon))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(agave))
print()

req_servings = float(input("How many servings would you like to make?\n"))

print()
print("Lemonade ingredients - yields {:.2f} servings".format(req_servings))
print("{:.2f} cup(s) lemon juice".format(lemon * req_servings / servings))
print("{:.2f} cup(s) water".format(water * req_servings / servings))
print("{:.2f} cup(s) agave nectar".format(agave * req_servings / servings))

print()
print("Lemonade ingredients - yields {:.2f} servings".format(req_servings))
print("{:.2f} gallon(s) lemon juice".format(lemon * req_servings / servings / 16))
print("{:.2f} gallon(s) water".format(water * req_servings / servings / 16))
print("{:.2f} gallon(s) agave nectar".format(agave * req_servings / servings / 16))