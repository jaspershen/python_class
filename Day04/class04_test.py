# using set to find the unique letters in a string
# create a new empty dictionary
nt_count = {}
nt_count
# get a set of unique characters in our DNA string
dna = 'GTACCNTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
dna
type(dna)
list(dna)
tuple(dna)

unique = set(dna)
unique

type(unique)

len(unique)

unique = set(dna)
print('unique nt: ', unique) ## {'C', 'A', 'G', 'T', 'N'}

dna.count("A")
dna.count("T")
dna.count("C")
dna.count("G")
dna.count("N")
dna.count("H")


nt_count = {}
# iterate through each unique nucleotide
for nt in unique:
  # count the number of this unique nt in dna
  count = dna.count(nt)

  # add our count to our dict
  nt_count[nt] = count

nt_count
type(nt_count)

len(nt_count)

nt_count.items()
nt_count.keys()
nt_count.values()
nt_count.get("A")

print('nt count:', nt_count)


animal_list = ['ewe', 'cat', 'dog', 'pig', 'hog', 'bat', 'cow',
               'ant', 'fox', 'rat', 'yak', 'ram', 'ape']

animal_list

animal_list.count("ewe")

print('Number of items in list:', len(animal_list))

# typical generator of integers for loop operation
range(len(animal_list))
for i in range(len(animal_list)):
    print(i)

type(animal_list)

animal_list[0]
animal_list[1]
animal_list[2]

for animal_i in range(len(animal_list)):
    print(animal_i, animal_list[animal_i])


# can use in many variations : range(start, stop, step)
len(animal_list) - 1

range(len(animal_list) - 1)
test = range(len(animal_list) - 1, -1, -1)


for i in range(len(test)):
    print(i, test[i])

for animal_i in range(len(animal_list)-1, -1, -1):
    print(animal_i, animal_list[animal_i])


help(range)

range(10, 2)


range(0, 5, 1)

test = range(0, 5, 2)


test2 = list(test)


len(test2)

test2[0]
test2[1]
test2[2]


test2
type(test2)
range(len(test2))

range(len(animal_list))

for i in range(len(test2)):
    print(i, test2[i])

# can use in many variations : range(start, stop, step)
for animal_i in range(len(animal_list)-1, -1, -1):
    print(animal_i, animal_list[animal_i])


range(0, len(animal_list), 2)

# jumping through with a defined step
for animal_i in range(0, len(animal_list), 2):
    print(animal_i, animal_list[animal_i])


# slice of list before len()
for animal_i in range(len(animal_list[3:7])):
    print(animal_i, animal_list[animal_i])


test = enumerate(animal_list)
test
type(test)
len(test)
test2 = list(test)
test2
type(test2)
len(test2)
test2[0]
type(test2[0])
print(list(enumerate(animal_list)))


# define list of numbers
numbers = [5, 7, 6, 5, 0, 1, 2, 9, 5, 6, 2, 8, 8, 7, 8, 9, 3, 3, 8]
numbers
deltas = []

# start at 1 so the second part of the delta calculation is 0
# range is like slicing, the end number is one more than what it generates.
# Said another way, range does not include the *end* number

print('number of items in the list numbers =', len(numbers),
      '\nrange output =', list(range(1,len(numbers))))

range(1, len(numbers))

list(range(1, len(numbers)))


# enumerate() example
print(numbers, '\n')

#print(enumerate(numbers), end='\n\n')
#print(list(enumerate(numbers)))

#for i, number in enumerate(numbers):
#    print(i, number)


# calculate difference by defining index
print('numbers  :', numbers)

for i in range(1, len(numbers)):
    delta = numbers[i] - numbers[i - 1]
    deltas.append(delta)
print('range    :', deltas)



enumerate(numbers[1:])
numbers[1:]

test = enumerate(numbers[1:])
test
test2 = list(test)
test2
test2[0][0]
# calculate difference by using result of enumerate()
deltas = []

for i, number in enumerate(numbers[1:]):
    delta = number - numbers[i]
    deltas.append(delta)
print('enumerate:', deltas)


print(list(enumerate(numbers)))



# global vs local variables
###全局变量和局部变量,和R种类似
def set_local_x_to_five():
  print('Inside def')
  x = 5 # local to set_local_x_to_five()
  y = 5
  print("x =", x)
  print("y =", y)

print('After def')
x = 100 # global x
y = 100 # global
print('x=', x)
print('y=', y)

set_local_x_to_five()
print('After function call')
print('x=', x)
print('y=', y)


##判断语句
# if, elif, else

range(1, 51)
list(range(1,51))
for x in range(1, 51):
    if (x % 3 == 0) and (x % 5 == 0):
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)



# zip two lists together to make a dictionary or array of tuples
numbers = [1, 2, 3]##list
letters = ['a', 'b', 'c']##list
test = zip(numbers, letters)
type(test)
list(test)
type(test)
len(test)
test
dict(test)

new_d = dict(zip(numbers, letters))
print('new_d', new_d)
new_l = list(zip(numbers, letters))
print('new_l', new_l)

# can use range, as its just making a list of integers
animal_dict = dict(zip(range(len(animal_list)), animal_list))
print(animal_dict)


# .format

# Type	Meaning
# d	Decimal integer
# c	Corresponding Unicode character
# b	Binary format
# o	Octal format
# x	Hexadecimal format (lower case)
# X	Hexadecimal format (upper case)
# n	Same as 'd'. Except it uses current locale setting for number separator
# e	Exponential notation. (lowercase e)
# E	Exponential notation (uppercase E)
# f	Displays fixed point number (Default: 6)
# F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
# g	General format. Rounds number to p significant digits. (Default precision: 6)
# G	Same as 'g'. Except switches to 'E' if the number is large.
# %	Percentage. Multiples by 100 and puts % at the end.


# writing a file with FizzBuzz results

numbers

with open('test_file.txt', mode='w') as test_fh:
    for x in range(1, 101):
        if (x % 3 == 0) and (x % 5 == 0):
            test_fh.write('{0:3d}\t{1:s}\n'.format(x, 'FizzBuzz'))
        elif x % 3 == 0:
            test_fh.write('{0:3d}\t{1:s}\n'.format(x, 'Fizz'))
        elif x % 5 == 0:
            test_fh.write('{0:3d}\t{1:s}\n'.format(x, 'Buzz'))
        else:
            test_fh.write('{0:3d}\n'.format(x))






# Find most common letter used by Skakespeare
# load the complete file into a string

FILENAME = 'shakespeare.txt'

with open(FILENAME, mode='r') as Shake_File:
    ShakespeareFileText = Shake_File.read()
#    ShakespeareFileText = Shake_File.read().upper()

len(ShakespeareFileText)

print('Size of {0:s} is {1:,d} and {2:,d}'.format(FILENAME, len(ShakespeareFileText), len(ShakespeareFileText)))

print(ShakespeareFileText[:300])

## ShakespeareFileText will be a single string holding the full text of
## the file ("shakespeare.txt")



# the characters to search for in the text
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'

## Convert the ALPHABET string 'ABC...' into a list of characters
## ['A', 'B', 'C', ...]
AlphList = list(ALPHABET)

#print(AlphList)

## Start with an empty list of counts
IncidenceList = []

for char in AlphList:
    # Do the this code block for every item in AlphList
    # Count number of occurrences of character in ShakespeareFileText.
    #
    # Append count to IncidenceList
    IncidenceList.append(ShakespeareFileText.count(char))

# how else could this have been done?
# make a dictionary with char:count

print(IncidenceList)

# Useful function: For any list of numbers max(List) is the largest
# value in the list
MaxAlpha = max(IncidenceList)
MaxAlpha
# two possible ways to find the character associated with MaxAlpha
# initialize counter for the number of times through the for loop
char_count = 0
if MaxAlpha in IncidenceList:
    for list_item in IncidenceList:
        if MaxAlpha == list_item:
            print('The character found most often is \'{0:s}\' with {1:,d} occurances'
                  .format(ALPHABET[char_count], list_item))
        char_count += 1
else:
    print('Error MaxAlpha not found in IncidenceList!')

IncidenceList.index(MaxAlpha)

print('The character found most often is \'{0:s}\' with {1:,d} occurances'
      .format(ALPHABET[IncidenceList.index(MaxAlpha)], MaxAlpha))



# Parse bionet restriction enzyme data file
#

# *** FORMAT of file ***
#
# last line of header starts with '..'

# EXAMPLE of enzyme file:
# enz  cut rec seq  overhang  isoscizomers         commer            refs

'''
;AanI	3	TTA'TAA	0	!	PsiI	>B	1089
AarI	11	CACCTGCnnnn'nnnn_	4	!	>B	368,662
;AasI	7	GACnn_nn'nnGTC	-2	!	DrdI,DseDI	>B	495
AatII	5	G_ACGT'C	-4	!	ZraI	>BIKMNV	293,294,1002
;Aba6411II	3	CrrTAAG	0	?	!	>	680
'''

FILENAME = 'rebase_gcgenz.txt'

header_flag = False
end_of_header_start = '..'
enz_count = 0
enz_dict = {}



with open(FILENAME, 'r') as rebase_f:
    for line in rebase_f:
        if header_flag and len(line) > 30 and ';' not in line[0:10]:
            cols = line.rstrip('\n').split('\t')
            # data line
            enz_name = cols[0]
            enz_cut = cols[1]
            enz_seq = cols[2].replace('\'', '').replace('_','')
            enz_overhang = int(cols[3])
            enz_dict[enz_name] = [enz_cut, enz_seq, enz_overhang, cols[2]]
            enz_count += 1
        if line.startswith(end_of_header_start):
            # found last line of header
            header_flag = True

print('Read rebase_gcgenz.txt. Loaded', enz_count, 'enzymes.\n')

enz_dict
len(enz_dict)
enz_dict
enz_dict.keys()
enz_dict["AarI"]

find_these = ['EcoRI', 'HindIII', 'HaeIII']


output_str = ''
#output_str = 'Enzyme\tCut\tSeq\tOver\tSummary\n'

for enz in enz_dict:
    print(enz)
    if enz in find_these:
        output_str += ('\nEnzyme: {0:s}\n\tCut {1:d}\tSeq {2:s}\tOverhang {3:d}\tSummary {4:s}'
                        .format(enz, int(enz_dict[enz][0]), enz_dict[enz][1],
                         enz_dict[enz][2], enz_dict[enz][3]))
#        output_str += ('{0:s}\t{1:d}\t{2:s}\t{3:d}\t{4:s}\n'
#                        .format(enz, int(enz_dict[enz][0]), enz_dict[enz][1],
#                         enz_dict[enz][2], enz_dict[enz][3]))


print(output_str)


# Type	Meaning<br>
# <	Left aligned to the remaining space<br>
# ^	Center aligned to the remaining space<br>
# >	Right aligned to the remaining space<br>
# =	Forces the signed (+) (-) to the leftmost position

# https://www.programiz.com/python-programming/methods/string/format


print('Enzyme:')
for item, value in enz_dict.items():
    #print('{} ({})'.format(item, '\t'.join(list(value) )))
    print('{0:8s}\t{1:>2s}\t{2:^25s}\t{3:>2d}\t{4}\n'
          .format(item, value[0], value[1], value[2], value[3]), end='')


# reverse complement a DNA sequence

sequence_string = 'CGCGGGCGTAGTTAGTTCCTCACCAGAACGTCATTTGGTCCTCATCAATC'
base_complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

rev = []

for i in range(len(sequence_string),0,-1):
    rev.append(base_complement_dict[sequence_string[i-1]])

revcomp = ''.join(rev)

print ('input   : 5\'-' + sequence_string + '-3\'')
print ()
print ('revcomp : 5\'-' + revcomp + '-3\'')


# print both strands

print ('input   : 5\'-' + sequence_string + '-3\'')
print ('revcomp : 3\'-' + revcomp[::-1] + '-5\'')

#from random import random
import random

for x in range(10):
    print(random.random())

# random.random, is it random
flips = pow(10, 4)

for outer_loop in range(1, 10):
    heads = 0
    tails = 0
    count = 0
    round_head = 0
    int_head = 0
    for inner_loop in range(flips):
        roll = random.random()
        if round(roll, 2) >= .5:
            round_head += 1
        if roll >= .5:
            int_head += 1
        if round(roll, 2) >= .5:
            heads += 1
        else:
            tails += 1
        count += 1

    # print('h = ' + str(heads), 't = ' + str(tails), 'count = ' + str(count),
    #      't% = ' + str(round(tails/count, 4)), sep='\t\t')

    print('h = {0:4d}\tt = {1:4d}\tcount = {2:5d}\tt% = {3:.2f}'
          .format(heads, tails, count, round((tails / count) * 100)))


# continue & break
count = -1
while True:
    count+=1
    print("count:" , count)
    if count == 3:
        continue
    if count == 6:
        break
    print("line after our continue")
print("Done")





a = 2 # 3, 2, 2
b = 5 # 4, 3, 5
c = True
d = False

while a == 2:
    print('\n0: begining\t', a, b, c, d)
    if b > 4:
        print('1: break\t', a, b, c, d)
        break
    if c:
        print('2: Truth\t', a, b, c, d)
        c = False
        continue
    elif not d:
        print('3: elif\t\t', a, b, c, d)
        c = True
        d = True
    else:
        b += 1
        a += 1
    print ('4: after if\t', a, b, c, d)
else:
    print('\n5: exiting\t', a, b, c, d)


def read_fasta(fasta_filename):
    '''
    Go through file, reading one line at a time, using a
    dictionary to store the DNA sequence for each of the FASTA
    entries (Gavin Sherlock, November 28, 2019)
    '''
    with open(fasta_filename, mode='r') as fasta_file:

        sequences = {}

        for line in fasta_file:
            line = line.rstrip()
            if line.startswith('>'): # it's a new fasta record
                line = line.lstrip('>') #line = line[1:]
                sequences[line] = '' # intialize dictionary for this entry
                currSeqName = line
            else:
                sequences[currSeqName] += line

    return(sequences)


sequences = read_fasta('rosalind_dna.fsa')

type(sequences)

key = sequences.keys()
key = list(key)
key[0]
sequences[key[0]]

# find all ATGs in sequence
for seq in sequences:
    atg_index = 0
    last_index = 0
    start_stop = []
    if seq != 'Rosalind_6820':
        continue
    while(atg_index > -1):
        atg_index = sequences[seq].find('ATG', atg_index + 1)
        if (atg_index > -1):
            print('found ATG in', seq, 'at', atg_index)



for seq in sequences:
    atg_index = 0
    last_index = 0
    start_stop = []
    if seq != 'Rosalind_6820':
        continue
    while(atg_index > -1):
        atg_index = sequences[seq].find('ATG', atg_index + 1)
        if (atg_index > -1):
            for codon_i in range(atg_index + 3, len(sequences[seq])-3, 3):
                if sequences[seq][codon_i:codon_i+3] in ['TAA', 'TAG', 'TGA']:
                    print(seq, ': start =', atg_index, 'end =', codon_i+3,
                          'nt length =', codon_i + 3 - atg_index,
                          'aa length =', (codon_i - atg_index) / 3)
                    print(sequences[seq][atg_index:codon_i+3], '\n')
                    atg_index = codon_i+3
                    break


def read_fasta_test(fasta_filename):
    '''
    Go through file, reading one line at a time, using a
    dictionary to store the DNA sequence for each of the FASTA
    entries (Gavin Sherlock, November 28, 2019)

    Remove all lines that end with '# just for testing' after
    you understand what this function is doing
    '''
    with open(fasta_filename, mode='r') as fasta_file:

        sequences = {}
        currSeqName = ''  # just for testing
        linecount = 0  # just for testing

        for line in fasta_file:
            line = line.rstrip()
            linecount += 1  # just for testing
            print(line, '|', currSeqName, '|', linecount)  # just for testing 2
            input('next:')  # just for testing 2
            if line.startswith('>'):  # it's a new fasta record
                line = line.lstrip('>')  # line = line[1:]
                sequences[line] = ''  # intialize dictionary for this entry
                currSeqName = line
            else:
                sequences[currSeqName] += line

    return (sequences)


read_seqs = read_fasta_test('rosalind_dna.fsa')
print('Read', len(read_seqs), 'sequences')



# Iterating over a list

myList = [1, 2, 3, 4, 5, 6]

for item in myList:
    print(item, item*5)

# Iterating over a dictionary

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Option 1
for key, value in myDict.items():
    print(key, value, value * 5)

print()

# Option 2
for key in myDict:
    value = myDict[key]
    print(key, value, value * 5)


x = 0

while x < 5:
    print(x)
    x += 1    # what would happen if we didn't have this line?

i = 0

while True:
    if i in [1,2,3,4]:
        print(i)
    i += 1
    if i == 5:
        print("Finished")
        break


print('Finished!')