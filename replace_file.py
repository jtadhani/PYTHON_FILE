import sys
#replace
with open(sys.argv[1],'r') as f:
    sp=f.read().split()
    word = input("Enter The Name ::")
    temp = 0

    for i in sp:
        if word == i:
            temp = 1
            break

    if temp == 1:
        w = input("Enter the reples word :- ")
        a = sp.replace(word,w)
        file = open(sys.argv[1],"w")
    else :
        print("note match")
