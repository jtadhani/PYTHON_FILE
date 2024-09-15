import sys
#word count
file = open(sys.argv[1],"r")

r = file.read()

count = 0
w = r.split(" ")

# print(len(w))

for i in w:
    count = count + 1

print(count)