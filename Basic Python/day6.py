
#Dictionary

info  = {
    "name" : "Liakot",
    "address" : "Dinajpur",
    "age" : 23
}
for key, val in info.items():
    print(f'key is "{key}" value is "{val}"')

info["address"] = "HSTU"
print(info)

print(info.get("Name", "Liton"))

#Problem solution

number_dic = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
}
str = input("Input : ")

out = ""
for i in str:
    out += number_dic.get(i, "*") + " "
print(out)

#Functions
def hello(name, address):
    return f'Your Name is "{name}" and \n Address is "{address}"'

print(hello("Liakot Ali Liton", "Dinajpur"))
print(hello(address="Liakot", name="HSTU"))

#Try and except
try:
    age = int(input("Age : "))
    salary = 20000 / age
    print(salary, age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Division of zero is not valid")
