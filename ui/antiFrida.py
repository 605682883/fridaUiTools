# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antiFrida.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_antiFrida(object):
    def setupUi(self, antiFrida):
        antiFrida.setObjectName("antiFrida")
        antiFrida.resize(668, 544)
        self.gridLayout_7 = QtWidgets.QGridLayout(antiFrida)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(antiFrida)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.chkExitThread = QtWidgets.QCheckBox(self.groupBox)
        self.chkExitThread.setObjectName("chkExitThread")
        self.gridLayout.addWidget(self.chkExitThread, 1, 1, 1, 1)
        self.txtKeyword = QtWidgets.QPlainTextEdit(self.groupBox)
        self.txtKeyword.setObjectName("txtKeyword")
        self.gridLayout.addWidget(self.txtKeyword, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.rdoAnti1 = QtWidgets.QRadioButton(self.groupBox)
        self.rdoAnti1.setObjectName("rdoAnti1")
        self.gridLayout_2.addWidget(self.rdoAnti1, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(antiFrida)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.rdoAnti2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rdoAnti2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rdoAnti2.setObjectName("rdoAnti2")
        self.gridLayout_3.addWidget(self.rdoAnti2, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(antiFrida)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.txtModule = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtModule.setObjectName("txtModule")
        self.gridLayout_4.addWidget(self.txtModule, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.txtSvcOffset = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.txtSvcOffset.setObjectName("txtSvcOffset")
        self.gridLayout_4.addWidget(self.txtSvcOffset, 1, 1, 1, 1)
        self.chkAutoOffset = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkAutoOffset.setObjectName("chkAutoOffset")
        self.gridLayout_4.addWidget(self.chkAutoOffset, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.rdoAnti3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rdoAnti3.setObjectName("rdoAnti3")
        self.gridLayout_5.addWidget(self.rdoAnti3, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.retranslateUi(antiFrida)
        QtCore.QMetaObject.connectSlotsByName(antiFrida)

    def retranslateUi(self, antiFrida):
        _translate = QtCore.QCoreApplication.translate
        antiFrida.setWindowTitle(_translate("antiFrida", "antiFrida"))
        self.groupBox.setTitle(_translate("antiFrida", "方案1 strstr过滤"))
        self.label.setText(_translate("antiFrida", "过滤关键词："))
        self.chkExitThread.setText(_translate("antiFrida", "检测到则退出线程"))
        self.txtKeyword.setPlainText(_translate("antiFrida", "frida;gdbus;gum-js-loop;gmain;linjector;"))
        self.rdoAnti1.setText(_translate("antiFrida", "启用"))
        self.groupBox_2.setTitle(_translate("antiFrida", "方案2 文件重定向"))
        self.label_2.setText(_translate("antiFrida", "详细说明："))
        self.lineEdit.setText(_translate("antiFrida", "对open、openat、readlink、readlinkat进行hook，替换maps和敏感词的处理"))
        self.rdoAnti2.setText(_translate("antiFrida", "启用"))
        self.groupBox_3.setTitle(_translate("antiFrida", "方案3 svc文件重定向（没有测试样本，暂时没做，todo）"))
        self.label_7.setText(_translate("antiFrida", "模块名称："))
        self.label_6.setText(_translate("antiFrida", "偏移地址："))
        self.chkAutoOffset.setText(_translate("antiFrida", "自动获取"))
        self.rdoAnti3.setText(_translate("antiFrida", "启用"))
