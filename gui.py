from tkinter import *

win= Tk()
win.geometry("600x300")

label= Label(win, text= "Write something !!", font= ('Helvetica', 25))
label.pack(pady=20)

#Create a Text Widget
text= Text(win, height=10)
text.pack()

def delete():
   text.delete("1.0","end")

#Create a Delete Button to remove the Text from the text-widget

b1= Button(win, text= "Delete",command= delete)
b1.pack(pady=10)
win.mainloop()