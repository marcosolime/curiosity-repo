def compute(aloha):
    if type(aloha) == str:
        return aloha + "!"
    elif type(aloha) == int:
        return "Hey Doc, we have a number!"

def salud():
    name = input('Put here your name: ')
    return str.capitalize(name)

def give():
    print("Give")

def foolish():
    print("this is a random message")

print(compute(3))
print(salud())
foolish()

car = input("tell me: ")
