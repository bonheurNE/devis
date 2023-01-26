# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_DevisMainWindow(object):
    def setupUi(self, DevisMainWindow):
        if not DevisMainWindow.objectName():
            DevisMainWindow.setObjectName(u"DevisMainWindow")
        DevisMainWindow.resize(588, 618)
        self.centralwidget = QWidget(DevisMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.our_socity_name = QLabel(self.frame)
        self.our_socity_name.setObjectName(u"our_socity_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.our_socity_name.setFont(font)

        self.horizontalLayout.addWidget(self.our_socity_name)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.our_cp_ville = QLabel(self.frame_2)
        self.our_cp_ville.setObjectName(u"our_cp_ville")

        self.gridLayout.addWidget(self.our_cp_ville, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.our_aadresse = QLabel(self.frame_2)
        self.our_aadresse.setObjectName(u"our_aadresse")

        self.gridLayout.addWidget(self.our_aadresse, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.our_telephone = QLabel(self.frame_2)
        self.our_telephone.setObjectName(u"our_telephone")

        self.gridLayout.addWidget(self.our_telephone, 2, 1, 1, 1)

        self.ou_url = QLabel(self.frame_2)
        self.ou_url.setObjectName(u"ou_url")

        self.gridLayout.addWidget(self.ou_url, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.devis_ref = QLabel(self.frame_6)
        self.devis_ref.setObjectName(u"devis_ref")

        self.gridLayout_2.addWidget(self.devis_ref, 0, 1, 1, 1)

        self.devis_date = QLabel(self.frame_6)
        self.devis_date.setObjectName(u"devis_date")

        self.gridLayout_2.addWidget(self.devis_date, 1, 1, 1, 1)

        self.devis_client_number = QLabel(self.frame_6)
        self.devis_client_number.setObjectName(u"devis_client_number")

        self.gridLayout_2.addWidget(self.devis_client_number, 2, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.client_address = QLabel(self.frame_7)
        self.client_address.setObjectName(u"client_address")

        self.gridLayout_3.addWidget(self.client_address, 1, 1, 1, 1)

        self.client_cp_ville = QLabel(self.frame_7)
        self.client_cp_ville.setObjectName(u"client_cp_ville")
        self.client_cp_ville.setFont(font1)

        self.gridLayout_3.addWidget(self.client_cp_ville, 2, 1, 1, 1)

        self.client_name = QLabel(self.frame_7)
        self.client_name.setObjectName(u"client_name")
        self.client_name.setFont(font2)

        self.gridLayout_3.addWidget(self.client_name, 0, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_17)

        self.project_description = QLabel(self.frame_8)
        self.project_description.setObjectName(u"project_description")

        self.horizontalLayout_3.addWidget(self.project_description)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.devis_table = QTableWidget(self.frame_9)
        if (self.devis_table.columnCount() < 4):
            self.devis_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.devis_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.devis_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.devis_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.devis_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.devis_table.rowCount() < 20):
            self.devis_table.setRowCount(20)
        self.devis_table.setObjectName(u"devis_table")
        self.devis_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.devis_table.setAlternatingRowColors(True)
        self.devis_table.setSortingEnabled(True)
        self.devis_table.setRowCount(20)
        self.devis_table.horizontalHeader().setCascadingSectionResizes(True)
        self.devis_table.horizontalHeader().setDefaultSectionSize(122)
        self.devis_table.horizontalHeader().setProperty("showSortIndicator", True)

        self.horizontalLayout_4.addWidget(self.devis_table)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.add_taxes_btn = QPushButton(self.frame_4)
        self.add_taxes_btn.setObjectName(u"add_taxes_btn")
        self.add_taxes_btn.setMinimumSize(QSize(0, 25))
        self.add_taxes_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.add_taxes_btn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.total_no_taxe = QLabel(self.frame_5)
        self.total_no_taxe.setObjectName(u"total_no_taxe")

        self.gridLayout_4.addWidget(self.total_no_taxe, 0, 1, 1, 1)

        self.tva = QLabel(self.frame_5)
        self.tva.setObjectName(u"tva")

        self.gridLayout_4.addWidget(self.tva, 1, 1, 1, 1)

        self.ful_total = QLabel(self.frame_5)
        self.ful_total.setObjectName(u"ful_total")

        self.gridLayout_4.addWidget(self.ful_total, 2, 1, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)

        self.print_btn = QPushButton(self.frame_5)
        self.print_btn.setObjectName(u"print_btn")
        self.print_btn.setMinimumSize(QSize(0, 30))
        self.print_btn.setFont(font1)

        self.gridLayout_4.addWidget(self.print_btn, 3, 1, 1, 1)

        self.save_btn = QPushButton(self.frame_5)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 30))
        self.save_btn.setFont(font1)

        self.gridLayout_4.addWidget(self.save_btn, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        DevisMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DevisMainWindow)

        QMetaObject.connectSlotsByName(DevisMainWindow)
    # setupUi

    def retranslateUi(self, DevisMainWindow):
        DevisMainWindow.setWindowTitle(QCoreApplication.translate("DevisMainWindow", u"DevisMainWindow", None))
        self.our_socity_name.setText(QCoreApplication.translate("DevisMainWindow", u"NO", None))
        self.label_2.setText(QCoreApplication.translate("DevisMainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:24pt;;\">DEVIS </span></p></body></html>", None))
        self.our_cp_ville.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.label_5.setText(QCoreApplication.translate("DevisMainWindow", u"R\u00e9f\u00e9rences Internet", None))
        self.our_aadresse.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.label.setText(QCoreApplication.translate("DevisMainWindow", u"Addresse", None))
        self.label_4.setText(QCoreApplication.translate("DevisMainWindow", u"T\u00e9l\u00e9phone", None))
        self.label_3.setText(QCoreApplication.translate("DevisMainWindow", u"CP Ville", None))
        self.our_telephone.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.ou_url.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.label_7.setText(QCoreApplication.translate("DevisMainWindow", u"Date          : ", None))
        self.label_8.setText(QCoreApplication.translate("DevisMainWindow", u"N\u00b0 Client     :", None))
        self.label_6.setText(QCoreApplication.translate("DevisMainWindow", u"R\u00e9f\u00e9rence : ", None))
        self.devis_ref.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.devis_date.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.devis_client_number.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.label_13.setText(QCoreApplication.translate("DevisMainWindow", u"Adresse", None))
        self.label_14.setText(QCoreApplication.translate("DevisMainWindow", u"CP Ville", None))
        self.client_address.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.client_cp_ville.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.client_name.setText(QCoreApplication.translate("DevisMainWindow", u"Soci\u00e9t\u00e9 et/ou Nom du client", None))
        self.label_17.setText(QCoreApplication.translate("DevisMainWindow", u"Intitul\u00e9: ", None))
        self.project_description.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        ___qtablewidgetitem = self.devis_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DevisMainWindow", u"Quantit\u00e9", None));
        ___qtablewidgetitem1 = self.devis_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DevisMainWindow", u"D\u00e9signation", None));
        ___qtablewidgetitem2 = self.devis_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DevisMainWindow", u"Prix unitaire HT", None));
        ___qtablewidgetitem3 = self.devis_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DevisMainWindow", u"Prix total HT", None));
        self.add_taxes_btn.setText(QCoreApplication.translate("DevisMainWindow", u"ADD TAXES", None))
        self.total_no_taxe.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.tva.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.ful_total.setText(QCoreApplication.translate("DevisMainWindow", u"NO/NI", None))
        self.label_20.setText(QCoreApplication.translate("DevisMainWindow", u"TVA a NI", None))
        self.label_19.setText(QCoreApplication.translate("DevisMainWindow", u"Total Hors Taxe", None))
        self.label_21.setText(QCoreApplication.translate("DevisMainWindow", u"Total TTC en NI", None))
        self.print_btn.setText(QCoreApplication.translate("DevisMainWindow", u"PRINT / Imprime", None))
        self.save_btn.setText(QCoreApplication.translate("DevisMainWindow", u"SAVE / Sauvegarder", None))
    # retranslateUi

