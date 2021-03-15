import time
import os
import subprocess
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def main():
    def testEscrita(path):
        proc = subprocess.Popen(
            "dd if=/dev/zero of="+path+"/arquivo bs=5k count=10000", shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output, err = proc.communicate()
        r1 = err.decode("utf-8").split("\n")[2]
        t1 = r1.split(" ")[7]
        s1 = float(r1.split(" ")[9].replace(",", "."))
        unid = r1.split(" ")[10]
        if (unid == "kB/s"):
            s1 = s1/1024
        return t1, s1

    def testLeitura(path):
        proc = subprocess.Popen(
            "dd if="+path+"/arquivo of=/dev/null bs=4k", shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output, err = proc.communicate()
        r1 = err.decode("utf-8").split("\n")[2]
        t1 = r1.split(" ")[7]
        s1 = float(r1.split(" ")[9].replace(",", "."))
        unid = r1.split(" ")[10]
        if (unid == "GB/s"):
            s1 = s1*1024
        return t1, s1

    def selectPath():
        path = os.path.curdir
        if os.name == 'posix':
            result = subprocess.check_output("df")
            print(result.decode("utf-8"))
            path = input(
                "Por favor, informe o caminho do pendrive. Ex: /media/pendrive \n")
            rep = int(input("Informe a quantidade de repeticoes desejadas\n"))
        if os.name == 'nt':
            path = input("Entre com a Letra do Disco. Ex: D")
            path = path.split(":")

        if not os.path.exists(path):
            print('Caminho invalido')
            selectPath()

        return path, rep

    def plotarGraf(VelEsc, VelLeit):
        plt.plot(VelEsc, 'go')  # green bolinha
        plt.plot(VelEsc, 'k--', color='green')  # linha pontilha

        plt.plot(VelLeit, 'r^')  # red triangulo
        plt.plot(VelLeit, 'k--', color='red')  # linha tracejada

        plt.title("Grafico de Desempenho")
        plt.tick_params(axis='x', which='both', bottom=False,
                        top=False, labelbottom=False)
        red_patch = mpatches.Patch(color='red', label='Velocidade Leitura')
        green_patch = mpatches.Patch(color='green', label='Velocidade Escrita')
        plt.legend(handles=[red_patch, green_patch])

        plt.grid(True)
        plt.xlabel("Quantidade de repeticoes")
        plt.ylabel("MB/s")
        plt.show()

    path, rep = selectPath()
    i = rep
    ArrayVelEscrita = []
    ArrayVelLeitura = []
    tempoTotalE = 0
    tempoTotalL = 0
    
    while(i > 0):
        tempoE, velocidadeE = testEscrita(path)
        tempoTotalE = float(tempoE.replace(",", ".")) + tempoTotalE
        ArrayVelEscrita.append(velocidadeE)

        tempoL, velocidadeL = testLeitura(path)
        tempoTotalL = float(tempoL.replace(",", ".")) + tempoTotalL
        ArrayVelLeitura.append(velocidadeL)
        i -= 1
    
    EscritaMedia = np.mean(ArrayVelEscrita)
    LeituraMedia = np.mean(ArrayVelLeitura)
    VarianciaEscrita= np.var(ArrayVelEscrita)
    VarianciaLeitura = np.var(ArrayVelLeitura)

    print("################### BENCHMARK TFLASHM ###################")
    print("Tempo total de execução: ", (tempoTotalE + tempoTotalL), "s")
    print("Tempo Médio de Escrita: ", tempoTotalE/rep, "s")
    print("Tempo Médio de Leitura: ", tempoTotalL/rep, "s")
    print("Velocidade Média de Escrita: ", EscritaMedia, "MB/s")
    print("Velocidade Média de Leitura: ", LeituraMedia, "MB/s")

    print("#######################Valores por Teste#################")
    print("Velocidade Escrita - MB/s")
    print(ArrayVelEscrita)
    print("Variancia de Escrita: ", VarianciaEscrita)
    
    print("Velocidade de Leitura - MB/s")
    print(ArrayVelLeitura)
    print("Variancia de Leitura: ", VarianciaLeitura)
    print("##########################################################")

    print("Obs: Quanto menor a variância mais próximo os valores estão em relação a média.")

    plotarGraf(ArrayVelEscrita, ArrayVelLeitura)

if __name__ == "__main__":
    main()
