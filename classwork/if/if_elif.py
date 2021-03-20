time=int(input('enter the time:'))
if time<=12:
    print(f'It is {time}am')
elif time>=12 and time <= 24:
    print(f'it is {time}pm')
else:
    print("enter the correct time.")

age=int(input("enter your age:"))
if age<=15:
    print("you are a child")
elif age<=15 and age>=40:
    print('you are adult')
else:
    print('you are old')
