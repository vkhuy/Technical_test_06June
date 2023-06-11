import numpy as np
from Bio import SeqIO
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('Question2.log')
fh.setFormatter(f)
logger.addHandler(fh)

logger.debug('Start of the program.')

# Read sequences from Seq02.fasta
sequences = []
with open("Seq02.fasta", "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))

# Check if all records have the same length
sequence_length = len(sequences[0])
all_same_length = all(len(seq) == sequence_length for seq in sequences)
if all_same_length:
    logger.info('All sequences have the same length.')
else:
    logger.debug("Sequences have different lengths.")

# Determine the consensus sequence
consensus = np.empty(sequence_length, dtype='U1')
for pos in range(sequence_length):
    column = np.array([seq[pos] for seq in sequences])
    unique, counts = np.unique(column, return_counts=True)
    max_count = np.max(counts)
    bases_with_max_count = unique[counts == max_count]

    if len(bases_with_max_count) == 1:
        consensus[pos] = bases_with_max_count[0]
    else:
        consensus[pos] = 'N'

# Convert the consensus array to a string
consensus_sequence = ''.join(consensus)

# Print the consensus sequence
print(consensus_sequence)
logger.info(consensus_sequence)
logger.debug('End of the program.')