import os

filepaths = ["/path01/teste01.txt", "/teste01.txt"]

for i in filepaths:
    # Split do path e normaliza para caixa baixa.
    ext = os.path.splitext(i)[-1].lower()

    # Verifica igualdade com a extensao .txt
    if ext == ".txt":
        print (i, "É um arquivo .txt!")
    else:
        print (i, "Não é um arquivo .txt")