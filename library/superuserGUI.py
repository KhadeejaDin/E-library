# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'superuserGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class SuperUserPage(QtGui.QWidget):
    #def __init__(self, library, user):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, superUser):
        superUser.setObjectName(_fromUtf8("superUser"))
        superUser.resize(610, 570)
        self.profileLabel = QtGui.QLabel(superUser)
        self.profileLabel.setGeometry(QtCore.QRect(330, 40, 71, 21))
        self.profileLabel.setObjectName(_fromUtf8("profileLabel"))
        self.layoutWidget_2 = QtGui.QWidget(superUser)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 70, 211, 371))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top5Label = QtGui.QLabel(self.layoutWidget_2)
        self.top5Label.setObjectName(_fromUtf8("top5Label"))
        self.verticalLayout.addWidget(self.top5Label)
        self.top5List = QtGui.QListWidget(self.layoutWidget_2)
        self.top5List.setObjectName(_fromUtf8("top5List"))
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        item = QtGui.QListWidgetItem()
        self.top5List.addItem(item)
        self.verticalLayout.addWidget(self.top5List)
        self.historyLabel = QtGui.QLabel(self.layoutWidget_2)
        self.historyLabel.setObjectName(_fromUtf8("historyLabel"))
        self.verticalLayout.addWidget(self.historyLabel)
        self.historyList = QtGui.QListWidget(self.layoutWidget_2)
        self.historyList.setObjectName(_fromUtf8("historyList"))
        item = QtGui.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.historyList.addItem(item)
        self.verticalLayout.addWidget(self.historyList)
        self.layoutWidget_3 = QtGui.QWidget(superUser)
        self.layoutWidget_3.setGeometry(QtCore.QRect(271, 231, 321, 161))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.requestListLabel = QtGui.QLabel(self.layoutWidget_3)
        self.requestListLabel.setObjectName(_fromUtf8("requestListLabel"))
        self.verticalLayout_3.addWidget(self.requestListLabel)
        self.requestTable = QtGui.QTableWidget(self.layoutWidget_3)
        self.requestTable.setObjectName(_fromUtf8("requestTable"))
        self.requestTable.setColumnCount(3)
        self.requestTable.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.requestTable.setItem(1, 0, item)
        self.verticalLayout_3.addWidget(self.requestTable)
        self.searchInput = QtGui.QLineEdit(superUser)
        self.searchInput.setGeometry(QtCore.QRect(21, 32, 133, 20))
        self.searchInput.setObjectName(_fromUtf8("searchInput"))
        self.searchButton = QtGui.QPushButton(superUser)
        self.searchButton.setGeometry(QtCore.QRect(160, 31, 75, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.contributLabel = QtGui.QLabel(superUser)
        self.contributLabel.setGeometry(QtCore.QRect(272, 163, 96, 16))
        self.contributLabel.setObjectName(_fromUtf8("contributLabel"))
        self.lineEdit_2 = QtGui.QLineEdit(superUser)
        self.lineEdit_2.setGeometry(QtCore.QRect(374, 163, 71, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.widget = QtGui.QWidget(superUser)
        self.widget.setGeometry(QtCore.QRect(271, 82, 166, 76))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.usernameLabel = QtGui.QLabel(self.widget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout_4.addWidget(self.usernameLabel)
        self.nameInLabel = QtGui.QLabel(self.widget)
        self.nameInLabel.setObjectName(_fromUtf8("nameInLabel"))
        self.horizontalLayout_4.addWidget(self.nameInLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.numOfBookLabel = QtGui.QLabel(self.widget)
        self.numOfBookLabel.setObjectName(_fromUtf8("numOfBookLabel"))
        self.horizontalLayout_3.addWidget(self.numOfBookLabel)
        self.numOfBookInLabel = QtGui.QLabel(self.widget)
        self.numOfBookInLabel.setObjectName(_fromUtf8("numOfBookInLabel"))
        self.horizontalLayout_3.addWidget(self.numOfBookInLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pointLabel = QtGui.QLabel(self.widget)
        self.pointLabel.setObjectName(_fromUtf8("pointLabel"))
        self.horizontalLayout_2.addWidget(self.pointLabel)
        self.pointInLabel = QtGui.QLabel(self.widget)
        self.pointInLabel.setObjectName(_fromUtf8("pointInLabel"))
        self.horizontalLayout_2.addWidget(self.pointInLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.levelLabel = QtGui.QLabel(self.widget)
        self.levelLabel.setObjectName(_fromUtf8("levelLabel"))
        self.horizontalLayout.addWidget(self.levelLabel)
        self.levelInlabel = QtGui.QLabel(self.widget)
        self.levelInlabel.setObjectName(_fromUtf8("levelInlabel"))
        self.horizontalLayout.addWidget(self.levelInlabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(superUser)
        QtCore.QMetaObject.connectSlotsByName(superUser)

    def retranslateUi(self, superUser):
        superUser.setWindowTitle(_translate("superUser", "Form", None))
        self.profileLabel.setText(_translate("superUser", "Profile", None))
        self.top5Label.setText(_translate("superUser", "Top 5 Books:", None))
        __sortingEnabled = self.top5List.isSortingEnabled()
        self.top5List.setSortingEnabled(False)
        item = self.top5List.item(0)
        item.setText(_translate("superUser", "1. Book1", None))
        item = self.top5List.item(1)
        item.setText(_translate("superUser", "2. Book2", None))
        item = self.top5List.item(2)
        item.setText(_translate("superUser", "3. Book3", None))
        item = self.top5List.item(3)
        item.setText(_translate("superUser", "4. Book4", None))
        item = self.top5List.item(4)
        item.setText(_translate("superUser", "5. Book5", None))
        self.top5List.setSortingEnabled(__sortingEnabled)
        self.historyLabel.setText(_translate("superUser", "Reading History:", None))
        __sortingEnabled = self.historyList.isSortingEnabled()
        self.historyList.setSortingEnabled(False)
        item = self.historyList.item(0)
        item.setText(_translate("superUser", "1. Book1", None))
        item = self.historyList.item(1)
        item.setText(_translate("superUser", "2. Book2", None))
        item = self.historyList.item(2)
        item.setText(_translate("superUser", "3. Book3", None))
        item = self.historyList.item(3)
        item.setText(_translate("superUser", "4. Book4", None))
        item = self.historyList.item(4)
        item.setText(_translate("superUser", "5. Book5", None))
        self.historyList.setSortingEnabled(__sortingEnabled)
        self.requestListLabel.setText(_translate("superUser", "Book donation request List:", None))
        item = self.requestTable.verticalHeaderItem(0)
        item.setText(_translate("superUser", "1", None))
        item = self.requestTable.verticalHeaderItem(1)
        item.setText(_translate("superUser", "2", None))
        item = self.requestTable.verticalHeaderItem(2)
        item.setText(_translate("superUser", "3", None))
        item = self.requestTable.horizontalHeaderItem(0)
        item.setText(_translate("superUser", "User Name", None))
        item = self.requestTable.horizontalHeaderItem(1)
        item.setText(_translate("superUser", "Book title", None))
        item = self.requestTable.horizontalHeaderItem(2)
        item.setText(_translate("superUser", "point requiest", None))
        __sortingEnabled = self.requestTable.isSortingEnabled()
        self.requestTable.setSortingEnabled(False)
        self.requestTable.setSortingEnabled(__sortingEnabled)
        self.searchButton.setText(_translate("superUser", "Search", None))
        self.contributLabel.setText(_translate("superUser", "Contribute Books:", None))
        self.lineEdit_2.setText(_translate("superUser", "Input File", None))
        self.usernameLabel.setText(_translate("superUser", "Name:", None))
        self.nameInLabel.setText(_translate("superUser", "none", None))
        self.numOfBookLabel.setText(_translate("superUser", "Num of book contributed:", None))
        self.numOfBookInLabel.setText(_translate("superUser", "0", None))
        self.pointLabel.setText(_translate("superUser", "Total points:", None))
        self.pointInLabel.setText(_translate("superUser", "0", None))
        self.levelLabel.setText(_translate("superUser", "level:", None))
        self.levelInlabel.setText(_translate("superUser", "register", None))

#
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     superUser = QtGui.QWidget()
#     ui = SuperUserPage()
#     ui.setupUi(superUser)
#     superUser.show()
#     sys.exit(app.exec_())
