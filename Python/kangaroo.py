def yes_no(x1,v1,x2,v2):
     while(True):
        if(x2 > x1 and v2 > v1 or x1 > x2 and v1 > v2 or v1 == v2):
            print("NO")
            break
        elif(x1 == x2):
            print("YES")
            break
        x1+=v1
        x2+=v2


xv  = input()
xv = xv.split(" ")

x1 = int(xv[0])
v1 = int(xv[1])

x2 = int(xv[2])
v2 = int(xv[3])

yes_no(x1,v1,x2,v2)
