import tkinter as tk
import mysql.connector
from tkinter import messagebox as msgbox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="libraryproject",
)

global final_details
global book_image
HOME_FRAME_BG = "#66806A"
BUTTON_BG = "#EAF0CE"
BUTTON_FONT = ("Arial", 20)
INDIVIDUAL_FRAME_BG = "#7B6B43"
MENU_STRIP = "#685634"


class Library:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(0, 0)
        self.window.geometry("854x480")
        self.window.title("Library Management")
        self.home_button_frame = self.homepage_frame()

    def homepage_frame(self):
        global book_image
        home_frame = tk.Frame(self.window)
        home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        book_image = tk.PhotoImage(file='home_background.png')
        book_label = tk.Label(home_frame, image=book_image)
        book_label.pack()

        # Search Book Button
        button1 = tk.Button(home_frame, text="Search Book", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.search_book_frame()))
        button1.place(x=20, y=130)

        # Search Member Button
        button2 = tk.Button(home_frame, text="Search Member", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.search_member_frame()))
        button2.place(x=20, y=200)

        # Search Author
        button3 = tk.Button(home_frame, text="Search Author", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.search_author_frame()))
        button3.place(x=20, y=270)

        # Issued Books
        button4 = tk.Button(home_frame, text="Book Issues", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.book_issue_frame()))
        button4.place(x=20, y=340)

        button5 = tk.Button(home_frame, text="New Member", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.new_member_frame()))
        button5.place(x=640, y=130)

        button6 = tk.Button(home_frame, text="New Book", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.new_book_frame()))
        button6.place(x=678, y=200)

        button7 = tk.Button(home_frame, text="Edit Stock", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.edit_stock_frame()))
        button7.place(x=676, y=270)

        button8 = tk.Button(home_frame, text="Delete Member", font=BUTTON_FONT, bd=3,bg =BUTTON_BG,
                            command=lambda: self.show_frame(self.delete_member_frame()))
        button8.place(x=615, y=340)

        return home_frame

    # ____________________________________________________________________________________
    def edit_stock_button(self):
        button = tk.Button(self.search_book_frame(), text="Back", font=("Arial", 10, "bold"))
        button.place(x=100, y=280)

    def search_book_result_format(self, book_name):
        global final_details
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM books WHERE book_name = %s or book_id = %s", (book_name, book_name))
            for x in cursor:
                book_id = x[0]
                name_of_book = x[1]
                author_name = x[2]
                price = x[3]
                stock = x[4]

                final_details = "BOOK DETAILS\n----------------\nBook ID: %s \nBook Name : %s \nAuthor Name : %s \nPrice : Rs. %s \nCurrent Stock : %s" % (
                    book_id, name_of_book, author_name, price, stock)

                return final_details
        except:
            final_details = "Please Enter Book Name or ID"
            return final_details

    def get_search_book_result(self, entry):

        result_label = tk.Label(self.search_book_frame(), font=("Helvetica", 15), justify="left", bg=INDIVIDUAL_FRAME_BG,
                                bd=2)
        result_label.place(x=295, y=100)
        result = self.search_book_result_format(entry)
        result_label["text"] = result

    def search_book_frame(self):
        search_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        search_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(search_frame, text="SEARCH BOOK", font=("Helvetica", 25), bg=MENU_STRIP)
        search_title.pack(fill='x')

        search_entry_title = tk.Label(search_frame, text="Name", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        search_entry_title.place(x=170, y=70)

        search_entry = tk.Entry(search_frame, font=("Arial", 15))
        search_entry.place(x=300, y=70)

        search_button = tk.Button(search_frame, text="SEARCH", font=("Helvetica", 12),
                                  command=lambda: self.get_search_book_result(search_entry.get()))
        search_button.place(x=600, y=67)

        return_home = tk.Button(search_frame, text="Back", font=("Helvetica", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))

        return_home.place(x=50, y=280)
        return search_frame

    # ____________________________________________________________________________________
    @staticmethod
    def search_member_result_format(member_names):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM members WHERE member_name = %s or member_id = %s", (member_names, member_names))
        for x in cursor:
            member_id = x[0]
            member_name = x[1]
            member_address = x[2]
            member_phone = x[3]
            final_detail = "MEMBER DETAILS\n----------------\nName : %s \nMember ID : %s\nMember Address : %s\nMember Phone : %s" % (
                member_name, member_id, member_address, member_phone)
            return final_detail

    def get_search_member_result(self, entry):
        result_label = tk.Label(self.search_member_frame(), font=("Arial", 15), justify="left",
                                bg=INDIVIDUAL_FRAME_BG, bd=2)
        result_label.place(x=295, y=125)
        result = self.search_member_result_format(entry)
        result_label["text"] = result

    def search_member_frame(self):
        search_member_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        search_member_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(search_member_frame, text="SEARCH MEMBER", font=("Arial", 25, "bold"), bg=MENU_STRIP)
        search_title.pack(fill='x')

        search_entry_title = tk.Label(search_member_frame, text="MEMBER NAME / ID", font=("Arial", 15, "bold"),
                                      bg=INDIVIDUAL_FRAME_BG)
        search_entry_title.place(x=120, y=70)

        search_entry = tk.Entry(search_member_frame, font=("Arial", 15, "bold"))
        search_entry.place(x=330, y=70)

        search_button = tk.Button(search_member_frame, text="SEARCH", font=("Arial", 12, "bold"),
                                  command=lambda: self.get_search_member_result(search_entry.get()))
        search_button.place(x=600, y=67)

        return_home = tk.Button(search_member_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)
        return search_member_frame

    # ---------------------------------------------------------------------------------
    @staticmethod
    def save_to_database_member(member_name, member_address, member_phone):
        mycursor = db.cursor()
        try:
            mycursor.execute("INSERT INTO members ( member_name, member_address, member_phone) VALUES (%s, %s, %s)",
                             (member_name, member_address, member_phone))
            db.commit()
            msgbox.showinfo("Saved", "Data Saved to Database")
        except:
            msgbox.showinfo("Error Occurred!! Please Try Again")

    def new_member_frame(self):
        new_member_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        new_member_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        new_member_title = tk.Label(new_member_frame, text="ADD NEW MEMBER", font=("Arial", 25, "bold"), bg=MENU_STRIP)
        new_member_title.pack(fill='x')

        name_label = tk.Label(new_member_frame, text="Name *", font=("Arial", 15, "bold"), bg=INDIVIDUAL_FRAME_BG)
        name_label.place(x=300, y=70)
        name_entry = tk.Entry(new_member_frame, font=("Arial", 15, "bold"))
        name_entry.place(x=400, y=70)

        member_address_label = tk.Label(new_member_frame, text="Address", font=("Arial", 15, "bold"),
                                        bg=INDIVIDUAL_FRAME_BG)
        member_address_label.place(x=300, y=120)
        member_address_entry = tk.Entry(new_member_frame, font=("Arial", 15, "bold"))
        member_address_entry.place(x=400, y=120)

        member_phone = tk.Label(new_member_frame, text="Phone *", font=("Arial", 15, "bold"), bg=INDIVIDUAL_FRAME_BG)
        member_phone.place(x=300, y=170)
        member_phone_entry = tk.Entry(new_member_frame, font=("Arial", 15, "bold"))
        member_phone_entry.place(x=400, y=170)

        submit_button = tk.Button(new_member_frame, text="Submit", font=("Arial", 13, "bold"),
                                  command=lambda: self.save_to_database_member(name_entry.get(),
                                                                               member_address_entry.get(),
                                                                               member_phone_entry.get()))
        submit_button.place(x=450, y=220)

        return_home = tk.Button(new_member_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return new_member_frame

    # -------------------------------------------------------------------------------
    @staticmethod
    def save_to_database_book(book_name, author_name, price, quantity, edition):
        mycursor = db.cursor()
        try:
            mycursor.execute(
                "INSERT INTO books ( book_name, author_name, price, stock, edition) VALUES (%s, %s, %s, %s, %s)",
                (book_name, author_name, price, quantity, edition))
            db.commit()
            msgbox.showinfo("Saved", "Data Saved to Database")
        except:
            msgbox.showinfo("Error Occurred!! Please Try Again")

    def new_book_frame(self):
        new_book_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        new_book_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        new_book_title = tk.Label(new_book_frame, text="ADD NEW BOOK", font=("Arial", 25, "bold"), bg=MENU_STRIP)
        new_book_title.pack(fill='x')

        name_label = tk.Label(new_book_frame, text="Name", font=("Arial", 10, "bold"), bg=INDIVIDUAL_FRAME_BG)
        name_label.place(x=300, y=70)
        name_entry = tk.Entry(new_book_frame, font=("Arial", 10, "bold"))
        name_entry.place(x=400, y=70)

        author_name_label = tk.Label(new_book_frame, text="Author Name", font=("Arial", 10, "bold"), bg=INDIVIDUAL_FRAME_BG)
        author_name_label.place(x=300, y=100)
        author_name_entry = tk.Entry(new_book_frame, font=("Arial", 10, "bold"))
        author_name_entry.place(x=400, y=100)

        price_label = tk.Label(new_book_frame, text="Price", font=("Arial", 10, "bold"), bg=INDIVIDUAL_FRAME_BG)
        price_label.place(x=300, y=130)
        price_entry = tk.Entry(new_book_frame, font=("Arial", 10, "bold"))
        price_entry.place(x=400, y=130)

        edition_label = tk.Label(new_book_frame, text="Edition", font=("Arial", 10, "bold"), bg=INDIVIDUAL_FRAME_BG)
        edition_label.place(x=300, y=160)
        edition_entry = tk.Entry(new_book_frame, font=("Edition", 10, "bold"))
        edition_entry.place(x=400, y=160)

        quantity_label = tk.Label(new_book_frame, text="Stock Quantity", font=("Arial", 10, "bold"), bg=INDIVIDUAL_FRAME_BG)
        quantity_label.place(x=300, y=190)
        quantity_entry = tk.Entry(new_book_frame, font=("Stock Quantity", 10, "bold"))
        quantity_entry.place(x=400, y=190)

        submit_button = tk.Button(new_book_frame, text="Submit", font=("Arial", 13, "bold"),
                                  command=lambda: self.save_to_database_book(name_entry.get(), author_name_entry.get(),
                                                                             price_entry.get(), quantity_entry.get(),
                                                                             edition_entry.get()))
        submit_button.place(x=430, y=220)

        return_home = tk.Button(new_book_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return new_book_frame

    # -------------------------------------------------------------------------------
    def search_author_result_format(self, author_name):
        cursor = db.cursor()
        try:
            l1 = []
            cursor.execute("SELECT * FROM books WHERE author_name = %s", (author_name,))
            for x in cursor:
                book_name = x[1]
                book_id = x[0]
                book_details = "Book ID : %s \nBook Name : %s\n" % (book_id, book_name)
                l1.append(book_details)
            return l1
        except:
            return "No Author Found"

    def search_author_result_frame(self, entry):
        result_label = tk.Label(self.search_author_frame(), font=("Helvetica", 15), justify="left", bg=INDIVIDUAL_FRAME_BG,
                                bd=2)
        result_label.place(x=295, y=120)
        result_label["text"] = self.search_author_result_format(entry)

    def search_author_frame(self):
        search_author = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        search_author.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(search_author, text="SEARCH AUTHOR", font=("Helvetica", 25), bg=MENU_STRIP)
        search_title.pack(fill='x')

        search_entry_title = tk.Label(search_author, text="Author Name", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        search_entry_title.place(x=170, y=70)

        search_entry = tk.Entry(search_author, font=("Arial", 15))
        search_entry.place(x=300, y=70)

        search_button = tk.Button(search_author, text="SEARCH", font=("Arial", 12),
                                  command=lambda: self.search_author_result_frame(search_entry.get()))
        search_button.place(x=600, y=67)

        return_home = tk.Button(search_author, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return search_author

    # --------------------------------------------------------------------------------
    def delete_member_from_database(self, member_id):

        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
            question = msgbox.askquestion("Important", "DELETE MEMBER WITH ID %s" % (member_id,), icon="warning")
            if question == "yes":
                db.commit()
        except:
            return msgbox.showerror("Error", "No Record Found")

    def delete_member_frame(self):
        delete_member = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        delete_member.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(delete_member, text="DELETE MEMBER", font=("Helvetica", 25, 'bold'), bg=MENU_STRIP)
        search_title.pack(fill='x')

        delete_title = tk.Label(delete_member, text="Member ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        delete_title.place(x=240, y=70)

        delete_entry = tk.Entry(delete_member, font=("Arial", 15))
        delete_entry.place(x=360, y=70)

        delete_button = tk.Button(delete_member, text="DELETE", font=("Arial", 12),
                                  command=lambda: self.delete_member_from_database(delete_entry.get()))
        delete_button.place(x=400, y=160)

        return_home = tk.Button(delete_member, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return delete_member

    # --------------------------------------------------------------------------------
    def stock_info(self, book_id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
        for x in cursor:
            book_name = x[1]
            total_stock = x[4]
            information = f"Book Name : {book_name} \nAvailable Stock : {total_stock}"
            stock_info = msgbox.showinfo("Stock Info", information)
            return stock_info

    def add_stock(self, book_id, stock):
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE books SET stock = stock + %s WHERE book_id = %s", (stock, book_id,))
            prompt = msgbox.askquestion("Add Stock", f"Add {stock} Books?")
            if prompt == "yes":
                db.commit()

        except:
            return msgbox.showerror("Error", "No Record Found")

    def remove_stock(self, book_id, stock):
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE books SET stock = stock - %s WHERE book_id = %s", (stock, book_id,))
            prompt = msgbox.askquestion("Remove Stock", f"Remove {stock} Books?")
            if prompt == "yes":
                db.commit()

        except:
            return msgbox.showerror("Error", "No Record Found")

    def remove_book_stock(self, book_id):
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
            question = msgbox.askquestion("Delete Book", "DELETE BOOK WITH ID %s" % (book_id,), icon="warning")
            if question == "yes":
                db.commit()
        except:
            return msgbox.showerror("Error", "No Record Found")

    def edit_stock_frame(self):
        edit_stock = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        edit_stock.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(edit_stock, text="EDIT STOCKS", font=("Helvetica", 25, 'bold'), bg=MENU_STRIP)
        search_title.pack(fill='x')

        book_id_title = tk.Label(edit_stock, text="Book ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        book_id_title.place(x=240, y=70)
        id_entry = tk.Entry(edit_stock, font=("Arial", 15))
        id_entry.place(x=400, y=70)

        stock_quantity_label = tk.Label(edit_stock, text="Stock Amount", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        stock_quantity_label.place(x=240, y=115)
        stock_quantity_entry = tk.Entry(edit_stock, font=("Arial", 15))
        stock_quantity_entry.place(x=400, y=115)

        stock_info = tk.Button(edit_stock, text="Get Stock Info", font=("Arial", 12),
                               command=lambda: self.stock_info(id_entry.get()))
        stock_info.place(x=200, y=180)

        add_stock = tk.Button(edit_stock, text="ADD to Stock", font=("Arial", 12),
                              command=lambda: self.add_stock(id_entry.get(), stock_quantity_entry.get()))
        add_stock.place(x=380, y=180)

        remove_stock = tk.Button(edit_stock, text="Remove from Stock", font=("Arial", 12),
                                 command=lambda: self.remove_stock(id_entry.get(), stock_quantity_entry.get()))
        remove_stock.place(x=550, y=180)

        remove_book_stock = tk.Button(edit_stock, text="Delete Book From Database", font=("Arial", 12),
                                      command=lambda: self.remove_book_stock(id_entry.get()))
        remove_book_stock.place(x=320, y=240)

        return_home = tk.Button(edit_stock, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return edit_stock

    # --------------------------------------------------------------------------------
    def display_all_issued_book(self):
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM issues WHERE date_return IS NULL;")
            issue_list = []
            for x in mycursor:
                member_id = x[1]
                book_id = x[2]
                date_issue = x[3]
                result = f"\nMember ID : {member_id} | Book ID : {book_id} | Date Issue : {date_issue}\n"
                issue_list.append(result)
            return issue_list
        except:
            return msgbox.showerror("Error", "Error Occurred! Please Try Again!")


    def view_all_issue(self):
        issue_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        issue_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(issue_frame, text="View All Pending Returns", font=("Helvetica", 25, 'bold'),
                                bg=MENU_STRIP)
        search_title.pack(fill='x')

        result_label = tk.Label(issue_frame, font=("Helvetica", 15), justify="left", bg=INDIVIDUAL_FRAME_BG,
                                bd=2)
        result_label.place(x=200, y=60)
        result_label["text"] = self.display_all_issued_book()

        return_home = tk.Button(issue_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.book_issue_frame()))
        return_home.place(x=50, y=280)
        return issue_frame

    def return_issue_store_db(self, book_id, member_id, date):

        try:
            mycursor = db.cursor()
            mycursor.execute("UPDATE issues SET date_return = %s WHERE book_id = %s and member_id = %s",
                             (date, book_id, member_id))
            mycursor.execute("UPDATE books SET stock = stock + 1 WHERE book_id = %s", (book_id,))
            message = f"Book ID : {book_id}\nMember ID : {member_id}\nReturn Date : {date}"
            prompt = msgbox.askquestion("Save", f"{message}")
            if prompt == "yes":
                db.commit()
        except:
            return msgbox.showerror("Error", "Something Went Wrong")

    def return_book(self):
        issue_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        issue_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(issue_frame, text="Return Issued Book", font=("Helvetica", 25, 'bold'), bg=MENU_STRIP)
        search_title.pack(fill='x')

        book_id_title = tk.Label(issue_frame, text="Book ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        book_id_title.place(x=240, y=70)
        book_id_entry = tk.Entry(issue_frame, font=("Arial", 15))
        book_id_entry.place(x=450, y=70)

        member_id_title = tk.Label(issue_frame, text="Member ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        member_id_title.place(x=240, y=120)
        member_id_entry = tk.Entry(issue_frame, font=("Arial", 15))
        member_id_entry.place(x=450, y=120)

        date_title = tk.Label(issue_frame, text="Date (yyyy:mm:dd)", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        date_title.place(x=240, y=170)
        date_entry = tk.Entry(issue_frame, font=("Arial", 15))
        date_entry.place(x=450, y=170)

        submit_button = tk.Button(issue_frame, text="Submit", font=("Arial", 13, "bold"),
                                  command=lambda: self.return_issue_store_db(book_id_entry.get(), member_id_entry.get(),
                                                                             date_entry.get()))
        submit_button.place(x=450, y=220)

        return_home = tk.Button(issue_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.book_issue_frame()))
        return_home.place(x=50, y=280)

        return issue_frame

    def new_issue_store_db(self, book_id, member_id, date):
        try:
            mycursor = db.cursor()
            mycursor.execute("INSERT INTO issues (book_id, member_id, date_issue) VALUES (%s, %s, %s)",
                             (book_id, member_id, date,))
            mycursor.execute("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))
            message = f"Book ID : {book_id}\nMember ID : {member_id}\nIssue Date : {date}"
            prompt = msgbox.askquestion("Save", f"{message}")
            if prompt == "yes":
                db.commit()
        except:
            return msgbox.showerror("Error", "Something Went Wrong")

    def new_book_issue(self):
        issue_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        issue_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(issue_frame, text="New Book Issue", font=("Helvetica", 25, 'bold'), bg=MENU_STRIP)
        search_title.pack(fill='x')

        book_id_title = tk.Label(issue_frame, text="Book ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        book_id_title.place(x=240, y=70)
        book_id_entry = tk.Entry(issue_frame, font=("Arial", 15))
        book_id_entry.place(x=450, y=70)

        member_id_title = tk.Label(issue_frame, text="Member ID", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        member_id_title.place(x=240, y=120)
        member_id_entry = tk.Entry(issue_frame, font=("Arial", 15))
        member_id_entry.place(x=450, y=120)

        date_title = tk.Label(issue_frame, text="Date (yyyy:mm:dd)", font=("Helvetica", 15), bg=INDIVIDUAL_FRAME_BG)
        date_title.place(x=240, y=170)
        date_entry = tk.Entry(issue_frame, font=("Arial", 15))
        date_entry.place(x=450, y=170)

        submit_button = tk.Button(issue_frame, text="Submit", font=("Arial", 13, "bold"),
                                  command=lambda: self.new_issue_store_db(book_id_entry.get(), member_id_entry.get(),
                                                                          date_entry.get()))
        submit_button.place(x=450, y=220)

        return_home = tk.Button(issue_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.book_issue_frame()))
        return_home.place(x=50, y=280)
        return issue_frame

    def book_issue_frame(self):
        issue_frame = tk.Frame(self.window, bg=INDIVIDUAL_FRAME_BG)
        issue_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        search_title = tk.Label(issue_frame, text="Book Issue", font=("Helvetica", 25, 'bold'), bg=MENU_STRIP)
        search_title.pack(fill='x')

        issue_book_button = tk.Button(issue_frame, text="Issue Book", font=("Arial", 17, "bold"),
                                      command=lambda: self.show_frame(self.new_book_issue()))
        issue_book_button.place(x=350, y=90)

        return_book_button = tk.Button(issue_frame, text="Return Book", font=("Arial", 17, "bold"),
                                       command=lambda: self.show_frame(self.return_book()))
        return_book_button.place(x=340, y=150)

        issued_book_button = tk.Button(issue_frame, text="View All Issued", font=("Arial", 17, "bold"),
                                       command=lambda: self.show_frame(self.view_all_issue()))
        issued_book_button.place(x=324, y=210)

        return_home = tk.Button(issue_frame, text="Back", font=("Arial", 10, "bold"),
                                command=lambda: self.show_frame(self.homepage_frame()))
        return_home.place(x=50, y=280)

        return issue_frame

    # --------------------------------------------------------------------------------
    @staticmethod
    def show_frame(frame):
        return frame.tkraise()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    lib = Library()
    lib.run()
