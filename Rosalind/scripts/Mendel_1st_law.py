import itertools

def mendel_first_law(AA, AB, BB, allele):
    population = ['AA'] * AA + ['BB'] * BB + ['AB'] * AB
    possible_combinations = itertools.combinations(population, 2)
    probabilities = [allele_passed_on(pair, allele) for pair in possible_combinations]
    return sum(probabilities)/len(probabilities)


def allele_passed_on(pair, allele):
    if allele*2 in pair:
        return 1
    elif 'AB' in pair:
        if pair[0] == pair[1]:
            return 0.75
        else:
            return 0.5
    else:
        return 0


print(mendel_first_law(24,23,23,'A'))