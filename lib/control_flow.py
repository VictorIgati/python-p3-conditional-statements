#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

    # Test cases
print(admin_login("sudo", "12345"))  # Output: "Access denied"
print(admin_login("admin", "12345"))  # Output: "Access granted"
print(admin_login("ADMIN", "12345"))  # Output: "Access granted"    
    
def hows_the_weather(temp):
    if temp <= 40:
        return "It's brisk out there!"
    elif temp>=40 and temp<=65:
        return "It's a little chilly out there!"
    elif temp>=85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"            
print(hows_the_weather(33))  # Output: "It's brisk out there!"
print(hows_the_weather(99))  # Output: "It's too dang hot out there!"
print(hows_the_weather(75))  # Output: "It's perfect out there!"
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(op, num1, num2):
    if op =='+':
        return(num1 + num2)
    elif op =='-':
        return(num1 - num2)
    elif op =='*':
        return(num1 * num2)
    elif op =='/':
        if num2 ==0:
            return "Error: num2 cannot be divided by  0"
        else:
            return(num1 / num2)    

    else:
        print("Invalid operation!")
        return None
                

print(calculator("+", 1, 2))
print(calculator("-", 1, 2))
print(calculator("*", 1, 2))
print(calculator("/", 1, 1))
print(calculator("/", 1, 0))
print(calculator("nope", 4,2))