print("Be between 8 and 12 character long")
print(" Contain at least one uppercase letter")
print(" Contain at least one lowercase letter")
print(" Contain at least one digit")
print("  Contain at least one 'special character'")

def validpass(pas):
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
    if (digit == True) and (upp == True) and (low == True) and (special == True)  and (len(pas)>8 and len(pas) <13):
        print("Nice the pasword is strong")
    else:
        print("bad password")
        badpass=True

    return pas



if __name__ == '__main__':
    pas = str(input("insert password: "))
    validpass(pas)








