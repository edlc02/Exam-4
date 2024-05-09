import pytest
from Exam_4 import get_kmers, collect_kmers, find_optimal_k  # Adjust 'your_module' to your actual module name

def test_get_kmers():
    sequence = "ATCGATCG"
    k = 3
    expected = {
        "ATC": {"TCG"},
        "TCG": {"CGA"},
        "CGA": {"GAT"},
        "GAT": {"ATC"}
    }
    assert get_kmers(sequence, k) == expected

    # Edge cases
    assert get_kmers("", 3) == {}
    assert get_kmers("ATCG", 5) == {}

def test_collect_kmers():
    sequences = ["ATCG", "TCGA", "CGAT"]
    k = 3
    expected = {
        "ATC": {"TCG"},
        "TCG": {"CGA", "GAT"},
        "CGA": {"GAT"},
        "GAT": {"ATC"}
    }
    aggregate_kmers = {}
    for sequence in sequences:
        sequence_kmers = get_kmers(sequence, k)
        for kmer, next_kmers in sequence_kmers.items():
            if kmer not in aggregate_kmers:
                aggregate_kmers[kmer] = set()
            aggregate_kmers[kmer].update(next_kmers)
    assert aggregate_kmers == expected

def test_find_optimal_k():
    sequences = ["ATCGATCG", "TCGATCGA"]
    k = 1
    while k < 10:
        aggregate_kmers = {}
        for sequence in sequences:
            sequence_kmers = get_kmers(sequence, k)
            for kmer, next_kmers in sequence_kmers.items():
                if kmer not in aggregate_kmers:
                    aggregate_kmers[kmer] = set()
                aggregate_kmers[kmer].update(next_kmers)
        if all(len(next_kmers) == 1 for next_kmers in aggregate_kmers.values()):
            break
        k += 1
    assert k == 8, f"Expected optimal k to be 8, found {k}"

if __name__ == "__main__":
    pytest.main()
