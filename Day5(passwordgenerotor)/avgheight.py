stu_he =input("input a list of student heights").split()
tot_height=0
no_of_stu = 0
for i in range(0,len(stu_he)):
    stu_he[i]= int(stu_he[i])
for i in range(0,len(stu_he)):
    tot_height = tot_height + stu_he[i]
    no_of_stu = no_of_stu + 1
print("total heights of student is ",tot_height)
print("total no of students is ",no_of_stu)
avg_height= round(tot_height/no_of_stu)
print("average height of students is {avg_height}")
    
    
   

