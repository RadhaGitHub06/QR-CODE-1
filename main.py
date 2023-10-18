#from curses.ascii import isalpha
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR GENERATOR|Developed by RADHA")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="QR CODE GENERATOR",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
#employee details window
#variable

        self.var_emp_code=IntVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)



        emp_code=Label(emp_Frame,text="Employee Id",font=("times new roman",15,'bold'),bg='white').place(x=15,y=50)
        emp_name=Label(emp_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=15,y=90)
        emp_department=Label(emp_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=15,y=130)
        emp_department=Label(emp_Frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=15,y=170)

        txt_code=Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=50)  
        txt_name=Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_name,bg='lightyellow').place(x=200,y=90)
        txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=130)
        txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=170)
        
        btn_generator=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=60,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='CLEAR',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=250,y=250,width=150,height=30)
        
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
###qr code window
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        
        self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_designation.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='':
                self.msg='All Feilds are Required!!!'
                self.lbl_msg.config(text=self.msg,fg='red')
        else:
                qr_data=(f"Employee ID:{self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}")
                qr_code=qrcode.make(qr_data)
                #print(qr_code)
                qr_code=resizeimage.resize_cover(qr_code,[180,180])
                qr_code.save("employee_QR\Emp_"+str(self.var_emp_code.get())+'.png')
                #qr code image update
                self.im=ImageTk.PhotoImage(file="employee_QR\Emp_"+str(self.var_emp_code.get())+'.png')
                self.qr_code.config(image=self.im)


                #updating notification
                self.msg='QR Generated Succesfully!'
                self.lbl_msg.config(text=self.msg,fg='green')
 


root=Tk()
obj=Qr_Generator(root)
root.mainloop()
       