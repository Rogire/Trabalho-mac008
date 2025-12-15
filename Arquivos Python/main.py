import numpy as np

from plot import *
from operacoes import *


class ElementosFinitos:
    #F=[{"Glib":x,"Força":y}]
    def __init__(self,x,y,Reac_Apoio,Desloc_apoio,num_el,num_nos_el,num_GLib,E,I,area,F,rho=1):
        self.x = x
        self.y = y
        self.Reac_Apoio = Reac_Apoio
        self.Desloc_apoio = Desloc_apoio
        self.num_el = num_el
        self.num_nos_el = num_nos_el
        self.num_GLib = num_GLib
        self.E = E
        self.I = I
        self.area = area
        self.rho = rho
        self.F = F

#Recebe a malha e condições de contorno e calcula o método
#com as funções do arquivo operacoes
    def CalcElementosFinitos(self):
        #Variáveis do problema
        tot_Nos = (self.num_nos_el-1)*(self.num_el+1)
        tot_Glib = tot_Nos*self.num_GLib
        F_Glib = np.zeros(tot_Glib)
        K_final = np.zeros((tot_Glib, tot_Glib))

        #Forças aplicadas na estrutura

        for i in self.F:
            F_Glib[i["Glib"]] = i["Forca"]

        for iel in range(1, num_el+1):
            index = u_vec_index(iel, self.num_nos_el, self.num_GLib)
            node1 = iel - 1
            node2 = iel

            # o---------------o
            # i    elemento   j
            No_i = {'x': self.x[node1], 'y': self.y[node1]}
            No_j = {'x': self.x[node2], 'y': self.y[node2]}

            #Tamanho elemento
            Le = np.sqrt((No_j['x'] - No_i['x'])**2+(No_j['y'] - No_i['y'])**2)

            if (No_j['x']-No_i['x'])==0:
                phi = np.pi/2 if No_j['y'] > No_i['y'] else -np.pi/2
            else:
                phi = np.arctan((No_j['y'] - No_i['y']) / (No_j['x'] - No_i['x']))

            K_transf, _ = Matriz_Total_Global(self.E, self.I, Le, self.area, phi, Calc_massa=True)
            K_final = Matriz_K(K_final, K_transf, index)

        K_final, F_Glib = Cond_cont(K_final, F_Glib, self.Reac_Apoio, self.Desloc_apoio)

        res = np.linalg.solve(K_final, F_Glib)

        ResMat = np.column_stack((np.arange(1, tot_Glib+1), res))

        print("GDL    Deslocamento")

        for linha in ResMat:
            print(f"{int(linha[0]):3d}        {linha[1]:.6e}")


        plot_desloc(x,y,ResMat,num_GLib,100)


#Variáveis do problema
num_nos_el = 2
num_GLib = 3
E=2e11 #kN/mm² = GPa
I= np.pi*(3**4)/4
area= np.pi*(30**2)
DA = [0,0,0, 0, 0, 0] 

#Discretização 1 da malha:
num_el = 12

#[x,y] = mm
x = [0,0,0,500,1000,2000,3000,4000,5000,6000,6000,6000,6000]
y = [0,2000,4000,4000,4000,4000,4000,4000,4000,4000,3500,2500,1000]

#Força aplicada sobre os graus de liberdade
F =[{"Glib":6,"Forca":10000},{"Glib":10,"Forca":-5000},{"Glib":30,"Forca":-5000}]
#Graus de liberdade restringidos (os apoios da estrutura)
RA = [1,2,3,37,38,39]  

MEF = ElementosFinitos(x,y,RA,DA,num_el,num_nos_el,num_GLib,E,I,area,F)
MEF.CalcElementosFinitos()

#Discretização 2 da malha:
num_el = 21

#[x,y] = mm
x = [0,0,0,0,0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6000,6000,6000,6000,6000]
y = [0,1000,2000,3000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,3500,3250,2500,1750,1000]

F =[{"Glib":12,"Forca":10000},{"Glib":16,"Forca":-5000},{"Glib":54,"Forca":-5000}]
#Graus de liberdade restringidos (os apoios da estrutura)
RA = [1,2,3,61,62,63]  

MEF = ElementosFinitos(x,y,RA,DA,num_el,num_nos_el,num_GLib,E,I,area,F)
MEF.CalcElementosFinitos()