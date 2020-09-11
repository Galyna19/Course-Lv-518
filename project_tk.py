from tkinter import*
from tkinter.filedialog import asksaveasfile

root=Tk()

def check():
    a = r(f'Name:{name1.get()} /n Surname:{name2.get()} Question:{name3.get()} Answer:{name4.get()}')
    file = asksaveasfile(defaultextension=".txt")
    file.write(a)

root.title('Welcome to Chat')
root.geometry('500x700')

label_name=Label(root, text='Name:', font=('Comic Sans', 14, 'bold italic'))
label_name.grid(row=0,column=0)
name1=Entry(width=50)
name1.grid(row=0,column=1,sticky=W)

label_surname=Label(root, text='Surname:', font=('Comic Sans', 14, 'bold italic'))
label_surname.grid(row=1,column=0)
name2=Entry(width=50)
name2.grid(row=1,column=1,sticky=W)

label_question=Label(root, text='Question:', font=('Comic Sans', 14, 'bold italic'))
label_question.grid(row=2,column=0)
name3=Entry(width=50)
name3.grid(row=2,column=1,sticky=W)

label_answer=Label(root, text='Answer:', font=('Comic Sans', 14, 'bold italic'))
label_answer.grid(row=3,column=0)
name4=Entry(width=50)
name4.grid(row=3,column=1,sticky=W)

knopka_savepool=Button(root, text='SAVE pool', bg="yellow", command=check)
knopka_savepool.grid(row=5,column=1)

root.mainloop()