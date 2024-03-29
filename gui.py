#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 14, 2019 10:54:46 PM IST  platform: Windows NT

import sys
import os
import video
import requests

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import gui_support


def returnUploads():
    List = os.listdir(os.getcwd() + "//uploads")
    return List


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    gui_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        self.url = "http://hitenjain88.pythonanywhere.com/uploads"
        self.files = os.listdir()
        self.result = []
        self.final = []
        self.dir_path = os.getcwd() + '\\uploads'
        self.length = 0
        self.path = ''

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("700x400+262+151")
        top.title("Mirror Screen")
        top.configure(borderwidth="10")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#141414")
        top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="File")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Exit",
            command=self.exit)
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="Help")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="View Help")
        self.sub_menu1.add_separator(
            background="#d9d9d9")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="About")
        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Refresh",
            command=self.sync)

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.014, rely=0.025, relheight=0.813, relwidth=0.971)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(borderwidth="5")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Data on Cloud''')
        self.Labelframe1.configure(background="#ffffff")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.829, rely=0.85, height=34, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Play Selected''')
        self.Button1.configure(command=self.play_selected)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.671, rely=0.85, height=34, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Play All''')
        self.Button2.configure(command=self.play_all)

        '''
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.895, height=31, width=444)
        self.Label1.configure(activebackground='#f9f9f9')
        self.Label1.configure(activeforeground='black')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground='#d9d9d9')
        self.Label1.configure(highlightcolor='black')
        self.Label1.configure(text='hello')'''

        self.canvas = tk.Canvas(self.Labelframe1, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self.Labelframe1, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.sync()

    def populate(self):
        self.files = sorted(os.listdir(self.dir_path), key=str.lower)
        self.length = len(max(self.files, key=len))
        self.files = [i.ljust(self.length) for i in self.files]
        self.result = []
        for i in range(len(self.files)):
            self.result.append(tk.IntVar())
            tk.Checkbutton(self.frame, text='', variable=self.result[i], background='#ffffff').grid(row=i, column=0)
            tk.Label(self.frame, text=self.files[i], background='#ffffff').grid(row=i, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def exit(self):
        sys.exit()

    '''def update(self, txt):
        self.Label1.configure(text=txt)'''

    def sync(self):
        r = requests.get(url=self.url)
        json = r.json()
        video = json['video']
        picture = json['picture']

        data = returnUploads()

        for i in video:
            if i not in data:
                re = requests.get(self.url + "/" + i, allow_redirects=True)
                with open(os.getcwd() + "//uploads//" + i, 'wb') as f:
                    f.write(re.content)
                    print(i)
        self.populate()

    def play_selected(self):
        self.final = []
        for i in range(len(self.files)):
            if self.result[i].get() == 1:
                self.final.append(self.files[i])
        self.play(self.final)

    def play_all(self):
        self.final = self.files
        self.play(self.final)

    def play(self, names):
        for item in names:
            self.path = self.dir_path + '\\' + item
            self.vid = video.Video(item, self.path)
            self.vid.run()


if __name__ == '__main__':
    vp_start_gui()
