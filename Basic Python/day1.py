
name = "liakot "
print(name * 9)
name = input("Enter your name : ")
color =  input("Your favourite color : ")
print(name + ' likes ' + color)

hight = input("Your height(inch) : ")
weight = input("Your weight(kg) : ")
hight = float(hight)
weight = int(weight)
hight = (hight * 2.54)/100
#print("hight is : " + str(hight))
bmi = weight/(hight*hight)
print('Your BMI is : ' + str(bmi))

index = "this string is for index check"
print(index[6:8])
print(index[:9])
print(index[5:])
print(index[1:-1])

first = 'hello'
last = 'Liakot'
msg = f'''{first} "{last}", you're genius'''
print(msg)

print(index.replace('string', 'paragraph'))
print('for' in index)

