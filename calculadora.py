while True:
    import math

    print("Esolha um número em Decimal| Binário| Octal| Hexadecimal para converter:")
    print("_________________________________________________________________________MENU___________________________________________________________")

    num_convert = int(input("Digite uma das Opções:  1 - Binário para Decimal| 2 - Binário para Octal| 3- Binário para Hexadecimal| 4- Octal para Binário| 5 - Octal para Decimal| 6 - Octal para Hexadecimal| 7 - Hexadecimal para Decimal| 8 - Hexadecimal para Binário| 9 - Hexadecimal para Octal| 10 - Decimal para Binário| 11 - Decimal para octal| 12 - Decimal para Hexadecimal| 13 para Sair: "))

    if num_convert == 13:
        break
    elif num_convert == 1:
        binario_decimal = input("Digite o valor em binário para converter em um número decimal: ")
        valor_convertido = int(binario_decimal, 2)
        print("O valor em decimal é:", valor_convertido)
    elif num_convert == 2:
        binario_octal = input("Digite o valor em binário para converter em um número octal: ")
        valor_convertido = oct(int(binario_octal, 2))[2:]# esse [2:] remove os dois primeros caracteres do númewro que pode ser octl, hexadecimal e por aí vai...
        print("O valor em octal é:", valor_convertido)
    elif num_convert == 3:
        binario_hex = input("Digite o valor em binário para converter em um número hexadecimal: ")
        valor_convertido = hex(int(binario_hex, 2))[2:]#aqui tbm
        print("O valor em hexadecimal é:", valor_convertido)
    elif num_convert == 4:
        octal_binario = input("Digite o valor em octal para converter em um número binário: ")
        valor_convertido = bin(int(octal_binario, 8))[2:]#aqui tbm
        print("O valor em binário é:", valor_convertido)
    elif num_convert == 5:
        octal_decimal = input("Digite o valor em octal para converter em um número decimal: ")
        valor_convertido = int(octal_decimal, 8)
        print("O valor em decimal é:", valor_convertido)
    elif num_convert == 6:
        octal_hex = input("Digite o valor em octal para converter em um número hexadecimal: ")
        valor_convertido = hex(int(octal_hex, 8))[2:]#aqui tbm
        print("O valor em hexadecimal é:", valor_convertido)
    elif num_convert == 7:
        hex_decimal = input("Digite o valor em hexadecimal para converter em um número decimal: ")
        valor_convertido = int(hex_decimal, 16)
        print("O valor em decimal é:", valor_convertido)
    elif num_convert == 8:
        hex_binario = input("Digite o valor em hexadecimal para converter em um número binário: ")
        valor_convertido = bin(int(hex_binario, 16))[2:]#aqui tbm
        print("O valor em binário é:", valor_convertido)
    elif num_convert == 9:
        hex_octal = input("Digite o valor em hexadecimal para converter em um número octal: ")
        valor_convertido = oct(int(hex_octal, 16))[2:]# aq tbm
        print("O valor em octal é:", valor_convertido)
    elif num_convert == 10:
        decimal_binario = int(input("Digite o valor em decimal para converter em um número binário: "))
        valor_convertido = bin(decimal_binario)[2:]# aqui tbm
        print("O valor em binário é:", valor_convertido)
    elif num_convert == 11:
        decimal_octal = input("Digite o valor em decimal para converter em um número octal: ")
        valor_convertido = int(decimal_octal, 8)
        print("O valor em octal é:", valor_convertido)
    elif num_convert == 12:
        decimal_hex = input("Digite o valor em decimal para converter em um número hexadecimal: ")
        valor_convertido = hex(int(decimal_hex, 10)) [2:] # aq tbm , funão hex retorna o número em sua base que é hexadecimal
        print("O valor em hexadecimal é:", valor_convertido)
    else :
        print("Digite uma opção válida!")