def is_continuous_sequence(sequence):
    if sequence == [] or len(sequence) == 1:
        return False
    else:
        sorted_sequence = sorted(sequence)
        length = len(sorted_sequence) - 1
        for index, item in enumerate(sorted_sequence[:length]):
            if sorted_sequence[index + 1] - sorted_sequence[index] == 1:
                continue
            else:
                return False
        return True
