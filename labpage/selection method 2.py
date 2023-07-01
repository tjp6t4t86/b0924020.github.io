import cv2
import numpy as np

#  win
win = tk.Tk()
win.title("selection method")
win.geometry("1590x790+0+0")
#  邊界=5  (padx=5)

def selection_4(img):
    choice4 = choice4_rad.get()
    if choice4 == "(0)":
        pass
    elif choice4 == "(1)":
        th1 = int(threshold1.get())
        th2 = int(threshold2.get())
        img = cv2.Canny(img, th1, th2)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    return img
def selection_3(img, imgHLS):
    choice_3 = choice3_rad.get()
    choice_2 = choice2_rad.get()
    choice = choice1_rad.get()
    if choice_3 == "(0)":
        return img
    else:
        #  防呆
        try:
            H_L = int(Hue_Low.get())
            H_U = int(Hue_Up.get())
            L_L = int(Light_Low.get())
            L_U = int(Light_Up.get())
            S_L = int(Sat_Low.get())
            S_U = int(Sat_Up.get())
            if H_L < 0 or H_U < 0 or L_L < 0 or L_U < 0 or S_L < 0 or S_U < 0:
                raise Exception()
            mask = cv2.inRange(imgHLS, np.array([H_L, L_L, S_L]), np.array([H_U, L_U, S_U]))
            res = cv2.bitwise_and(img, img, mask=mask)
            return res
        except:
            Hue_Low.set("0")
            Hue_Up.set("0")
            Light_Up.set("0")
            Light_Up.set("0")
            Sat_Low.set("0")
            Sat_Up.set("0")
            msg.showerror('輸入錯誤!', '請輸入正確的數字!')

def selection_2(img):
    choice_2 = choice2_rad.get()
    choice = choice1_rad.get()
    if choice_2 == "(0)":
        return img
    elif choice_2 == "(1)":
        th1 = int(threshold1.get())
        th2 = int(threshold2.get())
        img = cv2.Canny(img, th1, th2)
        return img
    else:
        if choice == "(0)":
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        elif choice == "(1)":
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        elif choice == "(2)":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif choice == "(3)":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif choice == "(4)":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif choice == "(5)":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif choice == "(6)":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

def selection(img):
    choice = choice1_rad.get()
    if choice == "(0)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    elif choice == "(1)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif choice == "(2)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif choice == "(3)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    elif choice == "(4)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    elif choice == "(5)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    elif choice == "(6)":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return img

def cv_imread(filePath):
    img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    ratio = float(size_ratio.get())
    img = cv2.resize(img, (0, 0), fx=ratio, fy=ratio)
    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    img = selection(img)
    img = selection_2(img)
    img = selection_3(img, imgHLS)
    img = selection_4(img)
    return img

def oas():
    #  選取圖、導入
    sfname = filedialog.askopenfilename(title='選擇', filetypes=[('All Files','*'), ("jpeg files","*.jpg"), ("png files","*.png"), ("gif files","*.gif")])
    im = cv_imread(sfname)
    img = Image.fromarray(im)
    img = ImageTk.PhotoImage(image=img)
    photo.img = img
    photo.configure(image=img)

#  按鈕框架
B_fm = tk.Frame(win, width=1000, height=20)
B_fm.pack(side=tk.TOP, fill=tk.BOTH)

#  resize框架
size_fm = tk.Frame(win, width=1000, height=20)
size_fm.pack(side=tk.TOP, fill=tk.BOTH)
size_lbl = tk.Label(size_fm, text="圖放大/縮小倍率:", font=('微軟正黑體', 13))
size_lbl.pack(side=tk.LEFT, padx=5)

#  輸入倍數
size_ratio = tk.StringVar(None, "0.5")
ent_size = tk.Entry(size_fm, width=20, justify='center', textvariable=size_ratio, font=('微軟正黑體', 13))
ent_size.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)


ch_fm = tk.Frame(win, width=1000, height=60)
ch_fm.pack(side=tk.TOP, fill=tk.BOTH)
#  要幹啥
choice1_fm = tk.Frame(ch_fm, width=1000, height=60)
choice1_fm.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
choice1_lbl = tk.Label(choice1_fm, text="圖像色碼", font=('微軟正黑體', 13))
choice1_lbl.pack(anchor=tk.W)

choice1_rad = tk.StringVar(None, "(0)")
r0 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(0) GBA", variable=choice1_rad, value="(0)")  # BGR2->GBA
r0.pack(anchor=tk.W)
r1 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(1) RGB", variable=choice1_rad, value="(1)")  # BGR2->RGB
r1.pack(anchor=tk.W)
r2 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(2) HSV", variable=choice1_rad, value="(2)")  # BGR2->HSV
r2.pack(anchor=tk.W)
r3 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(3) HLS", variable=choice1_rad, value="(3)")  # BGR2->HLS
r3.pack(anchor=tk.W)
r4 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(4) LUV", variable=choice1_rad, value="(4)")  # BGR2->LUV
r4.pack(anchor=tk.W)
r5 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(5) YUV", variable=choice1_rad, value="(5)")  # BGR2->YUV
r5.pack(anchor=tk.W)
r6 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(6) LAB", variable=choice1_rad, value="(6)")  # BGR2->LAB
r6.pack(anchor=tk.W)
r4 = tk.Radiobutton(choice1_fm, font=('微軟正黑體', 13), text="(7) BGR", variable=choice1_rad, value="(7)")  # x
r4.pack(anchor=tk.W)
#  其他
choice2_fm = tk.Frame(ch_fm, width=1000, height=60)
choice2_fm.pack(side=tk.LEFT, fill=tk.BOTH, padx=25)
choice2_lbl = tk.Label(choice2_fm, text="其他功能", font=('微軟正黑體', 13))
choice2_lbl.pack(anchor=tk.W)

choice2_rad = tk.StringVar(None, "(0)")
r_0 = tk.Radiobutton(choice2_fm, font=('微軟正黑體', 13), text="(0) 原圖", variable=choice2_rad, value="(0)")
r_0.pack(anchor=tk.W)
r_1 = tk.Radiobutton(choice2_fm, font=('微軟正黑體', 13), text="(1) 輪廓", variable=choice2_rad, value="(1)")  # Canny
r_1.pack(anchor=tk.W)
r_2 = tk.Radiobutton(choice2_fm, font=('微軟正黑體', 13), text="(2) 灰階", variable=choice2_rad, value="(2)")  # BGR2->GRAY
r_2.pack(anchor=tk.W)

#  mask
choice3_fm = tk.Frame(ch_fm, width=1000, height=100)
choice3_fm.pack(side=tk.LEFT, fill=tk.BOTH, padx=25)
choice3_lbl = tk.Label(choice3_fm, text="遮罩是否啟用", font=('微軟正黑體', 13))
choice3_lbl.pack(anchor=tk.W)
choice3_fm_0 = tk.Frame(choice3_fm, width=1000, height=20)
choice3_fm_0.pack(side=tk.TOP, fill=tk.BOTH, padx=0)
choice3_rad = tk.StringVar(None, "(0)")
r20 = tk.Radiobutton(choice3_fm_0, font=('微軟正黑體', 13), text="否", variable=choice3_rad, value="(0)")  # x
r20.pack(side=tk.LEFT)
r21 = tk.Radiobutton(choice3_fm_0, font=('微軟正黑體', 13), text="是", variable=choice3_rad, value="(1)")
r21.pack(side=tk.LEFT)

choice3_fm_1 = tk.Frame(choice3_fm, width=1000, height=20)
choice3_fm_1.pack(side=tk.TOP, fill=tk.BOTH, padx=0)
ch3_lbl_1 = tk.Label(choice3_fm_1, text="Hue:", font=('微軟正黑體', 13))
ch3_lbl_1.pack(side=tk.LEFT)
Hue_Low = tk.StringVar(None, '0')
ch3_lbl_H_a = tk.Label(choice3_fm_1, text="下限:", font=('微軟正黑體', 13))
ch3_lbl_H_a.pack(side=tk.LEFT)
Hue_L = tk.Entry(choice3_fm_1, width=5, justify='center', textvariable=Hue_Low, font=('微軟正黑體', 13))
Hue_L.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)
ch3_lbl_H_b = tk.Label(choice3_fm_1, text="上限:", font=('微軟正黑體', 13))
ch3_lbl_H_b.pack(side=tk.LEFT)
Hue_Up = tk.StringVar(None, '255')
Hue_U = tk.Entry(choice3_fm_1, width=5, justify='center', textvariable=Hue_Up, font=('微軟正黑體', 13))
Hue_U.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)

choice3_fm_2 = tk.Frame(choice3_fm, width=1000, height=20)
choice3_fm_2.pack(side=tk.TOP, fill=tk.BOTH, padx=0)
ch3_lbl_1 = tk.Label(choice3_fm_2, text="Lightness:", font=('微軟正黑體', 13))
ch3_lbl_1.pack(side=tk.LEFT)
Light_Low = tk.StringVar(None, '0')
ch3_lbl_L_a = tk.Label(choice3_fm_2, text="下限:", font=('微軟正黑體', 13))
ch3_lbl_L_a.pack(side=tk.LEFT)
Light_L = tk.Entry(choice3_fm_2, width=5, justify='center', textvariable=Light_Low, font=('微軟正黑體', 13))
Light_L.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)
ch3_lbl_L_b = tk.Label(choice3_fm_2, text="上限:", font=('微軟正黑體', 13))
ch3_lbl_L_b.pack(side=tk.LEFT)
Light_Up = tk.StringVar(None, '255')
Light_U = tk.Entry(choice3_fm_2, width=5, justify='center', textvariable=Light_Up, font=('微軟正黑體', 13))
Light_U.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)

choice3_fm_3 = tk.Frame(choice3_fm, width=1000, height=20)
choice3_fm_3.pack(side=tk.TOP, fill=tk.BOTH, padx=0)
ch3_lbl_1 = tk.Label(choice3_fm_3, text="Saturation:", font=('微軟正黑體', 13))
ch3_lbl_1.pack(side=tk.LEFT)
Sat_Low = tk.StringVar(None, '0')
ch3_lbl_S_a = tk.Label(choice3_fm_3, text="下限:", font=('微軟正黑體', 13))
ch3_lbl_S_a.pack(side=tk.LEFT)
Sat_L = tk.Entry(choice3_fm_3, width=5, justify='center', textvariable=Sat_Low, font=('微軟正黑體', 13))
Sat_L.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)
ch3_lbl_S_b = tk.Label(choice3_fm_3, text="上限:", font=('微軟正黑體', 13))
ch3_lbl_S_b.pack(side=tk.LEFT)
Sat_Up = tk.StringVar(None, '255')
Sat_U = tk.Entry(choice3_fm_3, width=5, justify='center', textvariable=Sat_Up, font=('微軟正黑體', 13))
Sat_U.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)


#  附加_2
choice4_fm = tk.Frame(ch_fm, width=1000, height=60)
choice4_fm.pack(side=tk.LEFT, fill=tk.BOTH, padx=25)
choice4_lbl = tk.Label(choice4_fm, text="附加_2", font=('微軟正黑體', 13))
choice4_lbl.pack(anchor=tk.W)
choice4_rad = tk.StringVar(None, "(0)")
r30 = tk.Radiobutton(choice4_fm, font=('微軟正黑體', 13), text="(0) 原圖", variable=choice4_rad, value="(0)")
r30.pack(anchor=tk.W)
r31 = tk.Radiobutton(choice4_fm, font=('微軟正黑體', 13), text="(1) 輪廓", variable=choice4_rad, value="(1)")  # Canny
r31.pack(anchor=tk.W)
r32 = tk.Radiobutton(choice4_fm, font=('微軟正黑體', 13), text="(2) 灰階", variable=choice4_rad, value="(2)")  # BGR2->GRAY
r32.pack(anchor=tk.W)

#  輸入Canny的閥值
choice5_fm = tk.Frame(ch_fm,width=1000,height=20)
choice5_fm.pack(side=tk.LEFT, fill=tk.BOTH,padx=25)
ch5_lbl_1 = tk.Label(choice5_fm, text="輪廓閥值(若無不必)", font=('微軟正黑體', 13))
ch5_lbl_1.pack(anchor=tk.W)
choice5_fm_1 = tk.Frame(choice5_fm,width=1000,height=20)
choice5_fm_1.pack(side=tk.TOP, fill=tk.BOTH,padx=0)
threshold1 = tk.StringVar(None, '100')
ch5_lbl_1 = tk.Label(choice5_fm_1, text="閥值1:", font=('微軟正黑體', 13))
ch5_lbl_1.pack(side=tk.LEFT)
th1 = tk.Entry(choice5_fm_1, width=5, justify='center', textvariable=threshold1, font=('微軟正黑體', 13))
th1.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)
choice5_fm_2 = tk.Frame(choice5_fm,width=1000,height=20)
choice5_fm_2.pack(side=tk.TOP, fill=tk.BOTH,padx=0)
ch5_lbl_2 = tk.Label(choice5_fm_2, text="閥值2:", font=('微軟正黑體', 13))
ch5_lbl_2.pack(side=tk.LEFT)
threshold2 = tk.StringVar(None, '200')
th2 = tk.Entry(choice5_fm_2, width=5, justify='center', textvariable=threshold2, font=('微軟正黑體', 13))
th2.pack(side=tk.LEFT, padx=0, pady=7, fill=tk.Y)

#  開始
B1 = tk.Button(B_fm, text="按此開始", font=('微軟正黑體', 13), command=oas)
B1.pack(side=tk.LEFT, padx=5)

#  創建canvas
canvas = tk.Canvas(win, width=1500, height=400, scrollregion=(0, 0, 1600, 1500))
canvas.pack(side=tk.TOP)
frame = tk.Frame(canvas)
#  把frame放在canvas
frame.place(width=1480, height=380)

#   滾動條
vbar = tk.Scrollbar(canvas,orient=tk.VERTICAL)
vbar.place(x = 1480, width=20, height=400)
vbar.configure(command=canvas.yview)
hbar = tk.Scrollbar(canvas,orient=tk.HORIZONTAL)
hbar.place(x =0, y=390, width=1480, height=20)
hbar.configure(command=canvas.xview)

#  設置
canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)
canvas.create_window((750, 750), window=frame)

#  圖 框
photoFrame = tk.Frame(frame)
photoFrame.pack(side=tk.TOP)
photo = tk.Label(photoFrame)
photo.pack(side=tk.TOP)

#  執行
win.mainloop()