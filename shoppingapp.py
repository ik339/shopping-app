from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QWidget)
import sys

totalofthing = 0
class Ui_shoppingApp(object):

    def setupUi(self,shoppingApp):
        if not shoppingApp.objectName():
            shoppingApp.setObjectName(u"shoppingApp")
        shoppingApp.resize(300, 300)
        shoppingApp.setMaximumSize(QSize(300, 300))
        self.nametextbox = QLineEdit(shoppingApp)
        self.nametextbox.setObjectName(u"nametextbox")
        self.nametextbox.setGeometry(QRect(130, 10, 113, 21))

        self.pricetextbox = QLineEdit(shoppingApp)
        self.pricetextbox.setObjectName(u"pricetextbox")
        self.pricetextbox.setGeometry(QRect(130, 40, 113, 21))

        self.qtyspinbox = QSpinBox(shoppingApp)
        self.qtyspinbox.setObjectName(u"qtyspinbox")
        self.qtyspinbox.setGeometry(QRect(130, 70, 111, 22))

        self.list = QListWidget(shoppingApp)
        QListWidgetItem(self.list)
        self.list.setObjectName(u"list")
        self.list.setGeometry(QRect(20, 100, 221, 81))

        self.calculatebutton = QPushButton(shoppingApp)
        self.calculatebutton.setObjectName(u"calculatebutton")
        self.calculatebutton.setGeometry(QRect(90, 190, 75, 24))

        self.calculatebutton.clicked.connect(self.performAdd)
        self.calculatebutton.clicked.connect(self.addtolist)

        self.deletebutton = QPushButton(shoppingApp)
        self.deletebutton.setObjectName(u"deletebutton")
        self.deletebutton.setGeometry(QRect(254, 120, 41, 21))

        self.deletebutton.clicked.connect(self.performDelete)

        self.namelabel = QLabel(shoppingApp)
        self.namelabel.setObjectName(u"namelabel")
        self.namelabel.setGeometry(QRect(40, 10, 49, 16))
        self.pricelabel = QLabel(shoppingApp)
        self.pricelabel.setObjectName(u"pricelabel")
        self.pricelabel.setGeometry(QRect(40, 40, 49, 16))
        self.qtylabel = QLabel(shoppingApp)
        self.qtylabel.setObjectName(u"qtylabel")
        self.qtylabel.setGeometry(QRect(40, 70, 49, 16))
        self.totallabel = QLabel(shoppingApp)
        self.totallabel.setObjectName(u"totallabel")
        self.totallabel.setGeometry(QRect(30, 230, 161, 41))

        self.retranslateUi(shoppingApp)

        QMetaObject.connectSlotsByName(shoppingApp)
    # setupUi

    def retranslateUi(self, shoppingApp):
        shoppingApp.setWindowTitle(QCoreApplication.translate("shoppingApp", u"Form", None))

        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        self.list.setSortingEnabled(__sortingEnabled)

        self.calculatebutton.setText(QCoreApplication.translate("shoppingApp", u"calculate", None))
        self.deletebutton.setText(QCoreApplication.translate("shoppingApp", u"-", None))
        self.namelabel.setText(QCoreApplication.translate("shoppingApp", u"name", None))
        self.pricelabel.setText(QCoreApplication.translate("shoppingApp", u"price", None))
        self.qtylabel.setText(QCoreApplication.translate("shoppingApp", u"quantity", None))
        self.totallabel.setText(QCoreApplication.translate("shoppingApp", u"Total", None))
    # retranslateUi

    def performAdd(self):
        global totalofthing
        p = self.pricetextbox.text()#get price£
        q = self.qtyspinbox.text()#get qty
        result = float(p)*float(q) #calc total first
        #self.totallabel.setText(str(result)) #output
        totalofthing = totalofthing + result
        totalNvat = totalofthing * 1.2
        self.totallabel.setText(str(totalNvat))

    def performDelete(self):
        selected_items = self.list.selectedItems()
        if not selected_items: return
        for item in selected_items:
            self.list.takeItem(self.list.row(item))

    def addtolist(self):
        p = self.pricetextbox.text()
        q = self.qtyspinbox.text()
        n = self.nametextbox.text()
        individual_unit = str(n) + " " + str(p) + " " + str(q)
        self.list.addItem(str(individual_unit))


app = QApplication([]) #makes the program run
widget = QWidget()
form = Ui_shoppingApp()
form.setupUi(widget)
widget.show()
sys.exit(app.exec())