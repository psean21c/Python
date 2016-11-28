# DNA

### Step 1

Open the starter code: a2_org.py

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

The parameter is a potential DNA sequence. Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). There are at least 2 ways to approach this. One way is to count the number of characters that are not nucleotides and then at the end check whether there were more than zero. Another way is to use a Boolean variable that represents whether you have found a non-nucleotide character; it would start off as True and would be set to False if you found something that wasn't an 'A', 'T', 'C' or 'G'. You should construct test cases that contain only 'A's, 'T's, 'C's and 'G's, and you should also create examples that contain other characters. A string is not a valid DNA sequence if it contains lowercase letters.

insert_sequence() : (str, str, int) -> str

The first two parameters are DNA sequences and the third parameter is an index. Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. (You can assume that the index is valid.)For example, If you call this function with arguments 'CCGG', 'AT', and 2, then it should return 'CCATGG'. When coming up with more examples, think about where the second DNA sequence might be inserted: what are the extremes?

### Step 4

```
get_complement()
get_complementary_sequence()

```

get_complement(): (str) -> str

The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement. We have intentionally not given you any examples for this function. The Problem Domain section explains what a nucleotide is and what a complement is.

get_complementary_sequence(): (str) -> str

The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence. For example, if you call this function with 'AT' as the argument, it should return 'TA'.
