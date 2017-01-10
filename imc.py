#-*-coding:utf8;-*-

###########################
# Programa: Calculadora
#           de índice de
#           massa corporal
#
# Autor: Bruno L. Carli
#
###########################

#declara as variaveis

peso = input ("insira o seu peso: ")
altura = input ("insira sua altura: ")
imc = peso / (altura**2)
genero = input ( "insira seu genero, digite 1 para masculino e 2 para feminino: ")

#se é masculino:
if genero == 1:
    #mostra o resultado na tela
    print "seu imc é : " , imc
    # condições
    if imc <=20.7:
        print " você está abaixo do peso"
    elif imc <= 26.4:
        print "você está dentro do peso ideal"
    elif imc <= 27.8:
        print "você está ligeiramente acima do peso"
    elif imc <= 31.1:
        print "você está acima do peso "
    elif imc <= 36.9:
        print " obesidade grau I"
    elif imc <=39.9:
        print "obesidade grau II"
    else:
        print "obesidade grau III"
#se é feminino
elif genero == 2:
#mostra o resultado na tela
    print "seu imc é: " , imc
    # condições
    if imc <=19.1:
        print " você está abaixo do peso"
    elif imc <= 25.8:
        print "você está dentro do peso ideal"
    elif imc <= 27.3:
        print "você está ligeiramente acima do peso"
    elif imc <= 32.3:
        print "você está acima do peso "
    elif imc >= 32.4 and imc <= 36.3:
        print " obesidade grau I"
    elif imc <=39.9:
        print "obesidade grau II"
    else:
        print "obesidade grau III"