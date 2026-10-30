name="Cici"
age=22
height=1.65
student_now=True
city="Poznan" 
print(name,"is",age,"years old")
print(type(name),type(age))
print(type(student_now),type(height))
print(type(city))

slices_per_student=3
student=10
enrolled_student=20
present_student=enrolled_student-student
total_slices_needed=present_student*slices_per_student
cost_per_student=500/present_student
boxes_to_order=total_slices_needed//8
leftover_slices=(boxes_to_order*8)%present_student