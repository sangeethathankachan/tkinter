from tkinter import *
root=Tk(className="Wine_Quality_Prediction")
def action():
	print("hello")
root.geometry("900x600")
label=Label(root,text="hiiiii")
label.pack()
entry=Entry(root)
entry.pack()
button=Button(root,text="click",command=action)
button.pack()
root.mainloop()
