#_*_ coding:UTF-8 _*_
import tkinter
from version_dao import Connect as con
from tkinter import StringVar

root = tkinter.Tk();
root.geometry('250x120')

tkinter.Label(root, text = "App Version").pack()

fm1 = tkinter.Frame(root)
v_label = tkinter.Label(fm1, text="version:")
v_label.pack(side=tkinter.LEFT)
app_version = con.getVersion();
versionText = StringVar();
versionText.set(app_version);
tkinter.Label(fm1, textvariable= versionText).pack(side=tkinter.LEFT);
fm1.pack(pady=10)

fm2 = tkinter.Frame(root)


text = tkinter.Entry(fm2, width = 10)
text.pack(side=tkinter.LEFT)


def updatev():
	textValue = text.get();
	con.updateVersion(textValue)
	new_version = con.getVersion();
	versionText.set(new_version)

tkinter.Button(fm2, text="Update", command=updatev).pack(side=tkinter.LEFT,padx=5)
fm2.pack()
root.mainloop();

