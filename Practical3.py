#Practical 3: Design a lexical analyzer to recognize the token defined by the given program.#

import keyword
import tokenize
from io import StringIO

def is_identifier(s):
    return s.isidentifier() or keyword.iskeyword(s)

def is_operator(s):
    try:
        tokens = list(tokenize.generate_tokens(StringIO(s).readline))
        return tokens[0].type == tokenize.OP
    except tokenize.TokenError:
        return False

def is_punctuation(s):
    punctuation = {".", ",", ";", "(", ")", "{", "}", "[", "]"}
    return s in punctuation

def is_constant(s):
    return s.isdigit()

def check_token():
    s = input("Enter a string: ")

    if (is_identifier(s) or is_operator(s) or
        is_punctuation(s) or is_constant(s)):
        print(f"{s} is a Token")
    else:
        print(f"{s} is Not a Token")

if __name__ == "__main__":
    check_token()
