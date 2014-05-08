from multiprocessing.connection import Listener
import sys

class RamDB(object):
	def __init__(self, d, address=('localhost', 6000), authkey='difficult password'):
		self.dict = d
		print 'accepting connections on %s' % str(address)
		self.listener = Listener(address, authkey=authkey)
	
	def accept(self):
		while True:
			try:
				self.conn = self.listener.accept()
				print 'connection accepted from ', self.listener.last_accepted
				while True:
					msg = self.conn.recv()
					if type(msg) is list:
				   		self.conn.send(dict((item, self.dict.get(item)) for item in msg))
				   	elif type(msg) is dict:
				   		self.dict.update(msg)
				   	else:
				   		self.conn.send(self.dict.get(msg))
			except EOFError: 
				self.conn.close()

def startDB(d):
	db = RamDB(d)
	db.accept()

def parseTabSepFile(filename):
	d = {}
	with open(filename) as in_f:
		for line in in_f:
			split = line.split()
			d[split[0]] = split[1]
	return d

if __name__=="__main__":
	fname = sys.argv[1]
	d = parseTabSepFile(fname)
	startDB(d)

