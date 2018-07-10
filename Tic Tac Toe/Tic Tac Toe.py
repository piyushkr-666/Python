from tkinter import *
import random
import itertools
import tkinter.messagebox
count=0
l=[]
l1=''
l2=''
l3=[]
win=['123','456','789','147','258','369','159','357']
player=0
player1name=''
player2name=''
s=''
winner=0
player1win=0
player2win=0
def game():
    global player,s,l1,l2,win,winner,count,l3,player2win,player1win
    def setimg(t,y):
        global player,s,l1,l2,win,winner,count,l3,player2win,player1win
        count=count-1
        if player==1:
            player=2
            button1=Button(f,height=125,width=108,image=imgo,state='disable')
            l3.append(button1)
            button1.grid(row=t[0],column=t[1],padx=5,pady=5)
            l1=l1+str(y)
            if len(l1)>=3:
                winp=list(itertools.permutations(list(l1),3))
                for i in win:
                    for j in winp:
                        if tuple(i)==j:
                            winner=1
                            label['text']='{} Wins'.format(player1name)
                            player1win=player1win+1
                            labelp1['text']='{} :- {}'.format(player1name,player1win)
                            for k in l:
                                k['state']='disable'
                            button['text']='Restart'
                            button['state']='active'
        else:    
            player=1
            button1=Button(f,height=125,width=108,image=imgx,state='disable')
            l3.append(button1)
            button1.grid(row=t[0],column=t[1],padx=5,pady=5)
            l2=l2+str(y)
            if len(l2)>=3:
                winp=list(itertools.permutations(list(l2),3))
                for i in win:
                    for j in winp:
                        if tuple(i)==j:
                            winner=1
                            label['text']='{} Wins'.format(player2name)
                            player2win=player2win+1
                            labelp2['text']='{} :- {}'.format(player2name,player2win)
                            for k in l:
                                k['state']='disable'

                            button['text']='Restart'
                            button['state']='active'
                            
        if winner!=1:
            if player==1:
                s='{}\'s Turn'.format(player1name)
            else:
                s='{}\'s Turn'.format(player2name)
            label['text']=s
        if count==0 and winner!=1:
            label['text']='Match Draw'
            button['text']='Restart'
            button['state']='active'


    def setplayer(t):
        global player,s
        if t==1:
            player=1
        if t==2:
            player=2

        if player==1:
            s='{}\'s Turn'.format(player1name)
        else:
            s='{}\'s Turn'.format(player2name)
        label['text']=s
        buttonp1['state']='disable'
        buttonp2['state']='disable'
        for i in l:
            i['state']='active'

    def active():
        global l3,l1,l2,l3,count,winner
        buttonp1['state']='active'
        buttonp2['state']='active'

        label['text']='Whose First'
        button['state']='disable'
        if button['text']=='Restart':
            for j in l3:
                j.destroy()
            l1=''
            l2=''
            l3=[]
            count=9
            winner=0



    


            

    def quitgame():
        answer=tkinter.messagebox.askokcancel('Quit','The application will be closed')
        if answer==True:
            root.destroy()


    


    root=Tk()
    root.title('Tic Tac Toe')
    imgo=PhotoImage(file='o.png')
    imgx=PhotoImage(file='x.png')
    f=Frame(root,bg='powder blue')
    for i in range (3):
        for j in range(3):
            count=count+1
        
            l.append(Button(f,command=lambda x=(i,j),y=count:setimg(x,y),height=8,width=15,state='disable'))
            l[-1].grid(row=i,column=j,padx=5,pady=5)

    f.grid()

    f1=Frame(root,bg='blue',height=100,width=100)
    labelt=Label(f1,bg='blue',text='Tic Tac Toe',fg='red',font=('arial',30,'italic underline bold'))
    labelt.pack()

    label=Label(f1,width=12,text='Welcome',bg='green',fg='white',font=('arial',25,'bold'))
    label.pack(pady=10)
    f2=Frame(f1,bg='blue')
    buttonp1=Button(f2,command=lambda a=1:setplayer(a),width=15,height=2,text='{}'.format(player1name),state='disable')
    buttonp1.grid(padx=3,pady=5)
    buttonp2=Button(f2,command=lambda a=2:setplayer(a),width=15,height=2,text='{}'.format(player2name),state='disable')
    buttonp2.grid(row=0,column=1,padx=3,pady=5)
    f2.pack()
    f3=Frame(f1,bg='blue')
    button=Button(f3,command=active,width=15,height=2,text='Start Game')
    button.grid(padx=3,pady=5)
    buttondes=Button(f3,command=quitgame,width=15,height=2,text='Quit Game')
    buttondes.grid(row=0,column=1,padx=3,pady=5)
    f3.pack()


    labelp2=Label(f1,text='{} :- {}'.format(player2name,player2win),width=12,fg='blue',bg='yellow',font=('comic sans ms',25,'bold italic'))
    labelp2.pack(side='bottom')
    labelp1=Label(f1,text='{} :- {}'.format(player1name,player1win),width=12,fg='blue',bg='yellow',font=('comic sans ms',25,'bold italic'))
    labelp1.pack(side='bottom')
    labelw=Label(f1,text='Score:-',width=12,fg='red',bg='yellow',font=('comic sans ms',25,'bold italic'))
    labelw.pack(pady=20,side='bottom')

    f1.grid(row=0,column=1,sticky='ewns')
    root.mainloop()


def root2():
    global player1name,player2name,player
    if buttonnext['text']=='Finish':
        player2name=entryname.get()
        window.destroy()
        game()
    else:
        player1name=entryname.get()
        labelname['text']='Enter Player 2\'s name (max. 7 letters) :-'
        entryname.delete(0,'end')
        buttonnext['text']='Finish'

window=Tk()
window.title('Tic Tac Toe')
frame=Frame(window,bg='sky blue',height=400,width=400)
labelgreet=Label(frame,text='Tic Tac Toe',fg='Red',bg='sky blue',font=('arial',25,'bold italic underline'),width=20)
labelname=Label(frame,text='Enter Player 1\'s name (max. 7 letters) :-',fg='green',bg='sky blue',font=('arial',13,'bold'))
buttonnext=Button(frame,text='Next',command=root2,width=10)
entryname=Entry(frame,font=('arial',10,'bold'))
labelgreet.grid(row=0,columnspan=2)
labelname.grid(row=1,pady=10)
entryname.grid(row=1,column=1,pady=10)
buttonnext.grid(row=2,columnspan=2,pady=10)

frame.grid()
window.mainloop()
