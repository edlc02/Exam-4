#!/usr/bin/env python3

import sys

def get_kmers(sequence, k):
    """
    Extracts k-mers of length k from a given DNA sequence and maps each k-mer to unique k-mer.
    Parameters:
        sequence (str): DNA from which k-mers are extracted.
        k (int): Length of k-mers.
    Returns:
        dict: Dict. where each key is a k-mer, and each value is a set of k-mers.
    """
    kmers = {}
    if k > 0 and len(sequence) >= k:
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]  # Current k-mer
            if i + k < len(sequence):
                next_kmer = sequence[i+1:i+1+k]  # k-mer that follows the current k-mer
                if kmer in kmers:
                    kmers[kmer].add(next_kmer)  # Add the next k-mer to the set of k-mers if already exists
                else:
                    kmers[kmer] = {next_kmer}  # Initialize a new set for new k-mers
    return kmers

def collect_kmers(filename, k):
    """
    Processes multiple DNA sequences from a file, collecting all k-mers of length k and their k-mers.
    Parameters:
        filename (str): The file path containing DNA sequences.
        k (int): Length of the k-mers.
    Returns:
        dict: Dict. of aggregated k-mers where keys are k-mers and values are sets of k-mers.
    """
    aggregate_kmers = {}
    with open(filename, 'r') as file:
        for line in file:
            sequence_kmers = get_kmers(line.strip(), k)
            for kmer, next_kmers in sequence_kmers.items():
                if kmer in aggregate_kmers:
                    aggregate_kmers[kmer].update(next_kmers)  # Merge sets if k-mer already exists
                else:
                    aggregate_kmers[kmer] = next_kmers  # Store new k-mer and its k-mers
    return aggregate_kmers

def find_optimal_k(filename):
    """
    Identifies the smallest k such that every k-mer in the sequence has exactly one unique k-mer.
    Parameters:
        filename (str): The file path containing DNA sequences.
    Returns:
        int: The smallest k value where each k-mer has exactly one k-mer.
    """
    k = 1  # Start checking from k=1
    while True:
        kmers = collect_kmers(filename, k)
        if not kmers:
            k += 1
            continue
        all_unique = all(len(next_kmers) == 1 for next_kmers in kmers.values())
        if all_unique:
            return k  # Return the smallest k that meets the condition
        k += 1  

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Exam_4.py <filename>")  # Command-line usage instruction
    else:
        filename = sys.argv[1]
        optimal_k = find_optimal_k(filename)  # Find the optimal k for the given file
        print(f"The optimal k is: {optimal_k}")  # Print the optimal k
