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

  imagem = abreImagem("lena.jpg")
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

  
  SzigzagList = []
  zigzagList = zigzag(height,width,FullDCT)
  for i in zigzagList: #fazendo join pra juntar td
    SzigzagList +=i
  # print(SzigzagList)


  n = 2
  for i in range(len(FullDCT)):
    for j in range(len(FullDCT[0])):
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
      pixel[j,i] = (int(iDCT[j][i]/10000),int(iDCT[j][i]/10000),int(iDCT[j][i]/10000))
  salvaImagem(newImage,str(n)+"_output.jpg")


  plt.ylabel('DCT Row X Col')
  plt.plot(SzigzagList)
  plt.show()
