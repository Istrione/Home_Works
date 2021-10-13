#Задание №5
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []
def get_jokes(number: int):

    i = 0
    while i != int(number):
        a = random.randrange(len(nouns))
        b = random.randrange(len(adverbs))
        c = random.randrange(len(adjectives))
        get_jokes = (nouns[a], adverbs[b], adjectives[c])
        jokes.append(' '.join(get_jokes))
        i = i + 1
    print(jokes)

get_jokes(2)

