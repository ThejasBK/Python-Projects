import itertools
import random

numbers = list('A23456789KQJ')
symbols = ['Spade', 'Diamond', 'Heart', 'Clover']
computer = 0
player = 0
computer_cards = []
player_cards = []

for _ in range(5):
    card1 = (random.choice(symbols), random.choice(numbers))
    card2 = (random.choice(symbols), random.choice(numbers))
    print(card1, card2)
    while card1 not in computer_cards:
        computer_cards.append(card1)
    while card2 not in player_cards:
        player_cards.append(card2)

computer_numbers = []
for i in computer_cards:
    computer_numbers.append(i[1])

player_numbers = []
for i in player_cards:
    player_numbers.append(i[1])

for i in range(1, 6):
    x = itertools.combinations(computer_numbers, i)
    for k in x:
        sum = 0
        for j in k:
            if j in 'AJKQ':
                sum += 10
            else:
                sum += int(j)
        if sum <= 21 and sum > computer:
             computer = sum

    x = itertools.combinations(player_numbers, i)
    for k in x:
        sum = 0
        for j in k:
            if j in 'AJKQ':
                sum += 10
            else:
                sum += int(j)
        if sum <= 21 and sum > player:
             player = sum

if computer > player:
    print('Computer scores {}, player scores {}. Hence, the computer wins'.format(computer, player)) 
elif player > computer:
    print('Computer scores {}, player scores {}. Hence, the player wins'.format(computer, player)) 
else:
    print('They both score {}. Hence, it\'s a draw'.format(computer))
