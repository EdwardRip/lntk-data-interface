#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Sep 26, 2018 01:26:18 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import lantekinfov2_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    lantekinfov2_support.set_Tk_var()
    top = Lantek_Data_Display (root)
    lantekinfov2_support.init(root, top)
    root.mainloop()

w = None
def create_Lantek_Data_Display(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    lantekinfov2_support.set_Tk_var()
    top = Lantek_Data_Display (w)
    lantekinfov2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Lantek_Data_Display():
    global w
    w.destroy()
    w = None


class Lantek_Data_Display:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("900x600+597+93")
        top.title("Lantek Data Display")
        top.configure(background="#d9d9d9")



        self.WO_Label = Label(top)
        self.WO_Label.place(relx=0.01, rely=0.02, height=21, width=70)
        self.WO_Label.configure(anchor=W)
        self.WO_Label.configure(background="#d9d9d9")
        self.WO_Label.configure(disabledforeground="#a3a3a3")
        self.WO_Label.configure(foreground="#000000")
        self.WO_Label.configure(justify=LEFT)
        self.WO_Label.configure(text='''Work Order:''')

        self.WO_Info = Label(top)
        self.WO_Info.place(relx=0.09, rely=0.02, height=21, width=140)
        self.WO_Info.configure(activebackground="#f9f9f9")
        self.WO_Info.configure(activeforeground="black")
        self.WO_Info.configure(anchor=W)
        self.WO_Info.configure(background="#ffffff")
        self.WO_Info.configure(disabledforeground="#a3a3a3")
        self.WO_Info.configure(foreground="#000000")
        self.WO_Info.configure(highlightbackground="#d9d9d9")
        self.WO_Info.configure(highlightcolor="black")
        self.WO_Info.configure(justify=LEFT)
        self.WO_Info.configure(textvariable=lantekinfov2_support.work_order)
        self.WO_Info.configure(width=140)

        self.Job_Date_Label = Label(top)
        self.Job_Date_Label.place(relx=0.76, rely=0.48, height=21, width=60)
        self.Job_Date_Label.configure(activebackground="#f9f9f9")
        self.Job_Date_Label.configure(activeforeground="black")
        self.Job_Date_Label.configure(anchor=W)
        self.Job_Date_Label.configure(background="#d9d9d9")
        self.Job_Date_Label.configure(disabledforeground="#a3a3a3")
        self.Job_Date_Label.configure(foreground="#000000")
        self.Job_Date_Label.configure(highlightbackground="#d9d9d9")
        self.Job_Date_Label.configure(highlightcolor="black")
        self.Job_Date_Label.configure(justify=LEFT)
        self.Job_Date_Label.configure(text='''Job Date:''')
        self.Job_Date_Label.configure(width=60)

        self.PO_Info = Label(top)
        self.PO_Info.place(relx=0.34, rely=0.02, height=21, width=140)
        self.PO_Info.configure(activebackground="#f9f9f9")
        self.PO_Info.configure(activeforeground="black")
        self.PO_Info.configure(anchor=W)
        self.PO_Info.configure(background="#ffffff")
        self.PO_Info.configure(disabledforeground="#a3a3a3")
        self.PO_Info.configure(foreground="#000000")
        self.PO_Info.configure(highlightbackground="#d9d9d9")
        self.PO_Info.configure(highlightcolor="black")
        self.PO_Info.configure(justify=LEFT)
        self.PO_Info.configure(textvariable=lantekinfov2_support.purchase_order)
        self.PO_Info.configure(width=140)

        self.Required_Date_Info = Label(top)
        self.Required_Date_Info.place(relx=0.59, rely=0.02, height=21, width=140)

        self.Required_Date_Info.configure(activebackground="#f9f9f9")
        self.Required_Date_Info.configure(activeforeground="black")
        self.Required_Date_Info.configure(anchor=W)
        self.Required_Date_Info.configure(background="#ffffff")
        self.Required_Date_Info.configure(disabledforeground="#a3a3a3")
        self.Required_Date_Info.configure(foreground="#000000")
        self.Required_Date_Info.configure(highlightbackground="#d9d9d9")
        self.Required_Date_Info.configure(highlightcolor="black")
        self.Required_Date_Info.configure(justify=LEFT)
        self.Required_Date_Info.configure(textvariable=lantekinfov2_support.required_date)
        self.Required_Date_Info.configure(width=140)

        self.Purchase_Order_Info = Label(top)
        self.Purchase_Order_Info.place(relx=0.24, rely=0.02, height=21, width=90)

        self.Purchase_Order_Info.configure(activebackground="#f9f9f9")
        self.Purchase_Order_Info.configure(activeforeground="black")
        self.Purchase_Order_Info.configure(anchor=W)
        self.Purchase_Order_Info.configure(background="#d9d9d9")
        self.Purchase_Order_Info.configure(disabledforeground="#a3a3a3")
        self.Purchase_Order_Info.configure(foreground="#000000")
        self.Purchase_Order_Info.configure(highlightbackground="#d9d9d9")
        self.Purchase_Order_Info.configure(highlightcolor="black")
        self.Purchase_Order_Info.configure(justify=LEFT)
        self.Purchase_Order_Info.configure(text='''Purchase Order:''')
        self.Purchase_Order_Info.configure(width=90)

        self.Lantek_Date_Info = Label(top)
        self.Lantek_Date_Info.place(relx=0.82, rely=0.48, height=21, width=144)
        self.Lantek_Date_Info.configure(activebackground="#f9f9f9")
        self.Lantek_Date_Info.configure(activeforeground="black")
        self.Lantek_Date_Info.configure(anchor=W)
        self.Lantek_Date_Info.configure(background="#ffffff")
        self.Lantek_Date_Info.configure(disabledforeground="#a3a3a3")
        self.Lantek_Date_Info.configure(foreground="#000000")
        self.Lantek_Date_Info.configure(highlightbackground="#d9d9d9")
        self.Lantek_Date_Info.configure(highlightcolor="black")
        self.Lantek_Date_Info.configure(justify=LEFT)
        self.Lantek_Date_Info.configure(textvariable=lantekinfov2_support.lantek_date)
        self.Lantek_Date_Info.configure(width=144)

        self.Required_Date_Label = Label(top)
        self.Required_Date_Label.place(relx=0.5, rely=0.02, height=21, width=84)
        self.Required_Date_Label.configure(activebackground="#f9f9f9")
        self.Required_Date_Label.configure(activeforeground="black")
        self.Required_Date_Label.configure(anchor=W)
        self.Required_Date_Label.configure(background="#d9d9d9")
        self.Required_Date_Label.configure(disabledforeground="#a3a3a3")
        self.Required_Date_Label.configure(foreground="#000000")
        self.Required_Date_Label.configure(highlightbackground="#d9d9d9")
        self.Required_Date_Label.configure(highlightcolor="black")
        self.Required_Date_Label.configure(justify=LEFT)
        self.Required_Date_Label.configure(text='''Required Date:''')
        self.Required_Date_Label.configure(width=90)

        self.Customer_Label = Label(top)
        self.Customer_Label.place(relx=0.01, rely=0.07, height=21, width=70)
        self.Customer_Label.configure(activebackground="#f9f9f9")
        self.Customer_Label.configure(activeforeground="black")
        self.Customer_Label.configure(anchor=W)
        self.Customer_Label.configure(background="#d9d9d9")
        self.Customer_Label.configure(disabledforeground="#a3a3a3")
        self.Customer_Label.configure(foreground="#000000")
        self.Customer_Label.configure(highlightbackground="#d9d9d9")
        self.Customer_Label.configure(highlightcolor="black")
        self.Customer_Label.configure(justify=LEFT)
        self.Customer_Label.configure(text='''Customer:''')

        self.Customer_Info = Label(top)
        self.Customer_Info.place(relx=0.09, rely=0.07, height=21, width=804)
        self.Customer_Info.configure(anchor=W)
        self.Customer_Info.configure(background="#ffffff")
        self.Customer_Info.configure(disabledforeground="#a3a3a3")
        self.Customer_Info.configure(foreground="#000000")
        self.Customer_Info.configure(justify=LEFT)
        self.Customer_Info.configure(text='''Label''')
        self.Customer_Info.configure(textvariable=lantekinfov2_support.customer)
        self.Customer_Info.configure(width=804)

        self.Tag_Label = Label(top)
        self.Tag_Label.place(relx=0.01, rely=0.12, height=21, width=70)
        self.Tag_Label.configure(activebackground="#f9f9f9")
        self.Tag_Label.configure(activeforeground="black")
        self.Tag_Label.configure(anchor=W)
        self.Tag_Label.configure(background="#d9d9d9")
        self.Tag_Label.configure(disabledforeground="#a3a3a3")
        self.Tag_Label.configure(foreground="#000000")
        self.Tag_Label.configure(highlightbackground="#d9d9d9")
        self.Tag_Label.configure(highlightcolor="black")
        self.Tag_Label.configure(justify=LEFT)
        self.Tag_Label.configure(text='''Tag:''')

        self.Tag_Info = Label(top)
        self.Tag_Info.place(relx=0.09, rely=0.12, height=21, width=804)
        self.Tag_Info.configure(activebackground="#f9f9f9")
        self.Tag_Info.configure(activeforeground="black")
        self.Tag_Info.configure(anchor=W)
        self.Tag_Info.configure(background="#ffffff")
        self.Tag_Info.configure(disabledforeground="#a3a3a3")
        self.Tag_Info.configure(foreground="#000000")
        self.Tag_Info.configure(highlightbackground="#d9d9d9")
        self.Tag_Info.configure(highlightcolor="black")
        self.Tag_Info.configure(justify=LEFT)
        self.Tag_Info.configure(text='''Label''')
        self.Tag_Info.configure(textvariable=lantekinfov2_support.cust_tag)
        self.Tag_Info.configure(width=804)

        self.Job_Name_Label = Label(top)
        self.Job_Name_Label.place(relx=0.01, rely=0.17, height=21, width=70)
        self.Job_Name_Label.configure(activebackground="#f9f9f9")
        self.Job_Name_Label.configure(activeforeground="black")
        self.Job_Name_Label.configure(anchor=W)
        self.Job_Name_Label.configure(background="#d9d9d9")
        self.Job_Name_Label.configure(disabledforeground="#a3a3a3")
        self.Job_Name_Label.configure(foreground="#000000")
        self.Job_Name_Label.configure(highlightbackground="#d9d9d9")
        self.Job_Name_Label.configure(highlightcolor="black")
        self.Job_Name_Label.configure(justify=LEFT)
        self.Job_Name_Label.configure(text='''Job Name:''')
        self.Job_Name_Label.configure(width=70)

        self.Job_Name_Info = Label(top)
        self.Job_Name_Info.place(relx=0.09, rely=0.17, height=21, width=804)
        self.Job_Name_Info.configure(activebackground="#f9f9f9")
        self.Job_Name_Info.configure(activeforeground="black")
        self.Job_Name_Info.configure(anchor=W)
        self.Job_Name_Info.configure(background="#ffffff")
        self.Job_Name_Info.configure(disabledforeground="#a3a3a3")
        self.Job_Name_Info.configure(foreground="#000000")
        self.Job_Name_Info.configure(highlightbackground="#d9d9d9")
        self.Job_Name_Info.configure(highlightcolor="black")
        self.Job_Name_Info.configure(justify=LEFT)
        self.Job_Name_Info.configure(text='''Label''')
        self.Job_Name_Info.configure(textvariable=lantekinfov2_support.job_name)

        self.Lantek_Description_STxt = ScrolledText(top)
        self.Lantek_Description_STxt.place(relx=0.01, rely=0.22, relheight=0.19
                , relwidth=0.97)
        self.Lantek_Description_STxt.configure(background="white")
        self.Lantek_Description_STxt.configure(font="TkTextFont")
        self.Lantek_Description_STxt.configure(foreground="black")
        self.Lantek_Description_STxt.configure(highlightbackground="#d9d9d9")
        self.Lantek_Description_STxt.configure(highlightcolor="black")
        self.Lantek_Description_STxt.configure(insertbackground="black")
        self.Lantek_Description_STxt.configure(insertborderwidth="3")
        self.Lantek_Description_STxt.configure(selectbackground="#c4c4c4")
        self.Lantek_Description_STxt.configure(selectforeground="black")
        self.Lantek_Description_STxt.configure(width=10)
        self.Lantek_Description_STxt.configure(wrap=WORD)
        self.Lantek_Description_STxt.insert('1.0',lantekinfov2_support.job_desc.get())

        self.File_ListBox = ScrolledListBox(top)
        self.File_ListBox.place(relx=0.01, rely=0.6, relheight=0.23
                , relwidth=0.45)
        self.File_ListBox.configure(background="white")
        self.File_ListBox.configure(disabledforeground="#a3a3a3")
        self.File_ListBox.configure(font="TkFixedFont")
        self.File_ListBox.configure(foreground="black")
        self.File_ListBox.configure(highlightbackground="#d9d9d9")
        self.File_ListBox.configure(highlightcolor="#d9d9d9")
        self.File_ListBox.configure(selectbackground="#c4c4c4")
        self.File_ListBox.configure(selectforeground="black")
        self.File_ListBox.configure(listvariable=lantekinfov2_support.curr_file_list.get())
        self.File_ListBox.configure(width=10)

        self.Designer_Label = Label(top)
        self.Designer_Label.place(relx=0.76, rely=0.42, height=21, width=60)
        self.Designer_Label.configure(activebackground="#f9f9f9")
        self.Designer_Label.configure(activeforeground="black")
        self.Designer_Label.configure(anchor=W)
        self.Designer_Label.configure(background="#d9d9d9")
        self.Designer_Label.configure(disabledforeground="#a3a3a3")
        self.Designer_Label.configure(foreground="#000000")
        self.Designer_Label.configure(highlightbackground="#d9d9d9")
        self.Designer_Label.configure(highlightcolor="black")
        self.Designer_Label.configure(justify=LEFT)
        self.Designer_Label.configure(text='''Designer:''')
        self.Designer_Label.configure(width=60)

        self.Designer_Info = Label(top)
        self.Designer_Info.place(relx=0.82, rely=0.42, height=21
                , width=144)
        self.Designer_Info.configure(activebackground="#f9f9f9")
        self.Designer_Info.configure(activeforeground="black")
        self.Designer_Info.configure(anchor=W)
        self.Designer_Info.configure(background="#ffffff")
        self.Designer_Info.configure(disabledforeground="#a3a3a3")
        self.Designer_Info.configure(foreground="#000000")
        self.Designer_Info.configure(highlightbackground="#d9d9d9")
        self.Designer_Info.configure(highlightcolor="black")
        self.Designer_Info.configure(justify=LEFT)
        self.Designer_Info.configure(textvariable=lantekinfov2_support.designer.get())
        self.Designer_Info.configure(width=144)

        self.Open_File_Btn = Button(top)
        self.Open_File_Btn.place(relx=0.01, rely=0.85, height=24, width=107)
        self.Open_File_Btn.configure(activebackground="#d9d9d9")
        self.Open_File_Btn.configure(activeforeground="#000000")
        self.Open_File_Btn.configure(background="#d9d9d9")
        self.Open_File_Btn.configure(command=lantekinfov2_support.open_file)
        self.Open_File_Btn.configure(disabledforeground="#a3a3a3")
        self.Open_File_Btn.configure(foreground="#000000")
        self.Open_File_Btn.configure(highlightbackground="#d9d9d9")
        self.Open_File_Btn.configure(highlightcolor="black")
        self.Open_File_Btn.configure(pady="0")
        self.Open_File_Btn.configure(text='''Open Selected File''')
        self.Open_File_Btn.configure(width=107)

        self.Directory_Label = Label(top)
        self.Directory_Label.place(relx=0.01, rely=0.42, height=21, width=130)
        self.Directory_Label.configure(activebackground="#f9f9f9")
        self.Directory_Label.configure(activeforeground="black")
        self.Directory_Label.configure(anchor=W)
        self.Directory_Label.configure(background="#d9d9d9")
        self.Directory_Label.configure(disabledforeground="#a3a3a3")
        self.Directory_Label.configure(foreground="#000000")
        self.Directory_Label.configure(highlightbackground="#d9d9d9")
        self.Directory_Label.configure(highlightcolor="black")
        self.Directory_Label.configure(justify=LEFT)
        self.Directory_Label.configure(text='''Job Program Folder:''')
        self.Directory_Label.configure(width=130)

        self.program_dir = Text(top)
        self.program_dir.place(relx=0.01, rely=0.47, relheight=0.09, relwidth=0.74)
        self.program_dir.configure(background="white")
        self.program_dir.configure(font="TkTextFont")
        self.program_dir.configure(foreground="black")
        self.program_dir.configure(highlightbackground="#d9d9d9")
        self.program_dir.configure(highlightcolor="black")
        self.program_dir.configure(insertbackground="black")
        self.program_dir.configure(selectbackground="#c4c4c4")
        self.program_dir.configure(selectforeground="black")
        self.program_dir.configure(width=664)
        self.program_dir.configure(wrap=WORD)



        self.Open_Folder_Btn = Button(top)
        self.Open_Folder_Btn.place(relx=0.61, rely=0.42, height=24, width=117)
        self.Open_Folder_Btn.configure(activebackground="#d9d9d9")
        self.Open_Folder_Btn.configure(activeforeground="#000000")
        self.Open_Folder_Btn.configure(background="#d9d9d9")
        self.Open_Folder_Btn.configure(command=lantekinfov2_support.open_dir)
        self.Open_Folder_Btn.configure(disabledforeground="#a3a3a3")
        self.Open_Folder_Btn.configure(foreground="#000000")
        self.Open_Folder_Btn.configure(highlightbackground="#d9d9d9")
        self.Open_Folder_Btn.configure(highlightcolor="black")
        self.Open_Folder_Btn.configure(pady="0")
        self.Open_Folder_Btn.configure(text='''Open Folder''')
        self.Open_Folder_Btn.configure(width=117)

        self.Scrolledtext2 = ScrolledText(top)
        self.Scrolledtext2.place(relx=0.47, rely=0.6, relheight=0.22
                , relwidth=0.51)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(font="TkTextFont")
        self.Scrolledtext2.configure(foreground="black")
        self.Scrolledtext2.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext2.configure(highlightcolor="black")
        self.Scrolledtext2.configure(insertbackground="black")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="#c4c4c4")
        self.Scrolledtext2.configure(selectforeground="black")
        self.Scrolledtext2.configure(width=10)
        self.Scrolledtext2.configure(wrap=NONE)

        self.Add_Job_Notes_Label = Label(top)
        self.Add_Job_Notes_Label.place(relx=0.47, rely=0.57, height=21
                , width=460)
        self.Add_Job_Notes_Label.configure(activebackground="#f9f9f9")
        self.Add_Job_Notes_Label.configure(activeforeground="black")
        self.Add_Job_Notes_Label.configure(background="#d9d9d9")
        self.Add_Job_Notes_Label.configure(disabledforeground="#a3a3a3")
        self.Add_Job_Notes_Label.configure(foreground="#000000")
        self.Add_Job_Notes_Label.configure(highlightbackground="#d9d9d9")
        self.Add_Job_Notes_Label.configure(highlightcolor="black")
        self.Add_Job_Notes_Label.configure(text='''Additional Job Notes''')
        self.Add_Job_Notes_Label.configure(width=460)

        self.DWG_Label = Label(top)
        self.DWG_Label.place(relx=0.01, rely=0.57, height=21, width=390)
        self.DWG_Label.configure(activebackground="#f9f9f9")
        self.DWG_Label.configure(activeforeground="black")
        self.DWG_Label.configure(background="#d9d9d9")
        self.DWG_Label.configure(disabledforeground="#a3a3a3")
        self.DWG_Label.configure(foreground="#000000")
        self.DWG_Label.configure(highlightbackground="#d9d9d9")
        self.DWG_Label.configure(highlightcolor="black")
        self.DWG_Label.configure(text='''Files / Drawings / PDFs''')
        self.DWG_Label.configure(width=390)

        self.Open_File_Btn_21 = Button(top)
        self.Open_File_Btn_21.place(relx=0.47, rely=0.85, height=24, width=157)
        self.Open_File_Btn_21.configure(activebackground="#d9d9d9")
        self.Open_File_Btn_21.configure(activeforeground="#000000")
        self.Open_File_Btn_21.configure(background="#d9d9d9")
        self.Open_File_Btn_21.configure(command=lantekinfov2_support.open_file)
        self.Open_File_Btn_21.configure(disabledforeground="#a3a3a3")
        self.Open_File_Btn_21.configure(foreground="#000000")
        self.Open_File_Btn_21.configure(highlightbackground="#d9d9d9")
        self.Open_File_Btn_21.configure(highlightcolor="black")
        self.Open_File_Btn_21.configure(pady="0")
        self.Open_File_Btn_21.configure(text='''Edit Additional Job Notes''')
        self.Open_File_Btn_21.configure(width=157)

        self.Find_WO_Btn = Button(top)
        self.Find_WO_Btn.place(relx=0.01, rely=0.93, height=24, width=107)
        self.Find_WO_Btn.configure(activebackground="#d9d9d9")
        self.Find_WO_Btn.configure(activeforeground="#000000")
        self.Find_WO_Btn.configure(background="#d9d9d9")
        self.Find_WO_Btn.configure(command=lantekinfov2_support.find_work_order)
        self.Find_WO_Btn.configure(disabledforeground="#a3a3a3")
        self.Find_WO_Btn.configure(foreground="#000000")
        self.Find_WO_Btn.configure(highlightbackground="#d9d9d9")
        self.Find_WO_Btn.configure(highlightcolor="black")
        self.Find_WO_Btn.configure(pady="0")
        self.Find_WO_Btn.configure(text='''Find Work Order''')
        self.Find_WO_Btn.configure(width=107)

        self.Find_PO_Btn = Button(top)
        self.Find_PO_Btn.place(relx=0.14, rely=0.93, height=24, width=127)
        self.Find_PO_Btn.configure(activebackground="#d9d9d9")
        self.Find_PO_Btn.configure(activeforeground="#000000")
        self.Find_PO_Btn.configure(background="#d9d9d9")
        self.Find_PO_Btn.configure(command=lantekinfov2_support.find_purchase_order)
        self.Find_PO_Btn.configure(disabledforeground="#a3a3a3")
        self.Find_PO_Btn.configure(foreground="#000000")
        self.Find_PO_Btn.configure(highlightbackground="#d9d9d9")
        self.Find_PO_Btn.configure(highlightcolor="black")
        self.Find_PO_Btn.configure(pady="0")
        self.Find_PO_Btn.configure(text='''Find Purchase Order''')
        self.Find_PO_Btn.configure(width=127)

        self.Close_Btn = Button(top)
        self.Close_Btn.place(relx=0.92, rely=0.93, height=24, width=40)
        self.Close_Btn.configure(activebackground="#d9d9d9")
        self.Close_Btn.configure(activeforeground="#000000")
        self.Close_Btn.configure(background="#d9d9d9")
        self.Close_Btn.configure(command=top.quit)
        self.Close_Btn.configure(disabledforeground="#a3a3a3")
        self.Close_Btn.configure(foreground="#000000")
        self.Close_Btn.configure(highlightbackground="#d9d9d9")
        self.Close_Btn.configure(highlightcolor="black")
        self.Close_Btn.configure(pady="0")
        self.Close_Btn.configure(text='''Close''')





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()


