#Python Encryption Experiment

key = 1

def encrypt(filename):
    def run(input):
        output = []
        for x in range (len(input)):
            output.append(ord(input[x])*key)
        return(output)
    f = open(filename, 'r')
    list = run(f.read())
    f.close()
    with open(filename, 'w') as b:
        for listitem in list:
            b.write('%s\n' % listitem)

def decrypt(filename):
    def decrypt(input):
        output = ''
        for x in range (len(input)):
            output = output + chr( int( int(input[x])/(key) ) )
        return(output)
    encrypted = []
    with open(filename, 'r') as b:
        for line in b:
            currentPlace = line[:-1]
            encrypted.append(currentPlace)
    f = open(filename, 'w')
    f.write(decrypt(encrypted))
    f.close()

print()
if int(input('Would you like to encrypt(1) or decrypt(2)?: ')) == 1:
    path = str(input('File Path:? '))    
    key = int(input('Encryption Key?: '))
    encrypt(path)
    print()
    print('Done')
    print()
else:
    path = str(input('File Path:? '))    
    key = int(input('Encryption Key?: '))
    decrypt(path)
    print()
    print('Done')
    print()