
def breeding_like_rabbits(months, litter_size, life_expectancy):
    breeding_pairs = 1
    population_dct = {'mature': 0, 'juvenile': 0}
    mortality = [0]*life_expectancy

    for i in range(months):
        if i == 0:
            population_dct['juvenile'] = procreation(breeding_pairs, litter_size)
            mortality[0] = breeding_pairs
        else:
            breeding_pairs +=  population_dct['mature']
            population_dct['mature'] = population_dct['juvenile']

            population_dct['juvenile'] = procreation(breeding_pairs, litter_size)

            breeding_pairs -= mortality.pop()
            mortality.insert(0, population_dct['juvenile'])

        print(breeding_pairs)

    return breeding_pairs


def procreation(pairs, litter_size):
    return pairs * litter_size


print(breeding_like_rabbits(82,1,17))