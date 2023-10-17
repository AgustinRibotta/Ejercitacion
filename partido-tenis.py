# Reto #2: EL PARTIDO DE TENIS
# Enunciado


'''
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
# Si saca p1, ventaja para p1
# si saca p2, ventaja para p2
# si pi = p2 deuce


def draw_victory():
    
    puntos_p1 = "Love"
    puntos_p2 = "Love"
    ronda = 0
    
    while True:
        
        punto = input('Indique el gnador ')        
        
        if ronda <= 5:
            
            if ronda == 5 and  puntos_p1 == puntos_p1:
                print("Deuce")
                ronda += 1
                return "Deuce"
            elif ronda < 5 :
        
                if punto == "P1":
                    
                    if puntos_p1 == "Love":
                        puntos_p1 = 15
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                    
                    elif puntos_p1 == 15:
                        puntos_p1 = 30
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                    
                    elif puntos_p1 == 30:
                        puntos_p1 = 40
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                        
                    else: 
                        print("Winer P1")
                        break

                
                if punto == "P2":
                    
                    if puntos_p2 == "Love":
                        puntos_p2 = 15
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                        
                    elif puntos_p2 == 15:
                        puntos_p2 = 30
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                        
                    elif puntos_p2 == 30:
                        puntos_p2 = 40
                        ronda = ronda + 1
                        print( puntos_p1 , puntos_p2)
                        
                    else: 
                        print("Winer P2")
                        break
                    

def tennis_match():
        
    draw_victory()

    p1 = 0
    p2 = 0
    
    while True:
        
        punto = input('Indique el gnador ')  
        
        if punto == "P1":
            p1 += 1
            
            if p1 == p2:
                print("Deuce")
                
            elif p1 < p2:
                print("Ventaja P2")
                
            elif p1 > p2:
                print("Ventaja P1")

        
        elif punto == "P2":
            p2 += 1
            
            if p1 == p2:
                print("Deuce")
                
            elif p1 < p2:
                print("Ventaja P2")
                
            elif p1 > p2:
                print("Ventaja P1")

        
        if   p1 - p2 == 2 :
            print("Winer P1")
            break
            
        if   p2 - p1 == 2  :
            print("Winer P2")
            break
            

            
print("Indicate P1 or P2 as appropriate")

tennis_match()    

    