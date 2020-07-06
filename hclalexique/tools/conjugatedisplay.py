#!/usr/bin/python
# -*- coding=utf-8 -*-
#************************************************************************
# $Id: conjugateddisplay.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  The Class used to display information after conjugated
#   All print and views and display are redirected to this class
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


import sys
import re
import string

class lexiquedisplay:
	tab_result={}

	def __init__(self,tab_resulted):
# بناء جدول عرض التصريفات
		self.tab_result=tab_resulted;
#------------------------------------------------------------------
	def setmode(self,mode):
		self.mode=mode
#------------------------------------------------------------------
	def display(self,mode):
		if mode=='Text':
		    return self.display_text()
		elif mode=='HTML':
		    return self.display_html()
		elif mode=='CSV':
		    return self.display_csv()
		elif mode=='GUI':
		    return self.display_table()
		elif mode=='TABLE':
		    return self.display_table()
		elif mode=='XML':
		    return self.display_xml()
		elif mode=='TeX'.upper():
		    return self.display_tex()
		else:
		    return self.display_text()
#-------------------------------------------------
#
#
#-------------------------------------------------
	def display_text(self):
		text = u""
		for title in self.text.keys():
			text+= u"%s: %s\n" %(title, self.text[title])
		text+= u"\t"
		text+=u"\t".join(listtense);
		for pronoun in PronounsTable:
			text+= u"\n%s" %(pronoun)
			for tense in listtense:
				if pronoun in self.tab_conjug[tense].keys():
					text+= u"\t%s" %(self.tab_conjug[tense][pronoun])
		return text
#-------------------------------------------------
#
#
#-------------------------------------------------
	def display_csv(self):
		text = u""
		for title in self.text.keys():
			text+= u"%s: %s\n" %(title,self.text[title])
		text+= u";".join(listtense);
		text+=u"\n";
		for pronoun in PronounsTable:
			text+= u"%s" %(pronoun)
			for tense in listtense:
#				print (self.verb).encode("utf-8"),
				if pronoun in self.tab_conjug[tense].keys():
					text+= u";%s" %(self.tab_conjug[tense][pronoun])
			text+= u"\n"
		return text

#----------------------------------------------------------
# display_gui
# return a HTML formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_html(self):
		rslt_tab=self.tab_result;
        if len(rslt_tab)>0:
            j=0;
            for k in rslt_tab[0].keys():
##                self.TabActiveResult.setHorizontalHeaderItem(j,QtGui.QTableWidgetItem(display_language(k)))
                for i in range(len(rslt_tab)):
                    #print i,j;
                    self.TabActiveResult.setItem(i,j,QtGui.QTableWidgetItem(rslt_tab[i][k]))
                j+=1;		indicativeTenses=[];
            text+= u"<table border=1 cellspacing=0 id='result' class='result' >\n"
            text+= u"<tr><th>&nbsp;</th>"
            for language in rslt_tab[0].keys():
				text+= u"<th>%s</th>" %(language)
            text+= u"</tr>\n"
			for pronoun in PronounsTable:
				text+= u"<tr>"
				text+= u"<th>%s</th>" %(pronoun)
				for tense in listtenseToDisplay:
					text+= u"<td>&nbsp;%s</td>" %(self.tab_conjug[tense][pronoun])
				text+=u"</tr>\n"
			text+=u"</table>\n"
			text+=u"</div><br/>\n"
		text+=u"</div>"
		passiveTenses=[];
		for t in listtense:
			if t in TableIndicativeTense:
				indicativeTenses.append(t);
			else:
				passiveTenses.append(t);
		text = u""
		text+= u"<h3>%s : %s - %s</h3>\n" %(self.verb,self.verb,self.future_form)
#		text+= u"<h3>%s - %s</h3>\n\n" %(self.verb,self.future_form)
        # print spelcial attribut of the verb
		text+= u"<ul>\n"
		for title in self.text.keys():
			text+= u"<li><b>%s:</b> %s</li>\n" %(title,self.text[title])
		text+= u"</ul>\n\n"
		# Ad mechanisme to set font size
		text+=u"<span id='holder1'></span>"


		if len(indicativeTenses)>0 and len(passiveTenses)>0:
			text+=u"""
			<a name="resultat"/>
			<a href="#resultat"  id='Bindicative'>المبني للمعلوم</a>
			<a href="#resultat"  id='Bpassive' >المبني للمجهول</a>
			"""

		# print conjugation
		text+=u"<div id='resultat'>"
		for  mode in("indicative","passive"):
			if mode=="indicative":
				listtenseToDisplay=indicativeTenses;
			else:
				listtenseToDisplay=passiveTenses;
			text+= u"<div id='Result%s' class='result'>\n"%mode;
			text+= u"<table border=1 cellspacing=0 id='result' class='result' >\n"
			text+= u"<tr><th>&nbsp;</th>"
			for tense in listtenseToDisplay:
				text+= u"<th>%s</th>" %(tense)
			text+= u"</tr>\n"
			for pronoun in PronounsTable:
				text+= u"<tr>"
				text+= u"<th>%s</th>" %(pronoun)
				for tense in listtenseToDisplay:
					text+= u"<td>&nbsp;%s</td>" %(self.tab_conjug[tense][pronoun])
				text+=u"</tr>\n"
			text+=u"</table>\n"
			text+=u"</div><br/>\n"
		text+=u"</div>"
		return text

#----------------------------------------------------------
# display_table
# return a table with tenses and conjugated verb
#
#
#-----------------------------------------------------------
	def display_table(self,listtense=TableTense):
		table={}

		j=0;
		table[0]={0:u"الضمائر"}
		for j in range(len(listtense)):
		  table[0][j+1]=listtense[j];
		i=1;
		for pronoun in PronounsTable:
		  table[i]={}
		  table[i][0]=pronoun;
		  j=1
		  for tense in listtense:
		      table[i][j]=self.tab_conjug[tense][pronoun]
		      j=j+1
		  i=i+1
		return table
#----------------------------------------------------------
# display_gui
# return a HTML formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_xml(self):
		text = u""
		text+= u"<verb_conjugation>\n"
		text+= u"\t<proprety name='verb' value='%s'/>\n" %(self.verb)
		for title in self.text.keys():
			text+= u"\t<proprety name='%s' value='%s'/>\n" %(title,self.text[title])
		for tense in listtense:
			text+= u"\t<tense name='%s'>\n" %(tense)
			for pronoun in PronounsTable:
			 if self.tab_conjug[tense][pronoun]!="":
			     text+= u"\t\t<conjugation pronoun='%s' value='%s'/>\n" %(pronoun,self.tab_conjug[tense][pronoun])
			text+= u"\t</tense>\n"
		text+= u"</verb_conjugation>"
		return text
#----------------------------------------------------------
# display_tex
# return a TeX formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_tex(self):
		text = u""
		text+= u"\\environment qutrub-layout\n"
		text+= u"\\starttext\n"

		text+= u"\\Title{%s}\n" %(self.verb)

		text+= u"\\startitemize\n"
		for title in self.text.keys():
			if title == u" الكتابة الداخلية للفعل ":
				text+= u"\\item {\\bf %s} \\DeShape{%s}\n" %(title,self.text[title])
			else:
				text+= u"\\item {\\bf %s} %s\n" %(title,self.text[title])
		text+= u"\\stopitemize\n"

		text+= u"\\starttable[|lB|l|l|l|l|l|]\n"
		text+= u"\\HL[3]\n\\NC"
		for tense in listtense:
			text+= u"\\NC {\\bf %s}" %(tense)
		text+= u"\\SR\n\\HL\n"
		for pronoun in PronounsTable:
			text+= u"\\NC %s" %(pronoun)
			for tense in listtense:
				text+= u"\\NC %s" %(self.tab_conjug[tense][pronoun])
			text+= u"\\AR\n"
		text+= u"\\LR\\HL[3]\n"
		text+= u"\\stoptable\n"

		text+= u"\\stoptext"
		return text
