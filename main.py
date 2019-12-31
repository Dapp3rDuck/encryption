
# Encryption
def run(input):
    output = []
    for x in range(len(input)): output.append(ord(input[x])*key)
    return output

# Decryption
def solve(input):
    return ''.join([
        chr(int(input[i])/int(key)) for i in range(len(input))
    ])

def encrypt(fname):
    f = open(fname, 'r')
    output = run(f.read())
    f.close()
    with open(fname, 'w') as b:
        for l in output: b.write('%s\n' % l)

def decrypt(fname):
    with open(fname, 'r') as b:
        encrypted = [l[:-1] for l in b]     
    f = open(filename, 'w')
    f.write(''.join([
        chr(int(input[i])/int(key)) for i in range(len(encrypted))
    ]))
    f.close()

path = str(input('File Path (relative): '))
key = int(input('Encryption Key (integer): '))

if int(input('\nEncrypt (1) or decrypt (2)?: ')) == 1: encrypt(path)
else: decrypt(path)

print('\nDone\n')
