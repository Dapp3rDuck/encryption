#Python Encryption Experiment
def decrypt(input): return ''.join([chr(int(input[x])) for x in range(len(input))])

b = open('input.txt', 'r')
encrypted = [line[:-1] for line in b]
b.close()

f = open("input.txt", 'w')
f.write(decrypt(encrypted))
f.close()
