def cipher(text, shift, encrypt=True):
    """
    Creating the function to encipher the code.
    Parameters
    ----------
    text : str
      The string we use to encode.
    shift : int
      The number of times each letter need to be shifted.
    encrypt : bool
      The boolean chooses the way of encode. If encryt = True, the function can encrypt the string. If encrypt = False, the function can decrypt the string.
    Returns
    -------
    new_text : str
      The encrypt or decrypt string calculated by the function.
    Examples
    --------
    >>> from cipher_jm5223 import cipher_jm5223
    >>> text = "happy"
    >>> shift = 1
    >>> encryt = True
    >>> cipher_jm5223.cipher(text,shift,encrypt=True)
    "ibqqz"
    >>> from cipher_jm5223 import cipher_jm5223
    >>> text = "ibqqz"
    >>> shift = 1
    >>> encryt = False
    >>> cipher_jm5223.cipher(text,shift,encrypt=False)
    "happy"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
