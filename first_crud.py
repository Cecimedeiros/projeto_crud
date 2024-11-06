import json
import os
from time import sleep
from sec_crud import main2
from third_crud import main3

caminho_arquivo= os.path.join(os.path.dirname(__file__), 'json_abrigo.json')

def carregar_abrigo():
    if not os.path.exists(caminho_arquivo):
        with open (caminho_arquivo,'w', encoding='utf-8') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, indent=3)
    with open (caminho_arquivo, 'r', encoding='utf-8') as arquivojson_aberto:
        return json.load(arquivojson_aberto)

def cadastrar_abrigo (nome, endereco, porte_animal, contato):
    abrigos= carregar_abrigo()
    abrigos.append({'nome': nome, 'endereco': endereco, 'porte_animal': porte_animal,'contato':contato})
    with open (caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
        json.dump (abrigos, arquivojson_aberto, indent=3, ensure_ascii=False)
    print ("\n O abrigo foi cadastrado!")

def listar_abrigo():
    abrigos= carregar_abrigo()
    if not abrigos:
        print (" Nenhum abrigo cadastrado! ")
        return
    for abrigo in abrigos:
        print (f" Nome: {abrigo['nome']}, \n Endereço: {abrigo['endereco']},\n Porte do animal: {abrigo['porte_animal']}, Contato: {abrigo['contato']} ")
           
def atualizar_abrigo (nome_antigo, novo_nome, novo_ende, novo_porte_animal, novo_contato):
    abrigos= carregar_abrigo()
    abrigo_encontrado = False
    for abrigo in abrigos:
        if abrigo['nome'] == nome_antigo:
            abrigo['nome']=novo_nome
            abrigo['endereco']= novo_ende
            abrigo['porte_animal']= novo_porte_animal
            abrigo['contato']=novo_contato
            abrigo_encontrado = True
            break
    with open (caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto: 
        json.dump(abrigos, arquivojson_aberto,indent=3, ensure_ascii=False)
    if abrigo_encontrado:
        print (" Informações sobre o abrigo atualizadas!")
    else:
        print("Abrigo não encontrado!")

def excluir_abrigo (nome):
    abrigos=carregar_abrigo()
    nome=nome.lower ()
    abrigo_encontrado= False
    
    for abrigo in abrigos:
        if abrigo['nome'].lower ()==nome:
            abrigos.remove (abrigo) 
            abrigo_encontrado= True
            print (" Dados do abrigo excluídos! ") 
            break
    if not abrigo_encontrado:
        print(" Abrigo não existente!") 
    with open (caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
        json.dump(abrigos, arquivojson_aberto, indent=3, ensure_ascii=False)

def buscar_abrigos(nome):
    abrigos=carregar_abrigo ()
    nome = nome.lower ()
    abrigo_encontrado= False
    for abrigo in abrigos:
        if abrigo['nome'].lower () == nome:
            print (f" Nome: {abrigo['nome']},\n Endereço: {abrigo['endereco']},\n Porte do animal: {abrigo['porte_animal']},\n Contato: {abrigo['contato']} ")    
            abrigo_encontrado= True
    if not abrigo_encontrado:
        print (" Nenhum abrigo encontrado!")

def main1 ():
    while True: 
        print ("\n  <<-------- PLATAFORMA \"EM BUSCA DE UM LAR\" -------->>")
        print ("\n Olá, somos uma plataforma de gerenciamento de animais para adoção. \n Conectamos você com abrigos, animais e também recebemos voluntários para nos ajudar nessa causa especial! \n Vamos explorar a plataforma?! " )
        op= int(input ("\n Escolha uma opção abaixo: \n 1 - Quero conectar com um abrigo \n 2 - Quero me tornar voluntário(a)/ Sou voluntário(a) da plataforma \n 3 - Quero adotar um animal  \n 4 - Sair da plataforma \n O que deseja fazer no momento? "))
  
        if op== 1: 
            opcao=input("\n Dentre as seguintes opções:  \n 1- Cadastrar um abrigo \n 2- Vizualizar informações do abrigo \n 3- Atualizar informações sobre o abrigo \n 4- Excluir informações sobre o abrigo \n 5- Listar os abrigos existentes \n 6- Voltar ao menu inicial \n O que você deseja fazer agora? ")
            match (opcao):
                case "1": 
                    while True:
                        print ("\n ->>> CADASTRAMENTO DE ABRIGOS PARA ANIMAIS <<<-")
                        print ("\n Para cadastrar um novo abrigo é preciso que responda as seguintes perguntas: ")
                        nome=input("\n Informe o nome do abrigo a ser cadastrado: ")
                        endereco= input ("\n Informe a localização do abrigo, o gerenciamento atende aos seguintes bairros: \n - Boa viagem \n - Casa Forte \n - Graças \n - Jaqueira \n - Torre \n - Várzea \n:")
                        porte_animal= input ("\n Informe o porte dos animais que esse abrigo é capaz de abrigar (pequeno - médio - grande): ")
                        while True:
                            try:
                                contato=input ("\n Informe o contato do abrigo: ")
                                break
                            except ValueError:
                                print("Por favor, digite apenas números!")
                        cadastrar_abrigo(nome, endereco, porte_animal,contato)
                        
                        maisum= input ("\n Deseja cadastrar mais um abrigo (s/n) ?")
                        if maisum.lower() == "n":
                            break
                        elif maisum.lower() != 's' or maisum.lower != 'n':
                            print("Opção inválida!")
                        
                case "2": 
                    while True:
                        print ("\n ->-> BUSCA DE ABRIGOS PARA ANIMAIS <-<-")
                        nome=input("\n Informe o nome do abrigo a ser procurado: ")
                        buscar_abrigos(nome)
                        
                        maisum= input ("Deseja buscar mais um abrigo (s/n) ?")                      
                        if maisum.lower() == "n":
                            break
                        elif maisum.lower() != 's' or maisum.lower != 'n':
                            print("Opção inválida!")
                        
                case "3":
                    while True:
                        print ("\n -->>  ATUALIZAÇÃO DE DADOS DOS ABRIGOS <<--")
                        nome_antigo= input ("Informe o nome a ser atualizado (o nome antigo): ")
                        if nome_antigo==nome_antigo:
                            novo_nome= input ("Informe o novo nome: ")
                            novo_ende= input ("Informe o novo endereço do abrigo (podendo estar localizado em: Boa viagem - Casa Forte - Graças - Jaqueira - Torre - Várzea): ")
                            novo_porte_animal=input ("Informe o novo tipo de porte de animal que será abrigado pelo abrigo (pequeno - médio - grande): ")
                            novo_contato= input ("Informe o novo contato do abrigo: ")
                            atualizar_abrigo(nome_antigo, novo_nome, novo_ende, novo_porte_animal, novo_contato)
                            
                            maisum= input ("Deseja atualizar mais um abrigo (s/n) ?")
                            if maisum.lower() == "n":
                                break 
                            elif maisum.lower() != 's' or maisum.lower != 'n':
                                print("Opção inválida!")

                case "4":
                    while True:
                        print ("\n ------> EXCLUSÃO DE DADOS DOS ABRIGOS PARA ANIMAIS <------")
                        nome= input ("Qual o nome do abrigo você deseja excluir?")
                        excluir_abrigo(nome)
                        maisum= input ("Deseja excluir mais um abrigo (s/n) ?")
                        if maisum.lower() == "n" :
                            break
                        elif maisum.lower() != 's' or maisum.lower != 'n':
                            print("Opção inválida!")
                        
                case "5":
                    listar_abrigo()
                case "6":
                    print ("Voltando ao menu inicial...")
                    sleep (4)
                    main1()  
                case _: 
                    print ("Opção inválida! Tente novamente.")
        elif op==2:
            main2 ()
        elif op==3: 
            main3 ()
        elif op==4:  
            fim()
            break
        else: 
            print ("Opção inválida, tente novamente! ")
            main1()
def fim ():
    print ("Saindo da plataforma...")
    
if __name__ == "__main__":
    main1 ()
main1 ()