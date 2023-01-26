# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_taxe.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 185)
        font = QFont()
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.taxe_name = QLineEdit(Dialog)
        self.taxe_name.setObjectName(u"taxe_name")
        self.taxe_name.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.taxe_name.setFont(font1)

        self.gridLayout.addWidget(self.taxe_name, 1, 0, 1, 1)

        self.add_new_taxe_btn = QPushButton(Dialog)
        self.add_new_taxe_btn.setObjectName(u"add_new_taxe_btn")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.add_new_taxe_btn.setFont(font2)
        self.add_new_taxe_btn.setStyleSheet(u"background-color:transparent;\n"
"color:darkgrey;")

        self.gridLayout.addWidget(self.add_new_taxe_btn, 0, 0, 1, 3)

        self.taxe_value = QDoubleSpinBox(Dialog)
        self.taxe_value.setObjectName(u"taxe_value")
        self.taxe_value.setMinimumSize(QSize(150, 25))
        self.taxe_value.setFont(font1)
        self.taxe_value.setMaximum(100.000000000000000)

        self.gridLayout.addWidget(self.taxe_value, 1, 1, 1, 1)

        self.save_taxe_btn = QPushButton(Dialog)
        self.save_taxe_btn.setObjectName(u"save_taxe_btn")
        self.save_taxe_btn.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.save_taxe_btn.setFont(font3)
        self.save_taxe_btn.setStyleSheet(u"border:1px solid rgb(38, 79, 136);\n"
"border-radius:5px;\n"
"color:white;\n"
"background-color: rgb(38, 79, 136);")

        self.gridLayout.addWidget(self.save_taxe_btn, 2, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"NewTaxeDialog", None))
        self.taxe_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nom de la texe", None))
        self.add_new_taxe_btn.setText(QCoreApplication.translate("Dialog", u"Ajouter une nouvelle taxe", None))
        self.taxe_value.setSuffix(QCoreApplication.translate("Dialog", u"  %", None))
        self.save_taxe_btn.setText(QCoreApplication.translate("Dialog", u"Sauvegarder la taxe", None))
    # retranslateUi

