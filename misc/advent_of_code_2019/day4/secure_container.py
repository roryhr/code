"""--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 109165-576723.
"""
def is_adjacent(number_str):
    # Two adjacent digits are the same
    if set(number_str) == 6:
        return False

    for index, digit in enumerate(number_str[:-1]):
        if digit == number_str[index+1]:
            return True

def check(number):
    number_str = str(number)
    # six-digit number
    if len(number_str) != 6:
        return False

    if not is_adjacent(number_str):
        return False

    if sorted(number_str) != list(number_str):
        return False

    return True

def contains_double_no_larger_group(d):
    # could be generalized similarly - too lazy atm :)
    if d[0] == d[1] and d[1] != d[2] \
        or d[0] != d[1] and d[1] == d[2] and d[2] != d[3] \
        or d[1] != d[2] and d[2] == d[3] and d[3] != d[4] \
        or d[2] != d[3] and d[3] == d[4] and d[4] != d[5] \
        or d[3] != d[4] and d[4] == d[5]:
        return True
    return False

if __name__ == '__main__':
    
    criteria = [
        check(number)
        for number
        in range(109165, 576723 + 1)
    ]

    print(sum(criteria))
    print('is adjacent', is_adjacent(str(111111)))
    print(check(111111))



    criteria = [
        check(number) and contains_double_no_larger_group(str(number))
        for number
        in range(109165, 576723 + 1)
    ]

    print(sum(criteria))
