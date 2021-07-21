import json
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
import requests

def calcular():
	moeda_selec = home.comboBox.currentText()
	quantidade = home.lineEdit.text()
	if quantidade != '':
		if isinstance(quantidade, int):
			quantidade = int(quantidade)
		elif isinstance(quantidade, float):
			quantidade = float(quantidade)
	else:
		quantidade = 1
	if moeda_selec == "Dólar":
		Dolar = dolar()
		result = float(Dolar) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Euro":
		Euro = euro()
		result = float(Euro) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Libra":
		Libra = libra()
		result = float(Libra) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Bitcoin":
		BTC = btc()
		result = float(BTC) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Iene":
		Iene = iene()
		result = float(Iene) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Dólar Canadense":
		Dolca = dolca()
		result = float(Dolca) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Peso Argentino":
		Pesoarg = pesoarg()
		result = float(Pesoarg) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	else:
		print("Não foi possivel pegar a moeda '-' ")

def dolar():
	request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
	moeda = json.loads(request.content)
	moeda = moeda["USDBRL"]["high"]
	return moeda

def euro():
	request = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
	moeda = json.loads(request.content)
	return moeda["EURBRL"]["high"]

def btc():
	request = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
	moeda = json.loads(request.content)
	return moeda["BTCBRL"]["high"]

def libra():
	request = requests.get("https://economia.awesomeapi.com.br/last/GBP-BRL")
	moeda = json.loads(request.content)
	return moeda["GBPBRL"]["high"]

def iene():
	request = requests.get("https://economia.awesomeapi.com.br/last/JPY-BRL")
	moeda = json.loads(request.content)
	return moeda["JPYBRL"]["high"]

def dolca():
	request = requests.get("https://economia.awesomeapi.com.br/last/CAD-BRL")
	moeda = json.loads(request.content)
	return moeda["CADBRL"]["high"]

def pesoarg():
	request = requests.get("https://economia.awesomeapi.com.br/last/ARS-BRL")
	moeda = json.loads(request.content)
	return moeda["ARSBRL"]["high"]

app = QtWidgets.QApplication([])

home = uic.loadUi("home.ui")

home.Button_calcular.clicked.connect(calcular)
home.Button_sair.clicked.connect(home.close)

home.show()

app.exec()
