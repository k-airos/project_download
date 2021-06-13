#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.Qt import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from bs4.element import Declaration
from pandas.core.reshape.concat import concat
import sqlalchemy
from sqlalchemy import create_engine
import mysql.connector
from sqlalchemy import engine
import parsing as pars
import update as up
import plotly
import main, graphs
import plotly.express as px 
import os, datetime
import pandas as pd
import plotly.offline as offline
from plotly.offline import plot
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from crontab import CronTab


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)


    def check_password(self):
        msg = QMessageBox()
        try:
            host = "127.0.0.1"
            global user
            user = self.lineEdit_username.text()
            global passw
            passw = self.lineEdit_password.text()
            f = open('text.txt','w')
            f.writelines([user+'..',passw])
            dbname = "MoES"
            mysql_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}'.format(user, passw, host))
            connection = mysql_engine.connect()
        except:
            msg.setText('Username/password incorrect')
            msg.exec_()
        else:
            msg.setText('Success')
            msg.exec_()
            form.hide()

    def closeEvent(msg, event):
        # Переопределить colseEvent
        reply = QMessageBox.question\
        (msg, 'Вы нажали на крестик',
            "Вы уверены, что хотите уйти?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            event.ignore()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, -1, 800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.firstTab = QtWidgets.QWidget()
        self.firstTab.setStyleSheet("tab_1{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"};")
        self.firstTab.setObjectName("firstTab")
        self.label = QtWidgets.QLabel(self.firstTab)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 17))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.firstTab)
        self.comboBox.setGeometry(QtCore.QRect(210, 20, 151, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.firstTab)
        self.pushButton.setGeometry(QtCore.QRect(390, 20, 131, 25))
        self.pushButton.setStyleSheet("#pushButton::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.firstTab)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.firstTab)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 191, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.firstTab)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 70, 131, 25))
        self.pushButton_2.setStyleSheet("#pushButton_2::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.firstTab)
        self.label_4.setGeometry(QtCore.QRect(10, 148, 191, 17))
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.firstTab)
        self.comboBox_4.setGeometry(QtCore.QRect(210, 148, 151, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.firstTab)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 148, 131, 25))
        self.pushButton_4.setStyleSheet("#pushButton_4::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.firstTab)
        self.comboBox_5.setGeometry(QtCore.QRect(620, 20, 151, 25))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_7 = QtWidgets.QLabel(self.firstTab)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 67, 17))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.firstTab)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 50, 150, 45))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.firstTab)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 220, 131, 25))
        self.pushButton_6.setStyleSheet("#pushButton_4::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(self.firstTab)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 191, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.firstTab)
        self.label_9.setGeometry(QtCore.QRect(180, 220, 191, 17))
        self.label_9.setObjectName("label_9")
        self.spinBox = QtWidgets.QSpinBox(self.firstTab)
        self.spinBox.setGeometry(QtCore.QRect(200, 220, 60, 26))
        self.spinBox.setMaximum(228)
        self.spinBox.setMinimum(1)
        self.spinBox.setSingleStep(5)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.label_10 = QtWidgets.QLabel(self.firstTab)
        self.label_10.setGeometry(QtCore.QRect(270, 220, 41, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.firstTab)
        self.label_11.setGeometry(QtCore.QRect(600, 220, 200, 17))
        self.label_11.setObjectName("label_11")
        self.spinBox_3 = QtWidgets.QSpinBox(self.firstTab)
        self.spinBox_3.setGeometry(QtCore.QRect(300, 220, 60, 26))
        self.spinBox_3.setMaximum(229)
        self.spinBox_3.setSingleStep(5)
        self.spinBox_3.setProperty("value", 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMinimum(1)
        self.pushButton_7 = QtWidgets.QPushButton(self.firstTab)
        self.pushButton_7.setGeometry(QtCore.QRect(260, 250, 51, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.firstTab)
        self.comboBox_6.setGeometry(QtCore.QRect(10, 240, 151, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.tabWidget.addTab(self.firstTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(60, 0, 94, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(60, 30, 94, 26))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(9, 9, 16, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 23, 17))
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 10, 89, 25))
        self.pushButton_5.setStyleSheet("#pushButton_5::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(600, 10, 89, 25))
        self.pushButton_9.setStyleSheet("#pushButton_5::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 70, 141, 25))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 70, 131, 25))
        self.pushButton_8.setStyleSheet("#pushButton_4::hover{\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(239, 41, 41);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.webView = QWebView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(10, 100, 771, 451))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(600, 70, 90, 35))
        self.pushButton_11.setObjectName("pushButton_11")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Актуализация данных:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Новости МЧС"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Новости регионов"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Происшествия"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Прогноз"))
        self.pushButton.setText(_translate("MainWindow", "Актуализировать"))
        self.label_2.setText(_translate("MainWindow", "Дамп:"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить"))
        self.label_4.setText(_translate("MainWindow", "Экспортирование в csv:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Новости МЧС"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Новости регионов"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Происшествия"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Прогноз"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Базу данных целиком"))
        self.pushButton_4.setText(_translate("MainWindow", "Экспортировать"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "5 min"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "30 min"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "1 hour"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "1 day"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "1 week"))
        self.pushButton_10.setText(_translate("MainWindow", "Актуализировать \n"
"по расписанию"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.firstTab), _translate("MainWindow", "База данных"))
        self.label_5.setText(_translate("MainWindow", "C:"))
        self.label_6.setText(_translate("MainWindow", "По:"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_9.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Отчеты"))
        self.pushButton_6.setText(_translate("MainWindow", "Заполнить"))
        self.label_8.setText(_translate("MainWindow", "Заполнение базы"))
        self.label_9.setText(_translate("MainWindow", "с"))
        self.label_10.setText(_translate("MainWindow", "по"))
        self.pushButton_7.setText(_translate("MainWindow", "жмяк"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Новости МЧС"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Новости регионов"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Происшествия"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Прогноз"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Новости МЧС"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Новости регионов"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Происшествия"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Прогноз"))
        self.pushButton_8.setText(_translate("MainWindow", "Сохранить в CSV"))
        self.pushButton_11.setText(_translate("MainWindow", "Сохранить \nв png"))

        self.pushButton.clicked.connect(self.getComboValue)
        self.pushButton_2.clicked.connect(self.createDumb)
        self.pushButton_4.clicked.connect(self.createCSV)
        self.pushButton_6.clicked.connect(self.toFill)
        self.pushButton_7.clicked.connect(self.checkLast)
        self.pushButton_5.clicked.connect(self.graph)
        self.pushButton_9.clicked.connect(self.clearGraph)
        self.pushButton_8.clicked.connect(self.dfToCSV)
        self.pushButton_11.clicked.connect(self.dfToPNG)
        self.pushButton_10.clicked.connect(self.timer)
        

    def getComboValue(self):
        try:
            text = self.comboBox.currentText()
            if(text == "Новости МЧС"):
                up.update("mchs_news",user,passw)
            if(text == "Новости регионов"):
                up.update("regional_news",user,passw)
            if(text == "Происшествия"):
                up.update("incidents",user,passw)
            if(text == "Прогноз"):
                up.update("forecasts",user,passw)
            if(text == "Базу данных целиком"):
                up.update("forecasts",user,passw)
                up.update("mchs_news",user,passw)
                up.update("regional_news",user,passw)
                up.update("incidents",user,passw)
        except sqlalchemy.exc.ProgrammingError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нет прав")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()
        except mysql.connector.errors.ProgrammingError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Выбранная вами таблица не существует\nВозможно, вы хотите хотите сначала ее заполнить?")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            pass

    def createDumb(self):
        try:
            os.mkdir("../Data")
        except:
            pass
        command = f'mysqldump --user={user} --password={passw} {dbname} > ../Data/dbexport.sql'
        if os.system(command) >0:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нет прав")
            msg.setIcon(QMessageBox.Warning)

    def createCSV(self):
        try:
            myTable = self.comboBox_4.currentText()
            current_date_time = datetime.datetime.now()
            current_time = current_date_time.time()
            if(myTable == "Новости МЧС"):
                myTable = "mchs_news"
            if(myTable == "Новости регионов"):
                myTable = "regional_news"
            if(myTable == "Происшествия"):
                myTable = "incidents"
            if(myTable == "Прогноз"):
                myTable = "forecasts"
            if(myTable == "Базу данных целиком"):
                myTable = "full"

            nameOfFile = myTable + str(current_time)
            db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user, passw, host,dbname))
            con = db_engine.raw_connection()
            cur = con.cursor()
            if myTable != "full":
                try:
                    cur.execute(f"""SELECT * FROM {myTable}
                                    INTO OUTFILE 'my{nameOfFile}.csv'
                                    FIELDS ENCLOSED BY '"'
                                    TERMINATED BY ';'
                                    ESCAPED BY '"'
                                    LINES TERMINATED BY '\r\n';
                                """)
                except mysql.connector.errors.DatabaseError:
                    pass
            else:
                a = ["mchs_news","regional_news","incidents","forecasts"]
                for i in a:
                    nameOfFile = i + str(current_time)
                    try:
                        cur.execute(f"""SELECT * FROM {i}
                                        INTO OUTFILE 'my{nameOfFile}.csv'
                                        FIELDS ENCLOSED BY '"'
                                        TERMINATED BY ';'
                                        ESCAPED BY '"'
                                        LINES TERMINATED BY '\r\n';
                                    """)
                    except mysql.connector.errors.DatabaseError:
                        pass
            con.close()
        except sqlalchemy.exc.ProgrammingError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нет прав")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
    


    def checkLast(self):
        try:
            myTable = self.comboBox_6.currentText()
            if(myTable == "Новости МЧС"):
                myTable = "mchs_news"
            if(myTable == "Новости регионов"):
                myTable = "regional_news"
            if(myTable == "Происшествия"):
                myTable = "incidents"
            if(myTable == "Прогноз"):
                myTable = "forecasts"
            lastPage = pars.find_last_page(myTable)
            self.spinBox_3.setMaximum(lastPage)
            self.spinBox_3.setSingleStep(5)
            self.spinBox_3.setProperty("value", lastPage)
        except:
            pass

    def toFill(self):
        try:
            myTable = self.comboBox_6.currentText()
            if(myTable == "Новости МЧС"):
                myTable = "mchs_news"
            if(myTable == "Новости регионов"):
                myTable = "regional_news"
            if(myTable == "Происшествия"):
                myTable = "incidents"
            if(myTable == "Прогноз"):
                myTable = "forecasts"
            lastPage = pars.find_last_page(myTable)
            if ((self.spinBox.value() > self.spinBox_3.value()) or (self.spinBox.value()>=lastPage) or (self.spinBox.value()>=lastPage)):
                self.label_11.setText("Введите данные корректно")
            else:
                self.label_11.setText(" ")
                main.Fill(self.spinBox.value(),self.spinBox_3.value(),myTable,user,passw)
        except sqlalchemy.exc.ProgrammingError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нет прав")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            pass

    def graph(self):
        myTable = self.comboBox_7.currentText()
        if(myTable == "Новости МЧС"):
            myTable = "mchs_news"
        if(myTable == "Новости регионов"):
            myTable = "regional_news"
        if(myTable == "Происшествия"):
            myTable = "incidents"
        if(myTable == "Прогноз"):
            myTable = "forecasts"
        myDateFrom = str(self.dateEdit.date().toPyDate())
        myDateTo = str(self.dateEdit_2.date().toPyDate())
        try:
            if 'myDataFrame' not in globals():
                global myDataFrame
                myDataFrame = graphs.DfForGraph(myDateFrom,myDateTo,myTable)
                fig = px.bar(myDataFrame, x="Происшествия", y="Количество", color="Даты", title="Данные за указанные периоды")
                plot = '<head><meta charset="utf-8" /></head>''<head><meta charset="utf-8" /><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
                plot += offline.plot(fig, output_type='div',include_plotlyjs=False)
                plot+='</body></html>'
                self.webView.setHtml(plot)
            else:
                df = graphs.DfForGraph(myDateFrom,myDateTo,myTable)
                if (df["Даты"][0] != myDataFrame["Даты"].iloc[-1]):
                    myDataFrame = pd.concat([myDataFrame, graphs.DfForGraph(myDateFrom,myDateTo,myTable)])
                    fig = px.bar(myDataFrame, x="Происшествия", y="Количество", color="Даты", title="Данные за указанные периоды")
                    plot = '<head><meta charset="utf-8" /></head>''<head><meta charset="utf-8" /><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
                    plot += offline.plot(fig, output_type='div',include_plotlyjs=False)
                    plot+='</body></html>'
                    self.webView.setHtml(plot)
        except mysql.connector.errors.ProgrammingError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нет прав/Нет такой таблицы в бд")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            pass

    def clearGraph(self):
        try:
            del globals()['myDataFrame']
        except:
            pass
        self.webView.setHtml('')
    
    def dfToCSV(self):
        try:
            os.mkdir("../Data")
        except:
            pass
        try:
            global myDataFrame
            myDataFrame.to_csv('../Data/myCSVdata.csv', encoding='utf-8', index=False)
        except NameError:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Нечего сохранять")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            pass

    
    def dfToPNG(self):
        global myDataFrame
        try:
            os.mkdir("../Data")
        except:
            pass
        try:
            global myDataFrame
            fig = px.bar(myDataFrame, x="Происшествия", y="Количество", color="Даты", title="Данные за указанные периоды")
            # offline.plot(fig, image='png')
            fig.write_image("../Data/myPlot.png")
        except:
            pass

    def timer(self):
        myTable = self.comboBox_5.currentText()
        up.updateForCron(myTable)
        


    


if __name__ == '__main__':
    host = "127.0.0.1"
    dbname = "MoES"
    app = QApplication(sys.argv)
    form = LoginForm()
    form.setWindowModality(Qt.ApplicationModal)
    form.show()
    MainWindow = QtWidgets.QMainWindow()
    gui = Ui_MainWindow()
    gui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())