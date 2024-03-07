import io
import tracemalloc

## Escrevendo e lendo no buffer
buffer = io.StringIO()

print('Escrevendo no buffer')
buffer.write('Este é conteúdo do buffer')

buffer.seek(0)
print('Lendo do Buffer')
print(buffer.read())

buffer.close()


tracemalloc.start()
## Escrevendo do buffer no arquivo
buffer = io.StringIO()
arquivo = open('arquivo_buffer.txt', 'w', encoding='utf-8')
print('Before write', tracemalloc.get_traced_memory())

print('Operação exaustiva de I/O')
for i in range(1000):
    buffer.write(f'Linha: {i}\n')
    if i % 100 == 0:
        print('In Write', tracemalloc.get_traced_memory())
        print('Escrevendo no arquivo')
        buffer.seek(0)
        arquivo.write(buffer.getvalue())
        buffer.truncate()
        arquivo.flush()

arquivo.write(buffer.getvalue())
buffer.truncate()
arquivo.flush()

print('Before close', tracemalloc.get_traced_memory())
buffer.close()
arquivo.close()
print('After close', tracemalloc.get_traced_memory())
tracemalloc.start()


## Lendo do arquivo no buffer
""" Arquivo - arquivo_buffer.txt
Linha 1
Linha 2
Linha 3
...
Linha N
"""
arquivo = open('arquivo_buffer.txt', 'r', encoding='utf-8')
buffer = io.StringIO()

while True:
    chuck = arquivo.read(1024)
    print(len(chuck))
    if not chuck:
        break
    ## Process chuck
    buffer.write(chuck)

buffer.seek(0)
print('Lendo buffer')
print(buffer.read())
arquivo.close()
buffer.close()


## Buffer linha por linha
""" Arquivo - arquivo_buffer.txt
Linha 1
Linha 2
Linha 3
...
Linha N
"""
arquivo = open('arquivo_buffer.txt', 'r', encoding='utf-8')
buffer = io.StringIO()

while True:
    chuck = arquivo.readline()
    if chuck == '':
        break
    ## Process chuck
    buffer.write(chuck)

buffer.seek(0)
print('Lendo buffer')
print(buffer.read())
arquivo.close()
buffer.close()


## Copiar um arquivo de texto usando buffer
""" Arquivo - origem.txt
Este é o texto do arquivo de origem
"""
arquivo_origem = open('origem.txt', 'r', encoding='utf-8')
arquivo_destino = open('arquivo_destino.txt', 'w', encoding='utf-8')

while True:
    chuck = arquivo_origem.read(1024)
    if not chuck:
        break
    arquivo_destino.write(chuck)

arquivo_destino.close()
arquivo_origem.close()


## Copiar um arquivo binário usando buffer
""" Arquivo - origem.txt
Este é o texto do arquivo de origem
"""
arquivo_origem = open('logo.png', 'rb')
arquivo_destino = open('arquivo_destino.png', 'wb')

while True:
    chuck = arquivo_origem.read(1024)
    if not chuck:
        break
    arquivo_destino.write(chuck)

arquivo_destino.close()
arquivo_origem.close()
