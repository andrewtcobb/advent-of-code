def part1(notes):
    output_numbers = [line.split('|')[1].strip().split(' ') for line in notes]

    count = 0

    for output_number in output_numbers:
        for digit in output_number:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                count += 1

    return count


def part2(notes):
    display_sets = [(line.split('|')[0].strip().split(
        ' '), line.split('|')[1].strip().split(' ')) for line in notes]

    count = 0

    for display_set in display_sets:
        seven_segment_displays, output = display_set
        known_digits = {0: '', 1: '', 2: '', 3: '',
                        4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

        known_digits.update(find_unique_signals(seven_segment_displays))
        known_digits.update(find_digit6(
            seven_segment_displays, known_digits[1]))
        known_digits.update(find_digit3(
            seven_segment_displays, known_digits[1]))
        known_digits.update(find_digit2_and_digit5(
            seven_segment_displays, known_digits))
        known_digits.update(find_digit0_and_digit_9(
            seven_segment_displays, known_digits))

        digits_to_value = {''.join(sorted(value)): key for key,
                           value in known_digits.items()}

        decoded_output = ''
        for digit in output:
            decoded_output += str(digits_to_value[''.join(sorted(digit))])

        count += int(decoded_output)

    return count

# 1,4,7, and 8 all have unique segment counts


def find_unique_signals(seven_segment_displays):
    unique_signals = {1: '', 4: '', 7: '', 8: ''}
    for display in seven_segment_displays:
        if len(display) == 2:
            unique_signals[1] = display
        elif len(display) == 3:
            unique_signals[7] = display
        elif len(display) == 4:
            unique_signals[4] = display
        elif len(display) == 7:
            unique_signals[8] = display

    return unique_signals


# The 6-letter digit that does not have both of the letters found in digit 1 must be digit 6
def find_digit6(seven_segment_displays, digit1):
    for display in seven_segment_displays:
        if len(display) == 6 and (digit1[0] not in display or digit1[1] not in display):
            return {6: display}


# The 5-letter digit that contains all the letters found in digit 1 must be 3
def find_digit3(seven_segment_displays, digit1):
    for display in seven_segment_displays:
        if len(display) == 5 and digit1[0] in display and digit1[1] in display:
            return {3: display}


# Find the letters in digit 4 that are not in digit 1. Of the unknown 5-letter digits remaining, the one that has both those letters must be digit 5
# The remaining unknown 5-letter digit must be digit 2
def find_digit2_and_digit5(seven_segment_displays, known_digits):
    letters_in_4_but_not_in_1 = tuple(
        set(known_digits[4])-set(known_digits[1]))

    remaining_5_letter_displays = [display for display in seven_segment_displays if len(
        display) == 5 and display != known_digits[3]]

    if letters_in_4_but_not_in_1[0] in remaining_5_letter_displays[0] and letters_in_4_but_not_in_1[1] in remaining_5_letter_displays[0]:
        return {5: remaining_5_letter_displays[0], 2: remaining_5_letter_displays[1]}
    else:
        return {5: remaining_5_letter_displays[1], 2: remaining_5_letter_displays[0]}


# Remove all letters found in digit 7 from the remaining unknown 6-letter digits. Remove the leftover common letters from each unknown digit, which will leave you with two letters. Find the letter that is in digit 5. The remaining unknown digit that contains that letter must by digit 9.
# The remaining unknown digit must be digit 0
def find_digit0_and_digit_9(seven_segment_displays, known_digits):
    remaining_6_letter_displays = [display for display in seven_segment_displays if len(
        display) == 6 and display != known_digits[6]]

    remaining_6_letter_displays_minus_letters_in_digit_7 = [''.join(tuple(
        set(display)-set(known_digits[7]))) for display in remaining_6_letter_displays]

    symmetric_difference = tuple(set(remaining_6_letter_displays_minus_letters_in_digit_7[0]).symmetric_difference(
        remaining_6_letter_displays_minus_letters_in_digit_7[1]))

    letter_that_is_in_5 = symmetric_difference[0] if symmetric_difference[
        0] in known_digits[5] else symmetric_difference[1]

    if letter_that_is_in_5 in remaining_6_letter_displays[0]:
        return {9: remaining_6_letter_displays[0], 0: remaining_6_letter_displays[1]}
    else:
        return {9: remaining_6_letter_displays[1], 0: remaining_6_letter_displays[0]}


input = open('input.txt', 'r').read().splitlines()
print(part1(input))
print(part2(input))
