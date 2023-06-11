from Bio import SeqIO
import argparse

# Create CLI for user inputting
parser = argparse.ArgumentParser(description='Assembly a DNA string based on sequences in a FASTA file.')
parser.add_argument('infile', help='Input FASTA file name')
args = parser.parse_args()

# Read sequence from input file
record = SeqIO.read(args.infile, "fasta")
sequence = record.seq

def count_kmers(sequence, k_size):
    '''
    Return a dictionary with key is kmer and value is count
    '''
    data = {}
    size = len(sequence)
    for i in range(size - k_size + 1):
        kmer = sequence[i: i + k_size]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    # Remove kmers with count 1 from the data dictionary
    data = {kmer: count for kmer, count in data.items() if count != 1}
    return data

# Separate key and value from the data dictionary
kmers = False
for i in range(10, len(sequence)):
    kmer_counts = count_kmers(sequence, i)
    if kmer_counts:
        for kmer, count in kmer_counts.items():
            print(f"{kmer}:{count}")
        kmers = True