from tkinter import *
import tkinter as tk
from Backtracking import *
from ColoringMap import intializeContext,drawGraph
from ForwardCheck import Forward
from forwad_CheckAC3 import *
class Interface:

    def __init__(self,root):
        self.frame = Frame(root) #Frame for the first interface
        self.frameAlgorithms = Frame(root) #contain the button frame and the map frame
        root.title('TP2 AI Mtibaa Amal & Riahi Med Wassim')
        self.introductionLabel=tk.Label(root, text="Welcome ! Choose Your Game")
        self.introductionLabel.config(font=("Arial", 24),foreground="#9999ff")
        self.introductionLabel.pack()

        #Algorithms buttons
        self.buttonsFrame = Frame(self.frameAlgorithms)
        self.mapFrame = Frame(self.frameAlgorithms) #for sudoku grid
        self.colorMapFrame=Frame(self.frameAlgorithms) #for colring card map
        self.nQueenFrame=Frame(self.frameAlgorithms) #for nQueen grid

        self.button1 = tk.Button(self.buttonsFrame, text="Backtracking LCV", width=24, height=1, bg="#b3ccff",
                             font=("Arial", 18))
        self.button2 = tk.Button(self.buttonsFrame, text="Forward Search MRV", width=24, height=1, bg="#b3ccff",
                                 font=("Arial", 18))
        self.button3 = tk.Button(self.buttonsFrame, text="AC3", width=24, height=1, bg="#b3ccff",
                                 font=("Arial", 18))

        coloringMapPhoto = tk.PhotoImage(file="intialMap.png")
        self.photoLabel=Label(self.colorMapFrame,image=coloringMapPhoto)

        def returnMethod():
            self.mapFrame.pack_forget()
            self.frameAlgorithms.pack_forget()
            self.frame.pack()
            self.photoLabel.grid_forget()

        self.resetButton = tk.Button(self.buttonsFrame, text="Reset", width=24, height=1, bg="red",
                                      font=("Arial", 18))
        self.returnButton = tk.Button(self.buttonsFrame, text="<=", width=24, height=1, bg="green",
                                      font=("Arial", 18), command=returnMethod)

        def callMethod(method): #Configure parameters and call backtracking for Sudoko
            t=setBacktracking()
            for i in range(0,9):
                for j in range(0,3):
                    for k in range(0,3):
                        if self.entries[i][j][k].get().isdigit():
                            t.domaines[int(i/3)*27+j*9+(i%3)*3+k]=[]
                            t.domaines[int(i/3)*27+j*9+(i%3)*3+k].append(self.entries[i][j][k].get())
            a = []
            for i in range(0, len(t.variables)):
                if len(t.domaines[i]) == 1:
                    a.append(t.domaines[i][0])
                else:
                    a.append(None)
            if method=='backtracking':
                Bactracking(a, t, 0)
            if method=='forward':
                Forward(a, t, 0)
            if method=='forwardAC3':
                forward_CheckAC3(a, t)
            print(a)
            for i in range(0,9):
                for j in range(0,3):
                    for k in range(0,3):
                        if  self.entries[i][j][k].get()=='':
                            self.entries[i][j][k].insert(0,a[int(i/3)*27+j*9+(i%3)*3+k])
            root.update()

        def callColoringMap(method):
            t=intializeContext()
            a=[]
            for i in range(0, len(t.variables)):
                if len(t.domaines[i]) == 1:
                    a.append(t.domaines[i][0])
                else:
                    a.append(None)
            if method=='backtracking':
                Bactracking(a, t, 0)
            if method=='forward':
                Forward(a,t,0)
            if method == 'forwardAC3':
                forward_CheckAC3(a,t)
            drawGraph(a,t,method)
            if(method=='backtracking'):
                photo=tk.PhotoImage(file='backtrackingColorMap.png')
                self.photoLabel.configure(image=photo)
                self.photoLabel.image=photo
            if(method=='forward'):
                #call forward
                photo = tk.PhotoImage(file='forward.png')
                self.photoLabel.configure(image=photo)
                self.photoLabel.image = photo
            if (method == 'forwardAC3'):
                photo = tk.PhotoImage(file='forwardAC3.png')
                self.photoLabel.configure(image=photo)
                self.photoLabel.image = photo
        def callNQueen():
            t = setBactraking8Queens()
            a = []
            for i in range(0, len(t.variables)):
                if len(t.domaines[i]) == 1:
                    a.append(t.domaines[i][0])
                else:
                    a.append(None)

            self.entries = []

            Bactracking(a, t, 1)

            for i in range(0, 64):
                self.entries.append(Entry(self.nQueenFrame, width=3, font=("Arial", 30)))
                if a[i] == '1':
                    self.entries[i].insert(0, '*')
            for i in range(0, 64):
                self.entries[i].grid(row=int(i / 8), column=i % 8)
            #AffichageNqueens(a, 8)
            self.nQueenFrame.grid(row=0, column=1)


        def restButton(method):
            if method=='ColoringMap':
                photo = tk.PhotoImage(file='intialMap.png')
                self.photoLabel.configure(image=photo)
                self.photoLabel.image = photo
            if method=='Sudoku':
                for i in range(0, 9):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            self.entries[i][j][k].delete(0,'end')

            root.update()
            if method=='N-Queen':
                for i in range(0,64):
                    self.entries[i].delete(0,'end')


        def Algorithms(game):
            self.frame.pack_forget()
            self.button1.grid(row=0, column=0)
            self.button2.grid(row=1, column=0)
            self.button3.grid(row=2, column=0)
            self.buttonsFrame.grid(row=0,column=0)
            self.mapFrame.grid(row=0, column=1)
            if game == "sudoku":

                self.colorMapFrame.grid_forget()
                self.nQueenFrame.grid_forget()
                self.button1.configure(command=lambda :callMethod('backtracking'))
                self.button2.configure(command=lambda :callMethod('forward'))
                self.button3.configure(command=lambda :callMethod('forwardAC3'))
                self.resetButton.configure(command=lambda :restButton('Sudoku'))
                self.frames = [[Frame(self.mapFrame, borderwidth=2) for i in range(0, 3)] for j in range(0, 3)]

                for i in range(0, 3):
                    for j in range(0, 3):
                        self.frames[i][j].grid(row=i, column=j)

                self.entries = [
                    [[Entry(self.frames[0][0], width=5) for a in range(0, 3)] for j in range(0, 3)],
                    [[Entry(self.frames[0][1], width=5) for b in range(0, 3)] for k in range(0, 3)],
                    [[Entry(self.frames[0][2], width=5) for c in range(0, 3)] for l in range(0, 3)],
                    [[Entry(self.frames[1][0], width=5) for d in range(0, 3)] for m in range(0, 3)],
                    [[Entry(self.frames[1][1], width=5) for e in range(0, 3)] for n in range(0, 3)],
                    [[Entry(self.frames[1][2], width=5) for f in range(0, 3)] for o in range(0, 3)],
                    [[Entry(self.frames[2][0], width=5) for g in range(0, 3)] for p in range(0, 3)],
                    [[Entry(self.frames[2][1], width=5) for h in range(0, 3)] for q in range(0, 3)],
                    [[Entry(self.frames[2][2], width=5) for i in range(0, 3)] for r in range(0, 3)],

                ]

                for i in range(0, 9):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            self.entries[i][j][k].grid(row=j, column=k)


            if game=='coloringMap':
                self.nQueenFrame.grid_forget()
                self.mapFrame.grid_forget()
                self.photoLabel.grid(row=0,column=1)
                self.colorMapFrame.grid(row=0,column=1)
                self.button1.configure(command=lambda:callColoringMap('backtracking'))
                self.button2.configure(command=lambda:callColoringMap('forward'))
                self.button3.configure(command=lambda:callColoringMap('forwardAC3'))
                self.resetButton.configure(command=lambda:restButton('ColoringMap'))

            if game=='nQueen':
                self.mapFrame.grid_forget()
                self.colorMapFrame.grid_forget()
                self.button1.configure(command=callNQueen,text="Backtracking")
                self.resetButton.configure(command=lambda:restButton('N-Queen'))
                self.button2.grid_forget()
                self.button3.grid_forget()
                t=setBactraking8Queens()

                a = []
                for i in range(0, len(t.variables)):
                    if len(t.domaines[i]) == 1:
                        a.append(t.domaines[i][0])
                    else:
                        a.append(None)

                self.entries=[]

                for i in range(0,64):
                    self.entries.append(Entry(self.nQueenFrame,width=3,font=("Arial",30)))
                    if a[i]=='1':
                        self.entries[i].insert(0,'*')
                for i in range(0,64):
                    self.entries[i].grid(row=int(i/8),column=i%8)
                #AffichageNqueens(a,8)
                self.nQueenFrame.grid(row=0, column=1)

            self.resetButton.grid(row=5,column=0)
            self.returnButton.grid(row=6,column=0)
            self.frameAlgorithms.pack()


        photoSudoko=tk.PhotoImage(file="sudoko.png")
        self.sudokoButton=tk.Button(self.frame,image=photoSudoko, width=400,height=300,command=lambda:Algorithms("sudoku"))
        self.sudokoButton.grid(row=0,column=0)


        coloringMap=tk.PhotoImage(file="coloringMap.PNG")
        self.coloringMapButton=tk.Button(self.frame,image=coloringMap,width=400,height=300,command=lambda:Algorithms("coloringMap"))
        self.coloringMapButton.grid(row=0,column=1)

        nQueen=tk.PhotoImage(file="nQueen.PNG")
        self.nQueen=tk.Button(self.frame,image=nQueen,width=400,height=300,command=lambda:Algorithms("nQueen"))
        self.nQueen.grid(row=0, column=2)

        self.frame.pack()
        root.geometry("1200x600")
        root.mainloop()



root = Tk()
interface=Interface(root)
