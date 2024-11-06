def empilhamento(c):
    pilha=[]
    for p in c :
        if p == '(' :
            pilha.append(p)

        elif p == ')' :
            if len(pilha) != 0 :
                pilha.pop()
            else :
                return "Não balanceado"

    if len(pilha) == 0 :
        return "Balanceado"
    else:
        return "Não balanceado"
    
print(empilhamento("(()"))
print(empilhamento("(()))"))
print(empilhamento("(())"))
print(empilhamento("(()))"))
print(empilhamento("()()()"))
