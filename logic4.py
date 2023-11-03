import math


def preprocess(word):
    letters_dict = {}
    for letter in word:
        letter_count = 0
        for letter2 in word:
            if letter == letter2:
                letter_count += 1
        letters_dict.update({letter: letter_count})
    return letters_dict


def generate_partitions_with_max(n, max_partition, I=2, length=None):
    if n == 0:
        if length == 0:
            yield []
        return
    if length == 0:
        return
    for i in range(I, min(n, max_partition) + 1):
        for p in generate_partitions_with_max(n - i, max_partition, i, length - 1 if length else None):
            if all(x >= I for x in [i] + p):
                yield [i] + p


def partition_letter_forms(letters_dict, output_word_length):
    unique_letters_count = len(letters_dict.keys())
    max_pow = max(letters_dict.values())
    print("maximal frequency is: ", max_pow)
    letter_forms = list(generate_partitions_with_max(output_word_length, max_pow, length=unique_letters_count))
    return letter_forms


def for_choice(letters_dict, letter_forms):
    choice_list = []
    for letter_form in letter_forms:
        print("letter_form: ", letter_form)
        denominator_count = 0
        choice = 1
        for power in sorted(set(letter_form), reverse=True):
            numerator_count = 0
            for freq in letters_dict.values():
                if freq >= power:
                    numerator_count += 1
            numerator_count -= denominator_count
            if numerator_count < 0:
                raise Exception("Error: Not enough letters in the original word")
            print("numerator_count: ", numerator_count)
            power_count = letter_form.count(power)
            print("power_count: ", power_count)
            choice *= math.comb(numerator_count, power_count)
            denominator_count += power_count
        print("choice = ", choice)
        choice_list.append(choice)
    return choice_list


def for_arrange(output_word_length, letter_forms):
    arrange_list = []
    numerator = math.factorial(output_word_length)

    for letter_form in letter_forms:
        denominator = 1
        for power in letter_form:
            denominator *= math.factorial(power)
        arrange_list.append(numerator // denominator)
    return arrange_list


def count_options(letters_dict, output_word_length):
    letter_forms = partition_letter_forms(letters_dict, output_word_length)
    print("letter_forms:", letter_forms)
    choice_list = for_choice(letters_dict, letter_forms)
    print("choice_list = ", choice_list)
    arrange_list = for_arrange(output_word_length, letter_forms)
    print("arrange_list = ", arrange_list)
    total = 0
    for i in range(len(arrange_list)):
        total += choice_list[i] * arrange_list[i]
    print("total = ", total)


if __name__ == '__main__':
    word = "aaaabbbbccccdddd"
    output_word_length = 10
    letters_dict = preprocess(word)
    print("letters_dict:", letters_dict)
    count_options(letters_dict, output_word_length)
