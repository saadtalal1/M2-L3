digit1=(input("Please enter the first digit: "))
digit2=(input("Please enter the second digit: "))
digit3=(input("Please enter the third digit: "))
print("Your number is",digit1+digit2+digit3)
num=int(digit1+digit2+digit3)
d1=int(digit1)
d2=int(digit2)
d3=int(digit3)
calculation=(d1**3)+(d2**3)+(d3**3)
while calculation==num:
    print("This is an armstrong number")
    break
else:
    print("This is not an armstrong number")
