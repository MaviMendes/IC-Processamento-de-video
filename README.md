# IC-Processamento-de-video
Iniciação Científica PUB/USP realizada em 2020/2021

## [Projeto: Análise biomecânica do salto do goleiro de futebol na cobrança de pênalti: efeito de vídeo instrucional na melhora do desempenho](https://youtu.be/9SIwRSML4O8) 

Nome do Orientador: Paulo Roberto Pereira Santiago\
Nome da Aluna: Maria Vitória Ribeiro Mendes

A minha participação no projeto foi focada na parte da programação de códigos. Passei a auxiliar no projeto buscando o desenvolvimento de códigos em Python 3, e posteriormente em Shell Script, que otimizam, automatizam e tornam o processo independente de softwares pagos. Esse projeto é uma parte da pesquisa do bolsista Rafael Monteiro, que teve aprovação da FAPESP para uma IC.

###### readCSVCallShell.py 
Desenvolvido com o objetido de ler um arquivo .csv, extrair o título dos vídeos a serem cortados, bem como os frames de intervalo dos cortes. Otimizou o processo, considerando que é possível deixar que o computador realize todo o processo, em vez de uma pessoa abrir vídeo a vídeo e realizá-lo. ( Considere que no projeto em questão, temos qusse 500 vídeos). O shell script chamado pelo programa foi em parte desenvolvido pelo professor orientador.\

###### reconstrucao.py
Após os vídeos estarem cortados, é necessário realizar os processos de calibração, DLT e reconstrução 3D.
Manualmente, seria necessário abrir cada vídeo, printar os frames de interesse, e executar um programa python para cada etapa.
A fim de agilizar esse processo, *reconstrucao.py* lê a lista de vídeos e realiza as chamadas automaticamente. O usuário deve ser responsável apenas por printar os frames de interesse e marcar os pontos para a calibração.
Terminado o processamento de cada salto, é criada uma pasta com os arquivos resultantes.
(Em processo de melhora)





