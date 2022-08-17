'''
Kevin Alejandro Abadia Caicedo
2025825-3743
Ciclo básico de instrucción
'''


def calcularCaso(instrucciones:list):
    contador = 0
    for inst in instrucciones:
        if  inst == "NULL":
            contador += 1
            
    ##print("contador:", contador)
    return contador
    

def setFunction(position:int, value:int, memoria:dict):
    
    #crea un objeto o valor en una posición de memoria específica
    
    memoria[position] = value
    
    
def addFunction(value:int, instrucciones:list, memoria:dict, acumRegister:int):
    
    #Suma al acumRegister el valor que hay en la posición de memoria
    
    if calcularCaso(instrucciones) == 2:
        memoria['accumRegister'] += value
    
    
    elif calcularCaso(instrucciones) == 1:
        #print("Caso dos")
        memoria['accumRegister'] += value
        pos = int(instrucciones[2][1])
        #print(instrucciones[2][1])
        memoria[pos] += memoria['accumRegister']
        
                
    elif calcularCaso(instrucciones) == 0:
        #print("Caso tres")
        memoria['accumRegister'] += value
        pos = int(instrucciones[2][1])
        memoria[pos] += memoria['accumRegister']
        memoria['accumRegister'] = memoria[pos]
        pos = int(instrucciones[3][1])
        memoria[pos] += memoria['accumRegister']


def subFunction(value:int, instrucciones:list, acumRegister:int, memoria:dict):
    
    #Resta al acumRegister el valor que hay en la posición de memoria

    if calcularCaso(instrucciones) == 2:
        memoria['accumRegister'] -= value
    
    
    elif calcularCaso(instrucciones) == 1:
        #print("Caso dos")
        memoria['accumRegister']-= value
        pos = int(instrucciones[2][1])
        memoria[pos] += memoria['accumRegister']
        
                
    elif calcularCaso(instrucciones) == 0:
        #print("Caso tres")
        memoria['accumRegister'] -= value
        pos = int(instrucciones[2][1])
        memoria[pos] += memoria['accumRegister']
        memoria['accumRegister'] = memoria[pos]
        pos = int(instrucciones[3][1])
        memoria[pos] += memoria['accumRegister']



def multFunction(value:int, instrucciones:list, acumRegister:int, memoria:dict):
    
    #Multiplica al acumRegister el valor que hay en la posición de memoria
    
    if calcularCaso(instrucciones) == 2:
        memoria['accumRegister'] *= value
    
    
    elif calcularCaso(instrucciones) == 1:
        #print("Caso dos")
        memoria['accumRegister'] *= value
        pos = int(instrucciones[2][1])
        memoria[pos] *= memoria['accumRegister']
        
                
    elif calcularCaso(instrucciones) == 0:
        #print("Caso tres")
        memoria['accumRegister'] *= value
        pos = int(instrucciones[2][1])
        memoria[pos] *= memoria['accumRegister']
        memoria['accumRegister'] = memoria[pos]
        pos = int(instrucciones[3][1])
        memoria[pos] *= memoria['accumRegister']
        

def divFunction(value:int, instrucciones:list, acumRegister:int, memoria:dict):
    
    #Divide el valor del acumRegister entre el valor que hay en memoria
    
    if calcularCaso(instrucciones) == 2:
        memoria['accumRegister'] *= value
    
        
    elif calcularCaso(instrucciones) == 1:
        #print("Caso dos")
        memoria['accumRegister'] *= value
        pos = int(instrucciones[2][1])
        memoria[pos] *= memoria['accumRegister']
        
            
    elif calcularCaso(instrucciones) == 0:
        #print("Caso tres")
        memoria['accumRegister'] *= value
        pos = int(instrucciones[2][1])
        memoria[pos] *= memoria['accumRegister']
        memoria['accumRegister'] = memoria[pos]
        pos = int(instrucciones[3][1])
        memoria[pos] *= memoria['accumRegister']
        
        
def incFunction(memoria:dict, position:int):
    memoria[position] += 1
    

def decFunction(memoria:dict, position:int):
    memoria[position] -= 1
    
    
def moveFunction(memoria:dict, instrucciones:list):
    pos = int(instrucciones[1][1])
    aux = memoria[pos]
    memoria[pos] = 'D' + str(pos)
    pos = int(instrucciones[2][1])
    memoria[pos] = aux
    
    
def loadFunction(memoria:dict, position:int):
    memoria['accumRegister'] = memoria[position]
    #print("accumRegister:", memoria['accumRegister'])
    

def storeFunction(memoria:dict, position:int):
    #print("accumRegister:", memoria['accumRegister'])
    memoria[position] = memoria['accumRegister']
    

def beqFunction(memoria:dict, position:int):
    
    if(memoria[position] - memoria['accumRegister'] == 0):
        pass


def showFunction(memoria:dict, position:int):
    print(memoria[position])