import tkinter as tk
from datetime import datetime

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.width=450
        self.height=400

        master.geometry(str(self.width)+"x"+str(self.height)) #ウィンドウの作成

        master.title("日付時刻") #タイトル
        self.master.config(bg="pink") #ウィンドウの背景色

        master.after(50, self.update) #ループ処理

    def update(self): #ループ処理
        #日付時刻の作成
        self.label4 = tk.Label(text=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),fg="black",bg="pink",font=("Helvetica",30,"bold"))
        self.label4.place(x=40,y=175)

        self.master.after(50,self.update)

def main():
    win = tk.Tk()
    win.resizable(width=False, height=False) #ウィンドウを固定サイズに
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()