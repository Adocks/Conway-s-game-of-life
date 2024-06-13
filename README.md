from tkinter import *
import math as m
import copy 
#Variables
TailleMap= [10,100]
TaillePixel=10
itération=1000
animationtime=1


#Fonctions
def grid(x,y):
    Matrices=[]
    for i in range(x):
        M=[]
        for j in range(y):
            M+=[0]
        Matrices+=[M]
    return(Matrices)

Matrice=grid(TailleMap[0],TailleMap[1])
Blanche=grid(TailleMap[0],TailleMap[1])

root=Tk()
def click(event,TaillePixel):
    k=len(list(str(TaillePixel)))-1
    x=event.x
    y=event.y
    if x<TaillePixel and y>=TaillePixel:
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
    global Matrice
    if Matrice[x][y]==1:
        cnv.create_rectangle(x*TaillePixel,y*TaillePixel,(x+1)*TaillePixel,(y+1)*TaillePixel,fill='Ivory')
    elif Matrice[x][y]==0:
        cnv.create_rectangle(x*TaillePixel,y*TaillePixel,(x+1)*TaillePixel,(y+1)*TaillePixel,fill='black')
    print(event.x,event.y)
    print(x,y)
    if Matrice[x][y]==1:
        Matrice[x][y]=0
    elif Matrice[x][y]==0:
        Matrice[x][y]=1

def evolution(Matrices):
    Fin=copy.deepcopy(Matrices)
    for i in range(len(Matrices[0])):
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
                
 

def changement(Matrices):
    cnv.delete('all')
    for i in range(len(Matrices[0])):
        for j in range(len(Matrices[1])):
            if Matrices[i][j]==1:
                cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='black')
            elif Matrices[i][j]==0:
                cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='Ivory')
                
def animation(Matrices,Blanche,itération,evolution,changement,i=0):
    K=copy.deepcopy(Matrices)
    if i!=itération and Matrices!=Blanche:
        X=evolution(K)
        root.update_idletasks()

        root.after(1,changement,K)
        root.update_idletasks()
        i+=1
        root.after(animationtime,animation,X,Blanche,itération,evolution,changement,i)
        


    
                

    
        
        
       

#Mainloop

cnv=Canvas(root, width=TailleMap[0]*TaillePixel, height=TailleMap[1]*TaillePixel, bg="grey")
cnv.grid(row=0,column=0)

for i in range(TailleMap[0]):
    for j in range(TailleMap[1]):
        cnv.create_rectangle(i*TaillePixel,j*TaillePixel,(i+1)*TaillePixel,(j+1)*TaillePixel,fill='Ivory')


button=Button(root,text='lancer animation',command = lambda: animation(Matrice,Blanche,itération,evolution,changement))
button.grid(row=0,column=1)

cnv.bind("<Button-1>", lambda event: click(event,TaillePixel))





root.mainloop()
