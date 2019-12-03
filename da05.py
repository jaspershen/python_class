import numpy as np
import pandas as pd
import re as re
import os as os
os.getcwd()

os.chdir("Day05")


def seq_list_from_fastq_file(filename):
    seq_list = []
    quality_list = []

    with open(filename) as FASTQ_INPUT:
        line_cnt = 0
        for line in FASTQ_INPUT:
            line_cnt += 1
            if line_cnt == 2:
                seq_list.append(line.strip())
            if line_cnt % 4 == 0:
                quality_list.append(line.strip())
                line_cnt = 0

    return seq_list, quality_list


# file = os.listdir()
# file
# file_name = "ENCFF733YBM-trunc.fastq"

def read_fastp(file_name):
    name_list = []
    seq_list = []
    comment_list = []
    quality_list = []

    with open(file_name) as fastq_file:
        line_cnt = 0
        for line in fastq_file:
            line_cnt += 1
            if line_cnt == 1:
                name_list.append(line.strip())
            if line_cnt == 2:
                seq_list.append(line.strip())
            if line_cnt == 3:
                comment_list.append(line.strip())
            if line_cnt == 4:
                quality_list.append(line.strip())
                line_cnt = 0

    return name_list, seq_list, comment_list, quality_list


fastq_filename = 'ENCFF733YBM-trunc.fastq'

name, sequence, comment, quality = read_fastp(fastq_filename)

name
len(name)
comment
len(comment)
sequence
len(sequence)
quality
len(quality)


# string at index 0 of list
print('Length of sequence list = ', len(sequence), ',\tFirst sequence = \'', \
      sequence[0], '\'', sep='')
print('Length of quality list  = ', len(quality),  ',\tFirst quality  = \'', \
      quality[0], '\'', sep='')

# take apart quality value encoding
for x in range(len(sequence[0])):
    print('{}\t{}\t{}\t{}\t{}'.format(sequence[0][x],
                                              quality[0][x],
                                              ord(quality[0][x]) - 33,
                                              (ord(quality[0][x]) - 33) * -0.1,
                                              pow(10, (ord(quality[0][x]) - 33) * -0.1 )))



# Return the Unicode code point for a one-character string.
# ord()

# a little easier to view with just the unique characters
quality_set = set(list(quality[0]))

# add float and scientific notation to output of probability
print('char\tASCII\tqual\texponent\tprob')
for x in quality_set:
    print('{}\t{}\t{}\t{:f}\t{:e}'.format(x,
                                        ord(x),
                                        ord(x) - 33,
                                        (ord(x) - 33) * -0.1,
                                        pow(10, (ord(x) - 33) * -0.1 )))




import math as math
# Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
# chr()


import gzip


import jupyter



pow()

