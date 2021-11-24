from tkinter import *
  
def dice_screen() :
  root = Tk()
  root.title("⚁ Random dice! ⚃")
  root.geometry("400x400")
  label = Label(root, text='행운의 숫자를 입력해주세요! : ', font=(20))
  label.place(x=80, y=0)
  label.pack
  label2 = Label(root) # 입력 받은 값 출력
  def luckey_socre(event) :
        label2.config(text="당신의 행운의 숫자는 : " + edit.get())
  edit = Entry(root, width=15)
  edit.bind('<Return>', luckey_socre)
  edit.place(x=120, y=25)
  edit.pack
  btn1 = Button(root, text='입력', width=8, height=0, command=luckey_socre,)
  btn1.flash()
  btn1.place(x=232, y=25)
  btn1.pack
  label2.place(x=120, y=50)
  label2.pack
  

    

#함수 추가할 부분

root = Tk()
root.title("⚁ Random dice! ⚃")
root.geometry("400x400")
label = Label(root, text="★ 랜덤 다이스에 오신걸 환영합니다! ★", fg='yellow', bg='black', font=(40))
label.pack()
startButton = Button(root, text='주사위 굴리러 가기', width=30, bg='gray19', fg='snow', command=dice_screen)
startButton.place(x=80, y=150)

root.mainloop()
