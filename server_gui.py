import tkinter as tk
from tkinter import font

from server import Server


def start():
    server = Server()
    # Create a window
    window = tk.Tk()
    window.title("Connect window")
    window['background'] = '#86daeb'
    window.geometry("600x600")
    # get input from user
    # create a label
    # create a text box
    # create a button

    button = tk.Button(window, text="Start", command=lambda: server.run(), height=7,
                       fg='black',
                       bg='#6faaf8', font=font.Font(size=14, weight='bold', family='courier'))
    # disable the button after click
    # pack the widgets
    button.pack(side=tk.TOP, padx=15, pady=20)
    text_box = tk.Text(window, width=70, height=20, state="disabled")
    text_box.pack(side=tk.LEFT, padx=15, pady=20)
    scrollbar = tk.Scrollbar(window, command=text_box.yview)
    scrollbar.place(x=570, y=70, height=325)
    server.funcs.append(lambda msg: update_chat(text_box, msg))
    # start the main loop
    # create new window and close current one

    window.mainloop()


def update_chat(text_box, msg):
    # update the text box according to received message
    text_box.config(state="normal")
    msg = msg.split("<")
    for m in msg:
        if len(m) > 0:
            if m[-1] == ">":
                text_box.insert(tk.END, m[:-1] + "\n")
            else:
                text_box.insert(tk.END, m + "\n")
    text_box.config(state="disabled")
    text_box.see(tk.END)


def run(server):
    server.run()


start()
