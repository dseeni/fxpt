# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copy_move_dialog_ui.ui'
#
# Created: Sat Nov 19 23:58:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 320))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiCHK_deleteSources = QtGui.QCheckBox(self.groupBox_2)
        self.uiCHK_deleteSources.setMinimumSize(QtCore.QSize(0, 20))
        self.uiCHK_deleteSources.setObjectName("uiCHK_deleteSources")
        self.gridLayout_3.addWidget(self.uiCHK_deleteSources, 2, 1, 1, 1)
        self.uiBTN_browseTarget = QtGui.QToolButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiBTN_browseTarget.setIcon(icon)
        self.uiBTN_browseTarget.setIconSize(QtCore.QSize(18, 18))
        self.uiBTN_browseTarget.setObjectName("uiBTN_browseTarget")
        self.gridLayout_3.addWidget(self.uiBTN_browseTarget, 0, 2, 1, 1)
        self.uiLED_targetRoot = LineEditPath(self.groupBox_2)
        self.uiLED_targetRoot.setObjectName("uiLED_targetRoot")
        self.gridLayout_3.addWidget(self.uiLED_targetRoot, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.uiCHK_retarget = QtGui.QCheckBox(self.groupBox_2)
        self.uiCHK_retarget.setMinimumSize(QtCore.QSize(0, 20))
        self.uiCHK_retarget.setObjectName("uiCHK_retarget")
        self.gridLayout_3.addWidget(self.uiCHK_retarget, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.uiGRP_folderStructure = QtGui.QGroupBox(self.groupBox_2)
        self.uiGRP_folderStructure.setCheckable(True)
        self.uiGRP_folderStructure.setObjectName("uiGRP_folderStructure")
        self.gridLayout = QtGui.QGridLayout(self.uiGRP_folderStructure)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLED_sourceRoot = LineEditPath(self.uiGRP_folderStructure)
        self.uiLED_sourceRoot.setObjectName("uiLED_sourceRoot")
        self.gridLayout.addWidget(self.uiLED_sourceRoot, 0, 1, 1, 1)
        self.uiBTN_browseSource = QtGui.QToolButton(self.uiGRP_folderStructure)
        self.uiBTN_browseSource.setIcon(icon)
        self.uiBTN_browseSource.setIconSize(QtCore.QSize(18, 18))
        self.uiBTN_browseSource.setObjectName("uiBTN_browseSource")
        self.gridLayout.addWidget(self.uiBTN_browseSource, 0, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.uiGRP_folderStructure)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiGRP_folderStructure)
        self.uiGRP_addTextures = QtGui.QGroupBox(self.groupBox_2)
        self.uiGRP_addTextures.setCheckable(True)
        self.uiGRP_addTextures.setObjectName("uiGRP_addTextures")
        self.gridLayout_2 = QtGui.QGridLayout(self.uiGRP_addTextures)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_22 = QtGui.QLabel(self.uiGRP_addTextures)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)
        self.uiLED_texSuffixes = QtGui.QLineEdit(self.uiGRP_addTextures)
        self.uiLED_texSuffixes.setObjectName("uiLED_texSuffixes")
        self.gridLayout_2.addWidget(self.uiLED_texSuffixes, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiGRP_addTextures)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiLBL_status = QtGui.QLabel(Dialog)
        self.uiLBL_status.setStyleSheet("QLabel {color : red}")
        self.uiLBL_status.setText("")
        self.uiLBL_status.setObjectName("uiLBL_status")
        self.horizontalLayout_2.addWidget(self.uiLBL_status)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uiBTN_ok = QtGui.QPushButton(Dialog)
        self.uiBTN_ok.setObjectName("uiBTN_ok")
        self.horizontalLayout_2.addWidget(self.uiBTN_ok)
        self.uiBTN_cancel = QtGui.QPushButton(Dialog)
        self.uiBTN_cancel.setObjectName("uiBTN_cancel")
        self.horizontalLayout_2.addWidget(self.uiBTN_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.uiBTN_cancel, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QObject.connect(Dialog, QtCore.SIGNAL("finished(int)"), Dialog.onDialogFinished)
        QtCore.QObject.connect(self.uiBTN_ok, QtCore.SIGNAL("clicked()"), Dialog.onOkClicked)
        QtCore.QObject.connect(self.uiBTN_browseTarget, QtCore.SIGNAL("clicked()"), Dialog.onBrowseTargetClicked)
        QtCore.QObject.connect(self.uiBTN_browseSource, QtCore.SIGNAL("clicked()"), Dialog.onBrowseSourceClicked)
        QtCore.QObject.connect(self.uiLED_sourceRoot, QtCore.SIGNAL("editingFinished()"), Dialog.onValidateUiNeeded)
        QtCore.QObject.connect(self.uiLED_targetRoot, QtCore.SIGNAL("editingFinished()"), Dialog.onValidateUiNeeded)
        QtCore.QObject.connect(self.uiGRP_folderStructure, QtCore.SIGNAL("clicked()"), Dialog.onValidateUiNeeded)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.uiBTN_cancel, self.uiBTN_ok)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Copy and Move", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCHK_deleteSources.setText(QtGui.QApplication.translate("Dialog", "Delete sources", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_browseTarget.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_browseTarget.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+S, Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Copy to:", None, QtGui.QApplication.UnicodeUTF8))
        self.uiCHK_retarget.setText(QtGui.QApplication.translate("Dialog", "Retarget", None, QtGui.QApplication.UnicodeUTF8))
        self.uiGRP_folderStructure.setTitle(QtGui.QApplication.translate("Dialog", "Copy folder structure", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_browseSource.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_browseSource.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+S, Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Original root folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.uiGRP_addTextures.setTitle(QtGui.QApplication.translate("Dialog", "Copy additional textures", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Texture suffixes:", None, QtGui.QApplication.UnicodeUTF8))
        self.uiLED_texSuffixes.setText(QtGui.QApplication.translate("Dialog", "_nm, _spec, _hdetm, _em", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_ok.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from line_edit_path import LineEditPath
import resources_rc
