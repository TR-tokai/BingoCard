import tkinter as tk
import hashlib
import random

card_string = 'bingocard'
random_string = str(hash(card_string)) # 出力されたランダムな整数を文字列に変換
print(random_string)
hash_value = hashlib.md5(random_string.encode()).hexdigest() # ランダムな文字列をMD5ハッシュ値に変換
random.seed(hash_value) # MD5ハッシュ値をランダムシードに設定
print(hash_value)

# リスト
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

# ウィンドウ設定
root = tk.Tk()
root.title('BingoCard')
root.geometry('400x500')
root.resizable(False, False)
button_font_size = 50
label_font_size = 60

# ボタン処理
def open(self):
    self['state'] = 'disabled'
    self['bg'] = 'black'

# B列
label_B = tk.Label(root, text='B', font=('', label_font_size), pady=20).grid(column=0, row=0)

button_B1 = tk.Button(root, text=bingo_B[0], command=lambda : open(button_B1),font=('', button_font_size))
button_B1.grid(column=0, row=1)

button_B2 = tk.Button(root, text=bingo_B[1], command=lambda : open(button_B2),font=('', button_font_size))
button_B2.grid(column=0, row=2)

button_B3 = tk.Button(root, text=bingo_B[2], command=lambda : open(button_B3),font=('', button_font_size))
button_B3.grid(column=0, row=3)

button_B4 = tk.Button(root, text=bingo_B[3], command=lambda : open(button_B4),font=('', button_font_size))
button_B4.grid(column=0, row=4)

button_B5 = tk.Button(root, text=bingo_B[4], command=lambda : open(button_B5),font=('', button_font_size))
button_B5.grid(column=0, row=5)

# I列
label_I = tk.Label(root, text='I', font=('', label_font_size)).grid(column=1, row=0)

button_I1 = tk.Button(root, text=bingo_I[0], command=lambda : open(button_I1),font=('', button_font_size))
button_I1.grid(column=1, row=1)

button_I2 = tk.Button(root, text=bingo_I[1], command=lambda : open(button_I2),font=('', button_font_size))
button_I2.grid(column=1, row=2)

button_I3 = tk.Button(root, text=bingo_I[2], command=lambda : open(button_I3),font=('', button_font_size))
button_I3.grid(column=1, row=3)

button_I4 = tk.Button(root, text=bingo_I[3], command=lambda : open(button_I4),font=('', button_font_size))
button_I4.grid(column=1, row=4)

button_I5 = tk.Button(root, text=bingo_I[4], command=lambda : open(button_I5),font=('', button_font_size))
button_I5.grid(column=1, row=5)

# N列
label_N = tk.Label(root, text='N', font=('', label_font_size)).grid(column=2, row=0)

button_N1 = tk.Button(root, text=bingo_N[0], command=lambda : open(button_N1),font=('', button_font_size))
button_N1.grid(column=2, row=1)

button_N2 = tk.Button(root, text=bingo_N[1], command=lambda : open(button_N2),font=('', button_font_size))
button_N2.grid(column=2, row=2)

button_N3 = tk.Button(root, text='FREE', command=lambda : open(button_N3),font=('', 25))
button_N3.grid(column=2, row=3, sticky=tk.NSEW)

button_N4 = tk.Button(root, text=bingo_N[2], command=lambda : open(button_N4),font=('', button_font_size))
button_N4.grid(column=2, row=4)

button_N5 = tk.Button(root, text=bingo_N[3], command=lambda : open(button_N5),font=('', button_font_size))
button_N5.grid(column=2, row=5)

# G列
label_G = tk.Label(root, text='G', font=('', label_font_size)).grid(column=3, row=0)

button_G1 = tk.Button(root, text=bingo_G[0], command=lambda : open(button_G1),font=('', button_font_size))
button_G1.grid(column=3, row=1)

button_G2 = tk.Button(root, text=bingo_G[1], command=lambda : open(button_G2),font=('', button_font_size))
button_G2.grid(column=3, row=2)

button_G3 = tk.Button(root, text=bingo_G[2], command=lambda : open(button_G3),font=('', button_font_size))
button_G3.grid(column=3, row=3)

button_G4 = tk.Button(root, text=bingo_G[3], command=lambda : open(button_G4),font=('', button_font_size))
button_G4.grid(column=3, row=4)

button_G5 = tk.Button(root, text=bingo_G[4], command=lambda : open(button_G5),font=('', button_font_size))
button_G5.grid(column=3, row=5)

# O列
label_O = tk.Label(root, text='O', font=('', label_font_size)).grid(column=4, row=0)

button_O1 = tk.Button(root, text=bingo_O[0], command=lambda : open(button_O1),font=('', button_font_size))
button_O1.grid(column=4, row=1)

button_O2 = tk.Button(root, text=bingo_O[1], command=lambda : open(button_O2),font=('', button_font_size))
button_O2.grid(column=4, row=2)

button_O3 = tk.Button(root, text=bingo_O[2], command=lambda : open(button_O3),font=('', button_font_size))
button_O3.grid(column=4, row=3)

button_O4 = tk.Button(root, text=bingo_O[3], command=lambda : open(button_O4),font=('', button_font_size))
button_O4.grid(column=4, row=4)

button_O5 = tk.Button(root, text=bingo_O[4], command=lambda : open(button_O5),font=('', button_font_size))
button_O5.grid(column=4, row=5)

# 伸縮比率
root.columnconfigure([0,1,2,3,4], weight=1)
root.rowconfigure([0,1,2,3,4,5], weight=1)

root.mainloop()