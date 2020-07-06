#!/usr/bin/python
# -*- coding=utf-8 -*-
# prograzm to treat a lexique for HCLA

import sys,re,string
import sys, getopt, os
from ar_ctype import*
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"
def chomp(s):
  if (s.endswith('\n')):
    return s[:-1]
  else:
    return s

def usage():
# "Display usage options"
	print "(C) CopyLeft 2009, %s"%AuthorName
	print "Usage: %s -f filename [OPTIONS]" % scriptname
#"Display usage options"
	print "\t[-h | --help]\t\toutputs this usage message"
	print "\t[-V | --version]\tprogram version"
	print "\t[-f | --file= filename]\tinput file to %s"%scriptname
	print "\r\nThis program is licensed under the GPL License\n"

def grabargs():
#  "Grab command-line arguments"
	all = False;
	future=False;
	past=False;
	passive=False;
	imperative=False;
	fname = ''

	if not sys.argv[1:]:
		usage()
		sys.exit(0)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hV:f:",
                               ["help", "version","file="],)
	except getopt.GetoptError:
		usage()
		sys.exit(0)
	for o, val in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit(0)
		if o in ("-V", "--version"):
			print scriptversion
			sys.exit(0)
		if o in ("-f", "--file"):
			fname = val
	return (fname)

def main():
	filename= grabargs()
	try:
		fl=open(filename);
	except:
		print " Error :No such file or directory: %s" % filename
		sys.exit(0)
	line=fl.readline().decode("utf");
	text=u""
	lexique_table=[];
	nb_field=2;
	current_term=u"";
	while line :
		if not line.startswith("#"):
			line=chomp(line);
			liste=line.split(";");
			if len(liste)>=nb_field:
				actual_term=liste[0]
				actual_term=actual_term.strip(" ");
				actual_term=ar_strip_marks_keepshadda(actual_term);
# if the previous term is given an other time,
# we writre only the number
				if current_term==actual_term:
				   actual_number=liste[1];
				   print ",",actual_number,
				else:
# if is a new term, we print it with Entree before
# and wait for an other term
				    current_term=actual_term;
				    print;
				    print line,
#case of letter positions
##			else :
##				print line;
		line=fl.readline().decode("utf");
	fl.close();


if __name__ == "__main__":
  main()







