import csv
import re
import os


def conta_frequencia_atividades(tipo, semana, pontos):
	presenca = {}
	diretorio = os.getcwd()
	pasta = diretorio+'/Semana'+semana+'_'+tipo
	for nome in os.listdir(pasta):
		file = open(pasta+'/'+nome)
		csv_f = csv.DictReader(file)
		for row in csv_f:
			if row['Nome Completo'] == 'live:.b44abc4b05463b85':
				row['Nome Completo'] = 'Ana Beatriz Ferreira da Silva'
			elif row['Nome Completo'] == 'live:.cid.235763fda51d58cd':
				row['Nome Completo'] = 'Larissa Silva Paiva'
			elif row['Nome Completo'] == 'live:.cid.f70f038f492cf762':
				row['Nome Completo'] = 'Bárbara Jordana da Silva'
			elif row['Nome Completo'] == 'live:.cid.3cfcaa8c129a1136':
				row['Nome Completo'] = 'Davi Silva'
			elif row['Nome Completo'] == 'live:.cid.ec4be6c1f9167e62':
				row['Nome Completo'] = 'Sarah Souza'
			elif row['Nome Completo'] == 'live:.cid.32b110fabe43d0b0':
				row['Nome Completo'] = 'live:.cid.32b110fabe43d0b0'
			elif row['Nome Completo'] == 'live:.cid.6a8df8fb916cf458':
				row['Nome Completo'] = 'live:.cid.9344696efdebd18a'
			elif row['Nome Completo'] == 'Paula de Fátima':
				row['Nome Completo'] = 'live:.cid.74e6e116ee7a641d'
			elif row['Nome Completo'] == 'live:.cid.74e6e116ee7a641d':
				row['Nome Completo'] = 'Caroline Da Silva'

			presenca[row['Nome Completo'].lower()] = presenca.get(row['Nome Completo'].lower(), 0) + pontos		 	 
		file.close()
	return(presenca)

def conta_presenca_final(semana):
	presenca = {}
	diretorio = os.getcwd()
	pasta = diretorio+'/Semana'+semana+'_completo'
	for nome in os.listdir(pasta):
		file = open(pasta+'/'+nome)
		csv_f = csv.DictReader(file)
		for row in csv_f:
			presenca[row['Nome']] = presenca.get(row['Nome'], 0) + int(row['Pontos'])		 	 
		file.close()
	return(presenca)

def ajeita_dict(dicionario):
	planilha_list = []
	planilha_dict = {}
	for name, frequency in dicionario.items():
		planilha_dict['Nome'] = name
		planilha_dict['Pontos'] = frequency
		planilha_dict_copy = planilha_dict.copy()
		planilha_list.append(planilha_dict_copy)
	return planilha_list

def cria_planilha(lista_planilha, tipo, semana): 
	keys = ['Nome', 'Pontos']
	diretorio = os.getcwd()
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
