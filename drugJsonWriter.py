import json
import re
from nltk import tokenize

class DrugJson:
	
	def __init__(self, drug, syns, features=None):
		if features is None:
			features = []
		self.drug = drug
		self.syns = syns
		self.features = features
		
	def dumps_drug(self):
		return json.dumps({"name": self.drug, "synonyms": self.syns, "features": self.features})
		
	@staticmethod
	def read_drug(jsonstring):
		comment = json.loads(jsonstring)
		return DrugJson(comment["name"], comment["synonyms"], comment["features"])
		
def read_ugly_file():
	filename="DrugsLex.txt"
	file = open(filename)
	tokens = tokenize.word_tokenize(file.read().lower())
	mode = "standard"
	name = ""
	term = ""
	result = {}
	for token in tokens:
		if token == ';':
			result[name].append(term)
			term = ""
		elif token == '{':
			if term!="":
				result[name].append(term)
			mode = "name"
			name = ""
		elif token == '}':
			mode = "standard"
			result[name] = []
		elif token == '(':
			mode = "extra"
		elif token == ')':
			mode = "standard"
		else:
			if mode == "standard":
				if term == "":
					term = token
				else:
					term += " " + token
			if mode == "name":
				if name == "":
					name = token
				else:
					name += " " + token
			
	ofilename = "drugslexicon.json"
	ofile = open(ofilename, "w")
	ofile.write(json.dumps(result))
				

if __name__ == "__main__":
	read_ugly_file()