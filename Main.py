gamespace = [0, 1, 0,
             0, 1, 0,
             0, 1, 0]

second_gamespace = [0, 0, 0,
                   0, 0, 0,
                   0, 0, 0]

def timepass(cycles, gamespace, second_gamespace):
    for i in range(cycles):
        for x in range(9):
            count = 0
            if ((x) % 3) == 0: # left edge
                if x<=3:
                    if gamespace[x + 3] == 1:
                           count += 1
                    if gamespace[x + 4] == 1:
                        count += 1
                if x >= 3:
                    if gamespace[x - 3] == 1:
                       count += 1
                    if gamespace[x - 2] == 1:
                        count += 1
                if gamespace[x + 1] == 1:
                    count += 1
            if ((x) % 3) == 1: # middle edge
                if x <= 4:
                    if gamespace[x + 3] == 1:
                        count += 1
                    if gamespace[x + 4] == 1:
                        count += 1
                    if gamespace[x + 2] == 1:
                        count += 1
                if x >= 4:
                    if gamespace[x - 3] == 1:
                        count += 1
                    if gamespace[x - 4] == 1:
                        count += 1
                    if gamespace[x - 2] == 1:
                        count += 1
                if gamespace[x - 1] == 1:
                    count += 1
                if gamespace[x + 1] == 1:
                    count += 1
            if ((x) % 3) == 2: # right edge
                if x <= 5:
                    if gamespace[x + 3] == 1:
                        count += 1
                    if gamespace[x + 2] == 1:
                        count += 1
                if x >= 5:
                    if gamespace[x - 3] == 1:
                        count += 1
                    if gamespace[x - 4] == 1:
                        count += 1
                if gamespace[x - 1] == 1:
                    count += 1
            if gamespace[x] == 1:
                if count > 3 or count < 2:
                    second_gamespace[x] = 0
                else:
                    second_gamespace[x] = 1
            else:
                if gamespace[x] == 0:
                    if count == 3:
                        second_gamespace[x] = 1
        print(second_gamespace[0:3])
        print(second_gamespace[3:6])
        print(second_gamespace[6:9])
        print("-------------------------------------------------------")
        gamespace = second_gamespace.copy()

timepass(10, gamespace, second_gamespace)

