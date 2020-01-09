#!/usr/bin/env python
# coding: utf-8

import random

__version__ = 0.1.1

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


def main():
    grp0 = GREEK_ALPHABET + PHONETIC_ALPHABET + OFFICER_NAMES + COLOR_NAME + NUMBERS
    grp1 = GREEK_ALPHABET + PHONETIC_ALPHABET + COLOR_NAME + NUMBERS*10
    sizepass = random.randrange(5, 9)
    passlist = [random.choice(grp0)]
    passlist[1:] = random.sample(grp1, k=sizepass-1)
    print('-'.join(passlist))


if __name__ == '__main__':
    main()
