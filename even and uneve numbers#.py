n0=int(input("insert a number of grades : "))
grd_list=[]
for i in range (0,n0):
     num=int(input("insert grade: "))
     grd_list.append(num)
sorted(grd_list)
print(grd_list)
if (n0%2)==0:#even number
     n=int(n0/2)
     y=int((n0/2)-1)
     print("the median value is :",str(grd_list[y]),",",str(grd_list[n]))
else:
     n=int(n0/2)
     print("the median value is :", str(grd_list[n]))









