import wave
from RSA import decrypt
from utilities import converter

def extraction(d, n):
    song = wave.open("Output.wav", mode='rb')
    fr_bytes = bytearray(song.readframes(song.getnframes()))

    ext = [fr_bytes[i] & 1 for i in range(len(fr_bytes))]
    rough = "".join(
        chr(int("".join(map(str, ext[i:i+8])), 2)) for i in range(0, len(ext), 8))

    sct_msg = rough.split("|")[0]
    song.close()

    cipher = converter(sct_msg)
    plain = decrypt(cipher, d, n)

    with open("OUTPUT.txt", 'w') as f:
        f.write(plain)
