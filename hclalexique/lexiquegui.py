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
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        self.result={}
        self.language="arabic"
        self.SuggestedVerbList=[];
#-----------------------------------------------
        self.font_base = QtGui.QFont()
        self.font_base.setFamily("KacstOne")
        self.font_base.setPointSize(12)
        self.font_base.setBold(True)



        RightToLeft=1;
        MainWindow.setLayoutDirection(RightToLeft)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(789, 593)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
##        self.Label = QtGui.QLabel(self.centralwidget)
##        self.Label.setObjectName("Label")
##        self.gridLayout_3.addWidget(self.Label, 1, 1, 1, 1)
##        self.Label_2 = QtGui.QLabel(self.centralwidget)
##        self.Label_2.setObjectName("Label_2")
##        self.gridLayout_3.addWidget(self.Label_2, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TSearch = QtGui.QLineEdit(self.centralwidget)
        self.TSearch.setEnabled(True)
        self.TSearch.setMaximumSize(QtCore.QSize(200, 40))

        self.TSearch.setFont(self.font_result)
        self.TSearch.setObjectName("TSearch")
        self.gridLayout_5.addWidget(self.TSearch, 0, 0, 1, 1)
        self.CBLexique = QtGui.QComboBox(self.centralwidget)
        self.CBLexique.setObjectName("CBLexique")

# add lexique
        self.tab_lexique=load_lexique();
        for i in range(len(self.tab_lexique)):
            name=self.tab_lexique[i]["name"]
##            print name;
            self.CBLexique.addItem(QtCore.QString())
            self.CBLexique.setItemText(i,self.tab_lexique[i]["title"])
##        self.CBLexique.addItem(QtCore.QString())
##        self.CBLexique.addItem(QtCore.QString())

        self.gridLayout_5.addWidget(self.CBLexique, 0, 5, 1, 1)
        self.CBLanguage= QtGui.QComboBox(self.centralwidget)
        self.CBLanguage.setObjectName("CBLanguage")
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.CBLanguage.addItem(QtCore.QString())
        self.gridLayout_5.addWidget(self.CBLanguage, 0, 2, 1, 1)
        self.BSearch = QtGui.QPushButton(self.centralwidget)

        self.BSearch.setFont(self.font_base)
        self.BSearch.setObjectName("BSearch")
        self.gridLayout_5.addWidget(self.BSearch, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.TabVoice = QtGui.QTabWidget(self.centralwidget)
        self.TabVoice.setFont(self.font_base)
        self.TabVoice.setObjectName("TabVoice")
        self.TabResult = QtGui.QWidget()
        self.TabResult.setObjectName("TabResult")
        self.gridLayout_2 = QtGui.QGridLayout(self.TabResult)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabActiveResult = QtGui.QTableWidget(self.TabResult)
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.setRowCount(25)
        self.TabActiveResult.setColumnCount(3)
        self.TabActiveResult.setObjectName("TabActiveResult")
        self.TabActiveResult.setColumnCount(3)
        self.TabActiveResult.setRowCount(25)
        item = QtGui.QTableWidgetItem()
        self.TabActiveResult.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TabActiveResult.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.TabActiveResult.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.TabActiveResult, 0, 0, 1, 1)
        self.TabVoice.addTab(self.TabResult, "")
        self.gridLayout.addWidget(self.TabVoice, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setLayoutDirection(RightToLeft)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
##        self.menu_6 = QtGui.QMenu(self.menu)
##        self.menu_6.setObjectName("menu_6")
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtGui.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.AExport = QtGui.QAction(MainWindow)
        self.AExport.setObjectName("AExport")
        self.AExit = QtGui.QAction(MainWindow)
        self.AExit.setObjectName("AExit")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ar/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExport.setIcon(icon)
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
        icon.addPixmap(QtGui.QPixmap("ar/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ACopy.setIcon(icon)
        self.AWhoisqutrub = QtGui.QAction(MainWindow)
        self.AWhoisqutrub.setObjectName("AWhoisqutrub")
        self.ASetting = QtGui.QAction(MainWindow)
        self.ASetting.setObjectName("ASetting")
        self.APrint = QtGui.QAction(MainWindow)
        self.APrint.setObjectName("APrint")
        icon.addPixmap(QtGui.QPixmap("ar/images/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrint.setIcon(icon)
##        self.APageSetup = QtGui.QAction(MainWindow)
##        self.APageSetup.setObjectName("APageSetup")
        self.menu.addAction(self.AExport)
##        self.menu.addAction(self.APageSetup)
        self.menu.addSeparator()
##        self.menu.addAction(self.menu_6.menuAction())
        self.menu.addAction(self.APrint)
        self.menu.addAction(self.AExit)
        self.menu_2.addAction(self.AFont)
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

#tool bar
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

        self.TSearch.setText(u"كَتَبَ");

        QtCore.QObject.connect(self.BSearch, QtCore.SIGNAL("clicked()"), self.display_result)
        QtCore.QObject.connect(self.TSearch, QtCore.SIGNAL("returnPressed()"), self.display_result)

        QtCore.QObject.connect(self.CBLanguage, QtCore.SIGNAL("activated(int)"), self.change_language)

        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.APrint, QtCore.SIGNAL("triggered()"), self.print_result)

		##QtCore.QObject.connect(self.APrintPreview, QtCore.SIGNAL("triggered()"), self.print_preview)
        QtCore.QObject.connect(self.AFont, QtCore.SIGNAL("triggered()"), self.change_font)
        QtCore.QObject.connect(self.AAbout, QtCore.SIGNAL("triggered()"), self.about)
        QtCore.QObject.connect(self.AWhoisqutrub, QtCore.SIGNAL("triggered()"), self.whoisqutrub)
        QtCore.QObject.connect(self.AManual, QtCore.SIGNAL("triggered()"), self.manual)
        QtCore.QObject.connect(self.AExport, QtCore.SIGNAL("triggered()"), self.save_result)
        QtCore.QObject.connect(self.AZoomIn, QtCore.SIGNAL("triggered()"), self.zoomin)
        QtCore.QObject.connect(self.AZoomOut, QtCore.SIGNAL("triggered()"), self.zoomout)

        QtCore.QObject.connect(self.ASetting, QtCore.SIGNAL("triggered()"), self.set_setting)
        #QtCore.QObject.connect(self.APagesetup, QtCore.SIGNAL("triggered()"), self.page_setup)
        QtCore.QObject.connect(self.ACopy, QtCore.SIGNAL("triggered()"), self.set_copy)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #---------
# Menu Right to Left
        self.menu.setLayoutDirection(RightToLeft);
        self.menu_2.setLayoutDirection(RightToLeft);
        self.menu_3.setLayoutDirection(RightToLeft);
        self.menu_4.setLayoutDirection(RightToLeft);
        self.menu_5.setLayoutDirection(RightToLeft);

# disable unallowed actions
        self.AExport.setEnabled(False)
        self.AFont.setEnabled(False)
        self.ACopy.setEnabled(False)
        self.APrint.setEnabled(False)
        #self.APrintPreview.setEnabled(False)
       # self.APagesetup.setEnabled(False)
        self.AZoomIn.setEnabled(False)
        self.AZoomOut.setEnabled(False)

        self.result={};
        self.TabVoice.hide();
        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("toggled(bool)"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readSettings();
        self.applySettings();
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/small-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "دليل المصطلحات", None, QtGui.QApplication.UnicodeUTF8))
##        self.Label.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
##        self.Label_2.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.TSearch.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KacstOne\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">1-اكتب الكلمة التي تبحث عنها</p>\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">2- اختر لغة الكلمة</p>\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">3- اختر الدليل الذي تريده</p>\n"
"<p dir=\'rtl\' style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">4-اضغط على بحث</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
##        self.CBLexique.setItemText(0, QtGui.QApplication.translate("MainWindow", "دليل الموارد والوسائل العامة", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(0, QtGui.QApplication.translate("MainWindow", "العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(1, QtGui.QApplication.translate("MainWindow", "فرنسية", None, QtGui.QApplication.UnicodeUTF8))
        self.CBLanguage.setItemText(2, QtGui.QApplication.translate("MainWindow", "إنجليزية", None, QtGui.QApplication.UnicodeUTF8))
        self.BSearch.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ابحث</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BSearch.setText(QtGui.QApplication.translate("MainWindow", "بحث", None, QtGui.QApplication.UnicodeUTF8))
        self.TabActiveResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.TabActiveResult.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "الفرنسية", None, QtGui.QApplication.UnicodeUTF8))
        self.TabActiveResult.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "الإنجليزية", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabResult), QtGui.QApplication.translate("MainWindow", "النتائج", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "ملف", None, QtGui.QApplication.UnicodeUTF8))
##        self.menu_6.setTitle(QtGui.QApplication.translate("MainWindow", "معاينة قبل الطباعة", None, QtGui.QApplication.UnicodeUTF8))
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
        self.AWhoisqutrub.setText(QtGui.QApplication.translate("MainWindow", "عن المجلس الأعلى للغة العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.ASetting.setText(QtGui.QApplication.translate("MainWindow", "تفضيلات", None, QtGui.QApplication.UnicodeUTF8))
        self.APrint.setText(QtGui.QApplication.translate("MainWindow", "طباعة...", None, QtGui.QApplication.UnicodeUTF8))
##        self.APageSetup.setText(QtGui.QApplication.translate("MainWindow", "إعداد الصفحة", None, QtGui.QApplication.UnicodeUTF8))



    def validate_verb(self):
        pass;




    def change_language(self):
        if self.CBLanguage.currentIndex()==0:
            self.language="arabic"
        elif self.CBLanguage.currentIndex()==1:
            self.language="french"
        elif self.CBLanguage.currentIndex()==2:
            self.language="english"
        else:
            self.language="arabic"
#        print self.language;

    def currentLexique(self):
        if self.tab_lexique.has_key(self.CBLexique.currentIndex()):
            return self.tab_lexique[self.CBLexique.currentIndex()]["name"];

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
            # resize cells to content
            self.TabActiveResult.resizeColumnsToContents();
            self.TabActiveResult.resizeRowsToContents();
            self.TabActiveResult.update();


    def zoomin(self):
        self.font_result.setPointSize(self.font_result.pointSize()+1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();

    def zoomout(self):
        self.font_result.setPointSize(self.font_result.pointSize()-1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();

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
                                u"لا شيء يمكن طبعه.")


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
        #self.BDict.setChecked(self.BDictOption!=0)
        self.TabActiveResult.update();
        #self.TabPassiveResult.update();

    def page_setup(self):
        QtGui.QMessageBox.warning(self.centralwidget,U"عذرا",
                                u"غير متوفر حاليا")


    def whoisqutrub(self):
        data=QtCore.QFile("ar/hcla_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=u"لا يمكن فتح ملف المساعدة"

        Dialog=QtGui.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(u'تعريف المجلس')
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
        Dialog.setWindowTitle(u'دليل الاستعمال')
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
        #print type(text2)
        textBrowser.setText(text2)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();

    def about(self):
        RightToLeft=1;
        msgBox=QtGui.QMessageBox(self.centralwidget);
        msgBox.setWindowTitle(u"عن البرنامج");
##          msgBox.setTextFormat(QrCore.QRichText);

        data=QtCore.QFile("ar/about.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text_about=textstream.readAll();
        else:
#            text=u"لا يمكن فتح ملف المساعدة"
            text_about=u"""<h1>فكرة</h1>

"""
        msgBox.setText(text_about);
        msgBox.setLayoutDirection(RightToLeft);
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
        msgBox.setIconPixmap(QtGui.QPixmap("images/logo.png"));
        msgBox.setDefaultButton(QtGui.QMessageBox.Ok);
        msgBox.exec_();
##          QtGui.QMessageBox.about(self.centralwidget,U"عن البرنامج",
##                                u"اسم ملف غير مناسب %s"%filename);
    def save_result(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.centralwidget,
        u"حفظ ملف","untitled","HTML document (*.html *.htm);;Text file (*.txt);;Text Unicode comma separeted format file (*.csv);;XML file (*.xml)");
        if filename:
            filename=unicode(filename)
            tuple=filename.split(".");
            if len(tuple)>=2:
                extention=tuple.pop();
            else:
                extention="html";
                filename+="."+extention
            text=""
            if extention.lower() in ('html','txt','xml','csv'):
                display_format=extention.upper();
            #Add text generation
                if not self.result.has_key(extention.upper()):
                    QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                                u"لاشيء يمكن تصديره")
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

        word = self.TSearch.text();
        if not word.isEmpty():

            word=unicode(word);
            word = word.strip(' ');
#            if not is_valid_arabic_word(word):
            if False:

                QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                            u"كلمة  %s غير صالحة  "%word)
                self.TSearch.clear();
                self.TSearch.setFocus();

            else:
                #print " result";
##                language="arabic"
                lexique=self.currentLexique();
                #print lexique;
                result=search_word(word,self.language,lexique)
##                print result;
                self.result["TABLE"]=result;
                self.result["HTML"]=display_format(result,"HTML")
                self.result["XML"]=display_format(result,"XML")
                self.result["TEXT"]=display_format(result,"TEXT")
                self.result["CSV"]=display_format(result,"CSV")

                self.display_result_in_grid();


    def display_result_in_grid(self):

        rslt_tab=self.result["TABLE"];
        #print rslt_tab;
# display in grid
        self.TabActiveResult.clear();

# display languages in columns labels


        self.TabActiveResult.setRowCount(len(rslt_tab));
        if len(rslt_tab)>0:

            j=0;
            for k in rslt_tab[0].keys():
                self.TabActiveResult.setHorizontalHeaderItem(j,QtGui.QTableWidgetItem(display_language(k)))
                for i in range(len(rslt_tab)):
                    #print i,j;
                    self.TabActiveResult.setItem(i,j,QtGui.QTableWidgetItem(rslt_tab[i][k]))
                j+=1;
    # resize cells to content
            self.TabActiveResult.resizeColumnsToContents();
            self.TabActiveResult.resizeRowsToContents();

            #show result /
            self.TabVoice.show();
            self.MainWindow.showMaximized();
            self.TabVoice.setCurrentIndex(0);
    # enable actions
            self.AExport.setEnabled(True)
            self.AFont.setEnabled(True)
            self.ACopy.setEnabled(True)
            self.APrint.setEnabled(True)
            #self.APrintPreview.setEnabled(True)
            #self.APagesetup.setEnabled(True)
            self.AZoomIn.setEnabled(True)
            self.AZoomOut.setEnabled(True)
            self.centralwidget.update();
        else:
            QtGui.QMessageBox.warning(self.centralwidget,U"خطأ",
                            u"لا نتائج  ")



def display_language(lang):
    if lang=="arabic":
        return u"عربي"
    elif lang=="french":
        return u"فرنسي"
    elif lang=="english":
        return u"إنجليزي"
    return lang;

#ToDo
# load lexique information from a file
def load_lexique():
    tab_lexique={
    0:{'name':"office",'title':u"دليل المكتبية",'file':"data/officelexique.db",'table':"office"
    }
,
    1:{'name':"finance",'title':u"دليل التسيير المالي والمحاسبي",'file':"data/financelexique.db",'table':"finance"    }
,
    2:{'name':"mecanique",'title':u"تجهيز ميكانيكي",'file':"data/mecaniquelexique.db",'table':"mecanique"    }
    }
    return tab_lexique;


import lexique_rc
