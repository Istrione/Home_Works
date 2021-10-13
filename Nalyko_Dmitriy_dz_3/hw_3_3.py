#Задание №3
def thesaurus(*names):

    state = {}
    for name in names:
        key = name[0].capitalize()
        if key not in state:
            state[key] = []
        state[key].append(name)
    return state
print(thesaurus("Иван", "Дмитрий", "Наталья", "Илья"))


