#Python Encryption Experiment
def decrypt(input):
    output = ''
    for x in range (len(input)):
        output = output + chr(int(input[x]))
    return(output)

encrypted = []
with open('input.txt', 'r') as b:
    for line in b:
        currentPlace = line[:-1]
        encrypted.append(currentPlace)

f = open("input.txt", 'w')
f.write(decrypt(encrypted))
f.close()