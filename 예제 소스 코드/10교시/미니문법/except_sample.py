try:
    f = open('noname.txt', 'r')
except OSError:
    pass
finally:
    print('cannot open the file')
