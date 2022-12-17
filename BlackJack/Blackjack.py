#!/usr/bin/python3
import os
import random
from blackjack_art import logo
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    print(logo)

    dhand = []
    uhand = []
    is_game_over = False

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def compare(uscore, dscore):
        if uscore == dscore:
            return "It is a Draw!"
        elif dscore == 0:
            return "You Lose, Oponet has a BlackJack!"
        elif uscore == 0:
            return "You Win - BlackJack"
        elif dscore > 21:
            return "You Win - Oponet went over the score"
        elif uscore > 21:
            return "You Lose, You went ovr the score!"
        elif uscore > dscore:
            return "You Win!"
        elif dscore > uscore:
            return "You Lose, Oponet has a higher score!"
        else:
            return "You Lose!"

    for _ in range(2):
        dhand.append(deal_card())
        uhand.append(deal_card())

    while not is_game_over:

        def calc_score(cards):
            '''Take a list of cards and return scores'''
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)
            if sum(dhand) == 21 or sum(uhand) == 0:
                return 0

            return sum(cards)

        uscore = calc_score(uhand)
        dscore = calc_score(dhand)

        print(f"User cards {uhand} user total is {sum(uhand)}")
        print(f"Dealer is showing card {dhand[0]}")

        if uscore == 0 or dscore == 0 or uscore > 21:
            is_game_over = True
        else:
            another_card = input("Another card? 'y' or 'n' to pass ").lower()
            if another_card == "y":
                uhand.append(deal_card())
            else:
                is_game_over = True

    while dscore != 0 and dscore < 17:
        dhand.append(deal_card())
        dscore = calc_score(dhand)

    print(f"\nYour cards {uhand} and your score {sum(dhand)}")
    print(f"Oponet cards {dhand} and the oponets score {sum(dhand)}\n")

    print(compare(uscore, dscore))


while input("\nDo you want to play a game of BlackJack? 'y' or 'n': ").lower() == 'y':
    os.system('clear')
    play_game()
