#while loops

print("enter a number")
number = int(input())

while(number>4):
    print("number is greater than 4")
    number = int(input())
    if (number ==9):
        break#after 9 input loop will exit
    if number ==8:
        continue#continue statement is used to break endstatement of loop
    print("loop ended")