from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login():
    email =email_input.get()
    password=password_input.get()
    if email == 'vivek@123' and password =='123456':
        messagebox.showinfo('yes','login Successfully')
    else:
        messagebox.showerror('Error','Login Failed')
    
    
    
    
root =Tk()

root.title('login form')
# root.iconbitmap('favicon.ico) this line is use to logo change

#root.minsize(100,100)
#root.maxsize(400,400)

root.geometry('350x500')
root.configure(background='#0096DC')
img=Image.open('first/flipcard.jpg')
resized_img= img.resize((70,70))
img=ImageTk.PhotoImage(resized_img)


img_label =Label(root,image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))
email_input=Entry(root,width=50)
email_input.pack(ipady=6)


password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(22,5))
password_label.config(font=('verdana',12))
password_input=Entry(root,width=50)
password_input.pack(ipady=8)


login_btn =Button(root,text='login Here',bg='white',fg='black',command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))
root.mainloop()