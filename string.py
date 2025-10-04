def spin_words(sentence):
    # Your code goes 
    l = sentence.split()
    n=[]
    for i in l:
        if len(i)>5:
            n.append(i[::-1])
        else:
            n.append(i)
    return " ".join(n)

print(spin_words("Hey fellow warriors"))