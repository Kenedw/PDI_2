#!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
from PIL import Image
import matplotlib.pyplot as plt
import math

##########################
#Segundo Trabalho de PDI#
##########################


# DCT tipo II
# https://en.wikipedia.org/wiki/Discrete_cosine_transform#DCT-II
def MyDCT(vector):
  result = []
  factor = math.pi / len(vector)
  for i in range(len(vector)):
    soma = 0.0
    for (j, val) in enumerate(vector):
      soma += val * math.cos((j + 0.5) * i * factor)
    result.append(soma)
  return result


def pegaPixel(imagem, i, j):
  width, height = imagem.size
  if((i > width) or (j > height)):
    return None
  pixel = imagem.getpixel((i, j))
  return pixel

def pegaLinhaPixel(imagem, row):
  width, height = imagem.size
  pixel = []
  if((row > width or row < 1):
    return None
  for i in range(height):
    pixel.append(imagem.getpixel((row, i)))
  return pixel

def pegaColunaPixel(imagem, col):
  width, height = imagem.size
  pixel = []
  if((col > height or col < 1):
    return None
  for i in range(width):
    pixel.append(imagem.getpixel((i, col)))
  return pixel

def abreImagem(destino):
  imagem = Image.open(destino)
  return imagem


def salvaImagem(imagem, destino):
  imagem.save(destino, 'png')

def criaImagem(i, j):
  imagem = Image.new("RGB", (i, j))
  return imagem

if __name__ == "__main__":

  fileInput = sys.argv[1]
  fileOutput = sys.argv[2]

  # while(True):
  imagem = abreImagem(fileInput)

    # imagem = abreImagem(fileInput)
  #   MenuSelect = input(
  #   " _____                                           _          ____  _     _ _       _      _        _                           \n"
  #   + "|  _  |___ ___ ___ ___ ___ ___ ___ _____ ___ ___| |_ ___   |    \|_|___|_| |_ ___| |   _| |___   |_|_____ ___ ___ ___ ___ ___ \n"
  #   + "|   __|  _| . |  _| -_|_ -|_ -| .'|     | -_|   |  _| . |  |  |  | | . | |  _| .'| |  | . | -_|  | |     | .'| . | -_|   |_ -|\n"
  #   + "|__|  |_| |___|___|___|___|___|__,|_|_|_|___|_|_|_| |___|  |____/|_|_  |_|_| |__,|_|  |___|___|  |_|_|_|_|__,|_  |___|_|_|___|\n"
  #   + "                                                                   |___|                                     |___|            \n\n\n\n"
  #   + "\t+---+-------------------------------------------------------+\n"
  #   + "\t|   |           Digite o numero da opção desejada           |\n"
  #   + "\t+---+-------------------------------------------------------+\n"
  #   + "\t| 1 |                                                       |\n"
  #   + "\t| 2 |                                                       |\n"
  #   + "\t| 3 |                                                       |\n"
  #   )
  #   if(MenuSelect == '1'):
  #     break
  #   elif(MenuSelect == '0'):
  #     break
