from tkinter import*

first_number=second_number=operator=None

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.configure(text=new)
    
def clear():
    result_label.config(text='')
    
    
def get_operator(op):
    global first_number,operator
    
    first_number=int(result_label['text'])
    operator =op
    result_label.config(text='')
    
    
def get_result():
    global first_number,second_number,operator
    
    second_number = int(result_label['text'])
    
    if operator =='+':
        result_label.config(text=str(first_number+second_number))
    elif operator =='-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number ==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number/second_number,2)))
root =Tk()

root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label =Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=15,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))


btn_7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn_7.grid(row=1,column=0)
btn_7.config(font=('verdana',14))

btn_8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn_8.grid(row=1,column=1)
btn_8.config(font=('verdana',14))

btn_9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn_9.grid(row=1,column=2)
btn_9.config(font=('verdana',14))

btn_add=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))


btn_4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn_4.grid(row=2,column=0)
btn_4.config(font=('verdana',14))

btn_5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn_5.grid(row=2,column=1)
btn_5.config(font=('verdana',14))

btn_6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn_6.grid(row=2,column=2)
btn_6.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))


btn_1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn_1.grid(row=3,column=0)
btn_1.config(font=('verdana',14))

btn_2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn_2.grid(row=3,column=1)
btn_2.config(font=('verdana',14))

btn_3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn_3.grid(row=3,column=2)
btn_3.config(font=('verdana',14))

btn_mul=Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))


btn_0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn_0.grid(row=4,column=0)
btn_0.config(font=('verdana',14))

btn_clear=Button(root,text='Clear',bg='#00a65a',fg='white',width=5,height=2,command=lambda:clear())
btn_clear.grid(row=4,column=1)
btn_clear.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=2)
btn_div.config(font=('verdana',14))

btn_equl=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btn_equl.grid(row=4,column=3)
btn_equl.config(font=('verdana',14))




root.mainloop()

