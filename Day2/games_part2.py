#The main process is identical to part 1, except for the totalling

import numpy as np

file = open("input.txt", "r")

lines = file.readlines()

game_power = 0
for line in lines:
    sum_game = True
    
    line = line.replace('\n', "")
    
    game = line.split(": ")
    game_id = int(game[0].replace("Game ", ""))

    line = game[1]
    rounds = line.split(";")
    
    max_red = max_blue = max_green = -np.inf
    for round in rounds:
        cubes = round.split(", ")

        red_count = blue_count = green_count = -1
        for index, color in enumerate(cubes):
            if "red" in color:
                red_count = int(color.replace(" red", ""))
            elif "blue" in color:
                blue_count = int(color.replace(" blue", ""))
            elif "green" in color:
                green_count = int(color.replace(" green", ""))
        
        
            if red_count == -1:
                red_count = 0
            elif green_count == -1:
                green_count = 0
            elif blue_count == -1:
                blue_count = 0
            
            #Rather than checking for a max, keep track of the biggest number
            max_red = max(max_red, red_count)
            max_green = max(max_green, green_count)
            max_blue = max(max_blue, blue_count)
    
    #Then just multiply
    game_power += max_red * max_green * max_blue
    
print(game_power)
    

