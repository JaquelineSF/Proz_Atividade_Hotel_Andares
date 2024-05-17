import time

andarInicial = 1 
andarFinal = 20

print("Contando os andares...")
for i in range(andarInicial, andarFinal + 1):
    if i != 13:  # Verifica se o número não é 13
        print(i)
        time.sleep(1)
print("Fim da contagem!")

