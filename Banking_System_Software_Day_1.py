# Day 1
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
class Transaction:
    global acc_no_entry
    global name_entry
    global id_entry
    global balance_entry
    global mobileno_entry
    def __init__(self,master):
        self.accounts={}
        self.master=master
        self.current_balance=0
        self.master.title("Banking Management System")
        width= self.master.winfo_screenwidth()
        height= self.master.winfo_screenheight()
        self.master.geometry('%dx%d' %(width,height))
        self.master['background'] = '#58F'
        
    def login(self):
        frame1=Frame(self.master,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        im_label = Label(frame1, image = img_photo)
        im_label.pack()
        label=Label(im_label, text="Welcome To Banking System Software",font='Arial 17 bold')
        label.place(relx=0.5, rely=0.1, anchor=CENTER)
        name=Label(im_label,text="User Name",font='Arial 15 bold',width=12,height=1)
        user_name=Entry(im_label,width=14, font=('Arial 17'))
        password=Label(im_label,text="Password",font='Arial 15 bold',width=12,height=1)
        user_password=Entry(im_label,show="*",width=14, font=('Arial 17'))
        name.place(x=400, y=300)
        user_name.place(x=600, y=300)
        password.place(x=400, y=400)
        user_password.place(x=600, y=400)
        log_in=Button(im_label,text="Log In",width=8,height=1,font='Arial 15 bold',command=self.main_page)
        log_in.place(x=680,y=470)
        self.master.mainloop() 
            
    def main_page(self):
        self.master1=Toplevel(self.master)
        self.master1.geometry('500x500')
        self.master1['background'] = '#42e3f5'
        width= self.master1.winfo_screenwidth()
        height= self.master1.winfo_screenheight()
        self.master1.geometry('%dx%d' %(width,height))
        self.master1.title("Main Window")
        frame1=Frame(self.master1,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        label = Label(frame1, image = img_photo)
        label.pack()
        Label(label,text="Online Banking Portal",font='Arial 17 bold').place(relx=0.5, rely=0.1, anchor=CENTER)
        create_Account=Button(label,text="Create Account",bg = "#d9d9d9",font='Arial 15 bold',width=15,height=2)
        Withdraw_Amount=Button(label,text="Withdraw Amount",bg="#d9d9d9",font='Arial 15 bold',width=15,height=2)
        Deposit_Amount=Button(label,text="Deposit Amount",bg = "#d9d9d9",font='Arial 15 bold',width=15,height=2)
        Transfer_Amount=Button(label,text="Transfer Amount",bg = "#d9d9d9",font='Arial 15 bold',width=15,height=2)
        Account_Details=Button(label,text="Account Details",bg = "#d9d9d9",font='Arial 15 bold',width=15,height=2)
        Exit=Button(label,text="Exit",bg = "#d9d9d9",font='Arial 15 bold',command=self.master1.destroy,width=15,height=2)
        create_Account.place(x=400,y=200)
        Withdraw_Amount.place(x=400,y=300)
        Deposit_Amount.place(x=1050,y=200)
        Transfer_Amount.place(x=1050,y=300)
        Account_Details.place(x=400,y=400)
        Exit.place(x=1050,y=400)
        self.master1.mainloop()
    
    
    
def main():
    root=Tk()
    app=Transaction(root)
    root.title("Login Page")
    app.login()
    root.mainloop()
           
if __name__=='__main__':
    main()
        
        