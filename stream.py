## Escrevendo em um arquivo sem encoding e line break
import tracemalloc

nome_arquivo = 'texto_simples.txt'
arquivo = open(nome_arquivo, mode='w')

arquivo.write('Usando a funcao Write sem Line Break')
arquivo.writelines(['Uma linha', 'Duas linhas'])

arquivo.close()


## Escrevendo em um arquivo sem encoding e com line break
nome_arquivo = 'line_break.txt'
arquivo = open(nome_arquivo, mode='w')

arquivo.write('Usando a funcao Write com Line Break\n')
arquivo.writelines(['Uma linha\n', 'Duas linhas'])

arquivo.close()


## Escrevendo em um arquivo com encoding e line break
nome_arquivo = 'encoded.txt'
arquivo = open(nome_arquivo, mode='w', encoding='UTF8')

arquivo.write('Usando a função Write com Line Break\n')
arquivo.writelines(['Uma linha\n', 'Duas linhas'])

arquivo.close()


tracemalloc.start()
## Escrevendo em um arquivo grande
nome_arquivo = 'large_file.txt'
arquivo = open(nome_arquivo, mode='w')
print('Before write', tracemalloc.get_traced_memory())

for i in range(1000):
    arquivo.write(f'Linha: {i}\n')
    print('In Write', tracemalloc.get_traced_memory())

print('Before close', tracemalloc.get_traced_memory())
arquivo.close()
print('After close', tracemalloc.get_traced_memory())
tracemalloc.stop()


## Concatenando em um arquivo com encoding e line break
""" Arquivo - concatenar.txt
Texto pré existente no arquivo
"""
nome_arquivo = 'concatenar.txt'
arquivo = open(nome_arquivo, mode='a', encoding='UTF8')

arquivo.write('\nTexto adicionado no final do arquivo')

arquivo.close()


## Ler um arquivo com encoding e uma linha
""" Arquivo - leitura_simples.txt
Uma linha
"""
nome_arquivo = 'leitura_simples.txt'
arquivo = open(nome_arquivo, mode='r', encoding='UTF8')

print(nome_arquivo)
print(arquivo.read())
print('Read with limit')
print(arquivo.read(2))
print('Read Line')
print(arquivo.readline())
print('Seek')
arquivo.seek(0)
print('Read with limit')
print(arquivo.read(2))
arquivo.seek(0)
print('Read Line')
print(arquivo.readline())
print()

arquivo.close()


## Ler um arquivo com encoding e várias linha
""" Arquivo - leitura_multi_line.txt
Uma linha
Duas linhas
Três linhas
Quatro linhas
"""
nome_arquivo = 'leitura_multi_line.txt'
arquivo = open(nome_arquivo, mode='r', encoding='UTF8')

print(nome_arquivo)
print(arquivo.read())
print('Seek')
arquivo.seek(0)
print('While Read Line')
while True:
    linha = arquivo.readline()
    if linha == '':
        print('Fim do arquivo')
        break
    print(linha)
print('Seek')
arquivo.seek(0)
linhas = arquivo.readlines()
print(f'Linhas: {linhas}')
print('Seek')
arquivo.seek(0)
print('While Lines with stream')
while True:
    try:
        linha = next(arquivo)
        print(linha, end='')
    except StopIteration:
        print('\nFim do arquivo')
        break

arquivo.close()


## Escrever um arquivo binário
nome_arquivo = 'arquivo_binario.txt'
arquivo = open(nome_arquivo, mode='wb')

texto_bytes = bytearray('\x4f\x69', encoding='utf-8')
print(type(texto_bytes))
print(texto_bytes)
arquivo.write(texto_bytes)

arquivo.close()


## Converter um arquivo binário em texto
nome_arquivo_origem = 'logo.png'
nome_arquivo_dest = 'logo.txt'
arquivo_origem = open(nome_arquivo_origem, mode='rb')
arquivo_dest = open(nome_arquivo_dest, mode='w', encoding='utf8')

arquivo_dest.write(str(arquivo_origem.read(1024)))

arquivo_origem.close()
arquivo_dest.close()


## Copiar um arquivo de texto
""" Arquivo - origem.txt
Este é o texto do arquivo de origem
"""
nome_arquivo_origem = 'origem.txt'
nome_arquivo_dest = 'copia.txt'
arquivo_origem = open(nome_arquivo_origem, mode='r', encoding='utf8')
arquivo_dest = open(nome_arquivo_dest, mode='w', encoding='utf8')

arquivo_dest.write(arquivo_origem.read())

arquivo_origem.close()
arquivo_dest.close()


## Copiar um arquivo de binario
nome_arquivo_origem = 'logo.png'
nome_arquivo_dest = 'logo_copia.png'
arquivo_origem = open(nome_arquivo_origem, mode='rb')
arquivo_dest = open(nome_arquivo_dest, mode='wb')

arquivo_dest.write(arquivo_origem.read())

arquivo_origem.close()
arquivo_dest.close()
