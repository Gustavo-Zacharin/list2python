name = input("Digite seu nome completo ou uma frase: ")

f = "aeiouAEIOU"

count = 0

for vogal in name:
    if vogal in f:
        count += 1
print(f"Sua frase ou nome tem {count} vogais")    