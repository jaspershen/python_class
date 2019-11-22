##function for reading fasta file
def read_fasta(fasta_filename):
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
            if linecount < 22 or linecount > 100:  # just for testing
                print(line, '*' + str(currSeqName) + '*')  # just for testing
            if linecount == 22:  # just for testing
                print('*********************')  # just for testing
            if line.startswith('>'):  # it's a new fasta record
                line = line.lstrip('>')  # line = line[1:]
                sequences[line] = ''  # intialize dictionary for this entry
                currSeqName = line
            else:
                sequences[currSeqName] += line
    return (sequences)

## read data
data = read_fasta("rosalind_dna.fsa")


enzyme_sites = {'EcoRI': 'GAATTC', 'HindIII': 'AAGCTT',
'BamHI': 'GGATCC', 'HpaI': 'GTTAAC',
'HaeIII': 'GGCC'}


cutsite_offset = {'EcoRI': 1, 'HindIII': 1, 'BamHI': 1,
'HpaI': 3, 'HaeIII': 2}


##function to find the site for a enzyme in a sequence
def find_site(sequence, site, offset):
    '''
    :param sequence: the DNA sequence
    :param site: recongization site of enzyme
    :param offset: offset of enzyme
    :return: a list of site
    '''
    final_site = [i for i in range(len(sequence)) if sequence.startswith(site, i)]
    final_site = [x + offset for x in final_site]
    return final_site


##function to find the fragments by a enzyme in a sequence

# sequence = data["Rosalind_6820"]
# sequence
#
# site = enzyme_sites["EcoRI"]
# offset = cutsite_offset["EcoRI"]
#
# find_site(sequence, site, offset)
# find_fragment(sequence, site, offset)

def find_fragment(sequence, site, offset):
    '''
    :param sequence: the DNA sequence
    :param site: recongization site of enzyme
    :param offset: offset of enzyme
    :return: a list of site
    '''
    final_site = [i for i in range(len(sequence)) if sequence.startswith(site, i)]
    if len(final_site) == 0:
        return []
    else:
        final_site = [x + offset for x in final_site]
        final_site1 = final_site + [0]
        final_site2 = final_site + [len(sequence)]
        final_site1.sort()
        final_site2.sort()
        final_fragment = [final_site2[i] - final_site1[i] for i in range(len(final_site1))]
        return final_fragment



##function to find the complementary sequence
def find_complentary_sequence(sequence):
    complentary_sequence = []
    for i in range(len(sequence)):
        complentary_sequence.append("TAGC"["ATCG".find(sequence[i])])
    complentary_sequence = ''.join(complentary_sequence)
    return(complentary_sequence)



## Part 1 code

output_file1 = "part1_file.txt"

with open(output_file1, "w") as file1:
    for sequence_key in data:
        sequence = data[sequence_key]
        sequence_final_site = {}
        for enzyme_key in enzyme_sites:
            site = enzyme_sites[enzyme_key]
            offset = cutsite_offset[enzyme_key]
            final_site = find_site(sequence, site, offset)
            sequence_final_site[enzyme_key] = final_site

        site_len = [len(x) for x in list(sequence_final_site.values())]

        if max(site_len) > 0:
            print("Sequence:", sequence_key, "(Cut sites)", "\n")
            # file1.write("Sequence:", sequence_key, "(Cut sites)")
            file1.write("\n")
            file1.write(' '.join(["Sequence:", sequence_key, "(Cut sites)", "\n"]))
            for enzyme_key in sequence_final_site:
                final_site = sequence_final_site[enzyme_key]
                if len(final_site) > 0:
                    final_site = [str(x) for x in final_site]
                    print(enzyme_key, ",".join(final_site))
                    file1.write(' '.join([enzyme_key, ", ".join(final_site), "\n"]))



## Part 2 code

output_file2 = "part2_file.txt"

with open(output_file2, "w") as file2:
    for sequence_key in data:
        sequence = data[sequence_key]
        sequence_final_site = {}
        sequence_final_fragment = {}
        for enzyme_key in enzyme_sites:
            site = enzyme_sites[enzyme_key]
            offset = cutsite_offset[enzyme_key]
            final_site = find_site(sequence, site, offset)
            final_fragment = find_fragment(sequence, site, offset)
            sequence_final_site[enzyme_key] = final_site
            sequence_final_fragment[enzyme_key] = final_fragment

        site_len = [len(x) for x in list(sequence_final_site.values())]

        if max(site_len) > 0:
            print("Sequence:", sequence_key, "(Cut sites)", "\n")
            # file2.write("Sequence:", sequence_key, "(Cut sites)")
            file2.write("\n")
            file2.write(' '.join(["Sequence:", sequence_key, "(Cut sites)", "\n"]))
            for enzyme_key in sequence_final_site:
                final_site = sequence_final_site[enzyme_key]
                if len(final_site) > 0:
                    final_site = [str(x) for x in final_site]
                    print(enzyme_key, ",".join(final_site))
                    file2.write(''.join([enzyme_key, ", ".join(final_site), "\n"]))

            print("Sequence:", sequence_key, "(fragment sizes)", "\n")
            file2.write("\n")
            file2.write(' '.join(["Sequence:", sequence_key, "(fragment sizes)", "\n"]))
            for enzyme_key in sequence_final_fragment:
                final_fragment = sequence_final_fragment[enzyme_key]
                if len(final_fragment) > 0:
                    final_fragment = [str(x) for x in final_fragment]
                    print(enzyme_key, ",".join(final_fragment))
                    file2.write(' '.join([enzyme_key, ", ".join(final_fragment), "\n"]))




## Part 3 code
#get the sequence and complent sequence

sequence_key = list(data.keys())[0]
enzyme_key = list(enzyme_sites.keys())[0]

output_file3 = "part3_file.txt"

with open(output_file3, "w") as file3:
    for sequence_key in data:
        sequence = data[sequence_key]
        sequence_final_site = {}

        for enzyme_key in enzyme_sites:
            site = enzyme_sites[enzyme_key]
            offset = cutsite_offset[enzyme_key]
            final_site = find_site(sequence, site, offset)
            sequence_final_site[enzyme_key] = final_site

        ##get the index for sequence printing
        complentary_sequence = find_complentary_sequence(sequence)
        sequence1 = list(sequence)
        complentary_sequence1 = list(complentary_sequence)
        index = list(range(0, len(sequence), 61))
        index1 = index.copy()
        index2 = index.copy()

        index2 = [x - 1 for x in index2]

        index1 = index1[:-1]
        index2 = index2[1:]

        ##the last DNA bases inclused?
        if index2[-1] != len(sequence):
            index1 = index1 + [index2[-1] + 1]
            index2 = index2 + [len(sequence)]

        index3 = list(zip(index1, index2))

        ##print and output DNA sequence
        print("Sequence: ", sequence_key, "\n")
        file3.write(' '.join(["Sequence:", sequence_key, "\n", "\n"]))

        for i in index3:
            idx1 = i[0]
            idx2 = i[1]
            for j in sequence_final_site:
                site_index = sequence_final_site[j]
                if len(site_index) == 0:
                    pass
                else:
                    for z in range(len(site_index)):
                        temp_site_index = site_index[z]
                        if temp_site_index >= idx1 and temp_site_index <= idx2:
                            print('|'.rjust(temp_site_index - idx1 + 13))
                            file3.write(''.join(['|'.rjust(temp_site_index - idx1 + 13), "\n"]))

            print(str(idx1 + 1).rjust(10), ''.join(sequence1[idx1:idx2]).rjust(60))
            print(''.join(complentary_sequence1[idx1:idx2]).rjust(71), "\n")
            file3.write(''.join([str(idx1 + 1).rjust(10), ''.join(sequence1[idx1:idx2]).rjust(60), "\n"]))
            file3.write(''.join([''.join(complentary_sequence1[idx1:idx2]).rjust(71), "\n", "\n"]))








