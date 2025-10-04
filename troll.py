def disemvowel(string_):
    vowel = [ 'a','e','i','o','u','A','E','I','O','U']
    s = ""    
    for i in string_:

        if i in vowel:
            pass

        else:

            s=s+i

    return s

print(disemvowel("Abin"))