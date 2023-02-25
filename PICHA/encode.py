from RSA import *
import wave

def encoding(e, n, song_path, text_path):

    song = wave.open(song_path, mode='rb')
    fr_bytes = bytearray(song.readframes(song.getnframes()))

    with open(text_path, 'r') as file:
        plaintext = file.read()

    sct_msg = str(encrypt(plaintext, e, n))
    sct_msg = sct_msg + int((len(fr_bytes)-(len(sct_msg)*8*8))/8) * '|'
    bit_arr = list(
        map(int, ''.join(bin(ord(i)).lstrip('0b').rjust(8, '0') for i in sct_msg)))

    for i, j in enumerate(bit_arr):
        fr_bytes[i] = (fr_bytes[i] & 254) | j

    fr_mod = bytes(fr_bytes)

    with wave.open("Output.wav", mode='wb') as Done:
        Done.setparams(song.getparams())
        Done.writeframes(fr_mod)
    song.close()
