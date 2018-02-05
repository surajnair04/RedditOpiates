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
		self.add_slang("codeine", ["codeine", "captain cody", "slizzurp"])
		self.add_slang("fentanyl", ["fentanyl", "fent", "murder 8"])
		self.add_slang("hydrocodone", ["hydrocodone", "narco", "norco", "vickies", "watson-387"])
		self.add_slang("hydromorphone", ["hydromorphone", "dillies"])
		self.add_slang("meperidine", ["meperidine", "demmies"])
		self.add_slang("methadone", ["methadone", "amidone", "fizzies"])
		self.add_slang("morphine", ["morphine", "emsel", "morf", "morpho"])
		self.add_slang("oxycodone", ["oxycodone", "oxy", "oxycet", "oxycotton", "percs"])
		self.add_slang("oxymorphone", ["oxymorphone"])
	
	def add_slang(self, drug, slang, parent=None):
		slangSet = set(slang)
		if drug in self.lex:
			self.lex[drug].add_syns(slangSet)
		else:
			self.lex[drug] = set(slangSet)
		
if __name__ == "__main__":
	dl = DrugLexicon()
	print(dl.lex)