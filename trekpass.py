#!/usr/bin/env python
# coding: utf-8

import random

__version__ = '0.1.1'

GREEK_ALPHABET = [
    'Alpha',
    'Beta',
    'Gamma',
    'Delta',
    'Epsilon',
    'Gamma',
    'Zeta',
    'Eta',
    'Theta',
    'Iota',
    'Kappa',
    'Lambda',
    'Mu',
    'Nu',
    'Xi',
    'Omicron',
    'Pi',
    'Rho',
    'Sigma',
    'Tau',
    'Upsilon',
    'Phi',
    'Chi',
    'Psi',
    'Omega',
]

PHONETIC_ALPHABET = [
    'Alfa',
    'Bravo',
    'Charlie',
    'Delta',
    'Echo',
    'Foxtrot',
    'Golf',
    'Hotel',
    'India',
    'Juliett',
    'Kilo',
    'Lima',
    'Mike',
    'November',
    'Oscar',
    'Papa',
    'Quebec',
    'Romeo',
    'Sierra',
    'Tango',
    'Uniform',
    'Victor',
    'Whiskey',
    'X-ray',
    'Yankee',
    'Zulu',
    'Decimal',
    'Stop',
]

COLOR_NAME = [
    'Black',
    'White',
    'Brown',
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Blue',
    'Cyan',
    'Violet',
    'Purple',
    'Pink',
    'Gray',
    'Magenta',
]

OFFICER_NAMES = [
    'Kirk',
    'Spock',
    'Scott',
    'Sulu',
    'Uhura',
    'Chekov',
    'Picard',
    'Riker',
    'Data',
    'Worf',
    'LaForge',
    'Yar',
    'Troi',
    'Crusher',
    'Pulaski',
    'Sisko',
    'Dax',
    'O-Brien',
    'Neris',
    'Bashir',
    'Nog',
    'Janeway',
    'Chakotay',
    'Tuvok',
    'Torres',
    'Kim',
    'Paris',
    'Doctor',
    'Seven-of-Nine',
    'Archer',
    'T-Pol',
    'Mayweather',
    'Hoshi',
    'Reed',
    'Tucker',
    'Phlox',
    'Lorca',
    'Saru',
    'Tyler',
    'Tilly',
    'Stamets',
    'Culber',
    'Pike',
    'Georgiou',
    'Burnham',
    'Detmer',
    'Januzzi',
    'Gant',
    'Connor',
    'Nambue',
]

NUMBERS = '0 1 2 3 4 5 6 7 8 9 0'.split()


class ComAuthCode:
    """
    """
    GRP_0 = GREEK_ALPHABET + PHONETIC_ALPHABET + OFFICER_NAMES + COLOR_NAME + NUMBERS
    GRP_1 = GREEK_ALPHABET + PHONETIC_ALPHABET + COLOR_NAME + NUMBERS*10

    def __init__(self, numwords=6, delimiter='-', case='first'):
        "docstring"
        self.numwords = numwords
        self.delimiter = delimiter
        self.case = case

    def generate_code(self, numwords=None):
        if numwords is None:
            numwords = self.numwords

        if len(numwords) == 2:
            min, max = numwords
            numwords = random.randrange(5, 9)

        numwords = int(numwords)

        self.terms = [random.choice(self.GRP_0)]
        self.terms[1:] = random.sample(self.GRP_1, k=numwords-1)

    def __str__(self):
        return self.delimiter.join(self.terms)


def main():
    command_code = ComAuthCode(numwords=(5, 9))
    command_code.generate_code()
    print(command_code)


if __name__ == '__main__':
    main()
