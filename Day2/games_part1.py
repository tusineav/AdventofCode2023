file = open("input.txt", "r")

lines = file.readlines()

game_id_sum = 0
for line in lines:
    sum_game = True
    
    #Remove the random \n
    line = line.replace('\n', "")
    
    #Grab the game id
    game = line.split(": ")
    game_id = int(game[0].replace("Game ", ""))

    #Rest of the line without "Game x: "
    line = game[1]

    #Each round ends in ;, split all rounds
    rounds = line.split(";")
    
    for round in rounds:
        #split to get each cube + color individually
        cubes = round.split(", ")

        #Count each cube
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
            
            #If anything exceeds the max count, do not add this game to the sum
            if red_count > 12 or green_count > 13 or blue_count > 14:
                sum_game = False
        
    if sum_game:
        game_id_sum += game_id

print(game_id_sum)