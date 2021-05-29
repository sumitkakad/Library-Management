from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import*
from tkinter import messagebox

class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management")
        self.root.geometry("1600x900+0+0")

        lbltitle=Label(self.root,text = "Library Management",bg="powder blue",fg="black",bd=20,relief=RIDGE,font=("times new roman",45,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1590,height=400)

        #==============Variables===========
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdate_var=StringVar()
        self.actualprice_var=StringVar()



        #==========DataframeLeft========

        DataFrameLeft=LabelFrame(frame,text = "Library Members Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=360)

        lblMember = Label(DataFrameLeft,bg="powder blue",text="Member type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Teacher")
        comMember.grid(row=0,column=1)

        lblPRN_NO = Label(DataFrameLeft,bg="powder blue",text="PRN NO. : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_No = Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",12,"bold"),width=30)
        txtPRN_No.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft,bg="powder blue",text="ID NO. : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",12,"bold"),width=30)
        txtTitle.grid(row=2,column=1)

        lblFirstName = Label(DataFrameLeft,bg="powder blue",text="First Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",12,"bold"),width=30)
        txtFirstName.grid(row=3,column=1)

        lblLastName = Label(DataFrameLeft,bg="powder blue",text="Last Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",12,"bold"),width=30)
        txtLastName.grid(row=4,column=1)

        lblAddress1 = Label(DataFrameLeft,bg="powder blue",text="Address 1 : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1 = Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman",12,"bold"),width=30)
        txtAddress1.grid(row=5,column=1)

        lblAddress2 = Label(DataFrameLeft,bg="powder blue",text="Address 2 : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2 = Entry(DataFrameLeft,textvariable=self.address2_var,font=("times new roman",12,"bold"),width=30)
        txtAddress2.grid(row=6,column=1)

        lblPostCode= Label(DataFrameLeft,bg="powder blue",text="Post Code : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode = Entry(DataFrameLeft,textvariable=self.postcode_var,font=("times new roman",12,"bold"),width=30)
        txtPostCode.grid(row=7,column=1)

        lblMobile = Label(DataFrameLeft,bg="powder blue",text="Mobile No. : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",12,"bold"),width=30)
        txtMobile.grid(row=8,column=1)

        lblBookID= Label(DataFrameLeft,bg="powder blue",text="Book Id. : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID = Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",12,"bold"),width=30)
        txtBookID.grid(row=0,column=3)

        lblBookTitle = Label(DataFrameLeft,bg="powder blue",text="Book Title : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle = Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",12,"bold"),width=30)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor = Label(DataFrameLeft,bg="powder blue",text="Author Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor = Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",12,"bold"),width=30)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed = Label(DataFrameLeft,bg="powder blue",text="Date Borrowed : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",12,"bold"),width=30)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue = Label(DataFrameLeft,bg="powder blue",text="Due Date : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue = Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",12,"bold"),width=30)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook = Label(DataFrameLeft,bg="powder blue",text="Days on Book : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("times new roman",12,"bold"),width=30)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine = Label(DataFrameLeft,bg="powder blue",text="Late Return Fine : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("times new roman",12,"bold"),width=30)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdate = Label(DataFrameLeft,bg="powder blue",text="Date Over Due : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate = Entry(DataFrameLeft,textvariable=self.dateoverdate_var,font=("times new roman",12,"bold"),width=30)
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice = Label(DataFrameLeft,bg="powder blue",text="Actual price : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice = Entry(DataFrameLeft,textvariable=self.actualprice_var,font=("times new roman",12,"bold"),width=30)
        txtActualPrice.grid(row=8,column=3)


        

        #=========Data Frame Right=========

        DataFrameRight=LabelFrame(frame,text = "Books Availables And Data Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=620,height=360)

        self.txtBox=Text(DataFrameRight , font=("times new roman",12,"bold"), width=38,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight) 
        listScrollbar.grid(row=0,column=1, sticky="ns")

        listBooks=["Python learning", "Machine learning", "Data Science","ML+AI","Deep Learning","Data Structure and Algorithm","Real Python Cousrse","Java Programming","Java Basics","C++ Programming","To Kill a Mockingbird","One Hundred Years of Solitude","A Passage to India","Invisible Man","Don Quixote","Beloved","Mrs. Dalloway","Things Fall Apart","Jane Eyre","The Color Purple","C++ Basics","Programming advance","Database Management","MySQL","TKinter"]

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=28,height=16) 
        listBox.grid(row=0,column=0,padx=4) 
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #====ButtonsFrame===
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1590,height=70)

        btnAddData=Button (Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=24, bg="blue",fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData=Button (Framebutton, command=self.showdata, text="Show Data", font=("arial",12, "bold"),width=24,bg="blue",fg="white") 
        btnAddData.grid(row=0,column=1)

        btnAddData=Button (Framebutton, command=self.update, text="Update", font=("arial", 12, "bold"),width=24,bg="blue",fg="white") 
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton, command=self.delete, text="Delete", font=("arial",12, "bold"),width=24,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button (Framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"),width=24,bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button (Framebutton, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=24,bg="blue",fg="white") 
        btnAddData.grid(row=0,column=5)

        #====Information=Frame===
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1590,height=225)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1530,height=194)

        xscroll=ttk.Scrollbar(Table_frame,orient= HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient= VERTICAL )

        self.library_table = ttk.Treeview(Table_frame,column=("Membertype","PRNno","Title","Firstname","Lastname","Address1","Address2","Postid","Mobile","Bookid","Booktitle","Author","Dateborrowed","Datedue","Daysonbook","Latereturnfine","Dateoverdue","Actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Membertype",text="Member type")
        self.library_table.heading("PRNno",text="PRN NO.")
        self.library_table.heading("Title",text="Title")
        self.library_table.heading("Firstname",text="First Name")
        self.library_table.heading("Lastname",text="Last Name")
        self.library_table.heading("Address1",text="Address1")
        self.library_table.heading("Address2",text="Address2")
        self.library_table.heading("Postid",text="Post Code")
        self.library_table.heading("Mobile",text="Mobile No.")
        self.library_table.heading("Bookid",text="Book ID.")
        self.library_table.heading("Booktitle",text="Book Title")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("Dateborrowed",text="Date Borrowed")
        self.library_table.heading("Datedue",text="Date Due")
        self.library_table.heading("Daysonbook",text="Days On Book")
        self.library_table.heading("Latereturnfine",text="Late Return Fine")
        self.library_table.heading("Dateoverdue",text="Date Over Due")
        self.library_table.heading("Actualprice",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Membertype",width=100)
        self.library_table.column("PRNno",width=100)
        self.library_table.column("Title",width=100)
        self.library_table.column("Firstname",width=100)
        self.library_table.column("Lastname",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("Postid",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("Bookid",width=100)
        self.library_table.column("Booktitle",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("Dateborrowed",width=100)
        self.library_table.column("Datedue",width=100)
        self.library_table.column("Daysonbook",width=100)
        self.library_table.column("Latereturnfine",width=100)
        self.library_table.column("Dateoverdue",width=100)
        self.library_table.column("Actualprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="smit@77#1432",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdate_var.get(),
                                                                                                                self.actualprice_var.get()
                                                                                                              ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been added successfully !!")

    
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="smit@77#1432",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostID=%s,Mobile=%s,BookTitle=%s,Author=%s,Dateborrowed=%s,Datedue=%s,Daysofbook=%s,Latereturnfine=%s,DateoverDue=%s,Actualprice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdate_var.get(),
                                                                                                                self.actualprice_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated.")

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="smit@77#1432",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),                                                                                                        
        self.address1_var.set(row[5]),                                                                                                       
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]), 
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdate_var.set(row[16]),
        self.actualprice_var.set(row[17])


    def showdata(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID NO:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile NO:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdate_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+self.actualprice_var.get()+"\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),                                                                                                        
        self.address1_var.set(""),                                                                                                       
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""), 
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdate_var.set(""),
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management", "Do you want to exit ?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="smit@77#1432",database="mydata")
            my_cursor = conn.cursor()
            query = "delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")


if __name__ == "__main__":
    root = Tk()
    obj = Library(root)
    root.mainloop()