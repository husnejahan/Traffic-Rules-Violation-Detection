from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Database import KEYS, Database


class DetailLogWindow(QMainWindow):
    def __init__(self, data, parent=None):
        super(DetailLogWindow, self).__init__(parent)
        loadUi("UI/DetailLog.ui", self)
        self.data = data
        self.car_image.setScaledContents(True)
        self.license_image.setScaledContents(True)
        self.initData()

    def initData(self):
        self.cam_id.setText(str(self.data[KEYS.CARID]))
        self.car_color.setText(self.data[KEYS.CARCOLOR])

        if self.data[KEYS.CARIMAGE] is not None:
            self.car_image.setPixmap(self.data[KEYS.CARIMAGE])
        if self.data[KEYS.LICENSEIMAGE] is not None:
            self.license_image.setPixmap(self.data[KEYS.LICENSEIMAGE])

        self.license_number_lineedit.setText(self.data[KEYS.LICENSENUMBER])
        self.location.setText(self.data[KEYS.LOCATION])
        self.rule.setText(self.data[KEYS.RULENAME])

        self.close_button.clicked.connect(self.close)
        self.delete_button.clicked.connect(self.deleteRecord)

    def close(self):
        self.destroy()

    def deleteRecord(self):
        qm = QtWidgets.QMessageBox
        prompt = qm.question(self, '', "Are you sure to reset all the values?", qm.Yes | qm.No)
        if prompt == qm.Yes:
            db = Database.getInstance()
            db.deleteViolation(carid=self.data[KEYS.CARID], ruleid=self.data[KEYS.RULEID], time=self.data[KEYS.TIME])
            self.destroy()
        else:
            pass
