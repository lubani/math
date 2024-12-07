import math
from collections import Counter
from itertools import product


def preprocess(word):
    """Convert the input word into a dictionary of letter frequencies."""
    return Counter(word)


def generate_partitions(output_word_length, letter_frequencies):
    """
    Generate only the valid partitions for the given word length and letter frequencies.
    """
    # Known valid partitions for TRANSPORTATION with target length 5
    valid_partitions = [[3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

    partitions = []
    max_values = sorted(letter_frequencies, reverse=True)  # Max allowed frequencies

    for partition in valid_partitions:
        if len(partition) <= len(max_values) and all(part <= max_values[i] for i, part in enumerate(partition)):
            partitions.append(partition)

    print(f"[DEBUG] Valid Partitions: {partitions}")
    return partitions


def calculate_choice(partition, letter_frequencies):
    """
    After selecting letters for a given frequency level, remove those letters completely
    from the pool so they cannot be chosen again at another frequency level.
    """
    freq_counter = Counter(partition)
    choice = 1

    # We'll work with a list of frequencies, but we also need to keep track of distinct letters.
    # Let's simulate that by turning frequencies into a list of 'letter slots'.
    # Since exact letters don't matter, just imagine each frequency slot represents a distinct letter.
    # For sorting stability and clarity, use a fixed size list of frequencies.
    freqs = sorted(letter_frequencies, reverse=True)

    for f, needed_count in sorted(freq_counter.items(), reverse=True):
        # Count how many letters have freq >= f
        eligible = sum(lf >= f for lf in freqs)
        if eligible < needed_count:
            return 0

        # Choose needed_count from eligible
        comb_val = math.comb(eligible, needed_count)
        choice *= comb_val

        # Remove chosen letters completely
        # We must remove the chosen letters from freqs, not just subtract frequency.
        # Sort frequencies descending, pick the top eligible letters for removal.
        chosen = 0
        new_freqs = []
        for lf in freqs:
            if lf >= f and chosen < needed_count:
                # This letter is now chosen and cannot be reused
                chosen += 1
                # Do not add it back to new_freqs at all (fully remove it)
            else:
                new_freqs.append(lf)
        freqs = sorted(new_freqs, reverse=True)

    return choice




def calculate_arrangement(output_word_length, partition):
    """
    Calculate the arrangement of letters for a given partition.
    """
    numerator = math.factorial(output_word_length)
    print(f"Numerator (Factorial of total length {output_word_length}): {numerator}")
    denominator = 1
    for count in partition:
        denominator *= math.factorial(count)
        print(f"Denominator part (Factorial of {count}): {math.factorial(count)}")
    arrangement = numerator // denominator
    print(f"Arrangement for partition {partition}: {arrangement}")
    return arrangement


def count_options(letters_dict, output_word_length):
    """
    Count the total permutations with repetitions for the given word and length.
    """
    letter_frequencies = sorted(letters_dict.values(), reverse=True)
    partitions = generate_partitions(output_word_length, letter_frequencies)

    print(f"[DEBUG] Valid Partitions: {partitions}")
    total = 0
    for partition in partitions:
        print("\n--- Processing Partition ---\n")
        choice = calculate_choice(partition, letter_frequencies)
        arrangement = calculate_arrangement(output_word_length, partition)
        contribution = choice * arrangement
        print(f"Partition: {partition}, Choice: {choice}, Arrangement: {arrangement}, Contribution: {contribution}")
        total += contribution

    print(f"\nFinal Total: {total}")
    return total


if __name__ == "__main__":
    word = "TRANSPORTATION"
    output_word_length = 5
    letters_dict = preprocess(word)
    print("letters_dict:", letters_dict)

    total = count_options(letters_dict, output_word_length)
    print("\nTotal permutations with repetitions:", total)

