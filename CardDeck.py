import time
import random


class Card:  # класс Карта
    NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10',
                "Валет", "Дама", "Король", "Туз"]
    MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, i, j):  # конструктор
        self.Mastb = self.MastList[i - 1]  # карта
        self.Num = self.NumsList[j - 1]  # масть


class DeckOfCards:
    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self, i):
        if 0 <= i <= 55:
            answer = self.deck[i].Num
            answer += " "
            answer += self.deck[i].Mastb
        else:
            answer = "В колоде только 56 карт"
        return answer


deck = DeckOfCards()  # создали колоду
deck.shuffle()
print('Выберите карту из колоды в 56 карт:')
n = int(input())
if n <= 56:
    card = deck.get_card(n - 1)
    print('Вы взяли карту: ', card, end='.\n')
else:
    print("В колоде только 56 карт")
