# Fizzbuzz: iterate from 1 to 100, and for every 3rd number, print out 'fizzbuzz'
# design: get an array of integers from 1 to 100, for loop through every number and if divisible by 3, print Fizzbuzz, otherwise print the number

def fizzbuzzOnetoOneHundred():
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizzbuzz")
        else:
            print(i)
    else:
        print("the result is done")

# new challenge: make it able to choose a 3rd number from any array of numbers
# design: iterate through an array and print numbers, but when the index of the array is divisible by 3, print fizzbuzz

userInput = [1, 4, 5, 6, 7, 8, 9, 0]

def fizzbuzzParser(array, i=0):
    print('index begins at ', i)
    for i in array:
        if i % 3 == 0:
            print("Fizzbuzz")
            i += 1
            print('index is ', i)
        else:
            print(array[i])
            i += 1
            print('index is ', i)
    else:
        print("task completed")

print('running fizzbuzz')
print(fizzbuzzParser(userInput))