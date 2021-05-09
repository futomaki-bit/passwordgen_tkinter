# Random Password Generator
# Aims to replicate popular password generators
# Side note: learn to use tkinter

import string
import random
from tkinter import * 

# blocks : how many parts with separator linked between them
# blocksize : how many characters in a block
# separator : separates blocks
# repeat : to generate how many times
blocks = 5
blocksize = 5
separator = '-'
repeat = 10

# string.digits*2 to have more chance of getting numbers.
# Numbers have 10 time 2 (0 to 9)
# Letters have 52 (2 * 26 for lower/uppercase)
# Chances in theory are about 28% num, 36% lowercase, 36% uppercase
# add string.punctuation to the usethesechars for a even more stronger password
usethesechars = string.digits*2 + string.ascii_letters

# Generate Password
password = []
for count in range(repeat):
    password.append('')
    for section in range(blocks):
        for sub in range(blocksize):
            password[count] += (''.join(random.choice(usethesechars)))

        if section != (blocks - 1):
            password[count] += (separator)

print(password)

# Tkinter stuff
root = Tk()
root.title("Password Generator")

tkpassword = StringVar()
# Label is not copyable by default
displaypassword = Text(root,bg='black',fg='white')
for count in range(repeat):
    displaypassword.insert(INSERT,password[count])
    displaypassword.insert(INSERT,'\n')
displaypassword.pack()

root.mainloop()

