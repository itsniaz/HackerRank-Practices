def isBalanced(s):
    stack = []
    dict = {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if(c == "(" or c =="{" or c == "["):
            stack.append(c)
        elif(c == ")" or c=="}" or c == "]"):
            if(len(stack)>0):
                popped = stack.pop()
                if(dict[popped] == c):
                    continue
                else:
                    return "NO"
            else:
                return "NO"
    
    if(len(stack)>0):
        return "NO"
    else:
        return "YES"

isBalanced("{{{}}}}")