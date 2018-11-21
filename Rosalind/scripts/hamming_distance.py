import itertools
import sys
from string import ascii_uppercase as alphabet



def hamming_distance(seqA, seqB):
    distance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            distance += 1
    return distance


def hamming_distance_calculator(sequenceA, sequenceB):
    if len(sequenceA) != len(sequenceB):
        print(f'Inputs of unequal length A: {sequenceA} and B: {sequenceB}')
        sys.exit(1)
    else:
        return hamming_distance(sequenceA, sequenceB)

A = 'GAGCCTACTAACGGGAT'
B = 'CATCGTAATGACGGCCT'

# print(hamming_distance_calculator(A, B))
# print(hamming_distance_calculator(A, 'A'))

X = 'CTCCGCATCGACGTCACCGCAGCAGGCCGATTTCGTTGAAATTGAATTGGCCCGAGCATGGTGACTAATGCTAGGCAGCGGTCAGTCTGCTCCGATACACCCCTTCGGGTTTTCCTTATTACTGACTAGTGTTAGAAATGGTCCAGATGTTCGAAAAGCCCTCCGCGTGGACTGGTCAATAAATGGTAGATCCCGCTGGTATACGCCATTAGCCTTCCTGCGTGAAGGTAGACCCATCCCCGGACAGGCAGGTCTGAGTAACATAAAACGGGAGCCAACCAAACGTTGAATCCTCATAAAGAGTTAGTTCAAAGCCCCGATACGCCCTTAGCGCCTCCATTAGGTGACACACGAGCGGCGGTGGGGGCAGGTAGATGATCCATGCATGTTTAATGGTCGTTGCACATACCTGAGACCAGACGCTCAATCTAGAAGGCCCTCATAGTCGTCCTCAAGCTGTCTGACAAACATACCCTGTATGGGGACTAGGTCTAAGCGGGGGGCCTAATGTACTTAGATCTAAAGTCCTCTCGCAAAGTCCAGCGGTAACGATTTACTTACTCGGGCTGCGAGGAGCCATTCGATTTGACACAAACTGGACAAGATTTCGTTCACCGCGCGAATATGACTATGATAGGATATCGTGACAGATGTGAGATCATCTCGTGACCGGGGGGCCGGGTGCGATTGCTGCGTTTGGCGTTTTCGCTGCTATGCAGGGAGGTGGAGTTCCGTTCCGTCCTTCCTCAGCTGCCCGGTTGGCATTCAATATGCCTATCATCAAGCCCATAAGCACAAGTTGCGGCCCGCAAAACGAAGACACACGCTGGGAACCGAAAAATCGTCAGGAGTACCCCACTATTTGGGCGGGGATCATAGAATTGAGCACAGACAGAAGGATAACGAACCTCAGAGACGCGTGCGGTGTTGTGGATGATTGTAGGGCCTTCTTCCGACCTTATACGGAACG'
Y = 'GTGTAGTGTAGCATTGGGCCATTAACCAAAATTAGGTGACATAGGAGGAACGCGGGCATGGTACCTAATGCTACGGGGTGCTGTTTGTAATCTAAAACACCCTTTGGGTTTTTTCTAGGCGGACACTAGTATTAGGCATAGGTCAAACGTTTGGCAACATTCCATCGGCGTTTCTTCAATAACTGGGATGACCTGCTGGATTACACAATTGGCCACCCTGAATTCACGTACACCCATCGTCTGACTCGGCACTCTCAGTAAGCTCTTTAGGGAGGCAACGGGAGTAGGAGTGCTTGGTTATGGTTTGTGTCGCTACTCTATGCGCCCATGCGCGCCCTAGGGTCTGATAAAGCAGCGATGATCGGATAAGGTGATTAATTAACCCCTGTACTTTCGGCTTATCTCCTTCAAGAGGGATGGCGAGCAATCTATCAGTCGCATCATGCCCACTACCCGAATTCTGCCCTGCGTGTCGAATAATATGCCTAGTCAAAGACGGCCGTCCCGGAGTCGAGACACCTAACTTCTGGCCGAGGAGGTGAGTCAGACGGATTTACTAACTCAGCTGGCGATTGAGGATGCGACCTGTACCCGATGAGAGGGCTTTGCTGACTCCGCTGAAGTATAACGCGGGCCGCACAACGAGAGAGATATCCGAACACGTCGTGGCCCCCGTGCCGGATTTTATCTCTGCCCTTACCGTTTTCGCGTTTATTATGATAGTACGACTATCCTCCAGTAGTGCGTCTGCTCCTTGTTTGGGCGTGAGTCAGTTAATAATCGAGCGCTTATCTAGCAGTGGTGTGTCGGAACACATTGGGCCTCTCACGATATTGTATGCCCTGGAGTAGTCCCATACAACTAACGCAGCGATCGTAGGGCGGATAATAGACATGTGTTATGAAGATCCCGGGGCCGCGGGGCTCTTAGAGTACACACGTGTGATCCGCATCCAATCTTAGGTCGAGGC'

# print(hamming_distance_calculator(X, Y))


def number_of_permutations(n):
    blocks = range(1,n+1)
    block_permutations = list(permutations(blocks))
    print(len(block_permutations))
    for x in block_permutations:
        print(' '.join([str(item) for item in x]))


def permutations(numbers):
    return itertools.permutations(numbers)

# number_of_permutations(5)


def make_kmers(bases, n):
    rtn_lst = []
    for base in bases:
        kmers = [base] * len(bases)
        kmers = extension(kmers, bases)

        for i in range(n-2):
            kmers = kmers * len(bases)
            kmers.sort()
            kmers = extension(kmers, bases)

        rtn_lst.extend(kmers)
    return  rtn_lst


def extension(seeds, bases):
    bases = bases * int(len(seeds)/len(bases))
    for i in range(len(bases)):
        seeds[i] += bases[i]
    return seeds


def variable_length_generator(bases, n):
    print(bases)
    rtn_mers = []
    for i in range(1, n+1):
        rtn_mers.extend(list(make_kmers(bases, i)))
    rtn_mers.extend(bases)
    return list(set(rtn_mers))


def permutation_with_replacement(bases, n, variable_length=False, lexicographical=True):

    if variable_length:
        kmers = variable_length_generator(bases, n)
    else:
        kmers = list(make_kmers(bases, n))

    if lexicographical:
        kmers.sort()
    else:
        kmers = none_lexicographical_ordering(kmers, bases)

    print(kmers[-4:])

    with open('/Users/johnmcgonigle/kmers.txt', 'w') as o:
        for kmer in kmers:
            o.write(kmer+'\n')


def none_lexicographical_ordering(lst, values):
    """ This function returns a list sorted by the order the values appear.

    E.g:
        values = ['C', 'B', 'A']
        lst = ['CC', 'BA', 'AA', 'CB', 'BC', 'AC']

        would be ordered:
        rtn = ['CC', 'CB', 'BC', 'BA', 'AC' 'AA']
    """

    values_dct = {x: i for i, x in enumerate(values)}
    print(values_dct)
    ordering_values = [calculate_ordering_values(values_dct, s) for s in lst]
    return [x for (y,x) in sorted(zip(ordering_values,lst), key=lambda pair: pair[0])]


def calculate_ordering_values(dct, string):
    return ''.join([alphabet[dct[s]] for s in list(string)])


# permutation_with_replacement(bases=['A', 'G', 'T', 'C'], n=2)

# permutation_with_replacement(bases=['A', 'B', 'C', 'D', 'E', 'F', 'G'], n=3)

# permutation_with_replacement(['D', 'N', 'A'], 3, variable_length=True, lexicographical=False)

permutation_with_replacement(['S', 'L', 'K', 'Z', 'R', 'N', 'O', 'G', 'F', 'P'], 3, variable_length=True, lexicographical=False)