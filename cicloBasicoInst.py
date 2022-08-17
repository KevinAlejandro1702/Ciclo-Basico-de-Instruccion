'''
Proyecto final (Ciclo básico de instrucción)

Integrantes:
------------
Kevin Alejandro Abadia Caicedo      |   2025825
Cristian Camilo Torijano Velasco    |   2025808
Daniel Jose Cubides Niño            |   2028844
'''

#modulos utilizados
from io import open

#set de instrucciones
from funcionesCiclo import *


''' Clase (CicloBasico)

    Decodificación del archivo .txt y ejecución de sus instrucciones
    
    También se define la memoria como un diccionario de datos que tiene como claves(keys)
    el número de la posición de la memoria
'''
class CicloBasico():

    #inicializa los registros de la CPU
    def __init__(self):
        #registros de la cpu
        self.pc = 0
        self.mar = 0
        self.mdr = ''
        self.icr = ''
        
        self.accumRegister = 0
        
        self.finished = False
        
        
    def getAccRegister(self):
        return self.accumRegister
   
    def showMAR(self):
        print(self.mar)
        return self.mar
    
    
    def showMDR(self):
        print(self.mdr)
        return self.mdr
        
        
    def showICR(self):
        print(self.icr)
        return self.icr
        
   
    #lee y retorna las lineas(instrucciones) del archivo de texto plano
    def readFile(self):
    
        tFile = open("instrucciones.txt","r")
        lines = tFile.readlines()

        tFile.close()
        
        return lines


    #separa las instrucciones en arrays para hacer más sencilla la
    #decodificación de las mismas
    def leerInstruccion(self):
    
        lines = self.readFile()
        it = 0
        palabras = []

        for line in lines:

            if (line):        
                
                it += 1
                palabras += [line.split()]
                #print(palabras)
        
            else:
                print("Esta  vacio\n")
                
        return palabras


    #obtiene los nombres de las posiciones de memoria para asignar
    #las claves en el diccionario que representa a la memoria principal
    def definirMemoria(self):
        inst = self.leerInstruccion()
        
        direcciones = []
        for i in range(len(inst)):
            for j in range(4):
                if inst[i][0] == 'SET':            
                    if inst[i][j].startswith('D') :
                        direcciones.append(inst[i][j])
        
        #print(direcciones)
        
        espacios = []
        keys = []
        
        for dir in direcciones:
            if dir not in espacios:
                espacios.append(dir)
                
        for x in espacios:
            keys.append(int(x.replace('D', '')))
        
        espacios.append(0)
        keys.append('accumRegister')
        
        espaciosMemoria = dict(zip(keys, espacios))

        #print("Posiciones:",keys)
        #print("MEMORIA PRINCIPAL:", espaciosMemoria, '\n')
        
        return espaciosMemoria
            
            
    #simula el ciclo que sigue la información entre los
    #registros de la CPU, además de la ejecución de las instrucciones
    #por parte de la unidad de control
    def executeDecodeCycle(self):
    
        
        instrucciones = self.leerInstruccion()
        #print(instrucciones)
        memoria = self.definirMemoria()
        
        for currentInst in range(len(instrucciones)):
            self.mdr = ''
            
            if(self.finished == True):
                print('terminó')
                break
            
            self.pc = currentInst + 1
            self.mar = self.pc
            
            #print('pc:', self.pc, 'mar:', self.mar)
            
            for i in(instrucciones[currentInst]):
                self.mdr += str(i)
                self.mdr += ' '
                
            #print('mdr:', self.mdr)
             
            '''
                pasa la instrucción al ICR para que este se comunique con
                la unidad de control que decodificará la instrucción y
                realizará su ejecución
            '''
            self.icr = self.mdr
            
            self.controlUnit(memoria, instrucciones[currentInst], 
                             instrucciones[currentInst][0])
        
        

    #decodifica e interpreta las instrucciones y permite su ejecución
    #basado en el 'set de instrucciones' 
    def controlUnit(self, espaciosMemoria, currentInstruction, function):
        
        self.accumRegister = espaciosMemoria['accumRegister']

        if(function == "END"):
            self.finished = True
        else:
            pos = currentInstruction[1].replace('D', '')

        #print("INSTRUCCION No.", i+1, currentInstruction)
    
        if function == "SET":
            
            val = int(currentInstruction[2])
            
            setFunction(pos, val, espaciosMemoria)
        
        
        elif function == "ADD":
            
            val = espaciosMemoria[pos]
            addFunction(val, currentInstruction, espaciosMemoria, self.accumRegister)
            
            
        elif function == "SUB":
            
            val = espaciosMemoria[pos]
            subFunction(val, currentInstruction, self.accumRegister, espaciosMemoria)
            
        
        elif function == "MUL":
            
            val = espaciosMemoria[pos]
            multFunction(val, currentInstruction, self.accumRegister, espaciosMemoria)
            
        
        elif function == "DIV":
            
            val = espaciosMemoria[pos]
            divFunction(val, currentInstruction, self.accumRegister, espaciosMemoria)
            
        
        elif function == "INC":
            
            incFunction(espaciosMemoria, pos)
        
        
        elif function == "DEC":
            
            decFunction(espaciosMemoria, pos)
            
        
        elif function == "MOV":

            moveFunction(espaciosMemoria, currentInstruction)
            
        
        elif function == "LDR":
            
            loadFunction(espaciosMemoria, pos)
            
        
        elif function == "STR":
            
            storeFunction(espaciosMemoria, pos)
            
        
        elif function == "BEQ":
            
            beqFunction(espaciosMemoria, pos)
            
        
        elif function == "SHW":
            if(currentInstruction[1]=='MAR'):
                self.showMAR()
                
            elif(currentInstruction[1]=='MDR'):
                self.showMDR()
                
            elif(currentInstruction[1]=='ICR'):
                self.showICR()
                
            else:
                showFunction(espaciosMemoria, pos)
            
            
        elif(function == "END"):
            #print("\n------INSTRUCTIONS READING FINISHED------")
            self.finished = True
        
        #print("------ MEMORIA: ------", '\n' + str(espaciosMemoria), '\n')            