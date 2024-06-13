# -*- coding: utf-8 -*-

"""Sorry if u guys don't understand some variable name as im french, i offen use french name for them"""
#Importations
from tkinter import *
import math as m
import copy 



#Variables
#The goal was to create the most free interface possible, so the variable are here to customize the game
TailleMap= [100,100] #Dimension of the map, please note that here the code implies to have a square type map so both numbers should be the same
TaillePixel=10 #Dimension of one cell
itération=1000 #Maximum itération of animation, for force stop
animationtime=1 #animation time in ms, please note that calculus time is not take in count


#Fonctions
def grid(x,y): #This function is here to create a square matrix with given dimension
    Matrices=[]
    for i in range(x):
        M=[]
        for j in range(y):
            M+=[0]
        Matrices+=[M]
    return(Matrices)

Matrice=grid(TailleMap[0],TailleMap[1]) #I choose to represent the grid of conway by a matrix of one (living cell) and zero (dead cell)

Blanche=grid(TailleMap[0],TailleMap[1]) #Here is a matrix full of zero for th initialisation and the end condition

root=Tk() #Using Tkinter we open a window 

def click(event,TaillePixel): #This function permit to recognise by usig  the carthesian coordinates of a mouse click on a canvas, the pixel choosen. Its the initialisation phase
    x=event.x #clearer
    y=event.y
    if x<TaillePixel and y>=TaillePixel: #in order to not have issues with the borders and the matrix, I splitted the case, however it is possible that this part is useless
        x=0
        y=event.y//TaillePixel
    elif x>=TaillePixel and y<TaillePixel:
        x=event.x//TaillePixel
        y=0
    elif x>=TaillePixel and y>=TaillePixel:
        x=event.x//TaillePixel
        y=event.y//TaillePixel
    elif x<TaillePixel and y<TaillePixel:
        x=0
        y=0    
    global Matrice #this function will be called in a Tkinter module, so i can't return any values, so i declare Matrice as a global variable to change it while in my function
    if Matrice[x][y]==1: #By clicking, this part add or eraze the selected dot
        cnv.create_rectangle(x*TaillePixel,y*TaillePixel,(x+1)*TaillePixel,(y+1)*TaillePixel,fill='Ivory')
    elif Matrice[x][y]==0:
        cnv.create_rectangle(x*TaillePixel,y*TaillePixel,(x+1)*TaillePixel,(y+1)*TaillePixel,fill='black')
    if Matrice[x][y]==1:
        Matrice[x][y]=0
    elif Matrice[x][y]==0:
        Matrice[x][y]=1

def evolution(Matrices): #This function, with a given matrix of 1 and 0, can calculate the next situation according to conway's game of life's rules
#please note that conway's rules can be changed changing this function
    Fin=copy.deepcopy(Matrices) #deepcopy module was hard to find for me, i had to use it because i needed to separate the matrix i create with the matrix i analyse, 
                                #otherwise, both would interfere
    for i in range(len(Matrices[0])): #Here the code check every neighbours of every case of the matrix and calculate the new matrix
                                        #I had to separate case depending of the border, otherwise i would have out of range error
        for j in range(len(Matrices[1])):

            if j!=0 and i!=0 and j!=len(Matrices[1])-1 and i!=len(Matrices[0])-1:
                s=0
                s+=Matrices[i-1][j-1]+Matrices[i-1][j]+Matrices[i-1][j+1]+Matrices[i][j-1]+Matrices[i][j+1]+Matrices[i+1][j-1]+Matrices[i+1][j]+Matrices[i+1][j+1]

                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=0
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1

            elif j==0 and i!=0 and i!=len(Matrices[0])-1:
                s=0
                s+=Matrices[i-1][j]+Matrices[i-1][j+1]+Matrices[i][j+1]+Matrices[i+1][j]+Matrices[i+1][j+1]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
            elif i==0 and j!=0 and j!=len(Matrices[1])-1:
                s=0
                s+=Matrices[i][j-1]+Matrices[i][j+1]+Matrices[i+1][j-1]+Matrices[i+1][j]+Matrices[i+1][j+1]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
            elif i==0 and j==0:
                s=0
                s+=Matrices[i][j+1]+Matrices[i+1][j]+Matrices[i+1][j+1]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
            elif i==len(Matrices[0])-1 and j!=len(Matrices[1])-1 and j!=0:
                s=0
                s+=Matrices[i-1][j-1]+Matrices[i-1][j]+Matrices[i-1][j+1]+Matrices[i][j-1]+Matrices[i][j+1]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
            elif i!=len(Matrices[0])-1 and j==len(Matrices[1])-1 and i != 0:
                s=0
                s+=Matrices[i-1][j-1]+Matrices[i-1][j]+Matrices[i][j-1]+Matrices[i+1][j-1]+Matrices[i+1][j]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
            elif i==len(Matrices[0])-1 and j==len(Matrices[1])-1 and j !=0 and i !=0:
                s=0
                s+=Matrices[i-1][j-1]+Matrices[i-1][j]+Matrices[i][j-1]
                if Matrices[i][j]==1:
                    if s<2:
                        Fin[i][j]=0
                    elif s>3:
                        Fin[i][j]=1
                if Matrices[i][j]==0:
                    if s==3:
                        Fin[i][j]=1
                    
                        
                
                        
    return(Fin)
                
 

def changement(Matrices): #This function permit to convert the previous calculated matrix into graphic, not a big deal
    cnv.delete('all') #we eraze all first
    for i in range(len(Matrices[0])):
        for j in range(len(Matrices[1])):
            if Matrices[i][j]==1:
                cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='black')
            elif Matrices[i][j]==0:
                cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='Ivory')
                
def animation(Matrices,Blanche,itération,evolution,changement,i=0): #using recursivity, while number of iteration is overpass, or that the grid is empty (comparaison with the 0 matrix)
                                                                    #we calculate the next situation
    K=copy.deepcopy(Matrices)
    if i!=itération and Matrices!=Blanche:
        X=evolution(K)
        root.update_idletasks()

        root.after(1,changement,K)
        root.update_idletasks()
        i+=1
        root.after(animationtime,animation,X,Blanche,itération,evolution,changement,i)
        


    
                

    
        
        
       

#Mainloop

cnv=Canvas(root, width=TailleMap[0]*TaillePixel, height=TailleMap[1]*TaillePixel, bg="grey") #creating the canvas
cnv.grid(row=0,column=0) #im not using place cause there is few gui widget

for i in range(TailleMap[0]):
    for j in range(TailleMap[1]):
        cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='Ivory') #this is for the initialisation of the first canvas


button=Button(root,text='lancer animation',command = lambda: animation(Matrice,Blanche,itération,evolution,changement)) #the button start the animation
button.grid(row=0,column=1)

cnv.bind("<Button-1>", lambda event: click(event,TaillePixel)) #the click change pixels





root.mainloop() #end of loop
        