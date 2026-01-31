l=[]
target =9
visit=[]
for i in range(5):
    x = int(input("provide memeber of list list - "))
    l.append(x)
print(l)  
for j in range(len(l)):
    for k in range(len(l)):
        if j != k:
            if l[j]+l[k] == target:
                if l[j] not in visit:
                    visit.append(l[k])
                    print([j,k])  
                
               
