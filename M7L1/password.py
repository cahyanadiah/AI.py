import random

def gen_pass(pass_length):
    huruf = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    tersimpan = ''
    for i in range(pass_length):
        v = random.choice(huruf)
        tersimpan = tersimpan + v
    return tersimpan