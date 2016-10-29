# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:56:51 2016

@author: Abdullah A. Alam
"""

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return(len(dna))



def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    else:
        return False



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return(dna.count(nucleotide))


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return(dna2 in dna1)
    

def is_valid_sequence(dna):
    """ (str) -> bool
    
    The parameter is a potential DNA sequence. Return True if and only if 
    the DNA sequence is valid (that is, it contains no characters other 
    than 'A', 'T', 'C' and 'G'). There are at least 2 ways to approach this. 
    One way is to count the number of characters that are not nucleotides 
    and then at the end check whether there were more than zero. Another 
    way is to use a Boolean variable that represents whether you have 
    found a non-nucleotide character; it would start off as True and 
    would be set to False if you found something that wasn't an 'A', 'T', 
    'C' or 'G'. You should construct test cases that contain only 'A's, 
    'T's, 'C's and 'G's, and you should also create examples that contain 
    other characters. A string is not a valid DNA sequence if it contains 
    lowercase letters.
    
    >>> is_valid_sequence('ATCG')
    True
    
    >>> is_valid_sequence('BATCG')
    False
    
    """
    
    valid_sequence = 'ATCG'
    for letter in dna:
        if letter not in valid_sequence:
            return False
    return True


    


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    
    The first two parameters are DNA sequences and the third parameter is an 
    index. Return the DNA sequence obtained by inserting the second DNA 
    sequence into the first DNA sequence at the given index. (You can assume 
    that the index is valid.)For example, If you call this function with 
    arguments 'CCGG', 'AT', and 2, then it should return 'CCATGG'. When 
    coming up with more examples, think about where the second DNA sequence 
    might be inserted: what are the extremes?
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    
    """
    
    dna1_split1 = dna1[:index]
    dna1_split2 = dna1[index:]
    new_sentence = dna1_split1 + dna2 + dna1_split2
    return new_sentence
    
    
    
def get_complement(nucleotide):
    """ (str) -> str
    
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the 
    nucleotide's complement. We have intentionally not given you any 
    examples for this function. The Problem Domain section explains what a 
    nucleotide is and what a complement is.
    
    >>> get_complement('A')
    'T'
    
    >>> get_complement('T')
    'A'
    
    >>> get_complement('C')
    'G'
    
    >>> get_complement('G')
    'C'
    
    >>> get_complement('B')
    False
    
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return False
    
    
def get_complementary_sequence(dna):
    """ (str) -> str
    
    The parameter is a DNA sequence. Return the DNA sequence that is 
    complementary to the given DNA sequence. For example, if you call this 
    function with 'AT' as the argument, it should return 'TA'.
    
    >>> get_complementary_sequence('AT')
    TA
    
    """
    complementary_sequence = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    letters = list(dna)
    letters = [complementary_sequence[base] for base in letters]
    return ''.join(letters)

    