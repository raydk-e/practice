l = []
dup =[]
counter = 0
size = int(input("enter the numebr of element: "))
for i in range(size):
    s = input(" enter the list element: ")
    l.append(s)
print(f"the list youhave created is {l}")
for j in range(len(l)):
    for k in range(len(l)):
        if j!=k:
            if l[j] == l[k]:
                counter+=1
                dup.append(f"{j} - place")
print(f"the duplicate memebre count is {counter}")
print( f"the duplicate elements are {dup}")
