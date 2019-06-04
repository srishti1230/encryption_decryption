
import tkinter as tk
from tkinter import messagebox
top=tk.Tk()
top.title("Encryption_Decryption")
l1=tk.Label(top,text="ENTER THE TEXT")
l1.pack()

e1=tk.Entry(top,bd=5)
e1.pack()
alphabet="abcdefghijklmnopqrstuvwxyz"
key=4
newmsg=" "
e2=tk.Entry(top,bd=5)
e2.pack()
def submit_1():
    messagebox.showinfo('CONFIRMATION',e1.get() +"-Your data")
    global newmsg

    for character in e1.get():
            position=alphabet.find(character)
            newposition=(position+key)%26
            newchar=alphabet[newposition]
            print("encrypted character is :", newchar)
            newmsg+=newchar
    print(newmsg)
    e2.insert(0,newmsg)
def submit_2():
    messagebox.showinfo('CONFIRMATION',e1.get() +"-Your data")
    global newmsg

    for character in e1.get():
            position=alphabet.find(character)
            newposition=(position-key)%26
            newchar=alphabet[newposition]
            print("decrypted character is :", newchar)
            newmsg+=newchar
    print(newmsg)
    e2.insert(0,newmsg)
redbutton_1=tk.Button(top,text="Encrypt_message",fg="red" ,command=lambda:submit_1())
redbutton_1.pack()
redbutton_2=tk.Button(top,text="Decrypt_message",fg="red" ,command=lambda:submit_2())
redbutton_2.pack()

top.mainloop()
