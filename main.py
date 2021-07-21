# Bibliotecas usadas
import json
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
import requests

def calcular():
	# Verifica se a quantidade é diferente de 0 ou ''
	moeda_selec = home.comboBox.currentText()
	quantidade = home.lineEdit.text()
	if quantidade != '':
		if isinstance(quantidade, int):
			quantidade = int(quantidade)
		elif isinstance(quantidade, float):
			quantidade = float(quantidade)
	else:
		quantidade = 1

	# Verifica qual a moeda e chama uma função
	if moeda_selec == "Dólar":
		Moeda = moeda("USD")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Euro":
		Moeda = moeda("EUR")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Libra":
		Moeda = moeda("GBP")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Bitcoin":
		Moeda = moeda("BTC")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Iene":
		Moeda = moeda("JPY")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Dólar Canadense":
		Moeda = moeda("CAD")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	elif moeda_selec == "Peso Argentino":
		Moeda = moeda("ARS")
		result = float(Moeda) * float(quantidade)
		result = str(result)
		home.label_resultado.setText(result)
	else:
		print("Não foi possivel pegar a moeda '-' ")

# Pega os dados da API e retorna para o programa
def moeda(currency):
	request = requests.get("https://economia.awesomeapi.com.br/last/"+currency+"-BRL")
	moeda = json.loads(request.content)
	moeda = moeda[currency + "BRL"]["high"]
	return moeda

# Cria o app Qt
app = QtWidgets.QApplication([])

# Carrega a interface
home = uic.loadUi("home.ui")

# Define o uso dos botões
home.Button_calcular.clicked.connect(calcular)
home.Button_sair.clicked.connect(home.close)

# Mostra a tela e executa o aplicativo
home.show()

app.exec()
