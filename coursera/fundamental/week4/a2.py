def get_length(dna):
    """ (str) -> int
    Return the length of the DNA sequence dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int
    Return the number of occurrences of nucleotide in the DNA sequence dna.
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    return (dna2 in dna1)
	
def is_valid_sequence(dna):
    """(str) -> bool
    """
    isValid = True
    sequence = "ATCG"
    for i in dna:
        if i not in sequence:
            isValid = False		
            break			
    return isValid



def insert_sequence(dna1, dna2, idx):
    """(str, str, int) -> str
	>>> insert_sequence('CCGG', 'AT',2)
	'CCATGG'
    """
    #print(dna1[:idx] + ":" + dna2 + ":"+ dna1[idx:])
    return dna1[:idx] + dna2 + dna1[idx:]

def get_complement(nucleotide):
    complement = ''
    if nucleotide == 'A':
        complement = 'T'
    if nucleotide == 'T':
        complement = 'A'
    if nucleotide == 'C':
        complement = 'G'
    if nucleotide == 'G':
        complement = 'C'
    return complement

def get_complementary_sequence(dna):
    complementary = ""
    for d in dna:
        complementary += get_complement(d)
    return complementary


