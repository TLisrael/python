# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer

mixer.init()
mixer.music.load('sentadona.mp3')
mixer.music.play()
mixer.music.set_volume(6)
while True:
    #############################################################
    print("Pressione 'P' para pausar e 'V' para voltar a reproduzir")
    print("Pressione 'S' para sair. ")
    controls = input("  ")
    if controls == 'p':
        mixer.music.pause()
    elif controls == 'v':
        mixer.music.unpause()
    elif controls == 's':
        mixer.music.stop()
        break
