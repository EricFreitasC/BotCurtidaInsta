import webbrowser
import pyautogui
from time import sleep

def logout(): # função para deslogar da conta
    pyautogui.click(48,960,duration=2)
    sleep(2)
    pyautogui.click(48,960,duration=1)
    pyautogui.click(140,952,duration=2)

while True:
    webbrowser.open_new('https://www.instagram.com')
    sleep(2)
    pyautogui.click(443,404,duration=1.5) # clicar no login
    pyautogui.write('Usuario') # coloque seu login do insta
    pyautogui.click(340,455,duration=1.5) # clicar na senha
    pyautogui.write('SenhaUsuario')
    sleep(1)
    pyautogui.press('enter') # enter para logar após digitar login e senha
    sleep(8)
    pyautogui.click(47,377,duration=1.5) # clicando na pesquisa na tela
    pyautogui.write('UsuarioInsta') # pesquisando o usuário
    sleep(1)
    pyautogui.click(208,367,duration=1) # clicando no usuário para entrar na conta do insta
    sleep(1)
    pyautogui.click(172,851,duration=1) # clicando na primeira imagem 
    sleep(2)


    curtido = None
    try:
        curtido = pyautogui.locateCenterOnScreen('curtido.png')
    except pyautogui.ImageNotFoundException:
        print("Exceção: Imagem 'curtido.png' não encontrada.")

    if curtido is not None:
        # Se já tiver curtido, deslogar do insta e pausar o bot por 24 horas
        logout() # deslogando da conta
        sleep(86400)
    else:
        # Se não tiver curtido, clicando e comentando
        pyautogui.click(477, 693, duration=1)
        sleep(3)
        pyautogui.click(526, 691, duration=1)
        sleep(3)
        pyautogui.write('Adorei a postagem')
        sleep(1)
        pyautogui.press('enter')
        logout() # deslogando da conta
        sleep(86400) # pausando o bot por 24 horas