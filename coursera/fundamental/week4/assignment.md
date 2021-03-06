# DNA

### 

A2 Problem Domain: Deoxyribo Nucleic Acid (DNA)

![dna](https://cloud.githubusercontent.com/assets/5623445/20695483/525625ca-b5ba-11e6-90f5-8c03a36c0b31.jpg)

The problem domain for A2 is Deoxyribonucleic Acid (DNA), the double-stranded molecule that encodes genetic information for living organisms. DNA is made up of four kinds of nucleotides, which are molecules that bond together to form DNA sequences.

The four nucleotides are adenine (A), guanine (G), cytosine (C), and thymine (T). Each strand of DNA is a sequence of nucleotides, for example AGCTAC. In a program, we will use a string representation of this, 'AGCTAC'.

DNA has 2 strands in a double helix. The nucleotides in one strand are bonded to the nucleotides in the other strand. A and T can be bonded together, and thus complement each other; similarly, C and G are complements of each other.

You can see a picture of this on the Wikipedia page for DNA. The two strands in DNA are complementary because each nucleotide in one strand is bonded with its complement in the other strand. 

Thus, given the DNA sequence ACGTACG, its complementary strand is TGCATGC.

```
ACGTACG
TGCATGC
```

### Step 1

Open the starter code: `a2_org.py`

### Step 2

```
get_length()
is_longer()
count_nucleotides()
contains_sequence()
```

### Step 3

```
is_valid_sequence()
insert_sequence()
```
is_valid_sequence() : (str) -> bool

The parameter is a potential DNA sequence. Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). There are at least 2 ways to approach this. 

One way is to count the number of characters that are not nucleotides and then at the end check whether there were more than zero.

Another way is to use a Boolean variable that represents whether you have found a non-nucleotide character; 

it would start off as True and would be set to False if you found something that wasn't an 'A', 'T', 'C' or 'G'. You should construct test cases that contain only 'A's, 'T's, 'C's and 'G's, and you should also create examples that contain other characters. A string is not a valid DNA sequence if it contains lowercase letters.

insert_sequence() : (str, str, int) -> str

The first two parameters are DNA sequences and the third parameter is an index. Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. (You can assume that the index is valid.)

For example, If you call this function with arguments 'CCGG', 'AT', and 2, then it should return 'CCATGG'. When coming up with more examples, think about where the second DNA sequence might be inserted: what are the extremes?

### Step 4

```
get_complement()
get_complementary_sequence()

```

get_complement(): (str) -> str

The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement. We have intentionally not given you any examples for this function. The Problem Domain section explains what a nucleotide is and what a complement is.

get_complementary_sequence(): (str) -> str

The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence. For example, if you call this function with 'AT' as the argument, it should return 'TA'.
