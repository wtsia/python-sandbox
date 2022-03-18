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
    userInput = input('enter a target guess with similar length to target: ')
    if userInput == shutoffCommand:
        break
    elif userInput < len(target):
        userInputDiff = len(target) - len(userInput)
        print('answer is ' + userInputDiff + ' less than target')
        continue
    elif userInput > len(target):
        userInputDiff = len(userInput) - len(target)
        print('answer is ' + userInputDiff + ' more than target')
        continue
    print('length of string is', len(userInput))
print('Task completed')