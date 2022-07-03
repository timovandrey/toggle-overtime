################################################################################
# File:         gui.py
# Author:       Timo Vandrey
# Date:         19.06.2022
# Version:      1
# Description:
# This is the GUI object and representation of the overtime calculator.
################################################################################
# IMPORTS                                                                      #
################################################################################
# Project specific
from cmath import e
from calculator import *
# General
from tkinter import *
from  tkinter import ttk

################################################################################
# OBJECT                                                                       #
################################################################################
class ToGui:
    # GUI ELEMENTS #############################################################
    tkObj : Tk
    frame : Frame
    listView : ttk.Treeview
    calculator : Calculator

    # CTRL FUNCTIONS ###########################################################
    def __init__(self) -> None:
        self.calculator = Calculator()
        self.__initialize()
        self.calculator.update()
        self.__initializeTreeview()
        self.frame.pack()
        return

    def __initialize(self):
        self.tkObj = Tk()
        self.tkObj.title("ToGui")
        self.tkObj.geometry("500x700")
        self.frame = Frame(self.tkObj)
        return

    def __initializeTreeview(self):
        self.listView = ttk.Treeview(self.frame)
        self.listView.pack()
        self.listView["columns"] = ("Date", "Work time", "Supposed work time", "Break time", "dayType")

        self.listView.column("#0", width=0, stretch=NO)
        self.listView.column("Date", anchor=W, stretch=YES)
        self.listView.column("Work time", anchor=W, stretch=YES)
        self.listView.column("Supposed work time", anchor=W, stretch=YES)
        self.listView.column("Break time", anchor=W, stretch=YES)
        self.listView.column("dayType", anchor=W, stretch=YES)

        self.listView.heading("#0", text="", anchor=W)
        self.listView.heading("Date", text="Date", anchor=W)
        self.listView.heading("Work time", text="Work time", anchor=W)
        self.listView.heading("Supposed work time", text="Supposed work time", anchor=W)
        self.listView.heading("Break time", text="Break time", anchor=W)
        self.listView.heading("dayType", text="Day type", anchor=W)

        i : int = 0
        for entry in self.calculator.entries:
            i += 1
            self.listView.insert(   parent='', 
                                    index='end',
                                    iid=i,
                                    text='',
                                    values=(    entry.date.strftime("%Y.%m.%d, %a"),
                                                entry.workTime * SEC_TO_HOURS, 
                                                entry.supposedWorkTime * SEC_TO_HOURS,
                                                entry.breakTime * SEC_TO_HOURS,
                                                entry.dayType
                                            )
                                )

    def run(self):
        self.tkObj.mainloop()

    # ACTION FUNCTIONS #########################################################