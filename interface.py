from tkinter import *
app=Tk()
app.title("LEARN")
app.geometry("400x500")

b1=Button(app, text="load training data", width=10)
b1.pack()

b2=Button(app, text="load labels",width=10)
b2.pack()

b3=Button(app, text="training", width=10)
b3.pack()

Label(app, text="input your data:").pack()
input_data=Entry(app)
input_data.pack()
Label(app, text="outcome is:").pack()

app.mainloop()