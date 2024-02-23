from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk
fonts = ('Times_New_Roman_Greek',15)
# font1 = ('Helvetica',18,'bold')
book_name_to_enter = 'Wings of Fire'
author_name_to_enter = 'Abdul Kalam'
blank_to_enter = 'Good Book'
root = Tk()
class Library:
    def __init__(self,root):
        self.root = root
        self.page = Frame(self.root,width = 1000,height = 1000)
        self.page.place(x = 0, y = 0)


        self.image_logo = Image.open('../assets/libblurimage.png')
        self.image_logo = self.image_logo.resize((820,820))
        self.image_logo = ImageTk.PhotoImage(self.image_logo)
        self.image_logo_label = Label(self.page,image = self.image_logo)
        self.image_logo_label.place(x = 0,y = 0)

        
        self.image_logos = Image.open('../assets/log.png')
        self.image_logos = self.image_logos.resize((175,175))
        self.image_logos = ImageTk.PhotoImage(self.image_logos)
        self.image_logos_label = Label(self.page,image = self.image_logos)
        self.image_logos_label.place(x = 300,y = 60)


        # self.book_name_title = Label(self.page,text = 'BIBILOSEEK',bg = 'gold',font = font1,width = 45,height = 6)
        # self.book_name_title.place(x = 75,y = 5)

        self.book_name = Label(self.page,text = 'BOOK NAME',bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
        self.book_name.place(x = 100,y = 300)
        self.book_name_entry = Entry(self.page,width = 30,font = fonts)
        self.book_name_entry.place(x = 300,y = 310)
        
        self.author_name = Label(self.page,text = 'AUTHOR NAME',bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
        self.author_name.place(x = 100,y = 370)
        self.author_name_entry = Entry(self.page,width = 30,font = fonts)
        self.author_name_entry.place(x = 300,y = 380)
        
        self.button = Button(self.page ,text = 'SHOW',font = fonts,width = 9,bg = 'steel blue',command =self.result)
        self.button.place(x = 330,y = 470)


    def result(self):
        global book_name_to_enter, author_name_to_enter
        self.bname = self.book_name_entry.get()
        self.aname = self.author_name_entry.get()
        if self.bname == book_name_to_enter and  self.aname == author_name_to_enter:
           self.page.destroy()
           login_obj = Login(root)
        else:
            messagebox.showerror('INVALID','NO RESULT FOUND')
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('MY BOOK')
        self.page = Frame(self.root,width = 1000,height = 1000)
        self.page.place(x = 0,y = 0)

        label_text = "Welcome to My Book"
        label = Label(self.page, text=label_text, font=("Arial", 24), bg="lightblue", fg="black")
        label.place(relx=0.5, rely=0.5, anchor="center")





root.geometry('750x600+400+100')
root.title('MY LIB')
library = Library(root)
root.mainloop()





