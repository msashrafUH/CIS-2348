#Muhammad S Ashraf 1763709
list = []
list = [item for item in input().split()]

for word in list:
        freq = list.count(word) 
        print(word, freq)