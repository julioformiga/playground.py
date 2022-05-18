from getpass import getpass


def rpsls_names(x=""):
    options = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
    if x != "":
        return options[x]
    return options


def rpsls(j1, j2):
    options = rpsls_names()
    if j1 == j2:
        return False
    if j1 > j2:
        j1, j2 = j2, j1
    if j1 == 0 and (j2 == 2 or j2 == 3):
        return options[j1]
    if j1 < j2 and (j1 + j2 == 5 or j1 + j2 == 7):
        return options[j1]
    if j1 < j2:
        return options[j2]


def rpsls_game():
    for idx, x in enumerate(rpsls_names()):
        print(f"[{idx}] - {x}")

    j1 = int(getpass("Escolha o primeiro movimento: "))
    while j1 < 0 or j1 > 4:
        print("Escolha inválida")
        j1 = int(getpass("Escolha o primeiro movimento: "))

    j2 = int(getpass("Escolha o segundo movimento: "))
    while j2 < 0 or j2 > 4:
        print("Escolha inválida")
        j2 = int(getpass("Escolha o segundo movimento: "))

    if not rpsls(j1, j2):
        print("\nEmpate!\nJogue novamente\n")
        rpsls_game()
    else:
        return print(f"\nDisputa {rpsls_names(j1)} x {rpsls_names(j2)}\nVencedor: ", rpsls(j1, j2))


rpsls_game()
