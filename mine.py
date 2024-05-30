'''def maths(factorial):
    if factorial == 1:
        return 1
    
    else:
        return factorial * maths(factorial - 1)
    
print(maths(5))'''

def factorial(numbers):
    if numbers == 1:
        return 1
    
    else:
        return numbers * factorial(numbers - 1)
    
print(factorial(11))

def label(recursion):
    if (recursion > 0):
        result = recursion + label(recursion - 1)
        print(result)

    else:
        result = 0
    return result

print("\n\nRecursion results are...")
label(10)
   
def my_label(trouble):
    if trouble > 0:
        result = trouble + my_label(trouble - 1)
        print(result)

    else:
        result = 0
    return result
print("\n\nThe important numbers are:")
my_label(20)