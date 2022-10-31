

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
    

def verificar_operador(expressao):
    i = len(expressao) - 1
    while i >= 0:
        x = expressao[i]
        if x == '+' or x == '-':
            return i

        else:
            if "+" not in expressao and "-" not in expressao:
                if x == '*' or x == '/':

                    return i
        i -= 1
def montando_arvore(expressao):
    i = verificar_operador(expressao)
    if i is not None:
        raiz = expressao[i]
        filho_esquerdo = expressao[0:i]
        filho_direito = expressao[i + 1]
        
        root = Node(raiz)
        root.left = Node(filho_esquerdo)
        root.rigth = Node(filho_direito)

        montando_arvore(filho_esquerdo)
        montando_arvore(filho_direito)

expressao = 'A*B+C*D-E'
montando_arvore(expressao)






