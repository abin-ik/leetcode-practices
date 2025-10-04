
def descending_order(num):
    n1 = list(str(num))

    n = int("".join(sorted(n1))[::-1])
        
    return n
        
print(descending_order(151))