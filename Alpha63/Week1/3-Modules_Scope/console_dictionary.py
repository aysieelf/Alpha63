python_dictionary = [
    ['time', 'The indefinite continued progress of existence and events in the past, present, and future regarded as '
             'a whole.'],
    ['person', 'A human being regarded as an individual.'],
    ['year', 'The period of 365 days (or 366 days in a leap year) starting from the first of January.'],
    ['way', 'A method, style, or manner of doing something.'],
    ['day', 'A period of 24 hours as a unit of time, reckoned from one midnight to the next.'],
    ['thing', 'An object that one need not, cannot, or does not wish to give a specific name to.'],
    ['man', 'An adult human male.'],
    ['world', 'The earth, together with all of its countries, peoples, and natural features.'],
    ['life', 'The existence of an individual human being or animal.'],
    ['hand', 'The end part of a person’s arm beyond the wrist, including the palm, fingers, and thumb.']
]

def add_word(word, meaning):
    # creates new entry in the dictionary
    python_dictionary.append([word, meaning])


def update_meaning(word, meaning):
    # replaces the word in the dict with a new meaning
    for pair in python_dictionary:
        if pair[0] == word:
            pair[1] = meaning


def find_word(word):
    # returns the meaning of the word or None, if no such word
    for pair in python_dictionary:
        if pair[0] == word:
            return pair[1]
    return None

