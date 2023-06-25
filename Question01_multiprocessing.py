import time
import argparse
from Bio import SeqIO
from multiprocessing import Pool

# Start timing
start_time = time.time()
# Create CLI for user input
parser = argparse.ArgumentParser(description='Assembly a DNA string based on sequences in a FASTA file.')
parser.add_argument('infile', help='Input FASTA file name')
args = parser.parse_args()

# Read sequence from input file
record = SeqIO.read(args.infile, "fasta")
sequence = record.seq

def count_kmers(kmer_size):
    '''
    Return a dictionary with key as kmer and value as count
    '''
    data = {}
    size = len(sequence)
    for i in range(size - kmer_size + 1):
        kmer = sequence[i: i + kmer_size]
        try:
            data[kmer] += 1
        except KeyError:
            data[kmer] = 1
    # Remove kmers with count 1 from the data dictionary
    data = {kmer: count for kmer, count in data.items() if count != 1}
    return data

def process_kmer_count(kmer_size):
    kmer_counts = count_kmers(kmer_size)
    if kmer_counts:
        for kmer, count in kmer_counts.items():
            print(f"{kmer}:{count}")

if __name__ == '__main__':
    # Number of processes to use
    num_processes = 4

    # Create a pool of processes
    pool = Pool(processes=num_processes)

    # Generate kmer sizes to process
    kmer_sizes = range(10, len(sequence))


    # Process kmers in parallel
    pool.map(process_kmer_count, kmer_sizes)

    # Close the pool
    pool.close()
    pool.join()

    # End timing
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
