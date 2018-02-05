import bz2
import json
import sys
import os.path
import drugLexicon
import winsound

year = input("Choose year:")
month = input("Choose month:")
archive = "Data/" + year + "/RC_" + year + "-" + month + ".bz2"
bz_file = bz2.BZ2File(archive, 'rb', 1000000)
commentCount = 0
ofile = "Data/" + year + "/opcomments" + year + "-" + month
output_file = open(ofile, 'w', encoding="utf-8")
dl = drugLexicon.DrugLexicon().lex
allSlang = set([])
for drug in dl:
	allSlang = allSlang.union(dl[drug])
while True:
	'''
	if commentCount>=1000000:
		break
	'''
	line = bz_file.readline().decode('utf8')
	if len(line)==0:
		break
	comment = json.loads(line)
	id = comment["id"]
	body = comment["body"]
	bodyl = body.lower().split()
	for word in bodyl:
		if word.lower() in allSlang:
			output_file.write(json.dumps(comment) + "\n")
			break
	if commentCount%100000 == 0:
		print(commentCount)
	commentCount+=1
	
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)