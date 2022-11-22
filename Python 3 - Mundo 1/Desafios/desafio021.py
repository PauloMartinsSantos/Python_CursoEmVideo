# Faça um programa em python que abra e reproduza o audio de um arquivo mp3.
import pygame

pygame.init()
pygame.mixer.load('NOME DO ARQUIVO')
pygame.mixer.music.play()
pygame.event.wait()
# Colocar o arquivo na mesma pasta do projeto