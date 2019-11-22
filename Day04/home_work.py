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
                    file1.write(''.join([enzyme_key, ", ".join(final_site), "\n"]))




sequence = data["Rosalind_3684"]
site = enzyme_sites["HaeIII"]
offset = cutsite_offset["HaeIII"]

find_site(sequence, site, offset)