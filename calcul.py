while True:
    chiffres = input("Entre les chiffres séparés par / (ou 'q' pour quitter) : ").split("/")
    if chiffres[0].strip().lower() == "q":
        break
    for c in chiffres:
        valeur = (1e-3 * float(c)) / 1.008
        print(f"({c}) → {valeur:.4e}")
