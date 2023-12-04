file = open("input.txt", "r")

total_points = 0

for line in file.readlines():
    line = line.replace('\n', '')
    cards = line.split(":")[1]
    
    hand, winning = cards.split("|")
    hand = hand.split(" ")
    winning = winning.split(" ")

    hand = [x for x in hand if x != '']
    winning = [x for x in winning if x != '']

    points = 0
    for card in hand:
        if card in winning:
            if points == 0:
                points = 1
            elif points != 0:
                points *= 2
    total_points += points

print(total_points)