from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox





class StudentManagement():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Students management form", font=("times new roman", 40,
                                                                         "bold"), bd=10, relief=GROOVE, bg="white",
                      fg="black")
        title.pack(side=TOP)

#============================All variable===============================
        self.StdID_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Age_var = StringVar()
        self.Gender_var = StringVar()
        self.Programme_var = StringVar()
        self.contact_var = StringVar()
        self.Address_var= StringVar()

        self.sorts_by=StringVar()
        self.sorts_txt=StringVar()
        self.sort_by=StringVar()
        self.sort_txt=StringVar()



#=================manage frame=============================
        manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        manage_Frame.place(x=20,y=100,width=415,height=600)

        m_title=Label(manage_Frame,text="Student Detail",bg="light blue",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_ID=Label(manage_Frame,text="StdID",bg="light blue",fg="white",font=("times new roman",15,"bold"))
        lbl_ID.grid(row=1, column=0,padx=20, pady=10,sticky="W")
        txt_ID=Entry(manage_Frame,textvariable=self.StdID_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_ID.grid(row=1,column=1,padx=20,pady=10,sticky="W")

        lbl_name = Label(manage_Frame, text="Name", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="W")
        txt_name = Entry(manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="W")

        lbl_Email = Label(manage_Frame, text="Email", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txt_Email = Entry(manage_Frame,textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_Age = Label(manage_Frame, text="Age", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_Age.grid(row=4, column=0, padx=20, pady=10, sticky="W")
        self.txt_Age = Entry(manage_Frame,textvariable=self.Age_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Age.grid(row=4, column=1, padx=20, pady=10, sticky="W")

        lbl_Gender = Label(manage_Frame, text="Gender", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=5, column=0, padx=20, pady=10, sticky="W")
        combo_gender = ttk.Combobox(manage_Frame,textvariable=self.Gender_var, font=("times new roman", 15, "bold"),state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=5, column=1, padx=20, pady=10)


        lbl_Address = Label(manage_Frame, text="Address", bg="light blue", fg="white", font=("arial", 15, "bold"))
        lbl_Address.grid(row=8, column=0, padx=20, pady=10, sticky="W")
        txt_Address = Entry(manage_Frame, textvariable=self.Address_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Address.grid(row=8, column=1, padx=20, pady=10, sticky="w")


        lbl_contact = Label(manage_Frame, text="contact", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=7, column=0, padx=20, pady=10, sticky="W")
        txt_contact = Entry(manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=7, column=1, padx=20, pady=10, sticky="W")

        lbl_programme = Label(manage_Frame, text="Programme", bg="light blue", fg="white", font=("times new roman", 15, "bold"))
        lbl_programme.grid(row=6, column=0, padx=20, pady=10, sticky="W")
        combo_programme = ttk.Combobox(manage_Frame,textvariable=self.Programme_var, font=("times new roman", 15, "bold"),state='readonly')
        combo_programme['values'] = ("Bsc Hons incomputing", "Bsc Hons in Ethical Hacking")
        combo_programme.grid(row=6, column=1, padx=20, pady=10)

#==================Button=========================================================

        btn_Frame = Frame(manage_Frame, bd=4, relief=RIDGE, bg="light blue")
        btn_Frame.place(x=10, y=530, width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



#==================== Detail Frame===================================================================




        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        Detail_Frame.place(x=500, y=100, width=1050, height=560)

        lbl_search=Label(Detail_Frame,text="Search By",bg="light blue",fg="white",font=("times new roaman",
                                10,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")



        self.combo_sort = ttk.Combobox(Detail_Frame, font=("times new roman", 10, "bold"), width=10,state='readonly')
        self.combo_sort['values'] = ("StdID", "Name","Email", "Age","Gender","Programme","Contact","Address")
        self.combo_sort.grid(row=0, column=3, padx=20, pady=10)



        self.txt_search = Entry(Detail_Frame,textvariable=self.sorts_txt,width=13, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, padx=20, pady=10, sticky="W")



        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=2, padx=10, pady=10)
        sortallbtn = Button(Detail_Frame, text="Sort", width=10,pady=5,command=self.sort_data).grid(row=0, column=5, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="showall", width=10, pady=5, command=self.fetch_data).grid(row=0, column=6,
                                                                                                      padx=10, pady=10)

        testing_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="light blue")
        testing_Frame.place(x=10, y=530, width=430)





#=================================Table Frame==========================================================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="light blue")
        Table_Frame.place(x=10, y=70, width=830, height=450)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("StdID","Name","Email","Age","Gender",
                            "Programme","contact","Address"),xscrollcommand=scroll_x.set,
                                   yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("StdID",text="StdID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Programme", text="Programme")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("Address", text="Address")
        self.student_table['show']='headings'
        self.student_table.column("StdID", width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=160)
        self.student_table.column("Age", width=40)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Programme", width=150)
        self.student_table.column("contact", width=50)
        self.student_table.column("Address", width=80)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#============function========
    def add_students(self):
        try:

            if int(self.StdID_var.get()) == "" or str(self.Name_var.get()) == "" or str(
                    self.Email_var.get()) == "" or int(self.Age_var.get()) == "" \
                    or str(self.Gender_var.get()) == "" or str(self.Programme_var.get()) == "" or \
                    int(self.contact_var.get()) == "" or str(self.Address_var.get()) == "":

                messagebox.showerror("Error", "All fields are required!!!")

            else:

                con = mysql.connector.connect(host="localhost", user="root", password="root",
                                              database="softwarica")
                cur = con.cursor()
                cur.execute("insert into student_tables values(%s,%s,%s,%s,%s,%s,%s,%s)", (int(self.StdID_var.get()),
                                                                                     self.Name_var.get(),
                                                                                     self.Email_var.get(),
                                                                                     self.Age_var.get(),
                                                                                     self.Gender_var.get(),
                                                                                     self.Programme_var.get(),
                                                                                     self.contact_var.get(),
                                                                                     self.Address_var.get()
                                                                                     ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Sucess", "Record has been inserted")

        except ValueError:
            messagebox.showerror("Error", "Invalid Input!!")



    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="softwarica")
        cur = con.cursor()
        cur.execute("select *from student_tables")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()

        con.close()

    def clear(self):
        self.StdID_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Age_var.set(""),
        self.Gender_var.set(""),
        self.Programme_var.set(""),
        self.contact_var.set(""),
        self.Address_var.set("")

    def get_cursor(self,ev):
        curosor_row=self.student_table.focus()
        contents=self.student_table.item(curosor_row)
        row=contents['values']

        self.StdID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Age_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Programme_var.set(row[5])
        self.contact_var.set(row[6])
        self.Address_var.set(row[7])


    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="softwarica")
        cur = con.cursor()
        cur.execute("update student_tables set Name=%s,Email=%s,Age=%s,Gender=%s,programme=%s,contact=%s,Address=%s where StdID=%s",
                                                (
                                                  self.Name_var.get(),
                                                  self.Email_var.get(),
                                                  self.Age_var.get(),
                                                  self.Gender_var.get(),
                                                  self.Programme_var.get(),
                                                  self.contact_var.get(),
                                                  self.Address_var.get(),
                                                  self.StdID_var.get()
                                                  ))



        con.commit()
        self.fetch_data()
        self.clear()
        con.close()



    def delete_data(self):

        con=mysql.connector.connect(host="localhost",user="root",password="root",database="softwarica")
        cur=con.cursor()

        cur.execute("Delete from student_tables where Age=%s", (self.txt_Age.get(),))
        print(self.txt_Age.get())
        con.commit()
        print('success')

        con.close()

        self.clear()
        self.fetch_data()
        print('success')




    def search(self,rows):


        data = rows
        def LinearSearch():
            found_list = []
            for i in data:
                if self.txt_search.get() in i:
                    found_list.append(i)

            return found_list
        #con.close()

        return LinearSearch()

    def search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="softwarica")
        cur = con.cursor()

        cur.execute('select * from student_tables')
        rows=cur.fetchall()
        print("rows")
        print(rows)
        row=self.search(rows)

        print("searchedRow")
        print(row)

        if len(rows):
            self.student_table.delete(*self.student_table.get_children())

        for i in row:
            self.student_table.insert('',END,values=i)

        con.close()





    def sort_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="softwarica")
        cur = con.cursor()

        cur.execute('select * from student_tables')
        list_i=cur.fetchall()
        rows=self.Sort(list_i)
        print(rows)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('',END,values=row)

        con.close()

    def Sort(self,list_i):

        l = len(list_i)
        if self.combo_sort.get()=="StdID":
            fieldId = 0
        elif self.combo_sort.get()=="Name":
            fieldId = 1
        elif self.combo_sort.get()=="Email":
            fieldId = 2
        elif self.combo_sort.get() == "Age":
            fieldId = 3
        elif self.combo_sort.get() == "Gender":
            fieldId = 4
        elif self.combo_sort.get() == "Programme":
            fieldId = 5
        elif self.combo_sort.get() == "Contact":
            fieldId = 6
        else:
            fieldId = 7

        print(fieldId)

        for i in range(0, l):
            for j in range(0, l - i - 1):
                if list_i[j][fieldId] > list_i[j+1][fieldId]:
                    list_i[j],list_i[j+1]=list_i[j+1], list_i[j]

        #con.close()
        return list_i






if __name__=='__main__':
    root=Tk()
    application=StudentManagement(root)
    root.mainloop()
