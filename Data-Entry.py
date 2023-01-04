from csv import *
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Data Entry")
window.geometry("700x350")
main_lst=[]

def Add():
   lst=[name.get(),age.get(),contact.get(),address.get(),Department.get()]
   main_lst.append(lst)
   messagebox.showinfo("Information","The data has been added successfully")

def Save():
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Age","Contact","Address","Department"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

def Clear():
   name.delete(0,END)
   age.delete(0,END)
   contact.delete(0,END)
   address.delete(0,END)
   Department.delete(0,END)

# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Name: ",padx=39,pady=10,background="Grey",foreground="black")
label2=Label(window,text="Age: ",padx=43.9,pady=10,background="Grey",foreground="black")
label3=Label(window,text="Contact: ",padx=34,pady=10,background="Grey",foreground="black")
label4=Label(window,text="Address: ",padx=34,pady=10,background="Grey",foreground="black")
label5=Label(window,text="Department: ",padx=23.4,pady=10,background="Grey",foreground="black")

name=Entry(window,width=30,borderwidth=3)
age=Entry(window,width=30,borderwidth=3)
contact=Entry(window,width=30,borderwidth=3)
address = Entry(window,width = 30 , borderwidth = 4)
Department = Entry(window,width = 30,borderwidth = 3)

save=Button(window,text="Save",padx=20,pady=10,background="Black",foreground="White",command=Save)
add=Button(window,text="Add",padx=20,pady=10,background="Black",foreground="White",command=Add)
clear=Button(window,text="Clear",padx=18,pady=10,background="Black",foreground="White",command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,background="Black",foreground="White",command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row = 3, column = 0)
label5.grid(row = 4,column = 0)

name.grid(row=0,column=1)
age.grid(row=1,column=1)
contact.grid(row=2,column=1)
address.grid(row=3,column = 1)
Department.grid(row=4,column=1)
save.grid(row=5,column=0,columnspan=2)
add.grid(row=5,column=1,columnspan=2)
clear.grid(row=7,column=0,columnspan=2)
Exit.grid(row=7,column=1,columnspan=2)

window.mainloop()
print(list)
print(main_lst)