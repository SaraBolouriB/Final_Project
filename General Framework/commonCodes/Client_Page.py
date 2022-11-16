from Service.service_contracts_list import service_list_dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import os


class Ui_client_dialog(QtWidgets.QDialog):
    def __init__(self, site_id, username, company_name):
        super().__init__()
        client_Dialog = self
        self.row_index = 0
        self.collum_index = 0
        self.button_map = {}
        self.username = username
        self.company_name = company_name
        self.site_id = site_id
        self._all_services = self.get_all_services(site_id=site_id)
        self.registered = os.path.exists('register.txt')
        self.setupUi(client_Dialog)

    def setupUi(self, client_dialog):
        client_dialog.setObjectName("client_dialog")
        client_dialog.setEnabled(True)
        client_dialog.resize(651, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(client_dialog.sizePolicy().hasHeightForWidth())
        client_dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../Desktop/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        client_dialog.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(client_dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.Subject = QtWidgets.QHBoxLayout()
        self.Subject.setObjectName("Subject")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Subject.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.framework = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.framework.setFont(font)
        self.framework.setObjectName("framework")
        self.verticalLayout.addWidget(self.framework)
        self.adminPage = QtWidgets.QLabel(self.frame)
        self.adminPage.setAlignment(QtCore.Qt.AlignCenter)
        self.adminPage.setObjectName("adminPage")
        self.verticalLayout.addWidget(self.adminPage)
        self.Subject.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Subject.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.Subject, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.Admin_bar = QtWidgets.QTabWidget(self.centralwidget)
        self.Admin_bar.setEnabled(True)
        self.Admin_bar.setMinimumSize(QtCore.QSize(627, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 202, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 202, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Admin_bar.setPalette(palette)
        self.Admin_bar.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.Admin_bar.setObjectName("Admin_bar")
        self.User_Infirmation = QtWidgets.QWidget()
        self.User_Infirmation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.User_Infirmation.setAccessibleName("")
        self.User_Infirmation.setObjectName("User_Infirmation")
        self.L = QtWidgets.QGridLayout(self.User_Infirmation)
        self.L.setObjectName("L")
        self.user_info = QtWidgets.QVBoxLayout()
        self.user_info.setObjectName("user_info")
        self.widget = QtWidgets.QWidget(self.User_Infirmation)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.LOGIN_API_LABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.LOGIN_API_LABEL.setFont(font)
        self.LOGIN_API_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGIN_API_LABEL.setObjectName("LOGIN_API_LABEL")
        self.gridLayout.addWidget(self.LOGIN_API_LABEL, 0, 0, 1, 2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.user_input = QtWidgets.QLabel(self.widget)
        self.user_input.setText("")
        self.user_input.setObjectName("user_input")
        self.horizontalLayout_2.addWidget(self.user_input)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.company_input = QtWidgets.QLabel(self.widget)
        self.company_input.setText("")
        self.company_input.setObjectName("company_input")
        self.horizontalLayout.addWidget(self.company_input)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 2)
        self.user_info.addWidget(self.widget)
        self.pushButton_2 = QtWidgets.QPushButton(self.User_Infirmation)
        self.pushButton_2.setObjectName("pushButton_2")
        if self.registered == True:
            self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.register_hf)
        self.L.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.L.addLayout(self.user_info, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.User_Infirmation, "")
        self.All_Services = QtWidgets.QWidget()
        self.All_Services.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.All_Services.setObjectName("All_Services")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.All_Services)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        # ------------------------------------------------------------------
        for service in self._all_services:
            buttom = self.create_new_button(name=service['name'])
            self.gridLayout_6.addWidget(buttom, self.row_index, self.collum_index, 1, 1)
            self.update_indexs()
        #-------------------------------------------------------------------
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.All_Services, "")
        self.gridLayout_3.addWidget(self.Admin_bar, 1, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(client_dialog)
        self.statusbar.setObjectName("statusbar")
        self.actionShow_PublicKey = QtWidgets.QAction(client_dialog)
        self.actionShow_PublicKey.setObjectName("actionShow_PublicKey")
        self.actionExit = QtWidgets.QAction(client_dialog)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(client_dialog)
        self.Admin_bar.setCurrentIndex(0)
        self.actionShow_PublicKey.triggered.connect(client_dialog.close)
        self.actionExit.triggered.connect(client_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(client_dialog)

    def retranslateUi(self, client_dialog):
        _translate = QtCore.QCoreApplication.translate
        client_dialog.setWindowTitle(_translate("client_dialog", "Framework"))
        self.framework.setText(_translate("client_dialog", "Framework"))
        self.adminPage.setText(_translate("client_dialog", "Client Page"))
        self.LOGIN_API_LABEL.setText(_translate("client_dialog", "Your Personal Information"))
        self.label_13.setText(_translate("client_dialog", "Your Username: "))
        self.user_input.setText(_translate("client_dialog", self.username))
        self.label_12.setText(_translate("client_dialog", "Company Name"))
        self.pushButton_2.setText(_translate("landing_page", "Register"))
        self.company_input.setText(_translate("client_dialog", self.company_name))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.User_Infirmation), _translate("client_dialog", "User Information"))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.All_Services), _translate("client_dialog", "All Services"))
        self.actionShow_PublicKey.setText(_translate("client_dialog", "Show PublicKey"))
        self.actionExit.setText(_translate("client_dialog", "Exit"))

    def register_hf(self):
        url = 'http://localhost:3000/data/register'
        data = {
            "username" : self.username
        }
        result = requests.post(url, data)
        if result.status_code == 200:
            with open('register.txt', 'w') as file:
                file.write("YES")
            self.pushButton_2.setEnabled(False)

    def get_all_services(self, site_id):
        service_url = 'http://127.0.0.1:8000/services/' + str(site_id)
        result = requests.get(
            url=service_url
        )
        return result.json()

    def create_new_button(self, name):
        _translate = QtCore.QCoreApplication.translate
        pushButton = QtWidgets.QPushButton(self.All_Services)
        pushButton.setObjectName(name)
        self.save_button(name=name, obj=pushButton)
        pushButton.clicked.connect(lambda: self.clicked_on_button())
        pushButton.setText(_translate("client_dialog", name))
        return pushButton

    def update_indexs(self):
        self.collum_index += 1
        
        if self.collum_index >= 2:
            self.collum_index = 0
            self.row_index += 1

    def save_button(self, name, obj):
        self.button_map[name] = obj

    def find_button_by_name(self, name):
        return self.button_map[name]

    def clicked_on_button(self):
        button_name = self.sender().text()
        for service in self._all_services:
            if service['name'] == button_name:
                self.service_dialog = service_list_dialog(widget=self, service=service, site_id=self.site_id)
                self.service_dialog.show()
                break
        
    def closeEvent(self, event):
        QtCore.QCoreApplication.quit
        