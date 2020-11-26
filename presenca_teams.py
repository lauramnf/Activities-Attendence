import csv
import re
import os


def conta_frequencia_atividades(tipo, semana, pontos):
# Função para contar a frequência de atividades semanais online pelo Microsoft Teams
	presenca = {}
	diretorio = os.getcwd()
	pasta = diretorio+'/Semana'+semana+'_'+tipo
	# Itera sobre cada um dos arquivos csv correspondentes a presença de uma aula
	for nome in os.listdir(pasta):
		file = open(pasta+'/'+nome)
		csv_f = csv.DictReader(file)
		for row in csv_f:
			# Corrige o nome dos alunos conforme necessário para que haja correspondência
			nome = row['Nome Completo'].lower()
			nome = re.sub('\s\(convidado\).*', '', nome)
			nome = re.sub('\s\(guest\).*', '', nome)
			# Soma frequência do aluno
			presenca[nome] = presenca.get(nome, 0) + pontos
		file.close()
	return(presenca)

def conta_presenca_final(semana):
# Função para o cálculo da frequência total da semana
	presenca = {}
	diretorio = os.getcwd()
	pasta = diretorio+'/Semana'+semana+'_completo'
	# Itera sobre cada um dos arquivos csv correspondentes a presença de uma aula
	for nome in os.listdir(pasta):
		file = open(pasta+'/'+nome) # Abre cada um dos arquivos
		csv_f = csv.DictReader(file) # Le arquivo
		for row in csv_f:
			presenca[row['Nome']] = presenca.get(row['Nome'], 0) + int(row['Pontos'])
		file.close()
	return(presenca)

def ajeita_dict(dicionario):
# Função para organizar o dicionario {nome_da_pessoa: pontuação} em uma lista de dicionarios [{nome: nome_da_pessoa, pontos: pontuação}]
	planilha_list = []
	planilha_dict = {}
	for name, frequency in dicionario.items(): # Itera sobre cada elemento do dicionário
		planilha_dict['Nome'] = name
		planilha_dict['Pontos'] = frequency
		planilha_dict_copy = planilha_dict.copy()
		planilha_list.append(planilha_dict_copy)
	return planilha_list

def cria_planilha(lista_planilha, tipo, semana):
# Função pra criar uma planilha com as pontuações resultantes
	keys = ['Nome', 'Pontos']
	diretorio = os.getcwd()
	# Cria arquivo csv
	with open(diretorio+'/Semana'+semana+'_completo/'+tipo+'_semana'+semana+'.csv', 'w') as file_escrita:
		writer = csv.DictWriter(file_escrita, fieldnames = keys)
		writer.writeheader()
		writer.writerows(lista_planilha)


pergunta = input("Você quer analisar uma frequência semanal (1) ou final (2)? ")
sem = input('Digite a semana: ')
if pergunta == '1':
	pergunta2 = input("São listas de exercícios/simulados (1), aulas (2), monitorias (3)? ")
	if pergunta2 == '1':
		cria_planilha(ajeita_dict(conta_frequencia_atividades('exercícios',sem, 1)), 'exercícios', sem)
	if pergunta2 == '2':
		cria_planilha(ajeita_dict(conta_frequencia_atividades('aulas',sem,2)), 'aulas', sem)
	if pergunta2 == '3':
		cria_planilha(ajeita_dict(conta_frequencia_atividades('monitorias',sem, 2)), 'monitorias', sem)
if pergunta == '2':
	cria_planilha(ajeita_dict(conta_presenca_final(sem)), 'final', sem)
