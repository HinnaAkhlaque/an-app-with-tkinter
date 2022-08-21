from tkinter import *
from tkinter.font import *
from tkinter import messagebox
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk

new_win = None
f = None
pop = None

window = Tk()


def popup():
    new_pop = Toplevel(window)
    new_pop.title("Sign up")
    new_pop.geometry("390x510")
    new_pop.config(bg="black")
    new_pop.iconbitmap("images/count_theapplication_themovie_3042.ico")
    username = Label(new_pop, text="Username: ", bg="black", foreground="red", font=fnt_label)
    username.place(x=40, y=50)
    username_entry = Entry(new_pop, width=30, font=fnt_entry)
    username_entry.place(x=40, y=85)
    email = Label(new_pop, text="Email: ", bg="black", foreground="red", font=fnt_label)
    email.place(x=40, y=125)
    email_entry = Entry(new_pop, width=30, font=fnt_entry)
    email_entry.place(x=40, y=160)
    password = Label(new_pop, text="Password: ", bg="black", foreground="red", font=fnt_label)
    password.place(x=40, y=200)
    password_entry = Entry(new_pop, width=30, show="*", font=fnt_entry)
    password_entry.place(x=40, y=240)
    card_num = Label(new_pop, text="Card number: ", bg="black", foreground="red", font=fnt_label)
    card_num.place(x=40, y=280)
    card_entry = Entry(new_pop, width=30, font=fnt_entry)
    card_entry.place(x=40, y=320)
    cvv = Label(new_pop, text="Security code(CVV):", bg="black", foreground="red", font=fnt_label)
    cvv.place(x=40, y=360)
    cvv_entry = Entry(new_pop, width=30, show="*", font=fnt_entry)
    cvv_entry.place(x=40, y=395)
    login = Button(new_pop, text="Log in", bd=5, width=20, bg="#d61313", fg="white", command=button)
    login.place(x=120, y=440)



def buy():
    global new_win
    new_win = Toplevel(f)
    new_win.geometry("500x250")
    new_win.iconbitmap("images/count_theapplication_themovie_3042.ico")
    new_win.title("Congratulations!")
    new_win.config(bg="black")

    msg_display = Label(new_win, text="Subscription bought successfully.\n"
                                      " Now binge watch all your favourite seasons, anytime, anywhere! ", fg="white",
                        bg="black", font=("Times New Roman", 13))
    msg_display.place(x=30, y=50)
    ok_btn = Button(new_win, text="OK", bg="red", fg="white", width=15, command=quit, font=("Arial", 15))
    ok_btn.place(x=150, y=160)


def button():
    global f

    f = Toplevel(window)
    f.geometry("1050x800")
    f.title("subs")
    f.iconbitmap("images/count_theapplication_themovie_3042.ico")
    f.config(bg="black")

    photo1 = Image.open("images/Mapping the Company (1).png")
    photo1 = photo1.resize((1050, 600))
    my_img = ImageTk.PhotoImage(photo1)
    p_label = Label(f, image=my_img, border=0)
    p_label.place(x=0, y=0)

    buy1 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10, font=("Arail", 15))
    buy1.place(x=140, y=600)
    buy2 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10, font=("Arail", 16))
    buy2.place(x=475, y=600)
    buy3 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10, font=("Arail", 16))
    buy3.place(x=800, y=600)
    f.mainloop()


window.title("Cine-flick")
window.geometry("920x700")
window.iconbitmap("images/count_theapplication_themovie_3042.ico")

fnt_label = Font(family="Congenial Black", size=15)
window.config(bg="black")

fnt_entry = Font(family="Calibri", size=15)

for i in range(0, 60):
    window.rowconfigure(i, weight=1)
for i in range(0, 60):
    window.columnconfigure(i, weight=1)

photo = Image.open("images/moodboard.png")
photo = photo.resize((920, 650))
my = ImageTk.PhotoImage(photo)
photo_label = Label(image=my, border=0)
photo_label.place(x=0, y=0)

sign = Button(window, text="Sign up", font=("helvetica", 18), width=16, bg="red", fg="white", command=popup)
sign.place(x=340, y=370)
copy = Label(window, text="All rights reserved, copyrights 2020 by Cine-flicks", font=("Arial Narrow", 12), fg="red",
             bg="black")
copy.place(x=260, y=660)

window.mainloop()

# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# from tkinter.font import *
# from PIL import Image, ImageTk
#
# new_win = None
# f = None
# pop = None
# window = Tk()
#
#
# class Form():
#     def popup(self):
#         global pop
#         self.username_entry = tk.StringVar()
#         self.new_pop = Toplevel(window)
#         self.new_pop.title("Sign up")
#         self.new_pop.geometry("390x510")
#         self.new_pop.config(bg="black")
#         self.username = Label(self.new_pop, text="Username: ", bg="black", foreground="red", font=fnt_label).place(x=40,
#                                                                                                                    y=50)
#         self.username_entry = Entry(self.new_pop, width=30, font=fnt_entry).place(x=40, y=85)
#         self.email = Label(self.new_pop, text="Email: ", bg="black", foreground="red", font=fnt_label).place(x=40,
#                                                                                                              y=125)
#         self.email_entry = Entry(self.new_pop, width=30, font=fnt_entry).place(x=40, y=160)
#         self.password = Label(self.new_pop, text="Password: ", bg="black", foreground="red", font=fnt_label).place(x=40,
#                                                                                                                    y=200)
#         self.password_entry = Entry(self.new_pop, width=30, show="*", font=fnt_entry).place(x=40, y=240)
#         self.card_num = Label(self.new_pop, text="Card number: ", bg="black", foreground="red", font=fnt_label).place(
#             x=40, y=280)
#         self.card_entry = Entry(self.new_pop, width=30, font=fnt_entry).place(x=40, y=320)
#         self.cvv = Label(self.new_pop, text="Security code(CVV):", bg="black", foreground="red", font=fnt_label).place(
#             x=40, y=360)
#         self.cvv_entry = Entry(self.new_pop, width=30, show="*", font=fnt_entry).place(x=40, y=395)
#         self.login = Button(self.new_pop, text="Log in", bd=5, width=20, bg="#d61313", fg="white",
#                             command=self.login_form).place(x=120, y=440)
#         self.new_pop.iconbitmap("images/count_theapplication_themovie_3042.ico")
#
#     def login_form(self):
#         if self.username_entry.get() == "":
#             messagebox.showinfo("Error", "Field Empty!")
#         else:
#             return button()
#
#
# form = Form()
#
#
# def buy():
#     global new_win
#     new_win = Toplevel(f)
#     new_win.geometry("500x250")
#     new_win.iconbitmap("images/count_theapplication_themovie_3042.ico")
#     new_win.title("Congratulations!")
#     new_win.config(bg="black")
#
#     msgdisplay = Label(new_win,
#                        text="Subscription bought successfully.\n Now binge watch all your favourite seasons, anytime, anywhere! ",
#                        fg="white", bg="black", font=("Times New Roman", 15)).place(x=30, y=50)
#     ok_btn = Button(new_win, text="OK", bg="red", fg="white", width=15, command=quit, font=("Arail", 15)).place(x=150,
#                                                                                                                 y=160)
#
#
# def button():
#     global f
#
#     f = Toplevel(window)
#     f.geometry("1050x800")
#     f.title("subs")
#     f.iconbitmap("images/count_theapplication_themovie_3042.ico")
#     f.config(bg="black")
#
#     photo1 = Image.open("images/Mapping the Company (1).png")
#     photo1 = photo1.resize((1050, 600))
#     my_img = ImageTk.PhotoImage(photo1)
#     plabel = Label(f, image=my_img, border=0).place(x=0, y=0)
#
#     buy1 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10,
#                   font=("Arail", 15)).place(x=140, y=600)
#     buy2 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10,
#                   font=("Arail", 16)).place(x=460, y=600)
#     buy3 = Button(f, text="Buy Now!", bd=0, bg="#b8040f", fg="white", command=buy, pady=8, padx=10,
#                   font=("Arail", 16)).place(x=800, y=600)
#     f.mainloop()
#
#
# window.title("Cine-flick")
# window.geometry("920x700")
# window.iconbitmap("images/count_theapplication_themovie_3042.ico")
#
# fnt_label = Font(family="Congenial Black", size=15)
# window.config(bg="black")
#
# fnt_entry = Font(family="Calibri", size=15)
#
# for i in range(0, 60):
#     window.rowconfigure(i, weight=1)
# for i in range(0, 60):
#     window.columnconfigure(i, weight=1)
#
# photo = Image.open("images/moodboard.png")
# photo = photo.resize((920, 650))
# my = ImageTk.PhotoImage(photo)
# photo_label = Label(image=my, border=0).place(x=0, y=0)
#
# sign = Button(window, text="Sign up", font=("helvetica", 18), width=16, bg="red", fg="white", command=form.popup)
# sign.place(x=340, y=370)
# copy = Label(window, text="All rights reserved, copyrights 2020 by Cine-flicks", font=("Arial Narrow", 14), fg="red",
#              bg="black").place(x=260, y=660)
#
# window.mainloop()