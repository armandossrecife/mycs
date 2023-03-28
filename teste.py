import datetime
import os

LIMPAR_TELA = 'clear'
COMANDO = 'ls -l'

now = datetime.datetime.now()

os.system(LIMPAR_TELA)

print("Testando o code space no github")
print(f'Data e hora atual: {now}')

print('Lista os arquivos do diretório corrente: ')
os.system(COMANDO)
