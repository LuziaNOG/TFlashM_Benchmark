# TFlashM_Benchmark
Benchmark desenvolvido na Disciplina de Analise de Desempenho-PCOMP UFC-Quixadá 2021

O TflashM benckmark é um benchmark para análise de desempenho de dispositivos de memória flash, especialmente pendrive, sua análise é realizada com base na velocidade de escrita e leitura. É usado para teste da escrita 50MB de carga de trabalho multiplicado pela quantidade de repetição. A leitura também recebe uma quantidade de repetição. A quantidade de repetição é a mesma para os testes de leitura e de escrita e é solicitada pelo programa durante a execução.

Manual de instalação:
1- O arquivo foi escrito na linguagem de programação python e para executar o mesmo é necessário que a máquina tenha o python3 instalado, caso não tenha instalado utilizar o seguinte comando para instalar: sudo apt-get install python3  
2- O arquivo utiliza algumas bibliotecas, caso não estejam instaladas é necessário que sejam instaladas, caso contrário irá da erro ao rodar o programa. As bibliotecas são as seguintes:
- subprocess
- matplotlib

Execução:
1.Baixe o scrip.py na maquina;
2.Pluge o pendrive via usb que deseja testar na máquina;
3.Utilize o comando para execução: python3 script.py;
4.Os parâmetros são pedidos durante a execução;
5.Caso gere erro, verifique se a máquina possui todas as bibliotecas instaladas e se o pendrive esta sendo reconhecido.
