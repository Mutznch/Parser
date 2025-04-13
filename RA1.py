# RA1
# Integrantes:
# Félix Augustus Motelevicz
# Gustavo Sampietro Rinaldi

import sys

# Operadores válidos
CONSTANTE = ["true", "false"]
ABREPAREN = "("
FECHAPAREN = ")"
OPERATORUNARIO = "\\neg"
OPERATORBINARIO = ["\\wedge", "\\vee", "\\rightarrow", "\\leftrightarrow"]

# Verifica se é uma proposição (ex: 1x, 2a3b, etc)
def PROPOSICAO(token):
    if not token or not token[0].isdigit(): return False
    return all(c.isdigit() or c.islower() for c in token)

# Função principal que verifica se uma expressão é válida
# FORMULA
def parse(tokens):
    if not tokens:
        return False, tokens

    token = tokens.pop(0)

    if token in CONSTANTE or PROPOSICAO(token):
        return True, tokens

    if token == ABREPAREN:
        if not tokens:
            return False, tokens
        operador = tokens.pop(0)

        # FORMULAUNARIA
        if operador == OPERATORUNARIO:
            valido, tokens = parse(tokens)
            if not valido or not tokens or tokens.pop(0) != FECHAPAREN:
                return False, tokens
            return True, tokens

        # FORMULABINARIA
        elif operador in OPERATORBINARIO:
            valido1, tokens = parse(tokens)
            valido2, tokens = parse(tokens)
            if not valido1 or not valido2 or not tokens or tokens.pop(0) != FECHAPAREN:
                return False, tokens
            return True, tokens

        else:
            return False, tokens

    return False, tokens

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python RA1.py <arquivo.txt>")
        exit(1)
    
    expressoes = []
    with open(sys.argv[1]) as f:
        try: 
            n_expr = int(f.readline())
        except: 
            print("Arquivo selecionado inválido")
            exit(1)
        
        for _ in range(n_expr):
            expressoes.append(f.readline())

    for expr in expressoes:
        tokens = expr.strip().split()
        valido, resto = parse(tokens)
        if valido and not resto:
            print("valida")
        else:
            print("inválida")
