'''
The code to help you cheat in calculus
A.K.A. The Calc Calculator
By Tyson Shannon

pip install:
sympy
'''
import tkinter as tk
import calculations

#get question
def enter():
    #get value from entry
    question = mathInput.get()
    #clear entry form
    mathInput.delete(0, tk.END)
    #add question to history
    historyBox.insert(tk.END, "Q: "+question+"\n")
    #get the answer
    getAnswer(question)

#process question
def getAnswer(question):
    #replaces math calls with valid python values
    question = question.replace("inf", "float('inf')")
    #splices in extra info for function to run
    question = "calculations."+question[0:-1]+", historyBox, tk"+question[-1:]
    #run input string as code and call function
    try:
        exec(question)
    except:
        historyBox.insert(tk.END, "Command error, check help for assistance.\n")

#GUI and algorithm for how to get a C
def cPLZ():
    #algorithm
    def gradeAlg():
        #current grade
        c = float(currentEnt.get())/100
        #% of course left
        w = float(weightEnt.get())/100
        #desired grade of C or 70%
        d = 70/100
        #to avoid divide by 0 error
        if w == 0:
            w = 0.000000000000000001
        #claculation for how to get 70% given current grade and course completion
        answer.configure(text="Minimum grade on rest of course to get a C: "+str(round(((d-(1-w)*c)/w)*100))+"%")

    #GUI
    cWindow = tk.Tk()
    cWindow.title("C's Get Degrees")
    cWindow["bg"] = "goldenrod"
    cWindow.geometry("500x500")
    
    cLabel1 = tk.Label(cWindow, text="What do you need to get a C?", fg="purple1", bg="goldenrod", font=("Times", "24", "bold italic"))
    cLabel1.pack()

    frame3 = tk.Frame(cWindow, bg="goldenrod")
    frame3.pack()

    cLabel2 = tk.Label(frame3, text="What is you current grade:", bg="goldenrod")
    currentEnt = tk.Entry(frame3)
    cLabel3 = tk.Label(frame3, text="What % of the course remains:", bg="goldenrod")
    weightEnt = tk.Entry(frame3)
    
    cLabel2.grid(column=0, row=0)
    currentEnt.grid(column=1, row=0)
    cLabel3.grid(column=0, row=1)
    weightEnt.grid(column=1, row=1)

    cEntBut = tk.Button(cWindow, text="Enter", command=lambda:gradeAlg())
    cEntBut.pack()

    answer = tk.Label(cWindow, bg="goldenrod")
    answer.pack()

    cWindow.mainloop()

#GUI for help screen
def help():
    helpWindow = tk.Tk()
    helpWindow.title("Help")
    helpWindow["bg"] = "goldenrod"
    helpWindow.geometry("500x500")
    frame2 = tk.Frame(helpWindow, bg="goldenrod")
    frame2.pack()
    limitL = tk.Label(frame2, text="Limit:\nlimit('y', 'x', v)\ny= function\nx= symbol being limitted\nv= value symbol is going towards (inf for infinity)", bg="goldenrod", justify=tk.LEFT)
    limitL.grid(column=0, row=0)
    derL = tk.Label(frame2, text="Derivative:\nder('y', 'x')\ny= function\nx= symbol being derived", bg="goldenrod", justify=tk.LEFT)
    derL.grid(column=1, row=0)
    difL = tk.Label(frame2, text="Differential:\ndif('y', 'x')\ny= function\nx= symbol being differentiated", bg="goldenrod", justify=tk.LEFT)
    difL.grid(column=0, row=1)
    helpWindow.mainloop()

#GUI for calculator
window = tk.Tk()
window.title("Calc Calculator")
window["bg"] = "goldenrod"
window.geometry("500x500")


title = tk.Label(window, text="Code to Help You Cheat in Calculus", fg="purple1", bg="goldenrod", font=("Times", "24", "bold italic"))
title.pack()
subtitle = tk.Label(window, text="A.K.A The Calc Calculator", fg="purple4", bg="goldenrod", font=("Helvetica", "16", "bold"))
subtitle.pack()
historyBox = tk.Text(window, height=20, width=50)
historyBox.pack()
space1 = tk.Label(bg="goldenrod")
space1.pack()

frame1 = tk.Frame(window, bg="goldenrod")
frame1.pack()

mathInput = tk.Entry(frame1)
mathInput.grid(column=0, row=0)
enterBut = tk.Button(frame1, text="Enter", command=lambda:enter())
enterBut.grid(column=1, row=0)

cBut = tk.Button(frame1, text="Minimum Grade to Get a C", command=lambda:cPLZ())
cBut.grid(column=0, row=1)

helpBut = tk.Button(frame1, text="Help", command=lambda:help())
helpBut.grid(column=0, row=2)


window.mainloop()