def compute(aloha):
    if type(aloha) == str:
        return aloha + "!"
    elif type(aloha) == int:
        return "Hey Doc, we have a number!"

print(compute(3))
