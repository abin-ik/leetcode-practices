def to_camel_case(text):
    count=0
    l=""
    for i in range(len(text)):
        if text[i] == "-" or text[i] == "_":
            count =1
            pass
        else:
            if count == 1:
                l1=text[i].upper()
                l=l+l1
                count=0
            else:
                l=l+text[i]
    return l

print(to_camel_case("the-stealth-warrior"))