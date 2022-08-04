import random
import os

char_list = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#+-=")

def randstr(leng=40):
    s = ""
    while leng > 0:
        s += random.choice(char_list)
        leng -= 1
    return s

# Const
B = 1
KB = B * 1024
MB = KB * 1024
GB = MB * 1024
TB = GB * 1024

# Size
size = 64*GB

while size > 0:
    filename = randstr(20)
    with open(filename,'wb') as f:
        i = 32*MB
        size -= i
        while i > 0:
            f.write(bytes([random.randint(0, 255)]))
            i -= 1
            if i%MB == 0:
                print(i//MB,"MB left")
    os.system("bypy upload "+filename)
    os.remove(filename)
    print("Finished",filename)
