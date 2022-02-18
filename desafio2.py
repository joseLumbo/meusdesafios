# Está funcionando:
def validar_letra_maiuscula(senha):
    count = 0
    for index, character in enumerate(senha):
        if character.upper() == senha[index] and senha[index] not in ('!@#$%^&()-+/123456789'):
            count += 1
    else:
        if count <= 0:
            print('Senha não contem letra maíuscula!')
        else:
            return validar_letra_minuscula(senha)

# funcionando:
def validar_letra_minuscula(senha):
    conta_minuscula = 0
    for k in list(senha):
        if k in ('qwertyuiopasdfghjklzxcvbnm'):
            conta_minuscula += 1

    if conta_minuscula <= 0:
        print('Senha não contem letra minuscula!')
    else:
        return validar_tamanho_senha(senha)


# funcionando:
def validar_tamanho_senha(senha):
    if len(senha) < 6:
        print('Sua senha é inferior a seis caracteres!')
    else:
        return validar_existencia_numero(senha)

# funcionando:
def validar_existencia_numero(senha):
    contar_numero = 0
    for k in list(senha):
        if k in set('0123456789'):
            contar_numero += 1
    if contar_numero <= 0:
        print('Senha não contem pelo menos um número!')
    else:
        return validar_caracter_especial(senha)


def validar_caracter_especial(senha):
    contar_caracter_especial = 0
    for caracter_especial in list(senha):
        if caracter_especial in ('!@#$%^&()-+/\'\\"'):
            contar_caracter_especial += 1
    if contar_caracter_especial <= 0:
        print('Senha não contem pelo menos um caracter especial!')
    else:
       
                
        print('Seja Bem Vindo !!!')


password = input('Digite sua senha: ')
validar_letra_maiuscula(password)