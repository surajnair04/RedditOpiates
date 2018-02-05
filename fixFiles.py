import bz2
import json
import sys
import os.path
import nltk
import drugLexicon

for i in range(5):
	filename = "Data/2016/opcomments2016-0" + str(5+i)
	file = open(filename, encoding="utf-8")
	s = file.read()
	s = s.replace("[[", "[")
	s = s.replace("]]", "]")
	ofilename = "Data/2016/opcomments2016-0" + str(5+i)
	ofile = open(ofilename, "w", encoding="utf-8")
	ofile.write(s)
	
for i in range(3):
	filename = "Data/2016/opcomments2016-" + str(10+i)
	file = open(filename, encoding="utf-8")
	s = file.read()
	s = s.replace("[[", "[")
	s = s.replace("]]", "]")
	ofilename = "Data/2016/opcomments2016-" + str(10+i)
	ofile = open(ofilename, "w", encoding="utf-8")
	ofile.write(s)
