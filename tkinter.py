from tkinter import *

window=Tk()
window.geometry("400x555")
window.title("jibi")
window.configure("#fff")
button = Button(window,text="ok",width=30,height=30,color="red")
label= Label(window,text="hello")

button.pack()
label.pack()

window.mainloop()