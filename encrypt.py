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
            b.write('%s ' % listitem)