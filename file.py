s = 'The filename is \'file.py\''
print (s.rjust(50))

#main start
f = file('test.txt','w')
f.write('im a boy')
f.close()

f = file('test.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print (line)
f.close()