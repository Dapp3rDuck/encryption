# key is not defined
def run(input): return [ord(input[x]*key for x in range(len(input))]

def encrypt(filename):
    with open(filename, 'r') as f: list = run(f.read())
    with open(filename, 'w') as b: for listitem in list: b.write('%s ' % listitem)
