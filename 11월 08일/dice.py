from tkinter import *

def dice_screen() :
  root = Tk()
  root.title("⚁ Random dice! ⚃")
  root.geometry("400x400")
  label = Label(root, text='행운의 숫자를 입력해주세요! : ')
  label.grid(column=0, row=0)
  input_edit = Entry(root, width=15)
  input_edit.grid(column=1, row=0)
#함수 추가할 부분

root = Tk()
root.title("⚁ Random dice! ⚃")
root.geometry("400x400")
label = Label(root, text="★ 랜덤 다이스에 오신걸 환영합니다! ★", fg='yellow', bg='black')
label.pack()

startButton = Button(root, text='주사위 굴리러 가기', width=30, bg='gray19', fg='snow', command=dice_screen)
startButton.place(x=80, y=150)

root.mainloop()
