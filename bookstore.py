from tkinter import *
import backend

def view_command():
	list.delete(0,END)
	rows = backend.view()
	for r in rows:
		list.insert(END,r)

def search_command():
	list.delete(0,END)
	rows = backend.search(title.get(), author.get(), year.get(), isbn.get())
	for r in rows:
		list.insert(END,r)

def add_command():
	backend.insert(title.get(), author.get(), year.get(), isbn.get())
	view_command()

def get_selected_row(event):
	global selected_row
	try:
		index=list.curselection()[0]
	except:
		return
	selected_row=list.get(index)
	e1.delete(0,END)
	e1.insert(0,selected_row[1])

	e2.delete(0,END)
	e2.insert(0,selected_row[2])

	e3.delete(0,END)
	e3.insert(0,selected_row[3])

	e4.delete(0,END)
	e4.insert(0,selected_row[4])



def delete_command():
	backend.delete(selected_row[0])
	view_command()

def update_command():
	backend.update(selected_row[0], title.get(), author.get(), year.get(), isbn.get())
	view_command()

app=Tk()
app.title("BookStore")
l1 = Label(app, text="Title")
l1.grid(row=0, column=0)

l2 = Label(app, text="Author")
l2.grid(row=0, column=2)

l3 = Label(app, text="Year")
l3.grid(row=1, column=0)

l4 = Label(app, text="ISBN")
l4.grid(row=1, column=2)

title=StringVar()
e1=Entry(app, textvariable=title)
e1.grid(row=0, column=1)

author=StringVar()
e2=Entry(app, textvariable=author)
e2.grid(row=0, column=3)

year=StringVar()
e3=Entry(app, textvariable=year)
e3.grid(row=1, column=1)

isbn=StringVar()
e4=Entry(app, textvariable=isbn)
e4.grid(row=1, column=3)

b1=Button(app, text="View All", width=12, command=view_command)
b1.grid(row=2 , column=3)

b2=Button(app, text="Search Entry", width=12, command=search_command)
b2.grid(row=3 , column=3)

b3=Button(app, text="Add Entry", width=12, command=add_command)
b3.grid(row=4 , column=3)

b4=Button(app, text="Update", width=12, command=update_command)
b4.grid(row=5 , column=3)

b5=Button(app, text="Delete", width=12, command=delete_command)
b5.grid(row=6 , column=3)

b6=Button(app, text="Close", width=12, command=app.destroy)
b6.grid(row=7 , column=3)

list=Listbox(app, height=10, width=35)
list.grid(row=2,column=0, columnspan=2, rowspan=6)

sb = Scrollbar(app)
sb.grid(row=2,column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)







app.mainloop()
