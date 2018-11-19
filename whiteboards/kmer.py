from time import time

from random import choice
from itertools import islice
from collections import defaultdict



def make_kmer_list(k, n):
    bases = ['A', 'T', 'G', 'C']
    rtn_lst = []
    for i in range(n):
        rtn_lst.append(''.join([choice(bases) for i in range(k)]))
    return rtn_lst


def sliding_window(k, seq):
    """Returns all kmers of size k from a sequence seq."""
    iterable = iter(seq)
    result = tuple(islice(iterable, k))
    if len(result) == k:
        yield result
    for kmer in iterable:
        result = result[1:] + (kmer,)
        yield result


def record_kmers(lst_of_seqs, k):
    codon_dct = defaultdict(list)
    codon_fequencies = defaultdict(int)

    for i in range(len(lst_of_seqs)):
        seq = lst_of_seqs[i]

        codons = sliding_window(k, seq)

        for codon in codons:
            codon = ''.join(codon)
            codon_dct[codon].append(seq)
            codon_fequencies[codon] += 1

    return codon_dct, codon_fequencies


def sort_dict_by_values(d, reversed):
    return sorted(d, key=d.get, reverse=reversed)


def get_target_sequences(codon_dct, sorted_codons):
    # Now we need to get a subset of targets on which to perform further analysis so:
    kmer_not_found = True  # set a logic gate
    i = 0  # value to keep track of our position
    current_pool = codon_dct[sorted_codons[1]]  # we start with sequences containing the rarest codons as these
    # are the most likely to be the most 'different'

    # This is where we'll store our potential targets:
    targets = []

    # Iterate through until we find a target that contains 2 of the rarest codons.
    while kmer_not_found:
        i += 1
        current_sequences = codon_dct[sorted_codons[i]]
        for kmer_seq in current_sequences:
            if kmer_seq in current_pool:
                # if we find a sequence that has both the rarest
                kmer_not_found = False
                targets.append(kmer_seq)
            else:
                current_pool.extend(current_sequences)

    return targets


def reduce_by_rarity(lst_of_sequences, k):
    sequences = lst_of_sequences
    for i in reversed(range(1, k+1)):
        # Record kmers present in each sequence, using a sliding window technique
        # To minimise iterations we record the sequences containing the kmers and the kmer frequencies separately
        kmer_dct, kmer_frequencies = record_kmers(sequences, i)

        # Sort the ckmers by their frequency so we evaluate the rarest codons first
        sorted_kmers = sort_dict_by_values(kmer_frequencies, False)

        targets = get_target_sequences(kmer_dct, sorted_kmers)

        if len(targets) == 1:
            return targets
        else:
            sequences = targets
    return targets


def time_function_runtime(func, *args):
    def wrapper(*args):
        t = time()
        func(*args)
        t1 = time()
        print(t1-t)
    return wrapper


@time_function_runtime
def run(no_of_values, kmer_size, starting_window_size):
    six_mers = make_kmer_list(kmer_size, no_of_values)  # Generate the kmers to iterate over
    targets = reduce_by_rarity(six_mers, starting_window_size)  # start with a sliding window of 3
    print(len(targets))


run(40, 6, 4)
run(400, 6, 4)
run(4000, 6, 4)


run(40, 2000, 200)


