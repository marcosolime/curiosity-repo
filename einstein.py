def compute(aloha):
    if type(aloha) == str:
        return aloha + "!"

def salud():
    name = input('Put here your name: ')
    return str.capitalize(name)

print(compute(3))
print(salud())