import mysql.connector as a
con = a.connect(host="localhost",user="root",password="smit@77#1432",database="library_m")

def addbook():
    bn = input("Enter Book Name : ")
    c = input("Enter Book code : ")
    t = input("Total Books : ")
    s = input("Enter Subject :")
    data = (bn,c,t,s)
    sql = "insert into books values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">>>>>>----------<<<<<<")
    print("Data Entered Successfully")
    main()

def issuebook():
    n = input("Enter Name : ")
    r = input("Enter Reg No. : ")
    co = input("Enter Book Code : ")
    d = input("Enter the issuing date : ")
    a = "insert into issue values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">>>>>>----------<<<<<<")
    print("Book Issued to : ",n)
    bookup(co,-1)

def submitbook():
    n = input("Enter Name : ")
    r = input("Enter Reg No. : ")
    co = input("Enter Book Code : ")
    d = input("Enter the issuing date : ")
    a = "insert into submit values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">>>>>>----------<<<<<<")
    print("Book Submitted from : ",n)
    bookup(co,1)

def bookup(co,u):
    a = "Select total from books where bcode = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set total = %s where bcode = %s"
    d = (t,co)
    c.execute(sql,d)
    con.commit()
    main()

def deletebook():
    ac = input("Enter Book Code : ")
    a = "delete from books where bcode=%s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def displaybook():
    a = "select * from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name : ",i[0])
        print("Book Code : ",i[1])
        print("Total : ",i[2])
        print("Subject : ",i[3])
        print(">>>>>>----------<<<<<<")
    main()  

def main():
    print("""
                    Library Management

    1. Add Book to library
    2. Issuing the book 
    3. Submitting the book
    4. Deleting the book
    5. Displaying the books
    """)
    choice = input("Choose the Task : ")
    print(">>>>>>----------<<<<<<")
    if(choice == "1"):
        addbook()
    elif(choice == "2"):
        issuebook()
    elif(choice == "3"):
        submitbook()
    elif(choice == "4"):
        deletebook()
    elif(choice == "5"):
        displaybook()
    else:
        print("Wrong Choice Chosen...")
        main()

def pswd():
    ps = input("Enter Password: ")
    if ps == "sk-library":
        main()
    else:
        print("Wrong Password..")
        pswd()
pswd()
    



