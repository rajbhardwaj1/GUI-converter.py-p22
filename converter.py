from tkinter import ttk
import tkinter as t
c=t.Tk()
c.geometry('600x450')
c.title('Unit Converter')
c.resizable(0,0) 
c.iconbitmap(r'C:\Users\rajku\OneDrive\Desktop\program_py\Rays\Python\GUI\Calicon.ico')
def choice(*s):
    k=com1.current()
    if k==0:
        com2['values']=('Miter','Km','Mile')
        com3['values']=('Miter','Km','Mile')
    elif k==1:
        com2['values']=('Gram','KG','Pound')
        com3['values']=('Gram','KG','Pound')
    elif k==2:
        com2['values']=('Ml','liter','Gallon')
        com3['values']=('Ml','liter','Gallon')
    elif k==3:
        com2['values']=('INR','USD','EURO')
        com3['values']=('INR','USD','EURO')
def con():
    a=com1.current()
    b=com2.current()
    c=com3.current()
    d=float(val.get())
    if a==0 :
        if b==0 and c==0:
            res.config(text=str(d)+' Miter')
        elif b==0 and c==1:
            res.config(text=str(d*0.001)+' Km')
        elif b==0 and c==2:
            res.config(text=str(d*0.001*0.621)+' Mile')
        elif b==1 and c==0:
            res.config(text=str(d*1000)+' Miter')
        elif b==1 and c==1:
            res.config(text=str(d)+' Km')
        elif b==1 and c==2:
            res.config(text=str(d*0.621)+' Mile')
        elif b==2 and c==0:
            res.config(text=str(d*1000*1.609)+' Miter')
        elif b==2 and c==1:
            res.config(text=str(d*1.609)+' Km')
        elif b==2 and c==2:
            res.config(text=str(d)+' Mile')
    elif a==1 :
        if b==0 and c==0:
            res.config(text=str(d)+' Gram')
        elif b==0 and c==1:
            res.config(text=str(d*0.001)+' Kg')
        elif b==0 and c==2:
            res.config(text=str(d*0.001*2.205)+' Pound')
        elif b==1 and c==0:
            res.config(text=str(d*1000)+' Gram')
        elif b==1 and c==1:
            res.config(text=str(d)+' Kg')
        elif b==1 and c==2:
            res.config(text=str(d*0.454)+' Pound')
        elif b==2 and c==0:
            res.config(text=str(d*1000*0.454)+' Gram')
        elif b==2 and c==1:
            res.config(text=str(d*0.454)+' Kg')
        elif b==2 and c==2:
            res.config(text=str(d)+' Pound')
    elif a==2 :
        if b==0 and c==0:
            res.config(text=str(d)+' Ml')
        elif b==0 and c==1:
            res.config(text=str(d*0.001)+' liter')
        elif b==0 and c==2:
            res.config(text=str(d*0.001*0.264)+' Gallon')
        elif b==1 and c==0:
            res.config(text=str(d*1000)+' Ml')
        elif b==1 and c==1:
            res.config(text=str(d)+' liter')
        elif b==1 and c==2:
            res.config(text=str(d*0.264)+' Gallon')
        elif b==2 and c==0:
            res.config(text=str(d*1000*3.785)+' Ml')
        elif b==2 and c==1:
            res.config(text=str(d*3.785)+' liter')
        elif b==2 and c==2:
            res.config(text=str(d)+' Gallon')
    elif a==3 :
        if b==0 and c==0:
            res.config(text=str(d)+' INR')
        elif b==0 and c==1:
            res.config(text=str(d*0.012)+' USD')
        elif b==0 and c==2:
            res.config(text=str(d*0.011)+' EURO')
        elif b==1 and c==0:
            res.config(text=str(d*82.81)+' INR')
        elif b==1 and c==1:
            res.config(text=str(d)+' USD')
        elif b==1 and c==2:
            res.config(text=str(d*0.91)+' EURO')
        elif b==2 and c==0:
            res.config(text=str(d*90.82)+' INR')
        elif b==2 and c==1:
            res.config(text=str(d*1.10)+' USD')
        elif b==2 and c==2:
            res.config(text=str(d)+' EURO')
        

a=t.StringVar()
t.Label(c,text='UNIT CONVERTER',font=('bold',20)).place(x=180,y=10)
com1=ttk.Combobox(c,width=28,font=('bold',18),textvariable=a)
com1['values']=('Distance','Weight','Volume','Currency')
com1.place(x=110,y=70)
com2=ttk.Combobox(c,width=26,font=('bold',10))
com2.place(x=10,y=200)
com3=ttk.Combobox(c,width=26,font=('bold',10))
com3.place(x=380,y=200)
t.Label(c,text='From',font=('bold',18)).place(x=80,y=150)
t.Label(c,text='To',font=('bold',18)).place(x=470,y=150)
val=t.Entry(c,width=15,font=('bold',18))
val.place(x=12,y=290)
res=t.Label(c,font=('bold',14))
res.place(x=382,y=287)
a.trace('w',choice)
b1=t.Button(c,text='Convert',font=('bold',18),bg='black',fg='dark orange',activebackground='light yellow',command=con)
b1.place(x=246,y=280)
c.mainloop()




