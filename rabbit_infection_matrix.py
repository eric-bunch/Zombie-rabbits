def answer(population, x, y, strength):
    
    # if the virus is not strong enough to infect patient z, 
    # then nothing happens
    if population[y][x] <= strength:
        population[y][x] = -1
    else:
        return population
    
    number_rows = len(population)
    number_cols = len(population[0])
    
    for i in range(0, number_rows):
        for j in range(0, number_cols):
            if population[i][j] == -1:
                # The first condition in these if statements will be 
                # checked first and if it is false then the statement is 
                # evaluated to false. The first condition checks to see 
                # if the rabbit is not an edge, and the second condition 
                # checks if it's neighbor is too weak to resist the virus
                if i > 0 and population[i - 1][j] <= strength:
                    population[i - 1][j] = -1
                    
                if i < number_rows - 1 and population[i + 1][j] <= strength:
                    population[i + 1][j] = -1
                    
                if j > 0 and population[i][j - 1] <= strength:
                    population[i][j - 1] = -1
                    
                if j < number_cols - 1 and population[i][j + 1] <= strength:
                    population[i][j + 1] = -1
                    
    # Here we run through the same checks as above, but in this 
    # case the conditions that would tell us to change a value 
    # in the population matrix will now tell us to call the 
    # function again so that the newly infected rabbits can have a
    # chance to infect more rabbits.
    for i in range(0, number_rows):
        for j in range(0, number_cols):
            if population[i][j] == -1:
                if i > 0 and 0 <= population[i - 1][j] <= strength:
                    return answer(population, x, y, strength)
                
                if i < number_rows - 1 and 0 <= population[i + 1][j] <= strength:
                    return answer(population, x, y, strength)
                    
                if j > 0 and 0 <= population[i][j - 1] <= strength:
                    return answer(population, x, y, strength)
                    
                if j < number_cols - 1 and 0 <= population[i][j + 1] <= strength:
                    return answer(population, x, y, strength)
    else:
        return population
