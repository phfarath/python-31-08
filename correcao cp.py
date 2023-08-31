#correcao cp
import random 
import re 


#funcao sortear nomes 
def sortearnome(nomes):
    sorteio= random.randint(0,2)
    return nomes[sorteio]

#tupla dos funcionarios
funcionarios= ("x", "y", "z")

#adicionando vinhos 
vinhos= {
    "vinho1":{"nome":"Tinto", "valor":15, "estoque":10},
    "vinho2":{"nome":"Tinto", "valor":15, "estoque":10},
    "vinho3":{"nome":"Tinto", "valor":15, "estoque":10},
    "vinho4":{"nome":"Tinto", "valor":15, "estoque":10},
    "vinho5":{"nome":"Tinto", "valor":15, "estoque":10}

}
#mensagem de boas-vindas 
nomefunc= sortearnome(funcionarios)
print("bem-vindo a vinheria ")
print(f"o funcionario {nomefunc} vai te atender ")

#info do cliente e validacao 
erro=""
try:
    cliente= input ("digite seu nome: ")
    if re.search("\d", cliente): #procura por letras na variavel 
        erro= "nome nao pode conter digitos "
        raise ValueError
    cep =input("digite seu cep: ")
    if not re.search("^\d{5}-\d{3}$", cep): #no comeco 5 digitos no final 3 digitos 
        erro =" Cep invalido"
        raise ValueError
    anonasc= input("Digite seu ano de nascimento: ")
    if not re.search("\d{4}$"):
        erro= "ano de nascimento invalido"
        raise ValueError
    
    #informacoes do cliente
    infocli={
        'nome': cliente,
        'idade': int(anonasc),
        'cep': cep

    }
    #verificando idade
    idade= 2023- infocli['ano']
    if idade<18:
        print("voce é menor de idade")
    else:
        #exibindo vinhos 
        print("escolha um dos vinhos: ")
        for i in range (1,len(vinhos)+1,1):
            if vinhos[('vinho'+str(i))]['estoque']>0:#printa com o for i para print generico de todos os vinhos 
                print(f"{i} {vinhos[('vinho'+str(i))]['nome']} \t {vinhos[('vinho'+str(i))]['valor']}")

                #armazenando escolha e quant de vinhos 
                vinho = int(input())
                quant= int(input("digite quantos deseja desse vinho: "))

                #verificacao do estoque do vinho disponivel
                if ("vinho"+str(vinho) in vinhos ):
                    estoque= vinhos[('vinho'+str(vinho))]['estoque']
                    if estoque>0 and quant<=estoque:
                        #atualizando o estoque
                        novo_estoque= estoque - quant 
                        vinhos[('vinho'+str(i))]['estoque']=novo_estoque 
                        #registrando a compra
                        compra= []
                        compra.append(vinhos[('vinho'+str(i))]["nome"])
                        compra.append(vinhos[('vinho'+str(i))]["valor"])
                        compra.append(quant)
                        compra.append(vinhos[('vinho'+str(i))]["valor"]* quant)

                else:
                    print("nao possui vinhos suficientes")
                
                #exibindo dados da compra 
                print(":"*70)
                print(f'{cliente} foi um prazer atende-lo')
                msg= "vinho \t preco \t quant \tsubtotal \n"
                for i in compra:
                    msg+= str(i)+ "\t"
                    print(msg)
                    print("volte sempre ")
                    print(":"*70)
                    for i in range(1, len(vinhos)+1, 1):
                        vinho= vinhos[('vinho'+str(i))]['nome']
                        valor= vinhos[('vinho'+str(i))]['valor']
                        estoque = vinhos[('vinho'+str(i))]['estoque']
                        print(f"{vinho} \t {valor} \t {estoque}")
                        print(":"*70)


except(ValueError):
    print(erro)