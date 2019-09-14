#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 07, 2019 09:16:45 PM IST  platform: Windows NT

import sys
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

import main_support

#def run_server():


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1000x480+145+103")
        top.title("Mirror Screen")
        top.configure(background="#a7d6d4")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="File")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Settings")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="Change Directory")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="Exit")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Help")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="View Help")
        self.sub_menu12.add_separator(
                background="#d9d9d9")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="About")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.002, relwidth=0.225)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.btn_cloud = tk.Button(self.Frame1)
        self.btn_cloud.place(relx=0.0, rely=0.0, height=60, width=225)
        self.btn_cloud.configure(activebackground="#ececec")
        self.btn_cloud.configure(activeforeground="#000000")
        self.btn_cloud.configure(background="#ffebeb")
        self.btn_cloud.configure(disabledforeground="#a3a3a3")
        self.btn_cloud.configure(foreground="#000000")
        self.btn_cloud.configure(highlightbackground="#d9d9d9")
        self.btn_cloud.configure(highlightcolor="black")
        self.btn_cloud.configure(pady="0")
        self.btn_cloud.configure(text='''Button''')

        self.btn_from_server = tk.Button(self.Frame1)
        self.btn_from_server.place(relx=0.0, rely=0.125, height=60, width=225)
        self.btn_from_server.configure(activebackground="#ececec")
        self.btn_from_server.configure(activeforeground="#000000")
        self.btn_from_server.configure(background="#ffebeb")
        self.btn_from_server.configure(disabledforeground="#a3a3a3")
        self.btn_from_server.configure(foreground="#000000")
        self.btn_from_server.configure(highlightbackground="#d9d9d9")
        self.btn_from_server.configure(highlightcolor="black")
        self.btn_from_server.configure(pady="0")
        self.btn_from_server.configure(text='''Button''')

        self.Btn_camera = tk.Button(self.Frame1)
        self.Btn_camera.place(relx=0.0, rely=0.249, height=60, width=225)
        self.Btn_camera.configure(activebackground="#ececec")
        self.Btn_camera.configure(activeforeground="#000000")
        self.Btn_camera.configure(background="#ffebeb")
        self.Btn_camera.configure(disabledforeground="#a3a3a3")
        self.Btn_camera.configure(foreground="#000000")
        self.Btn_camera.configure(highlightbackground="#d9d9d9")
        self.Btn_camera.configure(highlightcolor="black")
        self.Btn_camera.configure(pady="0")
        self.Btn_camera.configure(text='''Button''')

        self.btn_to_server = tk.Button(self.Frame1)
        self.btn_to_server.place(relx=0.0, rely=0.374, height=60, width=225)
        self.btn_to_server.configure(activebackground="#ececec")
        self.btn_to_server.configure(activeforeground="#000000")
        self.btn_to_server.configure(background="#ffebeb")
        self.btn_to_server.configure(disabledforeground="#a3a3a3")
        self.btn_to_server.configure(foreground="#000000")
        self.btn_to_server.configure(highlightbackground="#d9d9d9")
        self.btn_to_server.configure(highlightcolor="black")
        self.btn_to_server.configure(pady="0")
        self.btn_to_server.configure(text='''Button''')

if __name__ == '__main__':
    vp_start_gui()





