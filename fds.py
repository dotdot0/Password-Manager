
#Slices the string upto @
def stringmod(s):
    for i in range(0, len(s)+1):
        if s[i] == '@':
            return s[0:i]
