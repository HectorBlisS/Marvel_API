import requests
import hashlib


class PachuMarvel(object):
	""" Ingresa tu llaves publica primero y luego privada, si no se Ingresa
		el programa utilizara unas por default """

	def __init__(self,public_key='49b00060252ec6df688a67b44b75cc0e',private_key='d1eca4ab9b76596debb63de6f68be3e0e8bca898'):
		self.public_key = public_key
		self.private_key = private_key
		ts = '1'
		self.ha = hashlib.md5((ts+self.private_key+self.public_key).encode()).hexdigest()
		self.url = 'http://gateway.marvel.com/v1/public/'

		#aqui ponemos vacios los datos del superH
		self.nombre = ''
		self.descripcion = ''
		self.img = ''
		self.personaje = None
		self.id = ''

	def get_personaje(self,nombre="hulk"):
		""" Escribe el nombre del personaje corretamente"""
		try:
			self.personaje = requests.get(
				self.url+'characters',
					params={
					'apikey':self.public_key,
					'ts':'1',
					'hash':self.ha,
					'name':nombre
					}).json()
			self.nombre = nombre
			self.descripcion = self.personaje['data']['results'][0]['description']
			self.img = self.personaje['data']['results'][0]['thumbnail']['path']
			print('Asi joder!, ya guarde tu personaje maldito friky')

		except:
			print('Escribe bien cabron!')

	def get_response(self):
		""" Este metodo solo puede ser llamado despues de get_personaje"""
		try:
			print(self.personaje)
		except:
			print('Algo pasó y no se que X_X')

	def get_id(self):
		""" Este metodo setea el id del personaje """
		try:
			self.id = self.personaje['data']['results'][0]['id']
			print(self.id)
		except:
			print('llama primero get_personaje sonso')


		

