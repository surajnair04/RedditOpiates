from nltk import wordnet as wn

class MySynset:
		
	def __init__(self, set):
		self.synset = set
		self.hyponyms = []
		self.hypernyms = []
		
	def add_hypernym(self, synset):
		self.hypernyms.append(synset)
		synset.hyponyms.append(self)
		
	def add_syns(self, set):
		self.synset = self.synset.union(set)

class DrugLexicon:

	

	def __init__(self):
		self.lex = {}
		self.add_drugs()
		
	def add_drugs(self):
		self.add_slang("codeine", ["codeine", "captain cody", "slizzurp"]) #Natural
		self.add_slang("fentanyl", ["fentanyl", "fent", "murder 8"]) #Fully-Synthetic
		self.add_slang("hydrocodone", ["hydrocodone", "narco", "norco", "vickies", "watson-387"]) #Semi-Synthetic
		self.add_slang("hydromorphone", ["hydromorphone", "dillies"]) #Semi-Synthetic
		self.add_slang("meperidine", ["meperidine", "demmies"]) #Fully-Synthetic
		self.add_slang("methadone", ["methadone", "amidone", "fizzies"]) #Fully-Synthetic
		self.add_slang("morphine", ["morphine", "emsel", "morf", "morpho"]) #Natural
		self.add_slang("oxycodone", ["oxycodone", "oxy", "oxycet", "oxycotton", "percs"]) #Semi-Synthetic
		self.add_slang("oxymorphone", ["oxymorphone"]) #Semi-Synthetic
	
	def add_slang(self, drug, slang, parent=None):
		slangSet = set(slang)
		if drug in self.lex:
			self.lex[drug].add_syns(slangSet)
		else:
			self.lex[drug] = set(slangSet)
		
if __name__ == "__main__":
	dl = DrugLexicon()
	print(dl.lex)