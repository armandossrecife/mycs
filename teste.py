import datetime
import os

now = datetime.datetime.now()
limpar_tela = 'clear'
comando = 'ls -l'

os.system(limpar_tela)

print("Testando o code space no github")
print(f'Data e hora atual: {now}')


print('Lista os arquivos do diretório corrente: ')
os.system(comando)