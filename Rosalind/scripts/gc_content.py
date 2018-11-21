def file_parser(file_obj):
    rtn_dct = {}
    for line in file_obj:
        if line[0] == '>':
            key = line[1:].strip('\n')
            rtn_dct[key] = []
        else:
            value = line.strip('\n')
            rtn_dct[key].append(value)
    return {k: ''.join(v) for k, v in rtn_dct.items()}


def gc_percentage(sequence):
    t = len(sequence)
    gc = 0
    for base in sequence:
        if base in ['G', 'C']:
            gc += 1
    return (gc/t) * 100


def gc_content_calculator(path):
    gc_content_dct = {}
    with open(path, 'r') as inf:
        fasta_dct = file_parser(inf)
        for entry in fasta_dct:
            gc_content_dct[entry] = gc_percentage(fasta_dct[entry])
    largest = max(gc_content_dct, key=gc_content_dct.get)
    return largest, round(gc_content_dct[largest], 6)


print(gc_content_calculator('/Users/johnmcgonigle/Downloads/rosalind_fibd.txt'))
