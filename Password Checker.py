
def validpass(pas):
    isinvalid=True
    digit = False
    upp = False
    low = False
    special = False
    lenght = False
    for i in pas:
        if (pas>8 and pas<13):
            lenght=True
        if i.isdigit():
            digit = True
        if i.isupper():
            upp = True
        if i.lower():
            low = True
        if not i.isalnum():
            special = True
    print(pas)
    if (digit == True) and (upp == True) and (low == True) and (special == True) and ( lenght== True):
        print("Nice the pasword is strong")
    else:
        print("bad")
        isinvalid=False
    return isinvalid
if __name__ == '__main__':
    print(" im the password checker here is are the requisite for your password ")
    print(" Be between 8 and 12 character long")
    print(" Contain at least one uppercase letter")
    print(" Contain at least one lowercase letter")
    print(" Contain at least one digit")
    print(" Contain at least one 'special character'")
    pas = str(input("insert your password: "))

    validpass(pas)
    if isinvalid==False:
        validpass(pas)


