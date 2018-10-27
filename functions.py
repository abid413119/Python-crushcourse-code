# FUNCTION 

# Create a function 

def sayHello(name):
    print('Hello', name)

sayHello('Abid')

# Return a Value
def getSum(num1, num2):
    total = num1 + num2
    return total

sum = getSum(1, 2)
print(sum)

# Immutable data 
def addNumber(num):
    num = num + 1
    print("Value of num inside function: ", num)

num = 5
addNumber(num)
print("Value of num outside function: ", num)


# Mutable data 
def addInList(myList):
    myList.append(4)
    print("Value inside functon: ", myList)

myList = [1, 2, 3]
addInList(myList)
print("Value outside function: ", myList)