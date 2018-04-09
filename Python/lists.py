list = []
n = int(input())
for i in range(n):
    args = input().split(' ')
    opreation = args[0]
    if opreation == "insert":
        try:
            list.insert(int(args[1]),int(args[2]))
        except Exception:
            pass
    elif opreation == "print":
        print(list)
    elif opreation == "remove":
        try:
            list.remove(int(args[1]))
        except Exception:
            pass
    elif opreation == "append":
        try:
            list.append(int(args[1]))
        except Exception:
            pass
    elif opreation == "sort":
        try:
            list.sort()
        except Exception:
            pass
    elif opreation == "pop":
        try:
            list.pop()
        except:
            pass
    elif opreation == "reverse":
        try:
            list.reverse()
        except Exception:
            pass
    else:
        pass
        
        