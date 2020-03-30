#Python Encryption Experiment
def decrypt(input): return ''.join([chr(int(input[x])) for x in range(len(input))])

with open('input.txt', 'r') as b: encrypted = [line[:-1] for line in b]
with open('input.txt', 'w') as f: f.write(decrypt(encrypted))
