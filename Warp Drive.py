from tkinter import*
root = Tk()
root.title("UnKit")
root.geometry("400x400")

root.configure(background='gold')
enteryou = Entry(root)
enteryou.place(relx=0.5,rely=0.5,anchor=CENTER)

label = Label(root,text = "Its Hcci value is " , bg = "gold")
label2 = Label(root,text = "Encrypted " , bg = "gold")


def qwerty() : 
    inputWord = enteryou.get()
    for letter in inputWord:
        label["text"]+=str(ord(letter))+" " 
        encrypted = int(ord(letter))-1
        label2["text"]+=str(chr(encrypted))+"" 
        
        
btn = Button(root,text="Click" , command=qwerty,bg = "yellow")

btn.place(relx = 0.5,rely = 0.7,anchor=CENTER)
label.place(relx=0.5,rely=0.8,anchor=CENTER)
label2.place(relx=0.5,rely=0.9,anchor=CENTER)


enteryou.pack()
label.pack()
btn.pack()
label2.pack()

root.mainloop()














