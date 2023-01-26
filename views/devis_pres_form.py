# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'devis_pres_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_DevisUserInfo(object):
    def setupUi(self, DevisUserInfo):
        if not DevisUserInfo.objectName():
            DevisUserInfo.setObjectName(u"DevisUserInfo")
        DevisUserInfo.resize(559, 455)
        self.horizontalLayout = QHBoxLayout(DevisUserInfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(DevisUserInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tva = QSpinBox(self.frame)
        self.tva.setObjectName(u"tva")
        self.tva.setMaximum(100)

        self.gridLayout.addWidget(self.tva, 4, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.project_description = QLineEdit(self.frame)
        self.project_description.setObjectName(u"project_description")

        self.gridLayout.addWidget(self.project_description, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.payment_condition = QSpinBox(self.frame)
        self.payment_condition.setObjectName(u"payment_condition")

        self.gridLayout.addWidget(self.payment_condition, 7, 1, 1, 1)

        self.devis_validity = QSpinBox(self.frame)
        self.devis_validity.setObjectName(u"devis_validity")
        self.devis_validity.setMaximum(100)

        self.gridLayout.addWidget(self.devis_validity, 6, 1, 1, 1)

        self.pay_time_category = QComboBox(self.frame)
        self.pay_time_category.addItem("")
        self.pay_time_category.addItem("")
        self.pay_time_category.addItem("")
        self.pay_time_category.setObjectName(u"pay_time_category")

        self.gridLayout.addWidget(self.pay_time_category, 5, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.submit_button = QPushButton(self.frame)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.submit_button, 9, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.client_address = QLineEdit(self.groupBox_2)
        self.client_address.setObjectName(u"client_address")

        self.gridLayout_3.addWidget(self.client_address, 1, 1, 1, 1)

        self.client_cp_ville = QLineEdit(self.groupBox_2)
        self.client_cp_ville.setObjectName(u"client_cp_ville")

        self.gridLayout_3.addWidget(self.client_cp_ville, 2, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)

        self.client_phone = QLineEdit(self.groupBox_2)
        self.client_phone.setObjectName(u"client_phone")

        self.gridLayout_3.addWidget(self.client_phone, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.our_cp_ville = QLineEdit(self.groupBox)
        self.our_cp_ville.setObjectName(u"our_cp_ville")

        self.gridLayout_2.addWidget(self.our_cp_ville, 2, 1, 1, 1)

        self.our_address = QLineEdit(self.groupBox)
        self.our_address.setObjectName(u"our_address")

        self.gridLayout_2.addWidget(self.our_address, 1, 1, 1, 1)

        self.our_url = QLineEdit(self.groupBox)
        self.our_url.setObjectName(u"our_url")

        self.gridLayout_2.addWidget(self.our_url, 4, 1, 1, 1)

        self.our_phone = QLineEdit(self.groupBox)
        self.our_phone.setObjectName(u"our_phone")

        self.gridLayout_2.addWidget(self.our_phone, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.client_name = QLineEdit(self.groupBox)
        self.client_name.setObjectName(u"client_name")

        self.gridLayout_2.addWidget(self.client_name, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)

        self.currencies = QComboBox(self.frame)
        self.currencies.setObjectName(u"currencies")

        self.gridLayout.addWidget(self.currencies, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(DevisUserInfo)

        QMetaObject.connectSlotsByName(DevisUserInfo)
    # setupUi

    def retranslateUi(self, DevisUserInfo):
        DevisUserInfo.setWindowTitle(QCoreApplication.translate("DevisUserInfo", u"DevisInfo", None))
        self.tva.setSuffix(QCoreApplication.translate("DevisUserInfo", u" %", None))
        self.tva.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("DevisUserInfo", u"Validit\u00e9 du devis ", None))
        self.label_4.setText(QCoreApplication.translate("DevisUserInfo", u"Conditions de r\u00e8glement ", None))
        self.project_description.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Description du projet et/ou Produit factur\u00e9", None))
        self.label_5.setText(QCoreApplication.translate("DevisUserInfo", u"Intitul\u00e9", None))
        self.label.setText(QCoreApplication.translate("DevisUserInfo", u"TVA", None))
        self.pay_time_category.setItemText(0, QCoreApplication.translate("DevisUserInfo", u"Jours | Days", None))
        self.pay_time_category.setItemText(1, QCoreApplication.translate("DevisUserInfo", u"Mois | Months", None))
        self.pay_time_category.setItemText(2, QCoreApplication.translate("DevisUserInfo", u"Annees | Years", None))

        self.label_2.setText(QCoreApplication.translate("DevisUserInfo", u"Time Category", None))
        self.submit_button.setText(QCoreApplication.translate("DevisUserInfo", u"Submit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DevisUserInfo", u"Client Infos", None))
        self.label_10.setText(QCoreApplication.translate("DevisUserInfo", u"Addresse", None))
        self.label_11.setText(QCoreApplication.translate("DevisUserInfo", u"CP Ville", None))
#if QT_CONFIG(tooltip)
        self.client_address.setToolTip(QCoreApplication.translate("DevisUserInfo", u"Enter Your Addresse", None))
#endif // QT_CONFIG(tooltip)
        self.client_address.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter The Client Addresse", None))
        self.client_cp_ville.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter The Client CP Ville", None))
        self.label_12.setText(QCoreApplication.translate("DevisUserInfo", u"T\u00e9l\u00e9phone ", None))
#if QT_CONFIG(tooltip)
        self.client_phone.setToolTip(QCoreApplication.translate("DevisUserInfo", u"Enter Your Phone Number", None))
#endif // QT_CONFIG(tooltip)
        self.client_phone.setInputMask(QCoreApplication.translate("DevisUserInfo", u"+243 9999-999-999", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter Your Client Society Name", None))
        self.label_14.setText(QCoreApplication.translate("DevisUserInfo", u"Soci\u00e9t\u00e9 et/ou Nom du client", None))
        self.groupBox.setTitle(QCoreApplication.translate("DevisUserInfo", u"Society Infos", None))
        self.label_9.setText(QCoreApplication.translate("DevisUserInfo", u"R\u00e9f\u00e9rences Internet", None))
        self.label_8.setText(QCoreApplication.translate("DevisUserInfo", u"T\u00e9l\u00e9phone ", None))
        self.label_6.setText(QCoreApplication.translate("DevisUserInfo", u"Addresse", None))
        self.label_7.setText(QCoreApplication.translate("DevisUserInfo", u"CP Ville", None))
        self.our_cp_ville.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter Your CP Ville", None))
#if QT_CONFIG(tooltip)
        self.our_address.setToolTip(QCoreApplication.translate("DevisUserInfo", u"Enter Your Address", None))
#endif // QT_CONFIG(tooltip)
        self.our_address.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter your Addresse", None))
#if QT_CONFIG(tooltip)
        self.our_url.setToolTip(QCoreApplication.translate("DevisUserInfo", u"Enter Your URL ", None))
#endif // QT_CONFIG(tooltip)
        self.our_url.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter The URL To Your Web Site", None))
#if QT_CONFIG(tooltip)
        self.our_phone.setToolTip(QCoreApplication.translate("DevisUserInfo", u"Enter Your Phone Number", None))
#endif // QT_CONFIG(tooltip)
        self.our_phone.setInputMask(QCoreApplication.translate("DevisUserInfo", u"+243 9999-999-999", None))
        self.our_phone.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("DevisUserInfo", u"Le nom de votre soci\u00e9t\u00e9", None))
        self.client_name.setPlaceholderText(QCoreApplication.translate("DevisUserInfo", u"Enter Your Society Name", None))
        self.label_15.setText(QCoreApplication.translate("DevisUserInfo", u"Currency", None))
    # retranslateUi

