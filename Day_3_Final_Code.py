# Day 3
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
        create_Account=Button(label,text="Create Account",bg = "#d9d9d9",font='Arial 15 bold',command=self.creating_account,width=15,height=2)
        Withdraw_Amount=Button(label,text="Withdraw Amount",bg="#d9d9d9",font='Arial 15 bold',command=self.withdrawl,width=15,height=2)
        Deposit_Amount=Button(label,text="Deposit Amount",bg = "#d9d9d9",font='Arial 15 bold',command=self.deposit,width=15,height=2)
        Transfer_Amount=Button(label,text="Transfer Amount",bg = "#d9d9d9",font='Arial 15 bold',command=self.transfer,width=15,height=2)
        Account_Details=Button(label,text="Account Details",bg = "#d9d9d9",font='Arial 15 bold',command=self.details,width=15,height=2)
        Exit=Button(label,text="Exit",bg = "#d9d9d9",font='Arial 15 bold',command=self.master1.destroy,width=15,height=2)
        create_Account.place(x=400,y=200)
        Withdraw_Amount.place(x=400,y=300)
        Deposit_Amount.place(x=1050,y=200)
        Transfer_Amount.place(x=1050,y=300)
        Account_Details.place(x=400,y=400)
        Exit.place(x=1050,y=400)
        self.master1.mainloop()

    def creating_account(self):
        self.v = StringVar()
        self.master2=Toplevel(self.master)
        self.master2.geometry('500x500')
        self.master2['background'] = '#58F'
        width= self.master2.winfo_screenwidth()
        height= self.master2.winfo_screenheight()
        self.master2.geometry('%dx%d' %(width,height))
        self.master2.title("Create Account Window")
        frame1=Frame(self.master2,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        label = Label(frame1, image = img_photo)
        label.pack()
        Label(label,text="Online Banking Portal",font='Arial 17 bold').place(relx=0.5, rely=0.1, anchor=CENTER)
        self.name=Label(label,text="Customer Name ",font='Arial 15 bold')
        self.id=Label(label,text="Customer ID ",font='Arial 15 bold')
        self.mno=Label(label,text="Customer Mobile No",font='Arial 15 bold')
        self.acc_no=Label(label,text="Account No",font='Arial 15 bold')
        self.name_entry=Entry(label,textvariable=self.v,font='Arial 15 bold')
        self.id_entry=Entry(label,font='Arial 15 bold')
        self.mobileno_entry=Entry(label,font='Arial 15 bold')
        self.acc_no_entry=Entry(label,font='Arial 15 bold')
        self.name_entry.place(x=700,y=200)
        self.id_entry.place(x=700,y=250)
        self.mobileno_entry.place(x=700,y=300)
        self.acc_no_entry.place(x=700,y=350)
        self.name.place(x=400,y=200)
        self.id.place(x=400,y=250)
        self.mno.place(x=400,y=300)
        self.acc_no.place(x=400,y=350)
        submit=Button(label,text="Submit",bg = "#d9d9d9",font='Arial 15 bold',command=lambda:messagebox.showinfo("information","Account Created Successfully"))
        submit.place(x=840,y=400)
        label.mainloop()
    def calculate_withdrawl(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        if float(self.accounts['amount_entry']) > self.current_balance:
            messagebox.showerror("info","no balance")
            print("Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")
            messagebox.showinfo("Information","Amount Withdrawl Successfully")
    def withdrawl(self):
        self.master3=Toplevel(self.master)
        self.master3.geometry('500x500')
        self.master3['background'] = '#58F'
        self.master3.title("Amount Withdrawl Window")
        self.master3.resizable(False,False)
        width= self.master3.winfo_screenwidth()
        height= self.master3.winfo_screenheight()
        self.master3.geometry('%dx%d' %(width,height))
        frame1=Frame(self.master3,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        label = Label(frame1, image = img_photo)
        label.pack()
        Label(label,text="Online Banking Portal",font='Arial 17 bold').place(relx=0.5, rely=0.1, anchor=CENTER)
        acc_no_label=Label(label,text="Enter Your Account No:",font='Arial 15 bold')
        amount_label=Label(label,text="Enter Your Amount:",font='Arial 15 bold')
        acc_no_label.place(x=400,y=200)
        amount_label.place(x=400,y=250)
        acc_no_entry=Entry(label,font='Arial 15 bold')
        amount_entry=Entry(label,font='Arial 15 bold')
        acc_no_entry.place(x=700,y=200)
        amount_entry.place(x=700,y=250)
        submit=Button(label,text="Submit",font='Arial 15 bold',bg = "#d9d9d9",command=lambda:self.calculate_withdrawl(acc_no_entry, amount_entry))
        submit.place(x=840,y=300)
        self.master3.mainloop()
        
    def calculate_deposit(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        self.current_balance += float(self.accounts['amount_entry'])
        print(f"{float(self.accounts['amount_entry'])} deposited into account {float(self.accounts['acc_no_entry'])}. New balance: {self.current_balance}")

    def deposit(self):
        self.master4=Toplevel(self.master)
        self.master4.geometry('500x500')
        self.master4['background'] = '#58F'
        self.master4.title("Amount Deposite Window")
        self.master4.resizable(False,False)
        width= self.master4.winfo_screenwidth()
        height= self.master4.winfo_screenheight()
        self.master4.geometry('%dx%d' %(width,height))
        frame1=Frame(self.master4,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        label = Label(frame1, image = img_photo)
        label.pack()
        Label(label,text="Online Banking Portal",font='Arial 17 bold').place(relx=0.5, rely=0.1, anchor=CENTER)
        acc_no_label=Label(label,text="Enter Your Account No:",font='Arial 15 bold')
        amount_label=Label(label,text="Enter Your Amount:",font='Arial 15 bold')
        acc_no_label.place(x=400,y=200)
        amount_label.place(x=400,y=250)
        acc_no_entry=Entry(label,font='Arial 15 bold')
        amount_entry=Entry(label,font='Arial 15 bold')
        acc_no_entry.place(x=700,y=200)
        amount_entry.place(x=700,y=250)
        submit=Button(label,text="Submit",font='Arial 15 bold',bg = "#d9d9d9",command=lambda: [self.calculate_deposit(acc_no_entry, amount_entry),messagebox.showinfo("Information","Amount Deposited Successfully")])
        submit.place(x=840,y=300)        
        label.mainloop()
        
    def calculate_transfer(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        if float(self.accounts['amount_entry']) > self.current_balance:
            print("Insufficient balance!")
            messagebox.showerror("info","Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")
            messagebox.showinfo("Information","Amount Transfer Successfully")
    
    def transfer(self):
        self.master5=Toplevel(self.master)
        self.master5.geometry('500x500')
        self.master5['background'] = '#58F'
        self.master5.title("Amount Transfer Window")
        self.master5.resizable(False,False)
        width= self.master5.winfo_screenwidth()
        height= self.master5.winfo_screenheight()
        self.master5.geometry('%dx%d' %(width,height))
        frame1=Frame(self.master5,width=1550, height=1000,bg='#42e3f5')
        frame1.place(anchor='center', relx=0.5, rely=0.5)
        imag=Image.open('./photo-1579621970563-ebec7560ff3e.jpeg','r')
        imag=imag.resize((1550,1000))
        img_photo=ImageTk.PhotoImage(imag)
        label = Label(frame1, image = img_photo)
        label.pack()
        Label(label,text="Online Banking Portal",font='Arial 17 bold').place(relx=0.5, rely=0.1, anchor=CENTER)
        sender_acc_label=Label(label,text="Enter Sender Account No:",font='Arial 15 bold')
        rece_acc_label=Label(label,text="Enter Receiver Account No:",font='Arial 15 bold')
        money_label=Label(label,text="Enter Amount:",font='Arial 15 bold')
        sender_acc_label.place(x=400,y=200)
        rece_acc_label.place(x=400,y=250)
        money_label.place(x=400,y=300)
        sender_acc_entry=Entry(label,font='Arial 15 bold')
        rece_acc_entry=Entry(label,font='Arial 15 bold')
        money_entry=Entry(label,font='Arial 15 bold')
        sender_acc_entry.place(x=700,y=200)
        rece_acc_entry.place(x=700,y=250)
        money_entry.place(x=700,y=300)
        submit=Button(label,text="Submit",font='Arial 15 bold',bg = "#d9d9d9",command=lambda:self.calculate_transfer(sender_acc_entry, money_entry))
        submit.place(x=840,y=350)
        label.mainloop()

    def details(self):
        self.master6=Toplevel(self.master)
        self.master6.geometry('500x500')
        self.master6['background'] = '#58F'
        self.master6.title("Show Details Window")
        self.master6.resizable(False,False)
        width= self.master6.winfo_screenwidth()
        height= self.master6.winfo_screenheight()
        self.master6.geometry('%dx%d' %(width,height))
        label1=Label(self.master6, text="", font=("Arial 17 bold"))
        label1.grid(row=0,column=1,padx=10,pady=10)
        label2=Label(self.master6, text="", font=("Arial 17 bold"))
        label2.grid(row=1,column=1,padx=10,pady=10)
        label3=Label(self.master6, text="", font=("Arial 17 bold"))
        label3.grid(row=2,column=1,padx=10,pady=10)
        label4=Label(self.master6, text="", font=("Arial 17 bold"))
        label4.grid(row=3,column=1,padx=10,pady=10)
        label5=Label(self.master6, text="", font=("Arial 17 bold"))
        label5.grid(row=4,column=1,padx=10,pady=10)
        Label(self.master6,text="Account Number=", font=("Arial 17 bold")).grid(row=0,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer Name=", font=("Arial 17 bold")).grid(row=1,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer ID=", font=("Arial 17 bold")).grid(row=2,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer Mobile No=", font=("Arial 17 bold")).grid(row=3,column=0,padx=10,pady=10)
        Label(self.master6, text="Balance=", font=("Arial 17 bold")).grid(row=4,column=0,padx=10,pady=10)
        acc=self.acc_no_entry.get()
        name=self.name_entry.get()
        id=self.id_entry.get()
        mno=self.mobileno_entry.get()
        label1.configure(text=acc)
        label2.configure(text=name)
        label3.configure(text=id)
        label4.configure(text=mno)
        label5.configure(text=self.current_balance)
        self.master6.mainloop()
                
def main():
    root=Tk()
    app=Transaction(root)
    root.title("Login Page")
    app.login()
    root.mainloop()
           
if __name__=='__main__':
    main()