#!/usr/bin/python3
import sys

ciphertext = sys.argv[1]

# Dictionary of English-language letter frequencies.
f = {"A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
     "G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
     "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
     "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
     "Y": .01974, "Z": .00074}


# Returns index for a given letter.
def index(letter):
    return sorted(list(f.keys())).index(letter)


# Returns letter for a given index.
def letter(index):
    if index > 25: index = index - 26
    return sorted(list(f.keys()))[index]

# gets chi scored based on given observed count and expected count
def chi_squared(observed_count, expected):
    return ((observed_count - expected) ** 2) / expected

#returns chi score for a specific column
def chi_score(column):
    letter_occurances = []

    for i in range(26):
        letter_occurances.append(0)
    for letter in column:
        letter_occurances[ord(letter) - 65] = letter_occurances[ord(letter) - 65] + 1
    chi_score = 0
    for i in range(26):
        letter = chr(i + 65)
        if letter_occurances[i] != 0:
            expected = len(column) * f[letter]
            chi_score += chi_squared(letter_occurances[i], expected)
    return chi_score

#shifts letters in a column by given shift length
def shifted_column(column, shift):
    shifted_column_output = ""
    col = list(column)
    for letter in col:
          shifted_column_output += chr(ord(letter)-shift)
    return shifted_column_output

# finds value to shift for a column
def find_lowest_shift(column):
    col = ''
    min_chi = 9999999999
    min_shift = 0
    for shift in range(26):
        col = shifted_column(column, shift)
        chi = chi_score(col)
        if chi < min_chi:
            min_chi = chi
            min_shift = shift
    return min_shift


# -----------------------------------------------------------------

column_strings = []
for x in range(8):
    column_strings.append("")
for x in range(len(ciphertext)):
        index = x % 8
        column_strings[index] += ciphertext[x]
key = ''
for column in column_strings:
    shift = find_lowest_shift(column)
    key += letter(shift)

# -----------------------------------------------------------------
print(key)
