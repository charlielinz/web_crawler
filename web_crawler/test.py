import unicodedata


def chr_width(c):
    if unicodedata.east_asian_width(c) in ('F','W','A'):
        return 2
    else:
        return 1

chr_width("i")
chr_width("擬")

