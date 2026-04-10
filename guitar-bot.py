import cv2
import numpy as np
import mss
from pynput.keyboard import Controller
import time

# ==================================================================
# MODO TURBO
# ==================================================================
MOSTRAR_TELA = False

# ==================================================================
# COORDENADAS DA TELA
# ==================================================================
TELA_TOP = 660   
TELA_LEFT = 725
TELA_WIDTH = 450
TELA_HEIGHT = 60 

# ==================================================================
# AJUSTES FINOS
# ==================================================================
TOLERANCIA = 0     
PIXELS_MINIMOS = 10   

# TECLAS DO JOGO
GREEN_KEY = 'a'
RED_KEY = 's'
YELLOW_KEY = 'd'
BLUE_KEY = 'j'
ORANGE_KEY = 'k'

keyboard = Controller()

def guitarBot():
    greenPressed = False
    redPressed = False
    yellowPressed = False
    bluePressed = False
    orangePressed = False

    cooldown_verde = 0
    cooldown_vermelho = 0
    cooldown_amarelo = 0
    cooldown_azul = 0
    cooldown_laranja = 0

    memoria_verde = False
    memoria_vermelho = False
    memoria_amarelo = False
    memoria_azul = False
    memoria_laranja = False

    print("Bot Invencível! ATIVADO!")
    if not MOSTRAR_TELA:
        print("Modo TURBO ativado! Pressione Ctrl+C neste terminal para parar o bot.")

    with mss.mss() as sct:
        monitor = {"top": TELA_TOP, "left": TELA_LEFT, "width": TELA_WIDTH, "height": TELA_HEIGHT}
        coluna = TELA_WIDTH // 5 
        
        LIMITE_CLARAO = (TELA_WIDTH * TELA_HEIGHT) * 0.3 

        try:
            while(1):
                img = np.array(sct.grab(monitor))
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                # Radar
                hsv_radar = hsv[0:5, :]   
                hsv_botao = hsv[40:60, :] 

                # DETECTOR DE CLARÃO
                whiteMask = cv2.inRange(hsv, np.array([0, 0, 180]), np.array([179, 40, 255]))
                is_flashing = cv2.countNonZero(whiteMask) > LIMITE_CLARAO

                lowerGreen, upperGreen = np.array([45, 120, 100]), np.array([75, 255, 255])
                lowerRed, upperRed = np.array([0, 150, 100]), np.array([8, 255, 255])
                lowerYellow, upperYellow = np.array([25, 120, 100]), np.array([35, 255, 255])
                lowerBlue, upperBlue = np.array([100, 120, 100]), np.array([130, 255, 255])
                lowerOrange, upperOrange = np.array([10, 150, 100]), np.array([22, 255, 255])
                
                lowerEspecial, upperEspecial = np.array([80, 100, 150]), np.array([110, 255, 255])
                lowerShadow, upperShadow = np.array([0, 0, 0]), np.array([179, 255, 170])

                p_verde_R = hsv_radar[:, 0:coluna]
                p_verm_R = hsv_radar[:, coluna:coluna*2]
                p_amar_R = hsv_radar[:, coluna*2:coluna*3]
                p_azul_R = hsv_radar[:, coluna*3:coluna*4]
                p_lara_R = hsv_radar[:, coluna*4:TELA_WIDTH]

                if cv2.countNonZero(cv2.bitwise_or(cv2.inRange(p_verde_R, lowerGreen, upperGreen), cv2.inRange(p_verde_R, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS: memoria_verde = True
                if cv2.countNonZero(cv2.bitwise_or(cv2.inRange(p_verm_R, lowerRed, upperRed), cv2.inRange(p_verm_R, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS: memoria_vermelho = True
                if cv2.countNonZero(cv2.bitwise_or(cv2.inRange(p_amar_R, lowerYellow, upperYellow), cv2.inRange(p_amar_R, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS: memoria_amarelo = True
                if cv2.countNonZero(cv2.bitwise_or(cv2.inRange(p_azul_R, lowerBlue, upperBlue), cv2.inRange(p_azul_R, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS: memoria_azul = True
                if cv2.countNonZero(cv2.bitwise_or(cv2.inRange(p_lara_R, lowerOrange, upperOrange), cv2.inRange(p_lara_R, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS: memoria_laranja = True

                p_verde_B = hsv_botao[:, 0:coluna]
                p_verm_B = hsv_botao[:, coluna:coluna*2]
                p_amar_B = hsv_botao[:, coluna*2:coluna*3]
                p_azul_B = hsv_botao[:, coluna*3:coluna*4]
                p_lara_B = hsv_botao[:, coluna*4:TELA_WIDTH]

                def verifica_botao(pista, lower, upper, memoria):
                    tem_cor = cv2.countNonZero(cv2.bitwise_or(cv2.inRange(pista, lower, upper), cv2.inRange(pista, lowerEspecial, upperEspecial))) > PIXELS_MINIMOS
                    tem_sombra = is_flashing and (cv2.countNonZero(cv2.inRange(pista, lowerShadow, upperShadow)) > PIXELS_MINIMOS)
                    return tem_cor or (tem_sombra and memoria)

                btn_verde = verifica_botao(p_verde_B, lowerGreen, upperGreen, memoria_verde)
                btn_verm = verifica_botao(p_verm_B, lowerRed, upperRed, memoria_vermelho)
                btn_amar = verifica_botao(p_amar_B, lowerYellow, upperYellow, memoria_amarelo)
                btn_azul = verifica_botao(p_azul_B, lowerBlue, upperBlue, memoria_azul)
                btn_lara = verifica_botao(p_lara_B, lowerOrange, upperOrange, memoria_laranja)

                # ==========================================================
                # APERTANDO AS TECLAS
                # ==========================================================
                
                # VERDE
                if btn_verde:
                    cooldown_verde = TOLERANCIA
                    if not greenPressed:
                        keyboard.press(GREEN_KEY)
                        greenPressed = True
                else:
                    if greenPressed:
                        if is_flashing:
                            pass 
                        else:
                            cooldown_verde -= 1
                            if cooldown_verde <= 0:
                                keyboard.release(GREEN_KEY)
                                greenPressed = False
                                memoria_verde = False 

                # VERMELHO
                if btn_verm:
                    cooldown_vermelho = TOLERANCIA
                    if not redPressed:
                        keyboard.press(RED_KEY)
                        redPressed = True
                else:
                    if redPressed:
                        if is_flashing:
                            pass 
                        else:
                            cooldown_vermelho -= 1
                            if cooldown_vermelho <= 0:
                                keyboard.release(RED_KEY)
                                redPressed = False
                                memoria_vermelho = False

                # AMARELO
                if btn_amar:
                    cooldown_amarelo = TOLERANCIA
                    if not yellowPressed:
                        keyboard.press(YELLOW_KEY)
                        yellowPressed = True
                else:
                    if yellowPressed:
                        if is_flashing:
                            pass 
                        else:
                            cooldown_amarelo -= 1
                            if cooldown_amarelo <= 0:
                                keyboard.release(YELLOW_KEY)
                                yellowPressed = False
                                memoria_amarelo = False

                # AZUL
                if btn_azul:
                    cooldown_azul = TOLERANCIA
                    if not bluePressed:
                        keyboard.press(BLUE_KEY)
                        bluePressed = True
                else:
                    if bluePressed:
                        if is_flashing:
                            pass 
                        else:
                            cooldown_azul -= 1
                            if cooldown_azul <= 0:
                                keyboard.release(BLUE_KEY)
                                bluePressed = False
                                memoria_azul = False

                # LARANJA
                if btn_lara:
                    cooldown_laranja = TOLERANCIA
                    if not orangePressed:
                        keyboard.press(ORANGE_KEY)
                        orangePressed = True
                else:
                    if orangePressed:
                        if is_flashing:
                            pass 
                        else:
                            cooldown_laranja -= 1
                            if cooldown_laranja <= 0:
                                keyboard.release(ORANGE_KEY)
                                orangePressed = False
                                memoria_laranja = False

                if MOSTRAR_TELA:
                    cv2.imshow('Visao do Bot', img)
                    if cv2.waitKey(1) & 0xFF == 27: 
                        break
        
        except KeyboardInterrupt:
            print("\nBot parado pelo usuário!")
        
        finally:
            keyboard.release(GREEN_KEY)
            keyboard.release(RED_KEY)
            keyboard.release(YELLOW_KEY)
            keyboard.release(BLUE_KEY)
            keyboard.release(ORANGE_KEY)
            cv2.destroyAllWindows()
            print("Teclas soltas com segurança.")

if __name__ == '__main__':
    guitarBot()