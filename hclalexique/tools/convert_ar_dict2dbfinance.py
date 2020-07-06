from pysqlite2 import dbapi2 as sqlite
import os
import sys
from ar_ctype import *

#-------------------------
#  Parameters
SEPARATOR=";"
FILE_DATA=u"data/finance.csv"
FILE_DB=u"data/financelexique.db"
DB_CREATE_SQL=u'''create TABLE finance
    (
    ID INT UNIQUE NOT NULL,
    ARABIC TEXT NOT NULL,
    FRENCH TEXT NOT NULL,
    ENGLISH TEXT NOT NULL,
    ARABIC_NORMALIZED TEXT NOT NULL,
    FRENCH_NORMALIZED TEXT NOT NULL
    )
'''
NB_FIELD_MAX=4

#-------------------------------------
# create database file for
#------------------------------------
def create_database():
    liste=[];
    conn = sqlite.connect(FILE_DB)
    c = conn.cursor()

    sql = DB_CREATE_SQL;
    c.execute(sql)
    c.close();

#-------------------------------------
# test select
#------------------------------------
def test_select(word):
	liste=[];
	conn = sqlite.connect(FILE_DB)
	c = conn.cursor()
	sql = u"select arabic,french,english from finance WHERE french_normalized like '%"+word+"%'"
	c.execute(sql)
	list_words=[];
##	row=c.fetchone();
##	while len(row)==0:
	for row in c:
	   arabic=row[0]
	   french=row[1]
	   english=row[2]
	   list_words.append((arabic,french,english));
	c.close();
	if len(list_words)==0:
		return None;
	return list_words;



#---------------------------------
# main readfile
#---------------------------------
def import_file():
	filename=FILE_DATA;
	try:
		fl=open(filename);
	except:
		print " Error :No such file or directory: %s" % filename
		sys.exit(0)
	line=fl.readline().decode("utf");
	text=u""
	tuple_table=[];
	nb_field=NB_FIELD_MAX;
	while line :
		if not line.startswith("#"):
#		print "line ", line
			text=text+" "+chomp(line)
			line=chomp(line)
			liste=line.split(SEPARATOR);

			tuple_table.append(liste);
		line=fl.readline().decode("utf");
	fl.close();



	id=0;
    #connection
	conn = sqlite.connect(FILE_DB)
	c = conn.cursor()
    #--------------------
    # query
    #--------------------
	limit=100000;
	for i in range(min(limit,len(tuple_table))):
		id=i+1;# to avoid zero
#------------------------------------------------------
# treat data
#------------------------------------------------------
		tup=tuple_table[i];
##		id=tup[0]
		french=tup[1];
		english="";
		arabic=tup[2];
		arabic_normalized=normalize_searchtext(arabic);
		french_normalized=fr_normalize_searchtext(french)
		print "\t".join([arabic,french,english,arabic_normalized, french_normalized]);
##		print id,"[%s] '%s'(%s)-%s (%s)"%(type_word,word,str(lenght),word_vocalised,str(lenght_vocalised)),"'%s'"%root,categories;
		t=(id,arabic,french,english,arabic_normalized, french_normalized)
		# Insert a row of data
		c.execute("""insert into finance
          values (?,?,?,?,?,?)""",t)

#---------End treat data ------------------
    #commit
	conn.commit()
    #close
	c.close()
##	    print;




if __name__ == "__main__":
#  main()
#To create table
    create_database();
#To load info from csv file to db
    import_file();
#select
    word=u"contrôle"

##    word=u"**و*"
    list_words=test_select(word)
    print list_words;
    if list_words:
        for w in list_words:
            print w;
    else:
		print "no one";


