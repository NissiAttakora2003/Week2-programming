print("hello im a Program Temperatures please")
tep_day=[]
tot=0
avgtep=0
for i in range (0,3):
    tep=float(input("insert the temperature: "))
    tep_day.append(tep)
    tot+=tep_day[i]
avgtep=tot/3
print("the avarage temperature through day is", str(avgtep))
print("the max temp is : ",str(max(tep_day)))
print("the minmum values is :",str(min(tep_day)))
print ("the range  is",str(max(tep_day)-min(tep_day)) )


