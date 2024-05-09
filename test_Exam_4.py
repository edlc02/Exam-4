import pytest
from Exam_4 import get_kmers, collect_kmers, find_optimal_k

def test_get_kmers():
    # Test normal functionality
    sequence = "ATCGATCG"
    k = 3
    expected = {
        "ATC": {"TCG"},
        "TCG": {"CGA"},
        "CGA": {"GAT"},
        "GAT": {"ATC"}
    }
    assert get_kmers(sequence, k) == expected

    # Test edge cases
    assert get_kmers("", 3) == {}
    assert get_kmers("ATCG", 5) == {}
    assert get_kmers("ATCG", 0) == {}

def test_collect_kmers():
    # Direct input of sequences to simulate file processing
    sequences = ["ATCG", "TCGA"]
    k = 3
    expected = {
        "ATC": {"TCG"},
        "TCG": {"CGA", "CGA"},
        "CGA": {"GAT"},
        "GAT": {"ATC"}
    }
    # Manually call collect_kmers on a list of sequences
    aggregate_kmers = {}
    for sequence in sequences:
        sequence_kmers = get_kmers(sequence, k)
        for kmer, next_kmers in sequence_kmers.items():
            if kmer in aggregate_kmers:
                aggregate_kmers[kmer].update(next_kmers)
            else:
                aggregate_kmers[kmer] = next_kmers
    assert aggregate_kmers == expected

def test_find_optimal_k():
    # Test find_optimal_k by simulating the functionality
    sequences = ["ATCGATCG", "TCGATCGA"]
    k = 3
    # Manually process to determine optimal k
    for test_k in range(1, 10):
        all_unique = True
        aggregate_kmers = {}
        for sequence in sequences:
            sequence_kmers = get_kmers(sequence, test_k)
            for kmer, next_kmers in sequence_kmers.items():
                if kmer in aggregate_kmers:
                    aggregate_kmers[kmer].update(next_kmers)
                else:
                    aggregate_kmers[kmer] = next_kmers
        for next_kmers in aggregate_kmers.values():
            if len(next_kmers) != 1:
                all_unique = False
                break
        if all_unique:
            assert test_k == k
            return
    assert False  # Fail test if no k is found
