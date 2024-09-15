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
    if index > 25: index = index-26
    return sorted(list(f.keys()))[index]

def chi_squared(observed_count, expected):
        return (**2(observed_count-expected))/expected


def chi_score(column):
    letter_occurances = {}
    
    for i in range(26):
        letter_occurances.append(0)
    for letter in column:
        letter_occurances[letter-65] = letter_occurances[letter-65]+1
    chi_score = 0
    for i in range(26)
        if(letter_occurences[i] != 0):
             expected = len(column)*f[i]
             chi_score += chi_squared(letter_occurences[i], expected)
    return chi_score

def shifted_column(column, shift)
    shifted_column_output = ""
    for letter in column:
        shifted_column_output = shifted_column_output + (letter-shift)
    reuturn shifted_column_output

def find_lowest_chi_score(column):
    for i in range(26):

    #uses shifted_column, find_observed_count and chi_squared


# -----------------------------------------------------------------

cipherLength = int(len(ciphertext)/8)
block_list = []
for x in range(cipherLength):
        x=x*8
        j = ciphertext[x:x+8]
        block_list.append(j)
        print(j)


print("=============")
print(block_list)

column_strings = []
for x in range(8):
        column_strings.append("")
for block in block_list:
        for character in range(8):
                column_strings[character] += block[character]

for column in 8:
        minimun_chi
        for shift in range(26):
                chi_score()


# -----------------------------------------------------------------
key = ""
print(key)
