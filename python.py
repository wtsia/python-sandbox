# basics
welcome_message = "Initializing of hello Client"
print(welcome_message)

def function():
    welcome_message = 'Client Initialized after running through function'
    print(welcome_message)

function()

print(welcome_message.title())

test = 'nothing'

# while and break
shutoffCommand = 'exit'
target = 'target'

while True:
    userInput = input('enter a target guess with similar length to target (type exit to leave): ')
    if userInput == shutoffCommand:
        break
    elif len(userInput) < len(target):
        userInputDiff = len(target) - len(userInput)
        print('answer is less than target by', userInputDiff)
        continue
    elif len(userInput) > len(target):
        userInputDiff = len(userInput) - len(target)
        print('answer is more than target by', userInputDiff)
        continue
    print('length of string is', len(userInput))
print('Task completed')