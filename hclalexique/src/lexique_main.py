#************************************************************************
# $Id: lexique_main.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  This file is used by the web interface to execute verb conjugation
#
# -----------------
# Revision Details:    (Updated by Revision Control System)
# -----------------
#  $Date: 2009/06/02 01:10:00 $
#  $Author: Taha Zerrouki $
#  $Revision: 0.7 $
#  $Source: arabtechies.sourceforge.net
#
#***********************************************************************/
from pysqlite2 import dbapi2 as sqlite
import sys,re,string
import sys, os
from ar_ctype import *
FILE_DB=u"data/officelexique.db"

def search_word(word,language,lexique="default"):


    table={};
    result=test_select(word,language,lexique);
    #print result;
    if result:
        i=0;
        for r in result:
           arabic=r[0]
    	   french=r[1]
    	   english=r[2]
           table[i]=({"arabic":arabic,"french":french,"english":english})
           i+=1;
    return table;


#-------------------------------------
# test select
#------------------------------------
def test_select(word,language="french",lexique="default"):
	detected_language=detect_language(word)
	if lexique=="default":
		FILE_DB="officelexique.db";
		datatable="office";
	else :
		FILE_DB=lexique+"lexique.db";
		datatable=lexique;

	FILE_DB="data/"+FILE_DB;

	if detected_language=="arabic":
	   word=normalize_searchtext(word);
	   field="arabic_normalized";
	elif language=="french":
	   word=fr_normalize_searchtext(word);
	   field="french_normalized";
	elif language=="english":
	   field="english";
	   word=en_normalize_searchtext(word);
	else:
	   field="french_normalized";
	   word=fr_normalize_searchtext(word);

	conn = sqlite.connect(FILE_DB)
	c = conn.cursor()
	sql = u'''select arabic,french,english FROM '''+datatable+''' WHERE '''+field+''' like "%'''
	sql+=word + '''%"'''

	c.execute(sql)
	list_words=[];

	for row in c:
	   arabic=row[0]
	   french=row[1]
	   english=row[2]
	   list_words.append((arabic,french,english));
	c.close();
##	print list_words;
	if len(list_words)==0:
		return None;
	return list_words;

format_table={
"TEXT":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"CSV":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"HTML":
    {
    "table":"<html> <body dir='rtl'><table>",
    "/table":"</table></body></html>",
    "tr":"<tr>",
    "/tr":"</tr>",
    "td":"<td>",
    "/td":"</td>",
    },
"XML":
    {

    "table":"<?xml encoding='utf-8'><lexique>",
    "/table":"</lexique></xml>",
    "tr":"<term>",
    "/tr":"</term>",
    "td":"<language>",
    "/td":"</language>",
    },
}
def display_format(table,formatting):
    if not format_table.has_key(formatting):
        frmatting="TEXT";
    start_tag=format_table[formatting]["table"];
    end_tag=format_table[formatting]["/table"];
    start_line_tag=format_table[formatting]["tr"];
    end_line_tag=format_table[formatting]["/tr"];
    start_data_tag=format_table[formatting]["td"];
    end_data_tag=format_table[formatting]["/td"];
    text=""
    text+=start_tag;
    for i in range(len(table)):
        text+=start_line_tag;
        for v in table[i].values():
            text+=start_data_tag;
            text+=v;
            text+=end_data_tag;
        text+=end_line_tag;
    text+=end_tag;
    return text;
##table={
##0:{0:'A',1:'B',2:'C'},
##1:{0:'A',1:'B',2:'C'},
##2:{0:'A',1:'B',2:'C'},
##}
##print display_format(table,"TEXT");
##print "-------------------------"
##print display_format(table,"XML");
##print "-------------------------"
##print display_format(table,"HTML");
##print "-------------------------"
##print display_format(table,"CSV");
##

