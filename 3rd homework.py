class Game():
    def __init__(self, jizni, slovo):
        self.jizni = jizni
        self.slovo = slovo
        spisok = list(slovo)
        poehalo = ['_' for i in spisok]
        while True:
            print(' '.join(poehalo))
            print('Осталось жизней: ', jizni)
            bukva = input('Введи букву: ').strip(' ').lower()
            if bukva in spisok:
                for i, c in enumerate(spisok):
                    if c == bukva:
                        poehalo[i] = bukva
                if '_' not in poehalo:
                    print("Красавец! Я верил в тебя!")
                    break
            else:
                jizni -= 1
            if jizni == 0:
                print('Ну ты и лох, ахаха!')
                break
        print(' '.join(poehalo))
g = Game(3, input('Введи слово:').strip(' ').lower())
print(g.slovo)