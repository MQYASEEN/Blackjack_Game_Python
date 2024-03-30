import random
import os
from assets import logo

def choosecard():
    """Choose Random Card from deck and return"""
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards=random.choice(deck)
    return cards

def calculatescore(cards):
    """Take cards list and return the sum of cards"""
    score=sum(cards)
    if score==21 and len(cards)==2:
        return 0
    if 11 in cards and score==21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw🙃"
    elif computer_score==0:
        return "You Loose Oppent Has Black Jack 😱"
    elif user_score==0:
        return "You Win With Black Jack 😎"
    elif user_score>21:
        return "You Went Over ! You Loose 😭"
    elif user_score>computer_score:
        return "You Win 😃"
    else:
        return "You Loose 😭"
def game():
    print(logo)
    u_cards=[]
    comp_cards=[]
    game_over=False
    for _ in range(2):
        u_cards.append(choosecard())
        comp_cards.append(choosecard())
    while not game_over:
        user_score=calculatescore(u_cards)
        computer_score=calculatescore(comp_cards)
        print(f"User Cards {u_cards} and Your score :{user_score}")
        print(f"Computer Cards :{comp_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            if input("Do You Want to Draw another Card tyep 'y' or 'n':")=='y':
                u_cards.append(choosecard())
            else:
                game_over=True
                
    while computer_score!=0 and computer_score<17:
        comp_cards.append(choosecard())
        computer_score=calculatescore(comp_cards)
    print(f'Your Cards {u_cards} and Your score:{user_score}')
    print(f'Computer Cards {comp_cards} and Computer score:{computer_score}')
    print(compare(user_score,computer_score))
    
while input("Do You Want to Play Game Type 'y' or 'n':")=='y':
    os.system("CLS")
    game()
