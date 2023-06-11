import argparse
from Bio import SeqIO
import logging

parser = argparse.ArgumentParser(description='Assembly a DNA string based on sequences in a FASTA file.')
parser.add_argument('infile', help='Input FASTA file name')
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('Question3.log')
fh.setFormatter(f)
logger.addHandler(fh)

logger.debug('Start of the program.')

# Read sequences from Seq04.fasta
sequences = []
with open(args.infile, "r") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(record)

# Specify the minimum overlap length
min_overlap = 3

def find_overlap_endseq1_startseq2(seq1, seq2, min_overlap):
    '''
    Return the length of maximum overlap by compare end of sequence1 with start of sequence2
    '''
    max_overlap = 0
    for pos in range(len(seq2) - min_overlap + 1):
        if seq1.endswith(seq2[:len(seq2) - pos]):
            overlap_length = len(seq2) - pos
            if overlap_length > max_overlap:
                max_overlap = overlap_length

    return max_overlap

def find_overlap_endseq2_startseq1(seq1, seq2, min_overlap):
    '''
    Return the length of maximum overlap by compare end of sequence2 with start of sequence1
    '''
    max_overlap = 0
    for pos in range(len(seq1) - min_overlap + 1):
        if seq2.endswith(seq1[:len(seq1) - pos]):
            overlap_length = len(seq1) - pos
            if overlap_length > max_overlap:
                max_overlap = overlap_length
          
    return max_overlap

def assemble_sequences(sequences):
    '''
    Assemble two sequences
    '''
    assembled_sequence = str(sequences[0].seq)
    current_sequence = str(sequences[1].seq)
    
    for pos in range(1, len(sequences)):
        
        current_sequence = str(sequences[pos].seq)
        overlap_endseq1_startseq2 = find_overlap_endseq1_startseq2(assembled_sequence,current_sequence, min_overlap)
        overlap_endseq2_startseq1 = find_overlap_endseq2_startseq1(assembled_sequence,current_sequence ,min_overlap)
        logger.info('endseq1_position: ' + str(overlap_endseq1_startseq2))
        logger.info('endseq2_position: ' + str(overlap_endseq2_startseq1))
        if overlap_endseq2_startseq1 == overlap_endseq1_startseq2 == 0:
            if len(assembled_sequence) > len(current_sequence):
                assembled_sequence == assembled_sequence
            else:
                assembled_sequence == current_sequence    
        elif overlap_endseq1_startseq2 > overlap_endseq2_startseq1:
            assembled_sequence += current_sequence[overlap_endseq1_startseq2:]    
        else:
            assembled_sequence = current_sequence[:-overlap_endseq2_startseq1] + assembled_sequence
            
    return assembled_sequence

# Assemble sequences with overlaps
assembled_dna_string = assemble_sequences(sequences)

# Print the assembled DNA string
print(assembled_dna_string)
logger.info(assembled_dna_string)
logger.debug('End of the program.')
