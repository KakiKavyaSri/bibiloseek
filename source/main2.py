from tkinter import *
from PIL import Image,ImageTk
fonts = ('Times_New_Roman_Greek',15)
book_name_to_enter = 'Wings of Fire'
author_name_to_enter = 'Abdul Kalam'
root = Tk()
root.geometry('750x600+400+100')
root.title("MY LIBRARY")

def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        book_name.destroy()
        # book_name_entry.destroy()
        author_name.destroy()
        author_name_entry.destroy()
        
        
        label2 = Label(root,text = "SECOND PAGE",font = fonts)
        label2.place(x = 0,y = 0)

        bookAvai = Label(root,text = ' BOOK AVAILABLE!!',bg = 'green',fg = 'white',font = fonts,width = 20,height = 3)
        bookAvai.place(x = 250,y = 30)

        bookcontents = Label(root,text = ' BOOK CONTENTS : ',bg = 'grey',font = fonts,width = 16)
        bookcontents.place(x = 75,y = 120)

        booksection = Label(root,text = ' BOOK SECTION : ',bg = 'grey',font = fonts,width = 16)
        booksection.place(x = 75,y = 180)

        noofcopies = Label(root,text = 'NO OF COPIES : ',bg = 'grey',font = fonts,width = 16)
        noofcopies.place(x = 75,y = 240)

        bookreviews = Label(root,text = ' BOOK REVIEWS : ',bg = 'grey',font = fonts,width = 16)
        bookreviews.place(x = 75,y = 290)

        ratings = Label(root,text = ' RATING : ',bg = 'grey',font = fonts,width = 16)
        ratings.place(x = 75,y = 440)

        feedback = Label(root,text = ' FEEDBACK : ',bg = 'grey',font = fonts,width = 16)
        feedback.place(x = 75,y = 500)

        bookcontLabel = Label(root,text = 'It is a great story of Dedication & Achievement',bg = 'white',font = fonts)
        bookcontLabel.place(x = 300,y = 120)

        noofcopLabel = Label(root,text = '23',bg = 'white',font = fonts,width = 15)
        noofcopLabel.place(x = 300,y = 240)

        booksection_label = Label(root,text = ' Autobiographies ',bg = 'white',font = fonts,width = 20)
        booksection_label.place(x = 300,y = 180)

        bookratingsLabel = Label(root,text = 'Great Book ',bg = 'white',font = fonts,width = 20)
        bookratingsLabel.place(x = 300,y = 290)

        bookratingsLabel = Label(root,text = 'One must Read it ',bg = 'white',font = fonts,width = 20)
        bookratingsLabel.place(x = 300,y = 330)

        bookratingsLabel = Label(root,text = 'Excellent Book ',bg = 'white',font = fonts,width = 20)
        bookratingsLabel.place(x = 300,y = 370)

        bookratingsLabel = Label(root,text = ' 4.7 / 5 ',bg = 'white',font = fonts,width = 20)
        bookratingsLabel.place(x = 300,y = 440)

        book_name_entry = Entry(root,width = 30,font = fonts)
        book_name_entry.place(x = 300,y = 500)



        def back():

            label2.destroy()
            button2.destroy()
            tab1()
        button2 = Button(root,text = "BACK",font = fonts,command = back)
        button2.pack(side = BOTTOM)


    
    label1 = Label(root,text = "FIRST PAGE",font = fonts)
    label1.place(x = 0,y = 0)

    image_logo = Image.open('../assets/libblurimage.png')
    image_logo = image_logo.resize((820,820))
    image_logo = ImageTk.PhotoImage(image_logo)
    image_logo_label = Label(root,image = image_logo)
    image_logo_label.place(x = 0,y = 0)

    image_logos = Image.open('../assets/log.png')
    image_logos = image_logos.resize((175,175))
    image_logos = ImageTk.PhotoImage(image_logos)
    image_logos_label = Label(root,image = image_logos)
    image_logos_label.place(x = 300,y = 60)


    book_name = Label(root,text = "BOOK NAME",bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
    book_name.place(x = 100,y = 300)
    book_name_entry = Entry(root,width = 30,font = fonts)
    book_name_entry.place(x = 300,y = 310)
    author_name = Label(root,text = 'AUTHOR NAME',bg = 'green',fg = 'yellow',font = fonts,width = 15,height = 2)
    author_name.place(x = 100,y = 370)
    author_name_entry = Entry(root,width = 30,font = fonts)
    author_name_entry.place(x = 300,y = 380)
    button1 = Button(root,text = "SHOW",font = fonts,width = 9,bg = 'steel blue',command = tab2)
    button1.place(x = 330,y = 470)


def result():
    global book_name_to_enter,author_name_to_enter
    b = book_name_entry.get()
    if b == book_name_to_enter and a == author_name_to_enter:
        pass
    else:
        messagebox.showerror('INVALID','NO RESULT FOUND')

tab1()
root.mainloop()