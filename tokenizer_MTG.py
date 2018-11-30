#!/usr/bin/python3.5
# -*- coding: UTF-8 -*- 

import re, argparse

HELP_TEXT = """
Tokenize a text file (.txt) for Mind The Gap parser.

Example :
$python3 tokenize_MTG.py TXT_FILE.txt -o OUTPUT_FILE.tok
"""

def parse_args():
	parser = argparse.ArgumentParser(description=HELP_TEXT)
	#argument : inputfile
	parser.add_argument("input_file",default="",help="The text file to tokenize")
	#option : outputfile
	parser.add_argument("-o","--output_file",dest="output_file",default="", help="The output file")
	args = parser.parse_args()
	return args

args = parse_args()
inputfile = args.input_file
outputfile = args.output_file

input_file = open (inputfile,"r")


def tokenize():
	for line in input_file: 
		line = re.sub("\xA0"," ",line) #replacing non-breaking spaces with normal spaces
		line.strip() #remove trailing spaces
		line = re.sub("\."," .\n",line) # period
		line = re.sub("'","' ",line) #apostrophe
		line = re.sub("’","’ ",line) #apostrophe
		line = re.sub("\""," \" ",line) #quotes
		line = re.sub(","," ,",line) #comma
		line = re.sub(";"," ;",line) #semi-colon
		line = re.sub(":"," :",line) #colon
		line = re.sub("!"," !\n",line) #exclamation mark
		line = re.sub("\?"," ?\n",line)#question mark
		line = re.sub("\(","( ",line) #left round bracket
		line = re.sub("\)"," )",line) #right round bracket
		line = re.sub("\(","-LRB-",line) #formatting the parentheses to MTG format
		line = re.sub("\)","-RRB-",line) #formatting the parenthses to MTG format
		line = re.sub("«"," « ",line) #French quotes
		line = re.sub("»"," » ",line) #French quotes
		line = re.sub("\[","[ ",line) #left bracket
		line = re.sub("\]"," ]",line) #right bracket
		line = re.sub("^-","- ",line) # dash introducing a dialog
		line = re.sub("M \.\n","M.",line) # case of M.
		line = re.sub("(([A-Z]{1,}) \.\n)",r"\2.",line) #acronyms
		#aujourd'hui
		line = re.sub("aujourd' hui","aujourd'hui",line) #exception words
		line = re.sub("Aujourd' hui","Aujourd'hui",line) #exception words
		line = re.sub("aujourd’ hui","aujourd’hui",line) #exception words
		line = re.sub("Aujourd’ hui","Aujourd’hui",line) #exception words
		#quelqu'un
		line = re.sub("quelqu' un","quelqu'un",line) #exception words
		line = re.sub("Quelqu' un","Quelqu'un",line) #exception words
		line = re.sub("quelqu’ un","quelqu’un",line) #exception words
		line = re.sub("Quelqu’ un","Quelqu’un",line) #exception words
		#d'abord
		line = re.sub("d' abord","d'abord",line) #exception words
		line = re.sub("D' abord","D'abord",line) #exception words
		line = re.sub("d’ abord","d’abord",line) #exception words
		line = re.sub("D’ abord","D’abord",line) #exception words
		#tool words
		line = re.sub("d '","d'",line)
		line = re.sub("d ’","d’",line)
		line = re.sub("l '","l'",line)
		line = re.sub("l ’","l’",line)
		line = re.sub("s '","s'",line)
		line = re.sub("s ’","s’",line)
		line = re.sub("n '","n'",line)
		line = re.sub("n ’","n’",line)
		#split of verb and CLS linked with "-" in questions
		line = re.sub("-tu"," -tu",line)
		line = re.sub("-je"," -je",line)
		line = re.sub("-ce"," -ce",line)
		line = re.sub("-il"," -il",line)
		line = re.sub("-ils"," -ils",line)
		line = re.sub("-elle"," -elle",line)
		line = re.sub("-elles"," -elles",line)
		line = re.sub("-nous"," -nous",line)
		line = re.sub("-vous"," -vous",line)
		#removing extra and trailing spaces
		line = re.sub(" +"," ",line) #extra spaces
		line = re.sub("\n ","\n",line) #remove new line at beginning of a new line only by a new line
		line = re.sub("\n+","\n",line) #remove empty lines
		line = re.sub("^ +","",line) #remove spaces at beginning of line (if strip() doesn't work)
		output_file.writelines(line) 

if outputfile:
	output_file = open (outputfile,"w")
	tokenize()
	output_file.close()
else:
	print("Please specify an output file. Syntax is: $python3 tokenize_MTG.py inputfile -o outputfile")

input_file.close()
