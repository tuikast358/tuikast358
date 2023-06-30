###実行側ファイル###
import tkinter
import Quiz

def click_button_entrance():
    #入店後、選択画面
    #選択キャンパス作成
    button_entrance.place_forget()
    canvas.delete("all")
    canvas.create_image(900, 280, image=hito[0])
    #ラベル
    sitsumon = tkinter.Label(text="麻雀役のクイズをランダムで出題します！\n何問出題しますか?(最大11個)", 
                             font=("MSゴシック",28))
    sitsumon.place(x=100,y=80)
    #入力ボックス
    entry = tkinter.Entry(font=("",25))
    entry.place(x=300, y=250, width=240, height=60)
    kettei = tkinter.Button(text="決定", font=("MS ゴシック",18))
    kettei.place(x=550, y=250, width=100, height=60)
    def judge():
        val = float(entry.get())
        if val <=0 or val > 11:
            entry.place_forget()
            kettei.place_forget()
            sitsumon.place_forget()
            click_button_entrance()
            
        elif val >= 1 and val <= 11:
            entry.place_forget()
            kettei.place_forget()
            sitsumon.place_forget()
            quizmanager.quiz_start(val)                        
    
    kettei["command"] = judge

#ウィンドウ
root = tkinter.Tk()
root.title("麻雀 クイズ")
root.minsize(1220,720)
root.option_add("font",["メイリオ",18])
#キャンバス作成
canvas = tkinter.Canvas(root, width=1200, height=700)
canvas.place(x=20, y=20)
index = [tkinter.PhotoImage(file="img428/building_jansou.png")]
hito = [tkinter.PhotoImage(file="img428/annai_hito.png")]
canvas.create_image(600, 280, image=index[0])
button_entrance = tkinter.Button(text="入店する", height=2, width= 14, font=("MS ゴシック",18))
button_entrance.place(x=520, y=600)
# × button_entrance["command"] = click_button_entrance()
button_entrance["command"] = click_button_entrance


quizmanager = Quiz.QuizManager()

root.mainloop()