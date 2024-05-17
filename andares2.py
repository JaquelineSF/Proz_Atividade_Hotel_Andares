import time

andarInicial = 1
andarFinal = 20

print("Contando os andares...")
i = andarInicial
while i <= andarFinal:
    if i != 13:  # Verifica se o número não é 13
        print(i)
        time.sleep(1)
    i += 1
print("Fim da contagem!")

