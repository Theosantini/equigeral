# Simular modelo EGC CAP 3
import numpy as np
import sys
from scipy.optimize import *

nNumeroBens = 2

nNumeroFatores = 2

nNumeroDomicilios = 2

nReceitaGoverno = 1

j = nNumeroBens

nNumeroVariaveis= nNumeroBens+nNumeroFatores+nNumeroDomicilios+nReceitaGoverno

mDotacao = np.array([[30, 20], [20, 5]])

mBeta = np.array([[0.3, 0.6], [0.7, 0.4]])

mCoefTecnicos = np.array([[0.2, 0.5], [0.3, 0.25]])

mAlfa = np.array([[0.8, 0.4], [0.2, 0.6]])

vVa = np.array([0.5, 0.25])

# tTau é taxa de imposto na produção setorial

tTau = np.array([0.0, 0.0])

# tTrf é taxa de transferência de renda para consumidores

tTrf = np.array([0.5, 0.5])

def Modelo(vValores):
    vPrecosBens= vValores[0:nNumeroBens]
    vProducao = vValores[nNumeroBens:(nNumeroBens*2)]
    vPrecosFatores = vValores[(nNumeroBens*2):(nNumeroBens*2)+nNumeroFatores]
    vReceitaGov = vValores[(nNumeroBens*2)+nNumeroFatores:]

    mEquacoes = np.empty(nNumeroVariaveis)
    vApoio = np.dot(vPrecosFatores, mDotacao)
    # Equação de consumo
    for n in range(nNumeroBens):
        vApoio1 = vApoio + tTrf[n]*vReceitaGov
        vApoio2 = np.dot(mBeta[n,:],vApoio1.T)
        vApoio3 = vApoio2 / vPrecosBens[n]
        vApoio4 = np.dot(mCoefTecnicos[n,:],vProducao.T)
        vApoio5 = vApoio3 + vApoio4 - vProducao[n]
        mEquacoes[n] = vApoio5
    # Equação oferta e demanda de fatores
    for k in range(nNumeroFatores):
        vAux=np.zeros(nNumeroBens)
        vApoio2 = np.sum(mDotacao[k,:])
        nDivisao= vPrecosFatores[1]/vPrecosFatores[0]
        if k ==1:
            nDivisao= 1/nDivisao
        for p in range(nNumeroBens):
            vApoio1= vProducao[p] * vVa[p]
            if k==0:
                vApoio3 = mAlfa[0,p] * nDivisao **(mAlfa[1,p])
            else:
                vApoio3 = mAlfa[1, p] * nDivisao ** (mAlfa[0, p])

            vAux[p] = vApoio3 * vApoio1

        mEquacoes[nNumeroBens+k] = np.sum(vAux) - vApoio2
    # Equação de produção (lucro zero)
    nAux1 = 0
    for n in range(nNumeroBens):
        nAux = 1
        for k in range(nNumeroFatores):
            x = vPrecosFatores[k] ** mAlfa[k,n]
            nAux = nAux * vPrecosFatores[k] ** mAlfa[k,n]

        nAux2 = 0
        for l in range(nNumeroBens):
            nAux2 = nAux2 + vPrecosBens[l]*mCoefTecnicos[l, n]

        mEquacoes[(nNumeroBens+nNumeroFatores)+n] = (vPrecosBens[n] - nAux * vVa[n] + nAux2)*(1+tTau[n])


        nAux1 = nAux1 + vProducao[n] * (nAux * vVa[n] + nAux2) * tTau[n]

    mEquacoes[nNumeroBens + nNumeroFatores + nNumeroDomicilios] = np.sum(nAux1) - vReceitaGov

    return mEquacoes

if __name__ == '__main__':
    vValoresIniciais = np.array([1, 0.8, 2, 2, 0.8, 0.8, 0.8])
    vResult = fsolve(Modelo, vValoresIniciais)
    vPrecosBens= vResult[0:nNumeroBens]
    print("Preços dos Bens", vPrecosBens )
    vProducao = vResult[nNumeroBens:(nNumeroBens*2)]
    print("Produção", vProducao )
    vPrecosFatores = vResult[(nNumeroBens*2):nNumeroBens*3]
    print("Preços dos Fatores", vPrecosFatores )
    vReceitaGov = vResult[(nNumeroBens+nNumeroFatores+nNumeroDomicilios):]
    print("Receita do Governo", vReceitaGov)
    print("End")
    sys.exit(0)




