print("enter your marks")
number = int(input())
print(number)

if (number>90 or number<100):
    grade = 'a'
elif (number>80 and number<100):
    grade = 'b'
else:
    grade = 'i dont know'

print("the grade is", grade)