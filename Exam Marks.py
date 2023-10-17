print("hello im a program designed to take grades")
num = int(input("how many mark you got ? : "))
grade_list = []
totgrade=0
avg=0
for x in range(0, num):
  grade = float(input("insert you grade = "))
  if grade >0 and grade<100:
    grade_list.append(grade)  # it upgrade the list
    totgrade += grade_list[x] # add the value of each grade
  else:
     print("error the mark inserted does not match our criteria (0-100)")
avg=totgrade/num
print( "the avarage score is : ", avg)
print("here is the order of grade you inserted :", str(grade_list))
print("the sum of each grade is : ", str(totgrade))
print("the highest grade is :", str(max(grade_list)))
print("the lowest grade is ", str(min(grade_list)))