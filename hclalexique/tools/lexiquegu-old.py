# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qutrubgui.ui'
#
# Created: Mon Sep 28 14:46:07 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

import PyQt4.QtCore
import PyQt4.QtGui
##from PyQt4 import QtCore, QtGui
from src.lexique_main import *

from setting import *

class Ui_MainWindow(object):
    font_base=None;
    font_result=None;
    result={}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.MainWindow=MainWindow;
        self.font_base=None;
        self.result={}
        self.SuggestedVerbList=[];
#-----------------------------------------------
        self.font_base = QtGui.QFont()
        self.font_base.setFamily("KacstOne")
        self.font_base.setPointSize(12)
        self.font_base.setBold(True)
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        self.BDictOption=1;


        RightToLeft=1;
        MainWindow.setLayoutDirection(RightToLeft)


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.Label = QtGui.QLabel(self.centralwidget)
        self.Label.setObjectName("Label")
        self.gridLayout_3.addWidget(self.Label, 1, 1, 1, 1)
        self.Label_2 = QtGui.QLabel(self.centralwidget)


        self.Label_2.setObjectName("Label_2")
        self.gridLayout_3.addWidget(self.Label_2, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")


        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")


        self.BPast = QtGui.QCheckBox(self.centralwidget)
        self.BPast.setEnabled(False)

        self.BPast.setFont(self.font_base)
        self.BPast.setChecked(True)
        self.BPast.setObjectName("BPast")
        self.gridLayout_5.addWidget(self.BPast, 3, 1, 1, 1)
        self.BFuture = QtGui.QCheckBox(self.centralwidget)
        self.BFuture.setEnabled(False)

        self.BFuture.setFont(self.font_base)
        self.BFuture.setChecked(True)
        self.BFuture.setObjectName("BFuture")
        self.gridLayout_5.addWidget(self.BFuture, 3, 2, 1, 1)
        self.BImperative = QtGui.QCheckBox(self.centralwidget)
        self.BImperative.setEnabled(False)

        self.BImperative.setFont(self.font_base)
        self.BImperative.setChecked(True)
        self.BImperative.setObjectName("BImperative")
        self.gridLayout_5.addWidget(self.BImperative, 3, 3, 1, 1)



        self.BPassive = QtGui.QCheckBox(self.centralwidget)
        self.BPassive.setEnabled(False)

        self.BPassive.setFont(self.font_base)
        self.BPassive.setChecked(True)
        self.BPassive.setObjectName("BPassive")
        self.gridLayout_5.addWidget(self.BPassive, 4, 1, 1, 1)


        self.Tsearch = QtGui.QLineEdit(self.centralwidget)
        self.Tsearch.setEnabled(True)
        self.Tsearch.setMaximumSize(QtCore.QSize(200, 40))
        self.Tsearch.setFont(self.font_result)
##        self.Tsearch.setTabChangesFocus(False)
##        self.Tsearch.setUndoRedoEnabled(False)
##        self.Tsearch.setLineWrapMode(QtGui.QTextEdit.NoWrap)
##        self.Tsearch.setAcceptRichText(False)
        self.Tsearch.setObjectName("Tverb")
        self.gridLayout_5.addWidget(self.Tsearch, 0, 0, 1, 1)
        self.gridLayout_5.setColumnStretch(0,3)
##        self.gridLayout_5.setStretchFactor(sel.Tverb,3);

##        self.formLayout_suggest = QtGui.QFormLayout()
##        self.formLayout_suggest.setObjectName("formLayout_suggest")

##        self.CBSuggestLabel = QtGui.QLabel(self.centralwidget)
##        self.CBSuggestLabel.setObjectName("CBSuggestLabel")
##        self.CBSuggestLabel.setText(u"أتقصد؟")
##        self.CBSuggestLabel.setFont(self.font_base)
##        self.CBSuggestLabel.hide()

        self.CBSuggest = QtGui.QComboBox(self.centralwidget)
        self.CBSuggest.setFont(self.font_result)
        self.CBSuggest.setEditable(True)
        self.CBSuggest.setMaximumSize(QtCore.QSize(200, 40))
        self.CBSuggest.setObjectName("CBSuggest")
        self.CBSuggest.hide()

##        self.gridLayout_5.addLayout(self.formLayout_suggest, 1,0, 1, 1)
        self.gridLayout_5.addWidget(self.CBSuggest, 1,0, 1, 1)


        self.CBHarakaLabel = QtGui.QLabel(self.centralwidget)
        self.CBHarakaLabel.setObjectName("CBHarakaLabel")
        self.CBHarakaLabel.setText(u"حركة عين الثلاثي في المضارع")
        self.CBHarakaLabel.setFont(self.font_base)
        self.CBHarakaLabel.hide()
##        self.gridLayout_5.addWidget(self.CBHarakaLabel, 1, 1, 1, 1)

        self.CBHaraka = QtGui.QComboBox(self.centralwidget)
        self.CBHaraka.setFont(self.font_result)
        self.CBHaraka.setEditable(True)
        self.CBHaraka.setMaximumSize(QtCore.QSize(200, 40))
        self.CBHaraka.setObjectName("CBHaraka")
        self.CBHaraka.addItem(QtCore.QString(u"فتحة"))
        self.CBHaraka.addItem(QtCore.QString(u"ضمة"))
        self.CBHaraka.addItem(QtCore.QString(u"كسرة"))
        self.CBHaraka.setEnabled(False)
        self.CBHaraka.hide()
        self.formLayout_haraka = QtGui.QFormLayout()
        self.formLayout_haraka.setObjectName("formLayout_haraka")

        self.formLayout_haraka.setWidget(1, QtGui.QFormLayout.LabelRole, self.CBHarakaLabel)
        self.formLayout_haraka.setWidget(1, QtGui.QFormLayout.FieldRole, self.CBHaraka)
        self.gridLayout_5.addLayout(self.formLayout_haraka, 1, 2, 1, 1)

        self.BFuture_moode = QtGui.QCheckBox(self.centralwidget)
        self.BFuture_moode.setEnabled(False)

        self.BFuture_moode.setFont(self.font_base)
        self.BFuture_moode.setChecked(True)
        self.BFuture_moode.setObjectName("BFuture_moode")
        self.gridLayout_5.addWidget(self.BFuture_moode, 4, 3, 1, 1)
        self.BConfirmed = QtGui.QCheckBox(self.centralwidget)
        self.BConfirmed.setEnabled(False)

        self.BConfirmed.setFont(self.font_base)
        self.BConfirmed.setChecked(True)
        self.BConfirmed.setObjectName("BConfirmed")
        self.gridLayout_5.addWidget(self.BConfirmed, 4, 2, 1, 1)

# a search on a Transitive
        self.BTransitive = QtGui.QCheckBox(self.centralwidget)
        self.BTransitive.setFont(self.font_base)
        self.BTransitive.setChecked(True)
        self.BTransitive.setObjectName("BTransitive")
        self.gridLayout_5.addWidget(self.BTransitive, 0, 3, 1, 1)
# a more optionss
        self.BMoreOptions = QtGui.QCheckBox(self.centralwidget)
        self.BMoreOptions.setFont(self.font_base)
        self.BMoreOptions.setChecked(False)
        self.BMoreOptions.setObjectName("BMoreOptions")
        self.BMoreOptions.setText(u"خيارات")
        self.gridLayout_5.addWidget(self.BMoreOptions, 0, 4, 1, 1)
# a search on a dictionary options
        self.BDict = QtGui.QCheckBox(self.centralwidget)
        self.BDict.setFont(self.font_base)
        self.BDict.setChecked(self.BDictOption!=0)
        self.BDict.setObjectName("BDict")
        self.BDict.hide()
        self.BDict.setText(u"البحث في المعجم")
        self.gridLayout_5.addWidget(self.BDict, 1, 3, 1, 1)

        self.BAll = QtGui.QCheckBox(self.centralwidget)
        self.BAll.setEnabled(True)

        self.BAll.setFont(self.font_base)
        self.BAll.setChecked(True)
        self.BAll.setTristate(False)
        self.BAll.setObjectName("BAll")
        self.gridLayout_5.addWidget(self.BAll, 0, 2, 1, 1)
        self.BSearch = QtGui.QPushButton(self.centralwidget)

        self.BSearch.setFont(self.font_base)
        self.BSearch.setObjectName("BConjugate")
        self.gridLayout_5.addWidget(self.BSearch, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.TabVoice = QtGui.QTabWidget(self.centralwidget)

        self.TabVoice.setFont(self.font_base)
        self.TabVoice.setObjectName("TabVoice")
        self.TabActiveVoice = QtGui.QWidget()
        self.TabActiveVoice.setObjectName("TabActiveVoice")
        self.gridLayout_2 = QtGui.QGridLayout(self.TabActiveVoice)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabActiveResult = QtGui.QTableWidget(self.TabActiveVoice)

        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setObjectName("TabActiveResult")
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setRowCount(14)

        for i in range(14):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabActiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabActiveResult.setHorizontalHeaderItem(i,  emptyitem)

        self.gridLayout_2.addWidget(self.TabActiveResult, 0, 0, 1, 1)
        self.TabVoice.addTab(self.TabActiveVoice, "")

        self.TabPassiveVoice = QtGui.QWidget()

        self.gridLayout_2p = QtGui.QGridLayout(self.TabPassiveVoice)
        self.gridLayout_2p.setObjectName("gridLayout_2p")
        self.TabPassiveVoice.setObjectName("TabPassiveVoice")
        self.TabPassiveResult = QtGui.QTableWidget(self.TabPassiveVoice)

        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setObjectName("TabPassiveResult")
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setRowCount(14)
        for i in range(14):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabPassiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabPassiveResult.setHorizontalHeaderItem(i,  emptyitem)
        self.gridLayout_2p.addWidget(self.TabPassiveResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabPassiveVoice, "")
        self.gridLayout.addWidget(self.TabVoice, 1, 0, 1, 1)

#---------------------------------------
        self.TabVerbAttributs = QtGui.QWidget()

        self.gridLayout_vt = QtGui.QGridLayout(self.TabVerbAttributs)
        self.gridLayout_vt.setObjectName("gridLayout_vt")
        self.TabVerbAttributs.setObjectName("TabVerbAttributs")
        self.TabVerbAttributsResult = QtGui.QTableWidget(self.TabVerbAttributs)

        self.TabVerbAttributsResult.setFont(self.font_result)
        self.TabVerbAttributsResult.setColumnCount(1)
        self.TabVerbAttributsResult.setObjectName("TabVerbAttributsResult")
        self.TabVerbAttributsResult.setRowCount(5)
        emptyitem = QtGui.QTableWidgetItem()
        self.TabVerbAttributsResult.setHorizontalHeaderItem(0, emptyitem)
        self.gridLayout_vt.addWidget(self.TabVerbAttributsResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabVerbAttributs, "")
#---------------------------------------
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtGui.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtGui.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
# Menu Right to Left
        self.menu.setLayoutDirection(RightToLeft);
        self.menu_2.setLayoutDirection(RightToLeft);
        self.menu_3.setLayoutDirection(RightToLeft);
        self.menu_4.setLayoutDirection(RightToLeft);
        self.menu_5.setLayoutDirection(RightToLeft);

        MainWindow.setMenuBar(self.menubar)
#---------Actions
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.AExport = QtGui.QAction(MainWindow)
        self.AExport.setObjectName("AExport")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExport.setIcon(icon)
        self.AExit = QtGui.QAction(MainWindow)
        self.AExit.setObjectName("AExit")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExit.setIcon(icon)
        self.AFont = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("ar/images/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AFont.setIcon(icon)
        self.AFont.setObjectName("AFont")
        self.AAbout = QtGui.QAction(MainWindow)
        self.AAbout.setObjectName("AAbout")
        self.AManual = QtGui.QAction(MainWindow)
        self.AManual.setObjectName("AManual")
        self.ACopy = QtGui.QAction(MainWindow)
        self.ACopy.setObjectName("ACopy")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ACopy.setIcon(icon)
        self.AWhoisqutrub = QtGui.QAction(MainWindow)
        self.AWhoisqutrub.setObjectName("AWhoisqutrub")
        self.ASetting = QtGui.QAction(MainWindow)
        self.ASetting.setObjectName("ASetting")
        self.APrint = QtGui.QAction(MainWindow)
        self.APrint.setObjectName("APrint")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrint.setIcon(icon)
        self.APrintPreview = QtGui.QAction(MainWindow)
        self.APrintPreview.setObjectName("APrintPreview")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrintPreview.setIcon(icon)
        self.APagesetup = QtGui.QAction(MainWindow)
        self.APagesetup.setObjectName("APagesetup")
        self.AZoomIn = QtGui.QAction(MainWindow)
        self.AZoomIn.setObjectName("AZoomin")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomIn.setIcon(icon)
        self.AZoomOut = QtGui.QAction(MainWindow)
        self.AZoomOut.setObjectName("AZoomOut")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomOut.setIcon(icon)
#-------Menu--------------------
        self.menu.addAction(self.AExport)
#ToDo1
##        self.menu.addAction(self.APagesetup)
        self.menu.addSeparator()

        self.menu.addAction(self.APrint)

#ToDo1
##        self.menu.addAction(self.APrintPreview)
        self.menu.addAction(self.AExit)
        self.menu_2.addAction(self.AFont)
        self.menu_2.addAction(self.AZoomIn)
        self.menu_2.addAction(self.AZoomOut)
        self.menu_3.addAction(self.AAbout)
        self.menu_3.addAction(self.AManual)
        self.menu_3.addAction(self.AWhoisqutrub)
        self.menu_4.addAction(self.ACopy)
        self.menu_5.addAction(self.ASetting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.AFont)
        self.toolBar.addAction(self.ACopy)
        self.toolBar.addAction(self.AExport)
        self.toolBar.addAction(self.APrint)
#ToDo 2
##        self.toolBar.addAction(self.APrintPreview)
        self.toolBar.addAction(self.AZoomIn)
        self.toolBar.addAction(self.AZoomOut)
        self.retranslateUi(MainWindow)
        self.TabVoice.setCurrentIndex(0)

        self.Tsearch.setText(u"كَتَبَ");

        QtCore.QObject.connect(self.BSearch, QtCore.SIGNAL("clicked()"), self.display_result)
        QtCore.QObject.connect(self.Tsearch, QtCore.SIGNAL("textChanged(QString)"), self.validate_verb)
        QtCore.QObject.connect(self.BAll, QtCore.SIGNAL("clicked()"), self.check_alltenses)
        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.APrint, QtCore.SIGNAL("triggered()"), self.print_result)
        QtCore.QObject.connect(self.APrintPreview, QtCore.SIGNAL("triggered()"), self.print_preview)
        QtCore.QObject.connect(self.AFont, QtCore.SIGNAL("triggered()"), self.change_font)
        QtCore.QObject.connect(self.AAbout, QtCore.SIGNAL("triggered()"), self.about)
        QtCore.QObject.connect(self.AWhoisqutrub, QtCore.SIGNAL("triggered()"), self.whoisqutrub)
        QtCore.QObject.connect(self.AManual, QtCore.SIGNAL("triggered()"), self.manual)
        QtCore.QObject.connect(self.AExport, QtCore.SIGNAL("triggered()"), self.save_result)
        QtCore.QObject.connect(self.AZoomIn, QtCore.SIGNAL("triggered()"), self.zoomin)
        QtCore.QObject.connect(self.AZoomOut, QtCore.SIGNAL("triggered()"), self.zoomout)
        QtCore.QObject.connect(self.BMoreOptions, QtCore.SIGNAL("clicked()"), self.show_options)
        QtCore.QObject.connect(self.ASetting, QtCore.SIGNAL("triggered()"), self.set_setting)
        QtCore.QObject.connect(self.APagesetup, QtCore.SIGNAL("triggered()"), self.page_setup)
        QtCore.QObject.connect(self.ACopy, QtCore.SIGNAL("triggered()"), self.set_copy)
        QtCore.QObject.connect(self.CBSuggest, QtCore.SIGNAL("activated(int)"), self.selectSuggest)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #---------

        self.BAll.setChecked(True);
        self.BFuture.setEnabled(False);
        self.BPast.setEnabled(False);
        self.BImperative.setEnabled(False);
        self.BPassive.setEnabled(False);
        self.BConfirmed.setEnabled(False);
        self.BFuture_moode.setEnabled(False);

        self.BFuture.hide();
        self.BPast.hide();
        self.BImperative.hide();
        self.BPassive.hide();
        self.BConfirmed.hide();
        self.BFuture_moode.hide();
# disable unallowed actions
        self.AExport.setEnabled(False)
        self.AFont.setEnabled(False)
        self.ACopy.setEnabled(False)
        self.APrint.setEnabled(False)
        self.APrintPreview.setEnabled(False)
        self.APagesetup.setEnabled(False)
        self.AZoomIn.setEnabled(False)
        self.AZoomOut.setEnabled(False)

        self.result={};
        self.TabVoice.hide();
        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("toggled(bool)"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readSettings();
        self.applySettings();
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/qaf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "قطرب: تصريف الأفعال العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_2.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.BPast.setText(QtGui.QApplication.translate("MainWindow", "الماضي", None, QtGui.QApplication.UnicodeUTF8))
        self.BFuture.setText(QtGui.QApplication.translate("MainWindow", "المضارع", None, QtGui.QApplication.UnicodeUTF8))
        self.BImperative.setText(QtGui.QApplication.translate("MainWindow", "الأمر", None, QtGui.QApplication.UnicodeUTF8))
        self.BPassive.setText(QtGui.QApplication.translate("MainWindow", "المبني للمجهول", None, QtGui.QApplication.UnicodeUTF8))
        self.Tsearch.setToolTip(QtGui.QApplication.translate("MainWindow", "<html dir=\'rtl\'>\n"
"<body>\n"
"<ol>\n"
"  <li>اكتب الفعل مشكولا شكلا تاما\n"
"(الحركات والشدة ) في خانة الفعل مثال\n"
":\n"
"كَتَبَ، كَاتَبَ. </li>\n"
"  <li>ملاحظة إذا كان الفعل مهموز\n"
"الأول على وزن فاعل،مثل آخى يرجى كتابته على الشكل ءَاخَى. </li>\n"
"  <li>إذا كان الفعل ثلاثيا حدد\n"
"حركة عين الفعل في المضارع، مثلا كتب يكتُب تأخذ الحركة ضمة في المضارع.\n"
"إذا كان الفعل غير ثلاثي، تجاهل هذه الميزة. </li>\n"
"  <li>حدد اللزوم والتعدي للفعل، </li>\n"
"  <li>اختر الزمن الذي تريد\n"
"التصريف فيه </li>\n"
"  <li>اضغط على \"صرّف الفعل\".</li>\n"
"</ol>\n"
"</body>", None, QtGui.QApplication.UnicodeUTF8))
        self.BFuture_moode.setText(QtGui.QApplication.translate("MainWindow", "المضارع المنصوب والمجزوم", None, QtGui.QApplication.UnicodeUTF8))
        self.BConfirmed.setText(QtGui.QApplication.translate("MainWindow", "المؤكد ", None, QtGui.QApplication.UnicodeUTF8))
        self.BTransitive.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">حدد اللزوم والتعدي للفعل</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BTransitive.setText(QtGui.QApplication.translate("MainWindow", "متعدي", None, QtGui.QApplication.UnicodeUTF8))
        self.BAll.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">اختر الزمن الذي تريد التصريف فيه</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BAll.setText(QtGui.QApplication.translate("MainWindow", "كل الأزمنة", None, QtGui.QApplication.UnicodeUTF8))
        self.BSearch.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">صرف الفعل</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BSearch.setText(QtGui.QApplication.translate("MainWindow", "تصريف", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "أنا", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "نحن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "أنت", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "أنتِ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "أنتما", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "أنتما مؤ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "أنتم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "أنتن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "هو", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(9).setText(QtGui.QApplication.translate("MainWindow", "هي", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(10).setText(QtGui.QApplication.translate("MainWindow", "هما", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(11).setText(QtGui.QApplication.translate("MainWindow", "هما مؤ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(12).setText(QtGui.QApplication.translate("MainWindow", "هم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.verticalHeaderItem(13).setText(QtGui.QApplication.translate("MainWindow", "هن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "الماضي", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "المضارع المرفوع", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "المضارع المنصوب", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "المضارع المجزوم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "المضارع المؤكد المجهول", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "الأمر", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabActiveResult.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "الأمر المؤكد", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabActiveVoice), QtGui.QApplication.translate("MainWindow", "المبني للمعلوم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "أنا", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "نحن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "أنت", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "أنتِ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "أنتما", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "أنتما مؤ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "أنتم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "أنتن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "هو", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(9).setText(QtGui.QApplication.translate("MainWindow", "هي", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(10).setText(QtGui.QApplication.translate("MainWindow", "هما", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(11).setText(QtGui.QApplication.translate("MainWindow", "هما مؤ", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(12).setText(QtGui.QApplication.translate("MainWindow", "هم", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.verticalHeaderItem(13).setText(QtGui.QApplication.translate("MainWindow", "هن", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "الماضي المجهول", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "المضارع المرفوع المجهول", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "المضارع المنصوب المجهول", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "المضارع المجزوم المجهول", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabPassiveResult.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "المضارع المؤكد المجهول", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabPassiveVoice), QtGui.QApplication.translate("MainWindow", "نتائج البحث", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabVerbAttributs), QtGui.QApplication.translate("MainWindow", "خصائص الفعل", None, QtGui.QApplication.UnicodeUTF8))
##        self.TabVerbAttributsResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "القيمة", None, QtGui.QApplication.UnicodeUTF8))

        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "ملف", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "عرض", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_3.setTitle(QtGui.QApplication.translate("MainWindow", "مساعدة", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_4.setTitle(QtGui.QApplication.translate("MainWindow", "تحرير", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_5.setTitle(QtGui.QApplication.translate("MainWindow", "أدوات", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.AExport.setText(QtGui.QApplication.translate("MainWindow", "ت&صدير", None, QtGui.QApplication.UnicodeUTF8))
        self.AExit.setText(QtGui.QApplication.translate("MainWindow", "&خروج", None, QtGui.QApplication.UnicodeUTF8))
        self.AFont.setText(QtGui.QApplication.translate("MainWindow", "خط", None, QtGui.QApplication.UnicodeUTF8))

        self.AAbout.setText(QtGui.QApplication.translate("MainWindow", "حول البرنامج", None, QtGui.QApplication.UnicodeUTF8))
        self.AManual.setText(QtGui.QApplication.translate("MainWindow", "دليل الاستعمال", None, QtGui.QApplication.UnicodeUTF8))
        self.ACopy.setText(QtGui.QApplication.translate("MainWindow", "نسخ", None, QtGui.QApplication.UnicodeUTF8))
        self.AWhoisqutrub.setText(QtGui.QApplication.translate("MainWindow", "من هو قطرب؟", None, QtGui.QApplication.UnicodeUTF8))
        self.ASetting.setText(QtGui.QApplication.translate("MainWindow", "تفضيلات", None, QtGui.QApplication.UnicodeUTF8))
        self.APrint.setText(QtGui.QApplication.translate("MainWindow", "طباعة...", None, QtGui.QApplication.UnicodeUTF8))
        self.APrintPreview.setText(QtGui.QApplication.translate("MainWindow", "معاينة الطباعة", None, QtGui.QApplication.UnicodeUTF8))
        self.APagesetup.setText(QtGui.QApplication.translate("MainWindow", "إعداد الصفحة", None, QtGui.QApplication.UnicodeUTF8))
        self.AZoomIn.setText(QtGui.QApplication.translate("MainWindow", "تكبير", None, QtGui.QApplication.UnicodeUTF8))
        self.AZoomOut.setText(QtGui.QApplication.translate("MainWindow", "تصغير", None, QtGui.QApplication.UnicodeUTF8))

    def validate_verb(self):
        pass;
##        word = self.Tsearch.text();
##        self.CBHaraka.setEnabled(False);
##        if not word.isEmpty():
####            self.save_result();
##            word=unicode(word);
##            word = word.strip(' ');
##            if not is_valid_arabic_word(word):
####                self.Tsearch.setToolTip(u"الفعل %s غير صالح"%word)
##                QtGui.QToolTip.showText(self.Tsearch.geometry().bottomRight(),
##                            u"الفعل  غير صالح",self.Tsearch)
##                self.Tsearch.setStyleSheet ("QLineEdit { color: red;}")
##
##
##            else:
##                self.CBHaraka.setEnabled(is_triliteral_verb(word));
##                self.Tsearch.setStyleSheet ("QLineEdit { color: black;}")
##        else:
##            self.Tsearch.setStyleSheet ("QLineEdit { color: black;}")


    def check_alltenses(self):
        pass;
##        if self.BAll.checkState()!=0:
##            check=True;
##            self.BFuture.hide();
##            self.BPast.hide();
##            self.BImperative.hide();
##            self.BPassive.hide();
##            self.BConfirmed.hide();
##            self.BFuture_moode.hide();
##        else:
##            check=False;
##            self.BFuture.show();
##            self.BPast.show();
##            self.BImperative.show();
##            self.BPassive.show();
##            self.BConfirmed.show();
##            self.BFuture_moode.show();
####            self.BFuture.setEnabled(False);
##        self.BFuture.setEnabled(not check);
##        self.BPast.setEnabled(not check);
##        self.BImperative.setEnabled(not check);
##        self.BPassive.setEnabled(not check);
##        self.BConfirmed.setEnabled(not check);
##        self.BFuture_moode.setEnabled(not check);
##
##        self.BFuture.setChecked(check);
##        self.BPast.setChecked(check);
##        self.BImperative.setChecked(check);
##        self.BPassive.setChecked(check);
##        self.BConfirmed.setChecked(check);
##        self.BFuture_moode.setChecked(check);

    def show_options(self):
        pass;
##        if self.BMoreOptions.checkState()!=0:
##            self.CBHaraka.show();
##            self.CBHarakaLabel.show();
##            self.BDict.show();
##        else:
##            self.CBHaraka.hide();
##            self.CBHarakaLabel.hide();
##            self.BDict.hide();

    def restore_default_font(self):
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        fonttext=self.font_result.family()+"[%s]"%str(self.font_result.pointSize())
        self.TSettingFontResult.setText(fonttext)
        self.TSettingFontResult.update()
##        self.centralwidget.update();
    def change_font(self):
        newfont,ok = QtGui.QFontDialog.getFont(self.font_result);
        if ok:
            self.font_result=newfont;
            self.TabActiveResult.setFont(self.font_result)
            self.TabActiveResult.update();
            self.TabPassiveResult.setFont(self.font_result)
            self.TabPassiveResult.update();
##            self.writeSettings();

##            self.centralwidget.update();
    def zoomin(self):
        self.font_result.setPointSize(self.font_result.pointSize()+1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def zoomout(self):
        self.font_result.setPointSize(self.font_result.pointSize()-1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def set_copy(self):
        if self.result.has_key("TEXT"):
            QtGui.QApplication.clipboard().setText(self.result["TEXT"])
            #QtGui.QClipboard.setText(self.result["HTML"])

    def page_setup(self):
        pass;
    def print_preview(self):
        pass;
#ToDo 1
    def generate_preview(self,other):
        pass;

    def print_result(self):
        if self.result.has_key("HTML"):
            data=QtCore.QFile("ar/style.css");
            if (data.open(QtCore.QFile.ReadOnly)):
                mySTYLE_SHEET=QtCore.QTextStream(data).readAll();
    ##            text=unicode(text);
            else:
                mySTYLE_SHEET=u"""
body {
	direction: rtl;
	font-family: Traditional Arabic, "Times New Roman";
	font-size: 16pt;
}
"""
            document = QtGui.QTextDocument("")
            document.setDefaultStyleSheet(mySTYLE_SHEET)
            self.result["HTML"]=u"<html dir=rtl><body dir='rtl'>"+self.result["HTML"]+"</body></html>"
            document.setHtml(self.result["HTML"]);
            printer = QtGui.QPrinter()

            dlg = QtGui.QPrintDialog(printer, self.centralwidget)
            if dlg.exec_() != QtGui.QDialog.Accepted:
                return

            document.print_(printer)
        else:
            QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"لا شيء يمكن طبعه، صرّف أولا")


##    def set_setting(self):
##        QtGui.QMessageBox.warning(self.centralwidget,U"عذرا",
##                                u"غير متوفر حاليا")
    def set_setting(self):
        init_Dialog=QtGui.QDialog(self.centralwidget)
        Dialog=Ui_Dialog();
        Dialog.setupUi(init_Dialog);
        if init_Dialog.exec_() == QtGui.QDialog.Accepted:
            self.readSettings();
            self.applySettings();



    def readSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        family=settings.value("font_base_family", QtCore.QVariant(QtCore.QString("Traditional Arabic"))).toString()
        size,ok=settings.value("font_base_size", QtCore.QVariant(12)).toInt();
        if not ok:size=12;
        bold=settings.value("font_base_bold", QtCore.QVariant(True)).toBool()
        self.font_result.setFamily(family)
        self.font_result.setPointSize(size)
        self.font_result.setBold(bold)
        #read of dictsetting options
        dictsetting,ok=settings.value("DictSetting", QtCore.QVariant(1)).toInt();
        if not ok:dictsetting=1;

        self.BDictOption=dictsetting;
    def applySettings(self):
        self.BDict.setChecked(self.BDictOption!=0)
        self.TabActiveResult.update();
        self.TabPassiveResult.update();

    def page_setup(self):
        QtGui.QMessageBox.warning(self.centralwidget,U"عذرا",
                                u"غير متوفر حاليا")


    def whoisqutrub(self):
        data=QtCore.QFile("ar/qutrub_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=u"لا يمكن فتح ملف المساعدة"

        Dialog=QtGui.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(u'من هو قطرب؟')
        gridLayout = QtGui.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtGui.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtGui.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)
        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        textBrowser.setText(text)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();


    def manual(self):
        data=QtCore.QFile("ar/help_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=u"لا يمكن فتح ملف المساعدة"

        Dialog=QtGui.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(u'من هو قطرب؟')
        gridLayout = QtGui.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtGui.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtGui.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)


        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        text2=unicode(text)
        print type(text2)
        textBrowser.setText(text2)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();

    def about(self):
        RightToLeft=1;
        msgBox=QtGui.QMessageBox(self.centralwidget);
        msgBox.setWindowTitle(u"عن برنامج قطرب");
##          msgBox.setTextFormat(QrCore.QRichText);

        data=QtCore.QFile("ar/about.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text_about=textstream.readAll();
        else:
#            text=u"لا يمكن فتح ملف المساعدة"
            text_about=u"""<h1>فكرة</h1>
يقوم البرنامج
بتصريف الأفعال المدخلة مع بعض المعلومات
الضرورية لتوليد جميع أشكال التصريف في الأزمنة المختلفة.<br>
هدف البرنامج هو تمكين تصريف الأفعال العربية تصريفا آليا مبسطا.<br>
</p>
<b>موقع المشروع</b>
<a href="http://qutrub.arabeyes.org">http://qutrub.arabeyes.org</a><br>
<b>المطور </b>
<a href="mailto:taha_zerrouki@gawab.com">طه زروقي</a><br>
<hr/>
<h3>شكر خاص </h3>
<ul>
  <li>برمجة الويب :مصطفى عمارة  (<a href='http://moustafaemara.wordpress.com/'>moustafaemara.wordpress.com</a>) </li>
  <li>تصميم الشعار : عصام حمود (<a href="http://hamoudart.com/">hamoudart.com/</a>)</li>
<li>عيون العرب <a href='http://www.arabeyes.org'>arabeyes.org</a></li>
<li>التقنيين العرب <a href='http://www.arabtechies.net'>arabtechies.net</a></li>
</ul>

"""
        msgBox.setText(text_about);
        msgBox.setLayoutDirection(RightToLeft);
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
        msgBox.setIconPixmap(QtGui.QPixmap("images/logo.jpg"));
        msgBox.setDefaultButton(QtGui.QMessageBox.Ok);
        msgBox.exec_();
##          QtGui.QMessageBox.about(self.centralwidget,U"عن البرنامج",
##                                u"اسم ملف غير مناسب %s"%filename);
    def save_result(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.centralwidget,
        u"حفظ ملف","untitled","HTML document (*.html *.htm);;Text file (*.txt);;Text Unicode comma separeted format file (*.csv);;XML file (*.xml);;TeX file (*.tex)");
        if filename:
            filename=unicode(filename)
            tuple=filename.split(".");
            if len(tuple)>=2:
                extention=tuple.pop();
            else:
                extention="html";
                filename+="."+extention
            text=""
            if extention.lower() in ('html','tex','txt','xml','csv'):
                display_format=extention.upper();
            #Add text generation
                if not self.result.has_key(extention.upper()):
                    QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"لا بيانات للتصدير، صرّف أولا")
                    return None;
                text+=self.result[extention.upper()];
            else:
                QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"اسم ملف غير مناسب %s"%filename)
            try:
                file_saved=open(filename,'w+');
                if file_saved:
                    file_saved.write(text.encode("utf8"));
                    file_saved.flush();
                    file_saved.close();

                else:
                    QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"لا يمكن فتح الملف %s"%filename)
            except:
                QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"لا يمكن حفظ الملف %s"%filename)





    def display_result(self):

        word = self.Tsearch.text();
        if not word.isEmpty():

            word=unicode(word);
            word = word.strip(' ');
            if not is_valid_arabic_word(word):

                QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                            u"كلمة  %s غير صالحة  "%word)
                self.Tsearch.clear();
                self.Tsearch.setFocus();

            else:
                print " result";
                language="arabic"
                lexique="office"
                result=search_word(word,language,lexique)
##                print result;
                self.result["TABLE"]=result;
                self.display_result_in_grid();


    def display_result_in_grid(self):

        rslt_tab=self.result["TABLE"];
        print rslt_tab;
# display in grid
        self.TabActiveResult.clear();

# display languages in columns labels



        if len(rslt_tab)>0:
            j=0;
            for k in rslt_tab[0].keys():
                self.TabActiveResult.setHorizontalHeaderItem(j,QtGui.QTableWidgetItem(display_language(k)))
                for i in range(len(rslt_tab)):
                    print i,j;
                    self.TabActiveResult.setItem(i,j,QtGui.QTableWidgetItem(rslt_tab[i][k]))
                j+=1;
# resize cells to content
        self.TabActiveResult.resizeColumnsToContents();
        self.TabActiveResult.resizeRowsToContents();

        #show result /
        self.TabVoice.show();
        self.MainWindow.showMaximized();
        self.TabVoice.setCurrentIndex(0);
        self.centralwidget.update();

def display_language(lang):
    return lang;

import lexique_rc
