
# Encryption
def run(input): return [ord(input[i]) * key for i in range(len(input))]

def encrypt(fname):
    with open (fname, 'r') as b: output = run(b.read())
    with open(fname, 'w') as b: for l in output: b.write('%s\n' % l)

def decrypt(fname):
    with open(fname, 'r') as b: encrypted = [l[:-1] for l in b]
    with open(fname, 'w') as b: b.write(''.join([chr(int(input[i])/int(key)) for i in range(len(encrypted))]))

path, key = str(input('File Path (relative): ')), int(input('Encryption Key (integer): '))

if int(input('\nEncrypt (1) or decrypt (2)?: ')): encrypt(path)
else: decrypt(path)

print('\nDone\n')
