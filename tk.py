try:
    import scratchattach as s3
    import tkinter as tk
    import ttk
except ImportError:
    import os
    import sys
    os.system("pip install scratchattach")
    os.system("pip install tk")
    os.system("pip install pyttk")
    os.system("pip install requests")
    print("Please restart this project")
    sys.exit()


def cloud_variable():
    ent1_lab.pack()
    ent1.pack()
    ent2_lab.pack()
    ent2.pack()
    ent3_lab.pack()
    ent3.pack()
    b1.pack_forget()
    ent1_but.pack()
    back_but.pack()


def ent1_ok():
    if ent1.get().isnumeric() and ent2.get() and ent3.get().isnumeric():
        proj_sess = sess.connect_cloud(ent1.get())
        proj_sess.set_var(ent2.get(), ent3.get())
        back()


def back():
    ent1.pack_forget()
    back_but.pack_forget()
    ent1_lab.pack_forget()
    ent1_but.pack_forget()
    b1.pack()
    ent2.pack_forget()
    ent3.pack_forget()
    ent3_lab.pack_forget()
    ent2_lab.pack_forget()


app = tk.Tk()
b1 = ttk.Button(app, text="Set cloud variable value", command=cloud_variable)
b1.pack()
app.resizable(False, False)
ent1 = ttk.Entry(app)
ent1_lab = ttk.Label(app, text="Please print the project ID:")
ent2 = ttk.Entry(app)
ent2_lab = ttk.Label(app, text="Please print the variable name:")
ent3 = ttk.Entry()
ent3_lab = ttk.Label(app, text="Please print the new variable value:")
ent1_but = ttk.Button(app, text="Ok", command=ent1_ok)
back_but = ttk.Button(app, text="Back", command=back)
sess = s3.login("AnikeyPS", open("password.txt", "r").read())
app.mainloop()
