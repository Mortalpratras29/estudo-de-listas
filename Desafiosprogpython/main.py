responses = []
contador = 0

manha = []
tarde = []
noite = []

while contador < 5:
    r = input("Escolha um horário para a reunião: ")
    responses.append(r)
    contador += 1

for h in responses:
    if h == "manha":
        manha.append(h)
    elif h == "tarde":
        tarde.append(h)
    elif h == "noite":
        noite.append(h)

x = len(manha)
y = len(tarde)
z = len(noite)

if x > y and x > z:
    print(f"Reunião marcada para de manhã com {x} votos")
elif y > x and y > z:
    print(f"Reunião marcada para de tarde com {y} votos")
elif z > x and z > y:
    print(f"Reunião marcada para a noite com {z} votos")
