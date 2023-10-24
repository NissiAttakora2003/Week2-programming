if __name__ == '__main__':
    time="am"
    templist=[]
    temptot=0
    index=0
for i in range (8,20,2):
    if i > 10:
        time = "pm"
    celsius=float(input(f"insert themperature at {i} {time} :" ))
    templist.append(celsius)
    temptot += templist[index]
    index += 1
print("the temperature list is during te day :", str(templist))
print("the highest temperature ever registered during the day was :", str(max(templist)))
print(" the lowest temperature ever registered was : ", str(min(templist)))
avaragetemp = temptot/5
print(" the average temperature during the day was :", str(avaragetemp))
fahrenheit = (celsius*(9/4))+32
print("the equivalent of", str(celsius), "°C", "is", str(fahrenheit), "°F")
