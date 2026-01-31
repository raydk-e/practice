def get_list():
    l = []
    size = int(input("enter the numebr of element: "))
    for i in range(size):
        s = input(" enter the list element: ")
        l.append(s)
    return l
def find_dup(k: list) -> list[int]:
    dup =[]
    counter = 0
    for j in range(len(k)):
        for n in range(len(k)):
            if j!=n:
                if k[j] == k[n]:
                    counter+=1
                    dup.append(f"{j} - place")
    return counter, dup

def main():

    k = get_list ()
    p, q = find_dup(k)
    print(f" number of dupes {p} , list of dups {q}")

if __name__ == "__main__":
    main()
