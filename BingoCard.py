import tkinter as tk
from tkinter import messagebox as ms
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

# リーチ、ビンゴフラグ
bB1 = bB2 = bB3 = bB4 = bB5 = B_reach = B_bingo = False
bI1 = bI2 = bI3 = bI4 = bI5 = I_reach = I_bingo = False
bN1 = bN2 = bN3 = bN4 = bN5 = N_reach = N_bingo = False
bG1 = bG2 = bG3 = bG4 = bG5 = G_reach = G_bingo = False
bO1 = bO2 = bO3 = bO4 = bO5 = O_reach = O_bingo = False

# リーチ、ビンゴ数カウント
reach_count = 0
bingo_count = 0

# ウィンドウ設定
root = tk.Tk()
root.title('BingoCard')
root.geometry('400x550')
root.resizable(False, False)
button_font_size = 50
label_font_size = 60
reach_bingo_font_size = 18

# B列
label_B = tk.Label(root, text='B', font=('', label_font_size), pady=20).grid(column=0, row=0)

button_B1 = tk.Button(root, text=bingo_B[0], command=lambda : open(button_B1), font=('', button_font_size))
button_B1.grid(column=0, row=1)

button_B2 = tk.Button(root, text=bingo_B[1], command=lambda : open(button_B2), font=('', button_font_size))
button_B2.grid(column=0, row=2)

button_B3 = tk.Button(root, text=bingo_B[2], command=lambda : open(button_B3), font=('', button_font_size))
button_B3.grid(column=0, row=3)

button_B4 = tk.Button(root, text=bingo_B[3], command=lambda : open(button_B4), font=('', button_font_size))
button_B4.grid(column=0, row=4)

button_B5 = tk.Button(root, text=bingo_B[4], command=lambda : open(button_B5), font=('', button_font_size))
button_B5.grid(column=0, row=5)

# I列
label_I = tk.Label(root, text='I', font=('', label_font_size)).grid(column=1, row=0)

button_I1 = tk.Button(root, text=bingo_I[0], command=lambda : open(button_I1), font=('', button_font_size))
button_I1.grid(column=1, row=1)

button_I2 = tk.Button(root, text=bingo_I[1], command=lambda : open(button_I2), font=('', button_font_size))
button_I2.grid(column=1, row=2)

button_I3 = tk.Button(root, text=bingo_I[2], command=lambda : open(button_I3), font=('', button_font_size))
button_I3.grid(column=1, row=3)

button_I4 = tk.Button(root, text=bingo_I[3], command=lambda : open(button_I4), font=('', button_font_size))
button_I4.grid(column=1, row=4)

button_I5 = tk.Button(root, text=bingo_I[4], command=lambda : open(button_I5), font=('', button_font_size))
button_I5.grid(column=1, row=5)

# N列
label_N = tk.Label(root, text='N', font=('', label_font_size)).grid(column=2, row=0)

button_N1 = tk.Button(root, text=bingo_N[0], command=lambda : open(button_N1), font=('', button_font_size))
button_N1.grid(column=2, row=1)

button_N2 = tk.Button(root, text=bingo_N[1], command=lambda : open(button_N2), font=('', button_font_size))
button_N2.grid(column=2, row=2)

button_N3 = tk.Button(root, text='FREE', command=lambda : open(button_N3), font=('', 25))
button_N3.grid(column=2, row=3, sticky=tk.NSEW)

button_N4 = tk.Button(root, text=bingo_N[2], command=lambda : open(button_N4), font=('', button_font_size))
button_N4.grid(column=2, row=4)

button_N5 = tk.Button(root, text=bingo_N[3], command=lambda : open(button_N5), font=('', button_font_size))
button_N5.grid(column=2, row=5)

# G列
label_G = tk.Label(root, text='G', font=('', label_font_size)).grid(column=3, row=0)

button_G1 = tk.Button(root, text=bingo_G[0], command=lambda : open(button_G1), font=('', button_font_size))
button_G1.grid(column=3, row=1)

button_G2 = tk.Button(root, text=bingo_G[1], command=lambda : open(button_G2), font=('', button_font_size))
button_G2.grid(column=3, row=2)

button_G3 = tk.Button(root, text=bingo_G[2], command=lambda : open(button_G3), font=('', button_font_size))
button_G3.grid(column=3, row=3)

button_G4 = tk.Button(root, text=bingo_G[3], command=lambda : open(button_G4), font=('', button_font_size))
button_G4.grid(column=3, row=4)

button_G5 = tk.Button(root, text=bingo_G[4], command=lambda : open(button_G5), font=('', button_font_size))
button_G5.grid(column=3, row=5)

# O列
label_O = tk.Label(root, text='O', font=('', label_font_size)).grid(column=4, row=0)

button_O1 = tk.Button(root, text=bingo_O[0], command=lambda : open(button_O1), font=('', button_font_size))
button_O1.grid(column=4, row=1)

button_O2 = tk.Button(root, text=bingo_O[1], command=lambda : open(button_O2), font=('', button_font_size))
button_O2.grid(column=4, row=2)

button_O3 = tk.Button(root, text=bingo_O[2], command=lambda : open(button_O3), font=('', button_font_size))
button_O3.grid(column=4, row=3)

button_O4 = tk.Button(root, text=bingo_O[3], command=lambda : open(button_O4), font=('', button_font_size))
button_O4.grid(column=4, row=4)

button_O5 = tk.Button(root, text=bingo_O[4], command=lambda : open(button_O5), font=('', button_font_size))
button_O5.grid(column=4, row=5)

reach_label = tk.Label(root, text=' リーチ：', font=('', reach_bingo_font_size), pady=20).grid(column=0, row=6)
reach_count_label = tk.Label(root, text='', font=('', reach_bingo_font_size), pady=20)
reach_count_label.grid(column=1, row=6)
bingo_label = tk.Label(root, text=' ビンゴ：', font=('', reach_bingo_font_size), pady=20).grid(column=2, row=6)
bingo_count_label = tk.Label(root, text='', font=('', reach_bingo_font_size), pady=20)
bingo_count_label.grid(column=3, row=6)

# 伸縮比率
root.columnconfigure([0,1,2,3,4], weight=1)
root.rowconfigure([0,1,2,3,4,5,6], weight=1)

# ボタン、リーチ、ビンゴ処理
def open(self):
    global bB1,bB2,bB3,bB4,bB5,B_reach,B_bingo
    global bI1,bI2,bI3,bI4,bI5,I_reach,I_bingo
    global bN1,bN2,bN3,bN4,bN5,N_reach,N_bingo
    global bG1,bG2,bG3,bG4,bG5,G_reach,G_bingo
    global bO1,bO2,bO3,bO4,bO5,O_reach,O_bingo

    self['state'] = 'disabled'
    self['bg'] = 'black'

    if button_B1['state'] == 'disabled':
        bB1 = True
    if button_B2['state'] == 'disabled':
        bB2 = True
    if button_B3['state'] == 'disabled':
        bB3 = True
    if button_B4['state'] == 'disabled':
        bB4 = True
    if button_B5['state'] == 'disabled':
        bB5 = True

    if button_I1['state'] == 'disabled':
        bI1 = True
    if button_I2['state'] == 'disabled':
        bI2 = True
    if button_I3['state'] == 'disabled':
        bI3 = True
    if button_I4['state'] == 'disabled':
        bI4 = True
    if button_I5['state'] == 'disabled':
        bI5 = True

    if button_N1['state'] == 'disabled':
        bN1 = True
    if button_N2['state'] == 'disabled':
        bN2 = True
    if button_N3['state'] == 'disabled':
        bN3 = True
    if button_N4['state'] == 'disabled':
        bN4 = True
    if button_N5['state'] == 'disabled':
        bN5 = True

    if button_G1['state'] == 'disabled':
        bG1 = True
    if button_G2['state'] == 'disabled':
        bG2 = True
    if button_G3['state'] == 'disabled':
        bG3 = True
    if button_G4['state'] == 'disabled':
        bG4 = True
    if button_G5['state'] == 'disabled':
        bG5 = True

    if button_O1['state'] == 'disabled':
        bO1 = True
    if button_O2['state'] == 'disabled':
        bO2 = True
    if button_O3['state'] == 'disabled':
        bO3 = True
    if button_O4['state'] == 'disabled':
        bO4 = True
    if button_O5['state'] == 'disabled':
        bO5 = True

    # B列リーチ、ビンゴ
    if all((bB2, bB3, bB4, bB5 == True))and bB1 == False or all(
    (bB1, bB3, bB4, bB5 == True)) and bB2 == False or all(
    (bB1, bB2, bB4, bB5 == True)) and bB3 == False or all(
    (bB1, bB2, bB3, bB5 == True)) and bB4 == False or all(
    (bB1, bB2, bB3, bB4 == True)) and bB5 == False:
        if B_reach == False:
            B_reach = True
            reach()
    elif all((bB1, bB2, bB3, bB4, bB5 == True)):
        if B_bingo == False:
            B_bingo = True
            bingo()

    # I列リーチ、ビンゴ
    if all((bI2, bI3, bI4, bI5 == True))and bI1 == False or all(
    (bI1, bI3, bI4, bI5 == True)) and bI2 == False or all(
    (bI1, bI2, bI4, bI5 == True)) and bI3 == False or all(
    (bI1, bI2, bI3, bI5 == True)) and bI4 == False or all(
    (bI1, bI2, bI3, bI4 == True)) and bI5 == False:
        if I_reach == False:
            I_reach = True
            reach()
    elif all((bI1, bI2, bI3, bI4, bI5 == True)):
        if I_bingo == False:
            I_bingo = True
            bingo()

    # N列リーチ、ビンゴ
    if all((bN2, bN3, bN4, bN5 == True))and bN1 == False or all(
    (bN1, bN3, bN4, bN5 == True)) and bN2 == False or all(
    (bN1, bN2, bN4, bN5 == True)) and bN3 == False or all(
    (bN1, bN2, bN3, bN5 == True)) and bN4 == False or all(
    (bN1, bN2, bN3, bN4 == True)) and bN5 == False:
        if N_reach == False:
            N_reach = True
            reach()
    elif all((bN1, bN2, bN3, bN4, bN5 == True)):
        if N_bingo == False:
            N_bingo = True
            bingo()

    # G列リーチ、ビンゴ
    if all((bG2, bG3, bG4, bG5 == True))and bG1 == False or all(
    (bG1, bG3, bG4, bG5 == True)) and bG2 == False or all(
    (bG1, bG2, bG4, bG5 == True)) and bG3 == False or all(
    (bG1, bG2, bG3, bG5 == True)) and bG4 == False or all(
    (bG1, bG2, bG3, bG4 == True)) and bG5 == False:
        if G_reach == False:
            G_reach = True
            reach()
    elif all((bG1, bG2, bG3, bG4, bG5 == True)):
        if G_bingo == False:
            G_bingo = True
            bingo()

    # O列リーチ、ビンゴ
    if all((bO2, bO3, bO4, bO5 == True))and bO1 == False or all(
    (bO1, bO3, bO4, bO5 == True)) and bO2 == False or all(
    (bO1, bO2, bO4, bO5 == True)) and bO3 == False or all(
    (bO1, bO2, bO3, bO5 == True)) and bO4 == False or all(
    (bO1, bO2, bO3, bO4 == True)) and bO5 == False:
        if O_reach == False:
            O_reach = True
            reach()
    elif all((bO1, bO2, bO3, bO4, bO5 == True)):
        if O_bingo == False:
            O_bingo = True
            bingo()

# リーチウィンドウ
def reach():
    global reach_count
    ms.showinfo('BINGO', 'リーチです！')
    reach_count += 1
    reach_count_label['text'] = reach_count

# ビンゴウィンドウ
def bingo():
    global bingo_count
    ms.showinfo('BINGO','ビンゴです！')
    bingo_count += 1
    bingo_count_label['text'] = bingo_count

root.mainloop()