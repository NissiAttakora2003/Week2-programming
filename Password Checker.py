print("Be between 8 and 12 character long")
print(" Contain at least one uppercase letter")
print(" Contain at least one lowercase letter")
print(" Contain at least one digit")
print("  Contain at least one 'special character'")
def validpass(pas):
    print("print")
    digit = False
    upp = False
    low = False
    special = False
    for i in pas:
        if i.isdigit():
            digit = True
        if i.isupper():
            upp = True
        if i.lower():
            low = True
        if not i.isalnum():
            special = True
    if (digit==True) and (upp==True) and (low==True) and (special==True):
        print("good")
    else:
        print("bad")

    return pas


if __name__ == '__main__':
    pas = str(input("inseert password: "))
    while (len(pas) < 8 or len(pas) > 13):
        pas = str(input("inseert password: "))
    validpass(pas)





