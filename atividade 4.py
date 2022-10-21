

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None


expressao = 'A-B+C*D*E'
def verificar_operador(expressao):
        i = len(expressao) - 1
        while i >= 0:
            x = expressao[i]
            if x == '+' or x == '-':
                return i
               
            elif x == '*' or x == '/':
        
                return i
            i -= 1


i = verificar_operador(expressao)
print(i)
raiz = expressao[i]
print(raiz)
filho_esquerdo = expressao[0:i]
filho_direito = expressao[i+1]

root = Node(raiz)
root.left = Node(filho_esquerdo)
root.rigth = Node(filho_direito)

#criar uma função que use o verificador, para construir a arvore
#Separar em dois while, pra mais e menos e pra vezes e div
