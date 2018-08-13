def isFailed(mark):
    return mark<38

def round(x):
    x = int(x)
    if(not isFailed(x)):
        remainder = x%5
        if(remainder>=3):
            return x+(5-remainder)
        else:
            return x
    else:
        return x

def main():
    n = int(input())
    for i in range(n):
        print(round(input()))
main()