import tkinter as tk
import hashlib
import random

card_string = 'bingocard'
random_string = str(hash(card_string)) # 出力されたランダムな整数を文字列に変換
print(random_string)
hash_value = hashlib.md5(random_string.encode()).hexdigest() # ランダムな文字列をMD5ハッシュ値に変換
random.seed(hash_value) # MD5ハッシュ値をランダムシードに設定
print(hash_value)

list_B = list(range(1, 16))
list_I = list(range(16, 31))
list_N = list(range(31, 46))
list_G = list(range(46, 61))
list_O = list(range(61, 76))
bingo_B = random.sample(list_B, 5)
bingo_I = random.sample(list_I, 5)
bingo_N = random.sample(list_N, 4)
bingo_G = random.sample(list_G, 5)
bingo_O = random.sample(list_O, 5)


def pushed(self):
    self['state'] = 'disabled'
    self['bg'] = 'black'

root = tk.Tk()
root.title('BingoCard')
root.geometry('500x500')
root.resizable(False, False)
font_size=50

# B列
button_B1 = tk.Button(root, text=bingo_B[0], command= lambda : pushed(button_B1),font=('', font_size))
button_B1.grid(column=0, row=0, sticky=tk.NSEW)

button_B2 = tk.Button(root, text=bingo_B[1], command= lambda : pushed(button_B2),font=('', font_size))
button_B2.grid(column=0, row=1, sticky=tk.NSEW)

button_B3 = tk.Button(root, text=bingo_B[2], command= lambda : pushed(button_B3),font=('', font_size))
button_B3.grid(column=0, row=2, sticky=tk.NSEW)

button_B4 = tk.Button(root, text=bingo_B[3], command= lambda : pushed(button_B4),font=('', font_size))
button_B4.grid(column=0, row=3, sticky=tk.NSEW)

button_B5 = tk.Button(root, text=bingo_B[4], command= lambda : pushed(button_B5),font=('', font_size))
button_B5.grid(column=0, row=4, sticky=tk.NSEW)

# I列
button_I1 = tk.Button(root, text=bingo_I[0], command= lambda : pushed(button_I1),font=('', font_size))
button_I1.grid(column=1, row=0, sticky=tk.NSEW)

button_I2 = tk.Button(root, text=bingo_I[1], command= lambda : pushed(button_I2),font=('', font_size))
button_I2.grid(column=1, row=1, sticky=tk.NSEW)

button_I3 = tk.Button(root, text=bingo_I[2], command= lambda : pushed(button_I3),font=('', font_size))
button_I3.grid(column=1, row=2, sticky=tk.NSEW)

button_I4 = tk.Button(root, text=bingo_I[3], command= lambda : pushed(button_I4),font=('', font_size))
button_I4.grid(column=1, row=3, sticky=tk.NSEW)

button_I5 = tk.Button(root, text=bingo_I[4], command= lambda : pushed(button_I5),font=('', font_size))
button_I5.grid(column=1, row=4, sticky=tk.NSEW)

# N列
button_N1 = tk.Button(root, text=bingo_N[0], command= lambda : pushed(button_N1),font=('', font_size))
button_N1.grid(column=2, row=0, sticky=tk.NSEW)

button_N2 = tk.Button(root, text=bingo_N[1], command= lambda : pushed(button_N2),font=('', font_size))
button_N2.grid(column=2, row=1, sticky=tk.NSEW)

button_N3 = tk.Button(root, text='FREE', command= lambda : pushed(button_N3),font=('', 30))
button_N3.grid(column=2, row=2, sticky=tk.NSEW)

button_N4 = tk.Button(root, text=bingo_N[2], command= lambda : pushed(button_N4),font=('', font_size))
button_N4.grid(column=2, row=3, sticky=tk.NSEW)

button_N5 = tk.Button(root, text=bingo_N[3], command= lambda : pushed(button_N5),font=('', font_size))
button_N5.grid(column=2, row=4, sticky=tk.NSEW)

# G列
button_G1 = tk.Button(root, text=bingo_G[0], command= lambda : pushed(button_G1),font=('', font_size))
button_G1.grid(column=3, row=0, sticky=tk.NSEW)

button_G2 = tk.Button(root, text=bingo_G[1], command= lambda : pushed(button_G2),font=('', font_size))
button_G2.grid(column=3, row=1, sticky=tk.NSEW)

button_G3 = tk.Button(root, text=bingo_G[2], command= lambda : pushed(button_G3),font=('', font_size))
button_G3.grid(column=3, row=2, sticky=tk.NSEW)

button_G4 = tk.Button(root, text=bingo_G[3], command= lambda : pushed(button_G4),font=('', font_size))
button_G4.grid(column=3, row=3, sticky=tk.NSEW)

button_G5 = tk.Button(root, text=bingo_G[4], command= lambda : pushed(button_G5),font=('', font_size))
button_G5.grid(column=3, row=4, sticky=tk.NSEW)

# O列
button_O1 = tk.Button(root, text=bingo_O[0], command= lambda : pushed(button_O1),font=('', font_size))
button_O1.grid(column=4, row=0, sticky=tk.NSEW)

button_O2 = tk.Button(root, text=bingo_O[1], command= lambda : pushed(button_O2),font=('', font_size))
button_O2.grid(column=4, row=1, sticky=tk.NSEW)

button_O3 = tk.Button(root, text=bingo_O[2], command= lambda : pushed(button_O3),font=('', font_size))
button_O3.grid(column=4, row=2, sticky=tk.NSEW)

button_O4 = tk.Button(root, text=bingo_O[3], command= lambda : pushed(button_O4),font=('', font_size))
button_O4.grid(column=4, row=3, sticky=tk.NSEW)

button_O5 = tk.Button(root, text=bingo_O[4], command= lambda : pushed(button_O5),font=('', font_size))
button_O5.grid(column=4, row=4, sticky=tk.NSEW)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

root.mainloop()