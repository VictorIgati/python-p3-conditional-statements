#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass
def hows_the_weather(temp):
    if temp <= 40:
        return "It's brisk out there!"
    elif temp>=40 and temp<=65:
        return "It's a little chilly out there!"
    elif temp>=85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"            

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(num1, num2, op):
    if op =='+':
        return(num1 + num2)
    elif op =='-':
        return(num1 - num2)
    elif op =='*':
        return(num1 * num2)
    elif op =='/':
        return int((num1 / num2))
        if num2 ==0:
            return "Error: num2 cannot be divided by  0"
    else:
        print("Invalid operation")
        return None
                

print(calculator(1, 1, "+"))
print(calculator(3, 1, "-"))
print(calculator(3, 2, "*"))
print(calculator(4, 2, "/"))
print(calculator("nope", 4,2))