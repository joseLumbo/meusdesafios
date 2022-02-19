
#Essa função validará a existencia de letra maiúscula
def validar_maiuscula(senha):
    count = 0 #Contará a letra
    for index, character in enumerate(senha):#Itera sobre a senha
        #Vai verificar se existe letra maiúscula
        if character.upper() == senha[index] and senha[index] not in list('!@#$%^&()-+/123456789'):
            count += 1
    else:
        #Caso contador menor de zero implica que não contem nehuma letra maiúscula o contrario indica que existe
        if count <= 0:
            print('Senha não contem letra maíuscula!')
        else:
            return validar_minuscula(senha)

#Essa função validará a existencia de letra mainuscula
def validar_minuscula(senha):
    conta_minuscula = 0 #Contará a letra
    for k in list(senha):
        if k in list('qwertyuiopasdfghjklzxcvbnm'):
            conta_minuscula += 1
   #Caso contador menor de zero implica que não contem nehuma letra minuscula o contrario indica que existe
    if conta_minuscula <= 0:
        print('Senha não contem letra minuscula!')
    else:
        return validar_senha(senha)


#Esta função vai validar o tamanho
def validar_tamanho(senha):
    if len(senha) < 6:
        print('Sua senha é inferior a seis caracteres!')
    else:
        return validar_numero(senha)

# Validar a existencia de numeros
def validar_numero(senha):
    contar_numero = 0
    for k in list(senha):
        if k in set('0123456789'):
            contar_numero += 1
    if contar_numero <= 0:
        print('Senha não contem nenhum número!')
    else:
        return validar_especial(senha)

#Validadr a existencia de caracter especial
def validar_especial(senha):
    contar_especial = 0
    for caracter_especial in list(senha):
        if caracter_especial in ('!@#$%^&()-+/\'\\"'):
            contar_especial += 1
    if contar_especial <= 0:
        print('Senha não contem nenhum caracter especial!')
    else:
       
                
        print('Seja Bem Vindo !!!')


password = input('Digite sua senha: ')
validar_maiuscula(password)
