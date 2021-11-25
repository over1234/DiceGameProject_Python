from tkinter import *
import random


def dice_screen() :
  root = Tk()
  root.title("⚁ Random dice! ⚃")
  root.geometry("400x400")
  label = Label(root, text='행운의 숫자를 입력해주세요! : ', font=(20))
  label.place(x=80, y=0)
  label.pack
  label2 = Label(root, fg='blue',  font=(20))  # 입력 받은 값 출력
  
  def luckey_socre(event) :
        if(edit.get() == '0' or edit.get() == '') :
          label2.config(text="행운의 숫자를 입력해주세요.")
        else:
          label2.config(text="당신의 행운의 숫자는 : " + edit.get())
  edit = Entry(root, width=15)
  
  edit.bind('<Return>', luckey_socre)
  edit.place(x=120, y=45)
  edit.pack
  
  btn1 = Button(root, text='입력', width=8, height=0, command=luckey_socre,)
  btn1.flash()
  btn1.place(x=232, y=45)
  btn1.pack
  
  label2.place(x=80, y = 85)
  label2.pack
  
  label3 = Label(root, fg='blue', font=(20))
  
  label4 = Label(root, fg='blue', font=(20))
  
  def random_Dice() :
    if(edit.get() == '0' or edit.get() == ''):
      label4.config(text="행운의 숫자를 입력해주세요.")
    else :
      rand1 = random.randrange(1, 7)
      rand2 = random.randrange(1, 7)
      label3.config(text=f'주사위 값 : {rand1}, {rand2}')
      
      sum = int(rand1) + int(rand2)
      if(edit.get() == str(sum)) :
        label4.config(text='행운의 주사위! 축하드립니다~')
        label4.place(x=50, y=215)
        
      else :
        label4.config(text='아... 아쉽네요. 하지만 시도는 좋았습니다.')
        label4.place(x=10, y=215)
    
  
  btn2 = Button(root, text='주사위 굴리기', width=20, height=2, command=random_Dice);
  btn2.place(x = 110, y = 125)
  btn2.pack
  
  label3.place(x=110, y= 175)
  label3.pack


  label4.pack

    

#함수 추가할 부분

root = Tk()
root.title("⚁ Random dice! ⚃")
root.geometry("400x400")
label = Label(root, text="★ 랜덤 다이스에 오신걸 환영합니다! ★", fg='yellow', bg='black', font=(40))
label.pack()
startButton = Button(root, text='주사위 굴리러 가기', width=30, height=5, bg='gray19', fg='snow', font=(20), command=dice_screen)
startButton.place(x=28, y=150)

root.mainloop()
