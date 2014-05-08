from multiprocessing.connection import Client
from array import array

class DBClient(object):
	def __init__(self, address=('localhost',6000), authkey='difficult password'):
		self.conn = Client(address, authkey=authkey)

	def get_batch(self, elements):
		self.conn.send(list(elements))
		to_ret = self.conn.recv()
		return to_ret

	def get(self, element):
		self.conn.send(element)
		to_ret = self.conn.recv()
		return to_ret

	def set(self, key, val):
		self.conn.send({key: val})

	def set_batch(self, key_val_dict):
		self.conn.send(key_val_dict)

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, val):
		self.set(key, val)
