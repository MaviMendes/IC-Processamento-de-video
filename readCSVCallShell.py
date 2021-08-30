# Programa que le cvs file, chama shell script para cortar o video by frame
# Maria Vitoria - 09/08/2021 - versao 1

import pandas as pd # read csv
import itertools # zip
import subprocess # chamar shell script e passar parametros
import sys # stdout e stderr

# ABRIR ARQUIVO E REALIZAR A LEITURA
data = pd.read_csv('lista.csv',
usecols=['nome_entrada','nome_saida','Frame_inicio','Frame_chao'],
dtype={'nome_entrada':str,'nome_saida':str,'Frame_inicio':str,'Frame_chao':str})

# OBTER UMA LISTA COM CADA ATRIBUTO NECESSARIO
videoOriginal = data['nome_entrada'].to_list()
videoSaida = data['nome_saida'].to_list()
frameInicial = data['Frame_inicio'].to_list()
frameFinal = data['Frame_chao'].to_list()

"""
print('videoOriginal: ',videoOriginal)
print('videoSaida',videoSaida)
print('frameInicial: ',frameInicial)
print('frameFinal',frameFinal)

"""
# LOOP QUE VAI ABRIR CADA VIDEO E CHAMAR CUTBETWEEN

for (nomeInicialVideo,nomeFinalVideo,frameStart,frameEnd) in zip(videoOriginal,videoSaida,frameInicial,frameFinal):
    print("Iniciando processo: ",nomeInicialVideo,nomeFinalVideo,frameStart,frameEnd)
    saida = subprocess.run(['./cutByFrame.sh',nomeInicialVideo,nomeFinalVideo,frameStart,frameEnd], capture_output=True,text=True)
    print('stdout: ',saida.stdout)
    print('stderr: ', saida.stderr)

"""
teste - corta apenas 1 video

saida = subprocess.run(['./cutByFrame.sh',videoOriginal[3],videoSaida[3],frameInicial[3],frameFinal[3]], capture_output=True,text=True)
print('stdout: ',saida.stdout)
print('stderr: ', saida.stderr)

"""
