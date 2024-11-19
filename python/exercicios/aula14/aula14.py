a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
#string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
#formato = string.format(
#    nome1=a, nome2=b, nome3=c
#)
print("O professor utiliza esse modelo de cima, mas eu prefiro usar esse:")
formato = (f"a={a}, b={b}, c={c}")

print(formato)