#Grab the number of cards
file = open("input.txt", "r")
num_cards = len(file.readlines())
file.close()

file = open("input.txt", "r")

total_points = 0

#Pre initialize number of duplicate scratchcards
duplicates = {}
for i in range(0, num_cards):
    duplicates[i + 1] = 1

for card_num, line in enumerate(file.readlines()):
    line = line.replace('\n', '')
    card = line.split(":")[1]
    
    hand, winning = card.split("|")
    hand = hand.split(" ")
    winning = winning.split(" ")

    hand = [x for x in hand if x != '']
    winning = [x for x in winning if x != '']

    #Count the wins
    points = 0
    num_winning = 0
    for number in hand:
        if number in winning:
            num_winning += 1
            
    #Add the duplicate cards
    for i in range(card_num + 2, card_num + 2 + num_winning):
        duplicates[i] += duplicates[card_num + 1]

#Count the cards
import numpy as np
print(np.sum(list(duplicates.values())))
