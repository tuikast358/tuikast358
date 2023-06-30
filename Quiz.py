#実行はmajanQのほうで
import tkinter
import random 
import time


mondai_val = 11
seikai = 0
ok = 0
miss = 0
num = 0
count = 1

l = list(range(mondai_val))
random.shuffle(l)

class QuizManager:
    #コンストラクタ
    def __init__(self):
        self.dialog = tkinter.Frame(width=1220, height=720)
        self.dialog.place(x=0, y=0)
        self.canvas = tkinter.Canvas(self.dialog, width=1200, height=720)
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, 1200, 500, fill="black")
        self.label = tkinter.Label(self.dialog, text="ラベルインデックス",font=("MS ゴシック",40), 
                                   fg="black", bg="yellow")
        self.label.place(x=80, y=80)
        #ボタン作成
        self.obutton = tkinter.Button(self.dialog, text="1.",font=("MS ゴシック",18) )
        self.obutton.place(x=70, y=600, width=285, height=60)
        self.obutton["command"] = self.click_one
        self.twbutton = tkinter.Button(self.dialog, text="2.",font=("MS ゴシック",18) )
        self.twbutton.place(x=470, y=600, width=285, height=60)
        self.twbutton["command"] = self.click_two
        self.thbutton = tkinter.Button(self.dialog, text="3.",font=("MS ゴシック",18) )
        self.thbutton.place(x=870, y=600, width=285, height=60)
        self.thbutton["command"] = self.click_three
        

        #牌画像読み込み
        self.manzu = [tkinter.PhotoImage(file="img428/back.png"),
                     tkinter.PhotoImage(file="img428/manzu1.png"),
                     tkinter.PhotoImage(file="img428/manzu2.png"),
                     tkinter.PhotoImage(file="img428/manzu3.png"),
                     tkinter.PhotoImage(file="img428/manzu4.png"),
                     tkinter.PhotoImage(file="img428/manzu5.png"),
                     tkinter.PhotoImage(file="img428/manzu6.png"),
                     tkinter.PhotoImage(file="img428/manzu7.png"),
                     tkinter.PhotoImage(file="img428/manzu8.png"),
                     tkinter.PhotoImage(file="img428/manzu9.png")]
        self.pinzu = [tkinter.PhotoImage(file="img428/back.png"),
                     tkinter.PhotoImage(file="img428/pinzu1.png"),
                     tkinter.PhotoImage(file="img428/pinzu2.png"),
                     tkinter.PhotoImage(file="img428/pinzu3.png"),
                     tkinter.PhotoImage(file="img428/pinzu4.png"),
                     tkinter.PhotoImage(file="img428/pinzu5.png"),
                     tkinter.PhotoImage(file="img428/pinzu6.png"),
                     tkinter.PhotoImage(file="img428/pinzu7.png"),
                     tkinter.PhotoImage(file="img428/pinzu8.png"),
                     tkinter.PhotoImage(file="img428/pinzu9.png")]
        self.souzu = [tkinter.PhotoImage(file="img428/back.png"),
                     tkinter.PhotoImage(file="img428/souzu1.png"),
                     tkinter.PhotoImage(file="img428/souzu2.png"),
                     tkinter.PhotoImage(file="img428/souzu3.png"),
                     tkinter.PhotoImage(file="img428/souzu4.png"),
                     tkinter.PhotoImage(file="img428/souzu5.png"),
                     tkinter.PhotoImage(file="img428/souzu6.png"),
                     tkinter.PhotoImage(file="img428/souzu7.png"),
                     tkinter.PhotoImage(file="img428/souzu8.png"),
                     tkinter.PhotoImage(file="img428/souzu9.png")]
        self.wind = [tkinter.PhotoImage(file="img428/w_ton.png"),
                    tkinter.PhotoImage(file="img428/w_nan.png"),
                    tkinter.PhotoImage(file="img428/w_sya.png"),
                    tkinter.PhotoImage(file="img428/w_pe.png")]
        self.zihai = [tkinter.PhotoImage(file="img428/z_haku.png"),
                     tkinter.PhotoImage(file="img428/z_hatsu.png"),
                     tkinter.PhotoImage(file="img428/z_tyun.png")]   
        #非表示
        self.dialog.place_forget()
       
        
    def ending(self,t,f):
        percent = round(t/(ok+miss), 3)
        self.dialog.place(x=10, y=10)
        self.canvas.delete("all")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
        labeltext = str(count-1) + "問中 " + str(t)+ "問正解\n("+str(miss)+"問不正解)" + "  正答率" + str(percent*100) + "％"
        self.label["text"] = labeltext
        

    def quiz_start(self, n):
        global num, count,seikai
        num = n
        
        if n < count:
            self.ending(ok,miss)
        else:
            mondai = l[count - 1]
            print(mondai)
            
            #### elif == 10(全11問)、494行まで役問題の収録  ####
            ####  その下に、ボタンと確認画面用の関数を設置     ####
            if mondai == 0:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #四暗刻単騎[スーアンコウ単騎](アンコウ4つと単騎待ち):正解は2番に設定
                seikai = 2
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.タンヤオ"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.四暗刻(スーアンコー)単騎"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.清一色(チンイツ)"
                self.thbutton["text"] = thbuttontext   
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[2])
                for i in range(3, 6):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i])
                for i in range(6, 9):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i-3])
                for i in range(9, 12):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i-6])
                for i in range(12, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[8])
                count += 1
                
            elif mondai == 1:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #タンヤオ: 正解は1番に設定
                seikai = 1
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.タンヤオ"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.平和(ピンフ)"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.三暗刻(サンアンコー)"
                self.thbutton["text"] = thbuttontext   
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[5])
                for i in range(3, 6):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i])
                for i in range(6, 9):
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[3])
                for i in range(9, 12):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[i-7])
                for i in range(12, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[8])
                count += 1
            
            elif mondai == 2:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #ピンフ(順子4つと頭):正解は3番に設定
                seikai = 3
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                obuttontext = "1.三色同順"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.タンヤオ"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.平和(ピンフ)"
                self.thbutton["text"] = thbuttontext
                
                for i in range(5): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i+4])
                for i in range(5, 8):
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[i-4])
                for i in range(8, 10):
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[9])
                for i in range(10, 13):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[i-6])
                for i in range(13, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[9])
                count += 1
            
            elif mondai == 3:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #大三元:正解は2番に設定
                seikai =2
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.役牌(ヤクハイ)"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.大三元"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.三暗刻(サンアンコー)"
                self.thbutton["text"] = thbuttontext
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i+1])
                for i in range(3, 5):
                    self.canvas.create_image(i*70+50, 250, image=self.wind[0])
                for i in range(5, 8):
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[0])
                for i in range(8, 11):
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[1])
                for i in range(11, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[2])
                count += 1
    
            elif mondai == 4:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #国士無双:正解は1番に設定
                seikai = 1
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.国士無双"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.九蓮宝燈"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.大四喜(ダイスーシー)"
                self.thbutton["text"] = thbuttontext
                
                for i in range(2): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[1])
                for i in range(2,3):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[9])
                for i in range(3,4):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[1])
                for i in range(4, 5):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[9])
                for i in range(5, 6):
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[1])
                for i in range(6, 7):
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[9])
                for i in range(7, 11):
                    self.canvas.create_image(i*70+50, 250, image=self.wind[i-7])
                for i in range(11, 13):
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[i-11])
                for i in range(13,14):
                    i = i+1    
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[2])
                count += 1
    
            elif mondai == 5:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #緑一色:正解は3番に設定
                seikai = 3
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.役牌"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.一気通貫"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.緑一色(リューイーソー)"
                self.thbutton["text"] = thbuttontext
                
                for i in range(2): 
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[2])
                for i in range(2,4):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[3])
                for i in range(4,6):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[4])
                for i in range(6, 9):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[6])
                for i in range(9, 11):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[8])
                for i in range(11, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[1])
                count += 1
            
            elif mondai == 6:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #九蓮宝燈:正解は1番に設定
                seikai = 1
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.九蓮宝燈"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.字一色(ツーイーソー)"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.タンヤオ"
                self.thbutton["text"] = thbuttontext
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[1])
                for i in range(3,6):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i-1])
                for i in range(6,8):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[5])
                for i in range(8, 11):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i-2])
                for i in range(11, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[9])
                count += 1
    
            elif mondai == 7:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #字一色:正解は3番に設定
                seikai = 3
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.役なし"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.大三元"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.字一色(ツーイーソー)"
                self.thbutton["text"] = thbuttontext
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.wind[0])
                for i in range(3,6):
                    self.canvas.create_image(i*70+50, 250, image=self.wind[1])
                for i in range(6,8):
                    self.canvas.create_image(i*70+50, 250, image=self.wind[2])
                for i in range(8, 11):
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[0])
                for i in range(11, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[2])
                count += 1
    
            elif mondai == 8:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #混一色:正解は2番に設定
                seikai = 2
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.字一色(ツーイーソー)"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.混一色(ホンイツ)"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.役牌"
                self.thbutton["text"] = thbuttontext
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[i+1])
                for i in range(3,6):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[5])
                for i in range(6,9):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[i])
                for i in range(9, 12):
                    self.canvas.create_image(i*70+50, 250, image=self.wind[2])
                for i in range(12, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[0])
                count += 1
                
            elif mondai == 9:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #七対子:正解は番に設定
                seikai = 1
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.七対子(チートイツ)"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.平和(ピンフ)"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.タンヤオ"
                self.thbutton["text"] = thbuttontext
                
                for i in range(2): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[1])
                for i in range(2,4):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[4])
                for i in range(4,6):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[7])
                for i in range(6,8):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[3])
                for i in range(8,10):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[8])
                for i in range(10, 12):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[9])
                for i in range(12, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.wind[3])
                count += 1
    
            elif mondai == 10:
                self.obutton["state"] = "normal"
                self.twbutton["state"] = "normal"
                self.thbutton["state"] = "normal"
                #一盃口: 正解は3番に設定
                seikai = 3
                self.dialog.place(x=10, y=10)
                self.canvas.delete("all")
                self.canvas.place(x=0, y=0)
                self.canvas.create_rectangle(0, 0, 1200, 500, fill="blue")
                labeltext = "(" + str(count) + "問目)  "+"選択肢を選んでください"
                self.label["text"] = labeltext
                self.label.place(x=10, y=10)
                
                obuttontext = "1.二盃口(リャンペーコー)"
                self.obutton["text"] = obuttontext   
                twbuttontext = "2.役牌"
                self.twbutton["text"] = twbuttontext   
                thbuttontext = "3.一盃口(イーペーコー)"
                self.thbutton["text"] = thbuttontext   
                
                for i in range(3): 
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i+1])
                for i in range(3, 6):
                    self.canvas.create_image(i*70+50, 250, image=self.manzu[i-2])
                for i in range(6, 9):
                    self.canvas.create_image(i*70+50, 250, image=self.souzu[i-2])
                for i in range(9, 12):
                    self.canvas.create_image(i*70+50, 250, image=self.zihai[2])
                for i in range(12, 14):
                    if i == 13:
                        i = i+1
                    self.canvas.create_image(i*70+50, 250, image=self.pinzu[2])
                count += 1
    

    #1.ボタン
    def click_one(self):
        tmp=0
        self.obutton["state"] = "disabled"
        self.twbutton["state"] = "disabled"
        self.thbutton["state"] = "disabled"
        #global seikai
        if seikai == 1:
            global ok
            ok += 1
            tmp += 1
        else:
            global miss
            miss += 1
        self.confirm(tmp)
        self.quiz_start(num)
    
    #2.ボタン
    def click_two(self):
        tmp=0
        self.obutton["state"] = "disabled"
        self.twbutton["state"] = "disabled"
        self.thbutton["state"] = "disabled"
        #global seikai
        if seikai == 2:
            global ok
            ok += 1
            tmp += 1
        else:
            global miss
            miss += 1          
        self.confirm(tmp)
        self.quiz_start(num)
    
    #3.ボタン
    def click_three(self):
        tmp=0
        self.obutton["state"] = "disabled"
        self.twbutton["state"] = "disabled"
        self.thbutton["state"] = "disabled"          
        #global seikai
        if seikai == 3:
            global ok
            ok += 1
            tmp += 1
        else:
            global miss
            miss += 1
        self.confirm(tmp)
        self.quiz_start(num)
        
    #処理、正解確認画面
    def confirm(self,val):
        if val == 1:
            labeltext = "正解！！"
            self.label["text"] = labeltext        
            self.dialog.update()
            time.sleep(2) 
        else:
            labeltext = "不正解・・・。"
            self.label["text"] = labeltext        
            self.dialog.update()
            time.sleep(2) 
            