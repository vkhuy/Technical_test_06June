# Technical_test_06June
 
This repository contains all of my questions and solution in my technical test on 6th June 2023.

## Table of Contents


 - [Table of Contents](#table-of-contents)
 - [Questions](questions)
 - [Library](library)
 - [Input](input)
 - [Solution](solution)


## Questions

Question01: Given a DNA string (Seq01.fasta), report the sequence:numberofrepeat of the Kmers that has equal or greater than 10 base-pair. Using [argparser library](https://docs.python.org/3/library/argparse.html) for user inputing.

Question02: Building a consensus by taking 10 strings in Seq02.fasta in consideraIon. Use [logging library](https://docs.python.org/3/library/logging.html) to report the log file.

Question03: Assembly a DNA string based on 7 sequences in Seq03.fasta. Use both argparser and logging library.

## Library

Please download and install **Biopython** from [here](https://github.com/samtools/bcftools/releases/download/1.17/bcftools-1.17.tar.bz2) to read the FASTA file.

## Input

1. Seq01.fasta.
2. Seq02.fasta.
3. Seq03.fasta.

## Solution

You can find all of my solution question at Technical_test_06June.ipynb or for each question:

1. Question01.py
2. Question02.py
3. Question03.py

To input your sequences with CLI in Question01 and Question03, follow this instruction:

1. Open your terminal.
2. Copy this code.

```bash
python3 Question01.py Seq01.fasta
```

```bash
python3 Question03.py Seq03.fasta
```

3. Press Enter or Return.



