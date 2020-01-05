# Returns True if `number` has `num_digits` digits.
def has_num_digits(number, num_digits):
    assert(num_digits > 0)
    return number in range(10 ** (num_digits - 1), 10 ** num_digits)

# Generates a sequence of substrings in `string` that contain repeated
# characters (e.g. 'aabcc' generates 'aa', 'cc').
def repeated_substrings(string):
    i = 0
    while i < len(string):
        j = i
        while j < len(string) and string[j] == string[i]:
            j += 1
        if j > i + 1:
            yield string[i:j]
        i = j

# Returns `True` if `string` contains adjacent repeated characters. If
# `max_len` is specified, only returns `True` if a matching substring is at
# most `max_len` characters in length.
def has_repeated_substrings(string, max_len=None):
    for substring in repeated_substrings(string):
        if max_len is None or len(substring) <= max_len:
            return True
    return False

# Returns `True` if `number` is valid and within the range `[low, high]`.
def is_valid(number, low, high):
    if not has_num_digits(number, 6):
        return False
    if number < low or number > high:
        return False
    string = str(number)
    # Part 1
    # max_len = None
    # Part 2
    max_len = 2
    if not has_repeated_substrings(string, max_len=max_len):
        return False
    for i in range(1, len(string)):
        if int(string[i]) < int(string[i - 1]):
            return False
    return True

if __name__ == '__main__':
    low, high = 138241, 674034
    count = 0
    for number in range(low, high + 1):
        if is_valid(number, low, high):
            count += 1
    print(count)
