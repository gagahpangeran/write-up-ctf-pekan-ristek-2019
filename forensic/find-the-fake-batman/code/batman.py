f = open('../files/batman.png', 'rb').read()
g = open('../files/batmanplusplus.png', 'rb').read()
h = g[len(f):]

flag = open('../img/flag.png', 'wb')
flag.write(h)

flag.close()