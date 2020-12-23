# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_colormap_chooser.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_colorMapChooser(object):
    def setupUi(self, colorMapChooser):
        colorMapChooser.setObjectName("colorMapChooser")
        colorMapChooser.resize(437, 539)
        self.gridLayout = QtWidgets.QGridLayout(colorMapChooser)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(colorMapChooser)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 2)
        self.individual_colormap_legend = LegendMplCanvas(colorMapChooser)
        self.individual_colormap_legend.setObjectName("individual_colormap_legend")
        self.gridLayout_2.addWidget(self.individual_colormap_legend, 1, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(colorMapChooser)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.label_5 = QtWidgets.QLabel(colorMapChooser)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.individ_min_value_spinbox = QtWidgets.QSpinBox(colorMapChooser)
        self.individ_min_value_spinbox.setProperty("value", 1)
        self.individ_min_value_spinbox.setObjectName("individ_min_value_spinbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.individ_min_value_spinbox)
        self.label_6 = QtWidgets.QLabel(colorMapChooser)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.individ_max_value_spinbox = QtWidgets.QSpinBox(colorMapChooser)
        self.individ_max_value_spinbox.setProperty("value", 4)
        self.individ_max_value_spinbox.setObjectName("individ_max_value_spinbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.individ_max_value_spinbox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_8 = QtWidgets.QLabel(colorMapChooser)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(colorMapChooser)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.threecomp_min_value_spinbox = QtWidgets.QSpinBox(colorMapChooser)
        self.threecomp_min_value_spinbox.setProperty("value", 1)
        self.threecomp_min_value_spinbox.setObjectName("threecomp_min_value_spinbox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.threecomp_min_value_spinbox)
        self.label_10 = QtWidgets.QLabel(colorMapChooser)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.threecomp_max_value_spinbox = QtWidgets.QSpinBox(colorMapChooser)
        self.threecomp_max_value_spinbox.setProperty("value", 10)
        self.threecomp_max_value_spinbox.setObjectName("threecomp_max_value_spinbox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.threecomp_max_value_spinbox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_11 = QtWidgets.QLabel(colorMapChooser)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.label = QtWidgets.QLabel(colorMapChooser)
        self.label.setObjectName("label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label)
        self.individ_num_levels_spinBox = QtWidgets.QSpinBox(colorMapChooser)
        self.individ_num_levels_spinBox.setMinimum(3)
        self.individ_num_levels_spinBox.setMaximum(20)
        self.individ_num_levels_spinBox.setProperty("value", 4)
        self.individ_num_levels_spinBox.setObjectName("individ_num_levels_spinBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.individ_num_levels_spinBox)
        self.label_2 = QtWidgets.QLabel(colorMapChooser)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.individ_colormap_name_comboBox = QtWidgets.QComboBox(colorMapChooser)
        self.individ_colormap_name_comboBox.setObjectName("individ_colormap_name_comboBox")
        self.individ_colormap_name_comboBox.addItem("")
        self.individ_colormap_name_comboBox.setItemText(0, "coolwarm")
        self.individ_colormap_name_comboBox.addItem("")
        self.individ_colormap_name_comboBox.setItemText(1, "jet")
        self.individ_colormap_name_comboBox.addItem("")
        self.individ_colormap_name_comboBox.setItemText(2, "viridis")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.individ_colormap_name_comboBox)
        self.label_4 = QtWidgets.QLabel(colorMapChooser)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(colorMapChooser)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.threecomp_colormap_name_comboBox = QtWidgets.QComboBox(colorMapChooser)
        self.threecomp_colormap_name_comboBox.setEnabled(False)
        self.threecomp_colormap_name_comboBox.setObjectName("threecomp_colormap_name_comboBox")
        self.threecomp_colormap_name_comboBox.addItem("")
        self.threecomp_colormap_name_comboBox.setItemText(0, "coolwarm")
        self.threecomp_colormap_name_comboBox.addItem("")
        self.threecomp_colormap_name_comboBox.setItemText(1, "jet")
        self.threecomp_colormap_name_comboBox.addItem("")
        self.threecomp_colormap_name_comboBox.setItemText(2, "viridis")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.threecomp_colormap_name_comboBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.label_12 = QtWidgets.QLabel(colorMapChooser)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.label_12)
        self.checkBox_2 = QtWidgets.QCheckBox(colorMapChooser)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.checkBox_2)
        self.threecomp_num_levels_spinBox = QtWidgets.QSpinBox(colorMapChooser)
        self.threecomp_num_levels_spinBox.setEnabled(False)
        self.threecomp_num_levels_spinBox.setMinimum(3)
        self.threecomp_num_levels_spinBox.setMaximum(20)
        self.threecomp_num_levels_spinBox.setProperty("value", 4)
        self.threecomp_num_levels_spinBox.setObjectName("threecomp_num_levels_spinBox")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.threecomp_num_levels_spinBox)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 2, 1)
        self.three_components_colormap_legend = LegendMplCanvas(colorMapChooser)
        self.three_components_colormap_legend.setObjectName("three_components_colormap_legend")
        self.gridLayout_2.addWidget(self.three_components_colormap_legend, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 5)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(colorMapChooser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.label_5.setBuddy(self.individ_min_value_spinbox)
        self.label_6.setBuddy(self.individ_max_value_spinbox)
        self.label_10.setBuddy(self.individ_max_value_spinbox)
        self.label.setBuddy(self.individ_num_levels_spinBox)
        self.label_2.setBuddy(self.individ_colormap_name_comboBox)
        self.label_4.setBuddy(self.individ_num_levels_spinBox)
        self.label_3.setBuddy(self.individ_colormap_name_comboBox)

        self.retranslateUi(colorMapChooser)
        self.individ_colormap_name_comboBox.setCurrentIndex(0)
        self.threecomp_colormap_name_comboBox.setCurrentIndex(0)
        self.buttonBox.accepted.connect(colorMapChooser.accept)
        self.buttonBox.rejected.connect(colorMapChooser.reject)
        self.checkBox_2.toggled['bool'].connect(self.threecomp_num_levels_spinBox.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.threecomp_colormap_name_comboBox.setDisabled)
        self.threecomp_num_levels_spinBox.valueChanged['int'].connect(colorMapChooser.update_legend)
        self.threecomp_colormap_name_comboBox.currentIndexChanged['int'].connect(colorMapChooser.update_legend)
        self.individ_colormap_name_comboBox.currentIndexChanged['int'].connect(colorMapChooser.update_legend)
        self.individ_num_levels_spinBox.valueChanged['int'].connect(colorMapChooser.update_legend)
        QtCore.QMetaObject.connectSlotsByName(colorMapChooser)

    def retranslateUi(self, colorMapChooser):
        _translate = QtCore.QCoreApplication.translate
        colorMapChooser.setWindowTitle(_translate("colorMapChooser", "Colormap Options"))
        self.checkBox.setText(_translate("colorMapChooser", "Different colors for positive and negative values"))
        self.label_7.setText(_translate("colorMapChooser", "Individual compenents"))
        self.label_5.setText(_translate("colorMapChooser", "Min Value"))
        self.label_6.setText(_translate("colorMapChooser", "Max Value"))
        self.label_8.setText(_translate("colorMapChooser", "Three dimensional analysis"))
        self.label_9.setText(_translate("colorMapChooser", "Min Value"))
        self.label_10.setText(_translate("colorMapChooser", "Max Value"))
        self.label_11.setText(_translate("colorMapChooser", "Individual Components Legend Colors"))
        self.label.setText(_translate("colorMapChooser", "Number of levels"))
        self.label_2.setText(_translate("colorMapChooser", "Colormap Name"))
        self.label_4.setText(_translate("colorMapChooser", "Number of levels"))
        self.label_3.setText(_translate("colorMapChooser", "Colormap Name"))
        self.label_12.setText(_translate("colorMapChooser", "3D Compenets Legend Colors"))
        self.checkBox_2.setText(_translate("colorMapChooser", "Same as Individual Compenents"))
from spmclient.ui.gui.xml.customcomponents import LegendMplCanvas


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    colorMapChooser = QtWidgets.QDialog()
    ui = Ui_colorMapChooser()
    ui.setupUi(colorMapChooser)
    colorMapChooser.show()
    sys.exit(app.exec_())
