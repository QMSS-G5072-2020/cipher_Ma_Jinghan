from cipher_jm5223 import __version__
from cipher_jm5223 import cipher_jm5223

def test_version():
    assert __version__ == '0.1.0'

def test_cipher():
    example='happy'
    shift=1
    expected='ibqqz'
    actual=cipher_jm5223.cipher(example,shift,encrypt=True)
    assert actual==expected
