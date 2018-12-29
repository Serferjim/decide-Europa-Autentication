#Los emails se escriben en las líneas pares y el pass en las impares
#Por norma, el primer email y pass es el de decide-europa
def ficheroCorreoContraseña():
    emails = []
    passwords = []
    with open("emails.txt") as f:
        lines = f.readlines()
        for i in range (len(lines)-1):
            data = (lines[i].split(" = "))[1]
            if(i%2 == 0):
                emails.append(data)
            else:
                passwords.append(data)
    f.close()
    return (emails, passwords);


if __name__ == '__main__':
    ficheroCorreoContraseña()
