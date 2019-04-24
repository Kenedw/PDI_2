#!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
from PIL import Image
import matplotlib.pyplot as plt
import math

##########################
#Segundo Trabalho de PDI#
##########################

def MyDCT(vector):
  result = []
  factor = math.pi / len(vector)
  for i in range(len(vector)):
    soma = 0.0
    for (j, val) in enumerate(vector):
      soma += val * math.cos((j + 0.5) * i * factor)
    result.append(soma)
  return result

def InvMyDCT(vector):
	result = []
	factor = math.pi / len(vector)
	for i in range(len(vector)):
		soma = vector[0] / 2.0
		for j in range(1, len(vector)):
			soma += vector[j] * math.cos(j * (i + 0.5) * factor)
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
  if(row > width or row < 0):
    return None
  for i in range(height):
    pixel.append(imagem.getpixel((row, i)))
  return pixel

def pegaColunaPixel(imagem, col):
  width, height = imagem.size
  pixel = []
  if(col > height or col < 0):
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

def cinzaScale(imagem):
  return imagem.convert('L')

def trans(mat):
  result = []
  for n in range(len(mat[0])):
    aux = []
    for m in range(len(mat)):
      aux+=[mat[m][n]]
    result.append(aux)
  return result

def zigzag(rows,columns,matrix):
  solution=[[] for i in range(rows+columns-1)] 
  for i in range(rows): 
    for j in range(columns): 
      soma=i+j 
      if(soma%2 ==0): 
        solution[soma].insert(0,matrix[i][j]) 
      else: 
        solution[soma].append(matrix[i][j])
  return solution 

if __name__ == "__main__":

  # fileInput = sys.argv[1]
  # fileOutput = sys.argv[2]
  imagem = abreImagem("fox.jpg")
  imagem = cinzaScale(imagem)
  width, height = imagem.size
  ParcialDCTCol = []
  ParcialDCTRow = []
  FullDCT = []
  iDCT = []
  LinhasiDCT = []
  parinv = []

  #DCT
  for n in range(width): #Primeira DCT (DCT da Linha)
    RowVetPixel = pegaLinhaPixel(imagem,n)
    ParcialDCTRow.append(MyDCT(RowVetPixel))
  ParcialDCTCol = trans(ParcialDCTRow)
  for i in range(height):
    FullDCT.append(MyDCT(ParcialDCTCol[i]))  #Segunda DCT (DCT da coluna)

  #filtro n
  # SzigzagList = []
  # zigzagList = zigzag(height,width,FullDCT)
  # for i in zigzagList:
  #   SzigzagList +=i
  # print(SzigzagList)
  n = 200
  for i in range(width):
    for j in range(height):
      if(i+j>n):
        FullDCT[j][i] = 0

  # inversa DCT
  for i in range(height):
    parinv.append(InvMyDCT(FullDCT[i]))
  LinhasiDCT = trans(parinv)
  for i in range(width):
    iDCT.append(InvMyDCT(LinhasiDCT[i]))

  newImage = criaImagem(width,height)
  pixel = newImage.load()
  for i in range(height):
    for j in range(width):
      pixel[j,i] = (int(iDCT[j][i]/1000),int(iDCT[j][i]/1000),int(iDCT[j][i]/1000))
  salvaImagem(newImage,"test.jpg")


  plt.ylabel('DCT Row X Col')
  plt.plot(FullDCT)
  plt.show()


  # while(True):
  #   imagem = abreImagem(fileInput)
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
