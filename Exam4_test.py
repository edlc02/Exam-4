import pytest
from kmer_analysis import get_kmers, collect_kmers, find_optimal_k

"Checks basic functionality of extracting k-mers and their subsequent k-mers"
def test_get_kmers_basic():
    sequence = "ATGCATGC"
    k = 3
    expected_kmers = {
        "ATG": {"TGC"},
        "TGC": {"GCA"},
        "GCA": {"CAT"},
        "CAT": {"ATG"}
    }
    assert get_kmers(sequence, k) == expected_kmers

"Tests the case where the sequence has overlapping identical k-mers, a common scenario in sequences like 'AAA'"
def test_get_kmers_overlap():
    sequence = "AAA"
    k = 2
    expected_kmers = {
        "AA": {"AA"}
    }
    assert get_kmers(sequence, k) == expected_kmers

"Ensures that k-mers are correctly collected and aggregated across multiple sequences"
def test_collect_kmers_multiple_sequences():
    # Assuming test_data.txt contains the lines: "ATGCATGC\nAAA\n"
    k = 2
    expected_aggregate = {
        "AT": {"TG", "GC"},
        "TG": {"GC"},
        "GC": {"CA", "AT"},
        "CA": {"AT"},
        "AA": {"AA"}
    }
    assert collect_kmers('test_data.txt', k) == expected_aggregate


"Verifies that the find_optimal_k function correctly identifies the smallest k where each k-mer has exactly one subsequent k-mer."
def test_find_optimal_k_unique_subsequent():
    # Assuming test_data_unique.txt contains a sequence that meets the criteria for k=3
    assert find_optimal_k('test_data_unique.txt') == 3

@pytest.mark.parametrize("k, expected_result", [
    (1, True),  # Trivial case where each nucleotide follows uniquely
    (2, False), # Assuming there's an overlap in subsequences for k=2
])

"Uses tests to verify if all subsequences are unique for given k values."
def test_k_unique_subsequence_check(k, expected_result):
    filename = 'test_data.txt'
    aggregate = collect_kmers(filename, k)
    all_unique = all(len(subs) == 1 for subs in aggregate.values())
    assert all_unique == expected_result

if __name__ == "__main__":
    pytest.main()
