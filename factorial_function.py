# Python code​​​​​​‌‌​​​‌​​​​​‌​​‌​‌​‌‌​‌​‌​ to return factorial of a number
# Focus : Recursive Function

def factorial(num):
# Check if num is a positive integer or 0
    if type(num) != int:
        return None
    if num < 0: 
        return None
    if num == 0:
        return 1

# identifying a pattern
# 2! = num * 1 = 2
# 3! = num * 2 = 6 
# 4! = num * 6 = 24
# 5! = num * 24

    f = num * factorial(num - 1)       
    return f
    

