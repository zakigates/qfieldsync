# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/project_configuration_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QFieldProjectConfigurationBase(object):
    def setupUi(self, QFieldProjectConfigurationBase):
        QFieldProjectConfigurationBase.setObjectName("QFieldProjectConfigurationBase")
        QFieldProjectConfigurationBase.resize(608, 510)
        self.gridLayout = QtWidgets.QGridLayout(QFieldProjectConfigurationBase)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(QFieldProjectConfigurationBase)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layersTable = QtWidgets.QTableWidget(self.groupBox)
        self.layersTable.setObjectName("layersTable")
        self.layersTable.setColumnCount(2)
        self.layersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.layersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.layersTable.setHorizontalHeaderItem(1, item)
        self.layersTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.layersTable, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QFieldProjectConfigurationBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(QFieldProjectConfigurationBase)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.createBaseMapGroupBox = QtWidgets.QGroupBox(self.tab)
        self.createBaseMapGroupBox.setCheckable(True)
        self.createBaseMapGroupBox.setChecked(False)
        self.createBaseMapGroupBox.setObjectName("createBaseMapGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.createBaseMapGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mapThemeRadioButton = QtWidgets.QRadioButton(self.createBaseMapGroupBox)
        self.mapThemeRadioButton.setObjectName("mapThemeRadioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(QFieldProjectConfigurationBase)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.mapThemeRadioButton)
        self.gridLayout_3.addWidget(self.mapThemeRadioButton, 0, 1, 1, 1)
        self.baseMapTypeStack = QtWidgets.QStackedWidget(self.createBaseMapGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseMapTypeStack.sizePolicy().hasHeightForWidth())
        self.baseMapTypeStack.setSizePolicy(sizePolicy)
        self.baseMapTypeStack.setObjectName("baseMapTypeStack")
        self.mapThemePage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapThemePage.sizePolicy().hasHeightForWidth())
        self.mapThemePage.setSizePolicy(sizePolicy)
        self.mapThemePage.setObjectName("mapThemePage")
        self.formLayout_2 = QtWidgets.QFormLayout(self.mapThemePage)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.mapThemePage)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.mapThemeComboBox = QtWidgets.QComboBox(self.mapThemePage)
        self.mapThemeComboBox.setObjectName("mapThemeComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mapThemeComboBox)
        self.baseMapTypeStack.addWidget(self.mapThemePage)
        self.singleLayerPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleLayerPage.sizePolicy().hasHeightForWidth())
        self.singleLayerPage.setSizePolicy(sizePolicy)
        self.singleLayerPage.setObjectName("singleLayerPage")
        self.formLayout = QtWidgets.QFormLayout(self.singleLayerPage)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.singleLayerPage)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.layerComboBox = QgsMapLayerComboBox(self.singleLayerPage)
        self.layerComboBox.setObjectName("layerComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.layerComboBox)
        self.baseMapTypeStack.addWidget(self.singleLayerPage)
        self.gridLayout_3.addWidget(self.baseMapTypeStack, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.createBaseMapGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.tileSize = QtWidgets.QLineEdit(self.createBaseMapGroupBox)
        self.tileSize.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tileSize.setObjectName("tileSize")
        self.gridLayout_3.addWidget(self.tileSize, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.createBaseMapGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)
        self.mapUnitsPerPixel = QtWidgets.QLineEdit(self.createBaseMapGroupBox)
        self.mapUnitsPerPixel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.mapUnitsPerPixel.setObjectName("mapUnitsPerPixel")
        self.gridLayout_3.addWidget(self.mapUnitsPerPixel, 5, 1, 1, 1)
        self.singleLayerRadioButton = QtWidgets.QRadioButton(self.createBaseMapGroupBox)
        self.singleLayerRadioButton.setObjectName("singleLayerRadioButton")
        self.buttonGroup.addButton(self.singleLayerRadioButton)
        self.gridLayout_3.addWidget(self.singleLayerRadioButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.createBaseMapGroupBox, 0, 0, 1, 1)
        self.singleLayerRadioButton.raise_()
        self.createBaseMapGroupBox.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.onlyOfflineCopyFeaturesInAoi = QtWidgets.QCheckBox(self.tab_2)
        self.onlyOfflineCopyFeaturesInAoi.setObjectName("onlyOfflineCopyFeaturesInAoi")
        self.gridLayout_5.addWidget(self.onlyOfflineCopyFeaturesInAoi, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(QFieldProjectConfigurationBase)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(QFieldProjectConfigurationBase.accept)
        self.buttonBox.rejected.connect(QFieldProjectConfigurationBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QFieldProjectConfigurationBase)

    def retranslateUi(self, QFieldProjectConfigurationBase):
        _translate = QtCore.QCoreApplication.translate
        QFieldProjectConfigurationBase.setWindowTitle(_translate("QFieldProjectConfigurationBase", "Configure Project for QField synchronisation"))
        self.groupBox.setTitle(_translate("QFieldProjectConfigurationBase", "Layers"))
        item = self.layersTable.horizontalHeaderItem(0)
        item.setText(_translate("QFieldProjectConfigurationBase", "Layer"))
        item = self.layersTable.horizontalHeaderItem(1)
        item.setText(_translate("QFieldProjectConfigurationBase", "Action"))
        self.createBaseMapGroupBox.setToolTip(_translate("QFieldProjectConfigurationBase", "A base map is fully rendered to a raster image. Attributes from layers on a base map are no longer accessible."))
        self.createBaseMapGroupBox.setTitle(_translate("QFieldProjectConfigurationBase", "Create base map"))
        self.mapThemeRadioButton.setText(_translate("QFieldProjectConfigurationBase", "Map Theme"))
        self.label.setText(_translate("QFieldProjectConfigurationBase", "Map Theme"))
        self.label_2.setText(_translate("QFieldProjectConfigurationBase", "Layer"))
        self.label_3.setText(_translate("QFieldProjectConfigurationBase", "Tile Size"))
        self.tileSize.setToolTip(_translate("QFieldProjectConfigurationBase", "Rendering will happen in tiles. This number determines the width and height (in pixels) that will be rendered per tile."))
        self.tileSize.setText(_translate("QFieldProjectConfigurationBase", "1024"))
        self.label_4.setText(_translate("QFieldProjectConfigurationBase", "Map Units/Pixel"))
        self.mapUnitsPerPixel.setToolTip(_translate("QFieldProjectConfigurationBase", "This determines the spatial resolution of the resulting map image. It depends on the CRS of the map canvas. For map units in [m], a value of 1 means each pixel covers an area of 1x1 m, a value of 1000 means 1 pixel per square kilometer."))
        self.mapUnitsPerPixel.setText(_translate("QFieldProjectConfigurationBase", "100"))
        self.singleLayerRadioButton.setText(_translate("QFieldProjectConfigurationBase", "Single Layer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QFieldProjectConfigurationBase", "Base map"))
        self.onlyOfflineCopyFeaturesInAoi.setText(_translate("QFieldProjectConfigurationBase", "Only copy features in area of interest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QFieldProjectConfigurationBase", "Offline editing"))

from qgis.gui import QgsMapLayerComboBox
