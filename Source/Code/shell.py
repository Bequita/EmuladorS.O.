import os

class Shell:
	def __init__(self):
		self.dic = {"pwd" : self.pwd,"cd" : self.cd,"salir" : self.salir}
		self.run = True
		
	def salir(self):
		self.run = False
		
	def pwd(self):
		print(os.getcwd())

	def cd(self, directorio = ""):
		if(directorio == ""):
			os.chdir("/home/bequita")
		else:
			os.chdir(directorio)
	
	def comando(self, accion):
		acc = accion.split(" ")
		return acc[0]
	
	def argumento(self, accion):
		acc = accion.split(" ")
		if(len(acc)):
			return ""
		return acc[1]
	
	def ejecutarComando(self,accion):
		cmd = self.comando(accion)
		arg = self.argumento(accion)
		try:
			acc = self.dic[cmd]
			if(arg == ""):
				acc()
			else:
				acc(arg)
		except:
			print("El comando no existe")

			
shell = Shell()
while(shell.run):
	entrada = input(os.getcwd() + " >> ")
	shell.ejecutarComando(entrada)
