# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfesionalesjdwBSJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_Profesionales(object):
    def setupUi(self, Profesionales):
        if not Profesionales.objectName():
            Profesionales.setObjectName(u"Profesionales")
        Profesionales.resize(1385, 829)
        Profesionales.setAutoFillBackground(False)
        self.ProfesionalesWidget = QWidget(Profesionales)
        self.ProfesionalesWidget.setObjectName(u"ProfesionalesWidget")
        self.horizontalLayout = QHBoxLayout(self.ProfesionalesWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ProfesionalesFrame = QFrame(self.ProfesionalesWidget)
        self.ProfesionalesFrame.setObjectName(u"ProfesionalesFrame")
        self.ProfesionalesFrame.setFrameShape(QFrame.StyledPanel)
        self.ProfesionalesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ProfesionalesFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BarraNavegacionBox = QFrame(self.ProfesionalesFrame)
        self.BarraNavegacionBox.setObjectName(u"BarraNavegacionBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BarraNavegacionBox.sizePolicy().hasHeightForWidth())
        self.BarraNavegacionBox.setSizePolicy(sizePolicy)
        self.BarraNavegacionBox.setMaximumSize(QSize(1920, 90))
        self.BarraNavegacionBox.setBaseSize(QSize(1248, 90))
        self.BarraNavegacionBox.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.BarraNavegacionBox.setFrameShape(QFrame.StyledPanel)
        self.BarraNavegacionBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.BarraNavegacionBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Flechas = QFrame(self.BarraNavegacionBox)
        self.Flechas.setObjectName(u"Flechas")
        self.Flechas.setFrameShape(QFrame.StyledPanel)
        self.Flechas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Flechas)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.FlechasBox = QFrame(self.Flechas)
        self.FlechasBox.setObjectName(u"FlechasBox")
        self.FlechasBox.setFrameShape(QFrame.StyledPanel)
        self.FlechasBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.FlechasBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_FlechaI = QPushButton(self.FlechasBox)
        self.bt_FlechaI.setObjectName(u"bt_FlechaI")

        self.horizontalLayout_5.addWidget(self.bt_FlechaI)

        self.bt_FlechaD = QPushButton(self.FlechasBox)
        self.bt_FlechaD.setObjectName(u"bt_FlechaD")

        self.horizontalLayout_5.addWidget(self.bt_FlechaD)


        self.horizontalLayout_4.addWidget(self.FlechasBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.HomeBox = QFrame(self.Flechas)
        self.HomeBox.setObjectName(u"HomeBox")
        self.HomeBox.setFrameShape(QFrame.StyledPanel)
        self.HomeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.HomeBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_Home = QPushButton(self.HomeBox)
        self.bt_Home.setObjectName(u"bt_Home")

        self.verticalLayout_3.addWidget(self.bt_Home)


        self.horizontalLayout_4.addWidget(self.HomeBox)


        self.horizontalLayout_2.addWidget(self.Flechas)

        self.MenuBox = QFrame(self.BarraNavegacionBox)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setFrameShape(QFrame.StyledPanel)
        self.MenuBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.MenuBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_Profesionales = QPushButton(self.MenuBox)
        self.bt_Profesionales.setObjectName(u"bt_Profesionales")

        self.horizontalLayout_3.addWidget(self.bt_Profesionales)

        self.bt_Pacientes = QPushButton(self.MenuBox)
        self.bt_Pacientes.setObjectName(u"bt_Pacientes")

        self.horizontalLayout_3.addWidget(self.bt_Pacientes)

        self.bt_Alertas = QPushButton(self.MenuBox)
        self.bt_Alertas.setObjectName(u"bt_Alertas")

        self.horizontalLayout_3.addWidget(self.bt_Alertas)


        self.horizontalLayout_2.addWidget(self.MenuBox)

        self.ReporteFechaBox = QFrame(self.BarraNavegacionBox)
        self.ReporteFechaBox.setObjectName(u"ReporteFechaBox")
        self.ReporteFechaBox.setFrameShape(QFrame.StyledPanel)
        self.ReporteFechaBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ReporteFechaBox)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.ReporteFechaBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.ReporteFechaBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.BarraNavegacionBox)

        self.ContenidoBox = QFrame(self.ProfesionalesFrame)
        self.ContenidoBox.setObjectName(u"ContenidoBox")
        self.ContenidoBox.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.ContenidoBox.setFrameShape(QFrame.StyledPanel)
        self.ContenidoBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ContenidoBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ListaProfesionalesBox = QFrame(self.ContenidoBox)
        self.ListaProfesionalesBox.setObjectName(u"ListaProfesionalesBox")
        self.ListaProfesionalesBox.setStyleSheet(u"background-color: rgb(177, 177, 177);")
        self.ListaProfesionalesBox.setFrameShape(QFrame.StyledPanel)
        self.ListaProfesionalesBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ListaProfesionalesBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.BuscadorBox = QFrame(self.ListaProfesionalesBox)
        self.BuscadorBox.setObjectName(u"BuscadorBox")
        self.BuscadorBox.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.BuscadorBox.setFrameShape(QFrame.StyledPanel)
        self.BuscadorBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.BuscadorBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.inputBusqueda = QLineEdit(self.BuscadorBox)
        self.inputBusqueda.setObjectName(u"inputBusqueda")

        self.horizontalLayout_8.addWidget(self.inputBusqueda)

        self.bt_Buscar = QPushButton(self.BuscadorBox)
        self.bt_Buscar.setObjectName(u"bt_Buscar")

        self.horizontalLayout_8.addWidget(self.bt_Buscar)


        self.verticalLayout_4.addWidget(self.BuscadorBox)

        self.FiltroBox = QFrame(self.ListaProfesionalesBox)
        self.FiltroBox.setObjectName(u"FiltroBox")
        self.FiltroBox.setFrameShape(QFrame.StyledPanel)
        self.FiltroBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.FiltroBox)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.filtrosBarra = QComboBox(self.FiltroBox)
        self.filtrosBarra.setObjectName(u"filtrosBarra")

        self.horizontalLayout_9.addWidget(self.filtrosBarra)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.FiltroBox)

        self.ListadoBox = QFrame(self.ListaProfesionalesBox)
        self.ListadoBox.setObjectName(u"ListadoBox")
        self.ListadoBox.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.ListadoBox.setFrameShape(QFrame.StyledPanel)
        self.ListadoBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.ListadoBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ListaBox = QScrollArea(self.ListadoBox)
        self.ListaBox.setObjectName(u"ListaBox")
        self.ListaBox.setWidgetResizable(True)
        self.listaProfesionalesScroll = QWidget()
        self.listaProfesionalesScroll.setObjectName(u"listaProfesionalesScroll")
        self.listaProfesionalesScroll.setGeometry(QRect(0, 0, 550, 585))
        self.ListaBox.setWidget(self.listaProfesionalesScroll)

        self.horizontalLayout_10.addWidget(self.ListaBox)


        self.verticalLayout_4.addWidget(self.ListadoBox)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 25)

        self.horizontalLayout_7.addWidget(self.ListaProfesionalesBox)

        self.DatosBox = QFrame(self.ContenidoBox)
        self.DatosBox.setObjectName(u"DatosBox")
        self.DatosBox.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.DatosBox.setFrameShape(QFrame.StyledPanel)
        self.DatosBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.DatosBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.DatosProfesionalBox = QFrame(self.DatosBox)
        self.DatosProfesionalBox.setObjectName(u"DatosProfesionalBox")
        self.DatosProfesionalBox.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.DatosProfesionalBox.setFrameShape(QFrame.StyledPanel)
        self.DatosProfesionalBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.DatosProfesionalBox)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.TituloDatos = QFrame(self.DatosProfesionalBox)
        self.TituloDatos.setObjectName(u"TituloDatos")
        self.TituloDatos.setStyleSheet(u"background: #669098;")
        self.TituloDatos.setFrameShape(QFrame.StyledPanel)
        self.TituloDatos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.TituloDatos)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tit_DatosProfesional = QLabel(self.TituloDatos)
        self.tit_DatosProfesional.setObjectName(u"tit_DatosProfesional")

        self.verticalLayout_10.addWidget(self.tit_DatosProfesional, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.TituloDatos)

        self.DatosPrincipalesBox = QFrame(self.DatosProfesionalBox)
        self.DatosPrincipalesBox.setObjectName(u"DatosPrincipalesBox")
        self.DatosPrincipalesBox.setStyleSheet(u"background: #F4F4F4;")
        self.DatosPrincipalesBox.setFrameShape(QFrame.StyledPanel)
        self.DatosPrincipalesBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.DatosPrincipalesBox)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.DatosEspecificosBox = QFrame(self.DatosPrincipalesBox)
        self.DatosEspecificosBox.setObjectName(u"DatosEspecificosBox")
        self.DatosEspecificosBox.setFrameShape(QFrame.StyledPanel)
        self.DatosEspecificosBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.DatosEspecificosBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.datos_Nombre = QLabel(self.DatosEspecificosBox)
        self.datos_Nombre.setObjectName(u"datos_Nombre")

        self.verticalLayout_11.addWidget(self.datos_Nombre)

        self.datos_Rut = QLabel(self.DatosEspecificosBox)
        self.datos_Rut.setObjectName(u"datos_Rut")

        self.verticalLayout_11.addWidget(self.datos_Rut)

        self.datos_Cargo = QLabel(self.DatosEspecificosBox)
        self.datos_Cargo.setObjectName(u"datos_Cargo")

        self.verticalLayout_11.addWidget(self.datos_Cargo)


        self.horizontalLayout_13.addWidget(self.DatosEspecificosBox)

        self.AreaBox = QFrame(self.DatosPrincipalesBox)
        self.AreaBox.setObjectName(u"AreaBox")
        self.AreaBox.setFrameShape(QFrame.StyledPanel)
        self.AreaBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.AreaBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.area = QFrame(self.AreaBox)
        self.area.setObjectName(u"area")
        self.area.setStyleSheet(u"background: #45CBDC;")
        self.area.setFrameShape(QFrame.StyledPanel)
        self.area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.area)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.datos_Area = QLabel(self.area)
        self.datos_Area.setObjectName(u"datos_Area")

        self.verticalLayout_13.addWidget(self.datos_Area, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.area)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)
        self.horizontalLayout_14.setStretch(2, 1)

        self.horizontalLayout_13.addWidget(self.AreaBox)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.DatosPrincipalesBox)

        self.CoordinacionBox = QFrame(self.DatosProfesionalBox)
        self.CoordinacionBox.setObjectName(u"CoordinacionBox")
        self.CoordinacionBox.setStyleSheet(u"background: #DEEFF2;")
        self.CoordinacionBox.setFrameShape(QFrame.StyledPanel)
        self.CoordinacionBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.CoordinacionBox)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.CoordinadorBox = QFrame(self.CoordinacionBox)
        self.CoordinadorBox.setObjectName(u"CoordinadorBox")
        self.CoordinadorBox.setFrameShape(QFrame.StyledPanel)
        self.CoordinadorBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.CoordinadorBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.datos_Coordinador = QLabel(self.CoordinadorBox)
        self.datos_Coordinador.setObjectName(u"datos_Coordinador")

        self.verticalLayout_12.addWidget(self.datos_Coordinador)

        self.datos_SIS = QLabel(self.CoordinadorBox)
        self.datos_SIS.setObjectName(u"datos_SIS")

        self.verticalLayout_12.addWidget(self.datos_SIS)


        self.horizontalLayout_15.addWidget(self.CoordinadorBox)

        self.ContratoBox = QFrame(self.CoordinacionBox)
        self.ContratoBox.setObjectName(u"ContratoBox")
        self.ContratoBox.setFrameShape(QFrame.StyledPanel)
        self.ContratoBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.ContratoBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.datos_Contrato = QLabel(self.ContratoBox)
        self.datos_Contrato.setObjectName(u"datos_Contrato")

        self.verticalLayout_14.addWidget(self.datos_Contrato)

        self.datos_Otro = QLabel(self.ContratoBox)
        self.datos_Otro.setObjectName(u"datos_Otro")

        self.verticalLayout_14.addWidget(self.datos_Otro)


        self.horizontalLayout_15.addWidget(self.ContratoBox)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.CoordinacionBox)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 2)

        self.verticalLayout_6.addWidget(self.DatosProfesionalBox)

        self.Metricas = QFrame(self.DatosBox)
        self.Metricas.setObjectName(u"Metricas")
        self.Metricas.setStyleSheet(u"background-color: rgb(255, 60, 187);")
        self.Metricas.setFrameShape(QFrame.StyledPanel)
        self.Metricas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Metricas)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.EstadisticasBox = QFrame(self.Metricas)
        self.EstadisticasBox.setObjectName(u"EstadisticasBox")
        self.EstadisticasBox.setStyleSheet(u"background-color: rgb(213, 176, 255);")
        self.EstadisticasBox.setFrameShape(QFrame.StyledPanel)
        self.EstadisticasBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.EstadisticasBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.MetricaAsistBox = QFrame(self.EstadisticasBox)
        self.MetricaAsistBox.setObjectName(u"MetricaAsistBox")
        self.MetricaAsistBox.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.MetricaAsistBox.setFrameShape(QFrame.StyledPanel)
        self.MetricaAsistBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.MetricaAsistBox)
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.InasistenciaBox = QFrame(self.MetricaAsistBox)
        self.InasistenciaBox.setObjectName(u"InasistenciaBox")
        self.InasistenciaBox.setMinimumSize(QSize(122, 0))
        self.InasistenciaBox.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.InasistenciaBox.setFrameShape(QFrame.StyledPanel)
        self.InasistenciaBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.InasistenciaBox)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tituloInasis = QFrame(self.InasistenciaBox)
        self.tituloInasis.setObjectName(u"tituloInasis")
        self.tituloInasis.setStyleSheet(u"background: #48ABBF;")
        self.tituloInasis.setFrameShape(QFrame.StyledPanel)
        self.tituloInasis.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.tituloInasis)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tit_Inasistencias = QLabel(self.tituloInasis)
        self.tit_Inasistencias.setObjectName(u"tit_Inasistencias")

        self.verticalLayout_16.addWidget(self.tit_Inasistencias, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.tituloInasis)

        self.metricaIna = QFrame(self.InasistenciaBox)
        self.metricaIna.setObjectName(u"metricaIna")
        self.metricaIna.setStyleSheet(u"background: #FFFFFF;")
        self.metricaIna.setFrameShape(QFrame.StyledPanel)
        self.metricaIna.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.metricaIna)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.n_Inasistencias = QLabel(self.metricaIna)
        self.n_Inasistencias.setObjectName(u"n_Inasistencias")

        self.verticalLayout_17.addWidget(self.n_Inasistencias, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.metricaIna)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 2)

        self.horizontalLayout_12.addWidget(self.InasistenciaBox)

        self.JustificadasBox = QFrame(self.MetricaAsistBox)
        self.JustificadasBox.setObjectName(u"JustificadasBox")
        self.JustificadasBox.setMinimumSize(QSize(122, 0))
        self.JustificadasBox.setStyleSheet(u"background-color: rgb(149, 73, 255);")
        self.JustificadasBox.setFrameShape(QFrame.StyledPanel)
        self.JustificadasBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.JustificadasBox)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.titJust = QFrame(self.JustificadasBox)
        self.titJust.setObjectName(u"titJust")
        self.titJust.setStyleSheet(u"background: #48ABBF;")
        self.titJust.setFrameShape(QFrame.StyledPanel)
        self.titJust.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.titJust)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tit_Justificadas = QLabel(self.titJust)
        self.tit_Justificadas.setObjectName(u"tit_Justificadas")

        self.verticalLayout_19.addWidget(self.tit_Justificadas, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.titJust)

        self.metricaJust = QFrame(self.JustificadasBox)
        self.metricaJust.setObjectName(u"metricaJust")
        self.metricaJust.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.metricaJust.setFrameShape(QFrame.StyledPanel)
        self.metricaJust.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.metricaJust)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.n_Justificadas = QLabel(self.metricaJust)
        self.n_Justificadas.setObjectName(u"n_Justificadas")

        self.verticalLayout_20.addWidget(self.n_Justificadas, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.metricaJust)

        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 2)

        self.horizontalLayout_12.addWidget(self.JustificadasBox)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_8.addWidget(self.MetricaAsistBox)

        self.HorasTrabajadasBox = QFrame(self.EstadisticasBox)
        self.HorasTrabajadasBox.setObjectName(u"HorasTrabajadasBox")
        self.HorasTrabajadasBox.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.HorasTrabajadasBox.setFrameShape(QFrame.StyledPanel)
        self.HorasTrabajadasBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.HorasTrabajadasBox)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.MetricaHorasBox = QFrame(self.HorasTrabajadasBox)
        self.MetricaHorasBox.setObjectName(u"MetricaHorasBox")
        self.MetricaHorasBox.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.MetricaHorasBox.setFrameShape(QFrame.StyledPanel)
        self.MetricaHorasBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.MetricaHorasBox)
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.RealizadasBox = QFrame(self.MetricaHorasBox)
        self.RealizadasBox.setObjectName(u"RealizadasBox")
        self.RealizadasBox.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.RealizadasBox.setFrameShape(QFrame.StyledPanel)
        self.RealizadasBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.RealizadasBox)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tituloHoras = QFrame(self.RealizadasBox)
        self.tituloHoras.setObjectName(u"tituloHoras")
        self.tituloHoras.setMinimumSize(QSize(122, 0))
        self.tituloHoras.setStyleSheet(u"background: #48ABBF;")
        self.tituloHoras.setFrameShape(QFrame.StyledPanel)
        self.tituloHoras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.tituloHoras)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tit_Horas = QLabel(self.tituloHoras)
        self.tit_Horas.setObjectName(u"tit_Horas")

        self.verticalLayout_22.addWidget(self.tit_Horas, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.tituloHoras)

        self.metricaHoras = QFrame(self.RealizadasBox)
        self.metricaHoras.setObjectName(u"metricaHoras")
        self.metricaHoras.setStyleSheet(u"background: #FFFFFF;")
        self.metricaHoras.setFrameShape(QFrame.StyledPanel)
        self.metricaHoras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.metricaHoras)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.n_Horas = QLabel(self.metricaHoras)
        self.n_Horas.setObjectName(u"n_Horas")

        self.verticalLayout_23.addWidget(self.n_Horas, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.metricaHoras)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 2)

        self.horizontalLayout_16.addWidget(self.RealizadasBox)

        self.ExtrasBox = QFrame(self.MetricaHorasBox)
        self.ExtrasBox.setObjectName(u"ExtrasBox")
        self.ExtrasBox.setMinimumSize(QSize(122, 0))
        self.ExtrasBox.setStyleSheet(u"background-color: rgb(149, 73, 255);")
        self.ExtrasBox.setFrameShape(QFrame.StyledPanel)
        self.ExtrasBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.ExtrasBox)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.titExtra = QFrame(self.ExtrasBox)
        self.titExtra.setObjectName(u"titExtra")
        self.titExtra.setStyleSheet(u"background: #48ABBF;")
        self.titExtra.setFrameShape(QFrame.StyledPanel)
        self.titExtra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.titExtra)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.tit_Extra = QLabel(self.titExtra)
        self.tit_Extra.setObjectName(u"tit_Extra")

        self.verticalLayout_25.addWidget(self.tit_Extra, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.titExtra)

        self.metricaExtra = QFrame(self.ExtrasBox)
        self.metricaExtra.setObjectName(u"metricaExtra")
        self.metricaExtra.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.metricaExtra.setFrameShape(QFrame.StyledPanel)
        self.metricaExtra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.metricaExtra)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.n_Extra = QLabel(self.metricaExtra)
        self.n_Extra.setObjectName(u"n_Extra")

        self.verticalLayout_26.addWidget(self.n_Extra, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.metricaExtra)

        self.verticalLayout_24.setStretch(0, 1)
        self.verticalLayout_24.setStretch(1, 2)

        self.horizontalLayout_16.addWidget(self.ExtrasBox)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_27.addWidget(self.MetricaHorasBox)


        self.verticalLayout_8.addWidget(self.HorasTrabajadasBox)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)

        self.horizontalLayout_11.addWidget(self.EstadisticasBox)

        self.CalendarioBox = QFrame(self.Metricas)
        self.CalendarioBox.setObjectName(u"CalendarioBox")
        self.CalendarioBox.setStyleSheet(u"background-color: rgb(255, 85, 127);")
        self.CalendarioBox.setFrameShape(QFrame.StyledPanel)
        self.CalendarioBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.CalendarioBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.calendarWidget = QCalendarWidget(self.CalendarioBox)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_7.addWidget(self.calendarWidget)


        self.horizontalLayout_11.addWidget(self.CalendarioBox)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.Metricas)

        self.HistorialBox = QFrame(self.DatosBox)
        self.HistorialBox.setObjectName(u"HistorialBox")
        self.HistorialBox.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.HistorialBox.setFrameShape(QFrame.StyledPanel)
        self.HistorialBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.HistorialBox)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.BotonesCambioBox = QFrame(self.HistorialBox)
        self.BotonesCambioBox.setObjectName(u"BotonesCambioBox")
        self.BotonesCambioBox.setStyleSheet(u"background: #669098;")
        self.BotonesCambioBox.setFrameShape(QFrame.StyledPanel)
        self.BotonesCambioBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.BotonesCambioBox)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bt_Remuneraciones = QPushButton(self.BotonesCambioBox)
        self.bt_Remuneraciones.setObjectName(u"bt_Remuneraciones")

        self.horizontalLayout_17.addWidget(self.bt_Remuneraciones)

        self.bt_Historial = QPushButton(self.BotonesCambioBox)
        self.bt_Historial.setObjectName(u"bt_Historial")

        self.horizontalLayout_17.addWidget(self.bt_Historial)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_28.addWidget(self.BotonesCambioBox)

        self.OpcionesBox = QFrame(self.HistorialBox)
        self.OpcionesBox.setObjectName(u"OpcionesBox")
        self.OpcionesBox.setFrameShape(QFrame.StyledPanel)
        self.OpcionesBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.OpcionesBox)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.RemuneracionBox = QFrame(self.OpcionesBox)
        self.RemuneracionBox.setObjectName(u"RemuneracionBox")
        self.RemuneracionBox.setStyleSheet(u"background: #F9F9F9;")
        self.RemuneracionBox.setFrameShape(QFrame.StyledPanel)
        self.RemuneracionBox.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.RemuneracionBox)

        self.HistorialPacientesBox = QScrollArea(self.OpcionesBox)
        self.HistorialPacientesBox.setObjectName(u"HistorialPacientesBox")
        self.HistorialPacientesBox.setStyleSheet(u"background: #FFFFFF;")
        self.HistorialPacientesBox.setWidgetResizable(True)
        self.historialPacientesScroll = QWidget()
        self.historialPacientesScroll.setObjectName(u"historialPacientesScroll")
        self.historialPacientesScroll.setGeometry(QRect(0, 0, 349, 182))
        self.HistorialPacientesBox.setWidget(self.historialPacientesScroll)

        self.horizontalLayout_18.addWidget(self.HistorialPacientesBox)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)

        self.verticalLayout_28.addWidget(self.OpcionesBox)

        self.verticalLayout_28.setStretch(0, 1)
        self.verticalLayout_28.setStretch(1, 20)

        self.verticalLayout_6.addWidget(self.HistorialBox)

        self.ObtenerBox = QFrame(self.DatosBox)
        self.ObtenerBox.setObjectName(u"ObtenerBox")
        self.ObtenerBox.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.ObtenerBox.setFrameShape(QFrame.StyledPanel)
        self.ObtenerBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.ObtenerBox)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.bt_Obtener = QPushButton(self.ObtenerBox)
        self.bt_Obtener.setObjectName(u"bt_Obtener")

        self.horizontalLayout_19.addWidget(self.bt_Obtener)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 2)
        self.horizontalLayout_19.setStretch(2, 1)

        self.verticalLayout_6.addWidget(self.ObtenerBox)

        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 3)
        self.verticalLayout_6.setStretch(2, 8)
        self.verticalLayout_6.setStretch(3, 1)

        self.horizontalLayout_7.addWidget(self.DatosBox)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.ContenidoBox)


        self.horizontalLayout.addWidget(self.ProfesionalesFrame)

        Profesionales.setCentralWidget(self.ProfesionalesWidget)

        self.retranslateUi(Profesionales)

        QMetaObject.connectSlotsByName(Profesionales)
    # setupUi

    def retranslateUi(self, Profesionales):
        Profesionales.setWindowTitle(QCoreApplication.translate("Profesionales", u"MainWindow", None))
        self.bt_FlechaI.setText(QCoreApplication.translate("Profesionales", u"Iz", None))
        self.bt_FlechaD.setText(QCoreApplication.translate("Profesionales", u"Dr", None))
        self.bt_Home.setText(QCoreApplication.translate("Profesionales", u"Home", None))
        self.bt_Profesionales.setText(QCoreApplication.translate("Profesionales", u"Profesionales", None))
        self.bt_Pacientes.setText(QCoreApplication.translate("Profesionales", u"Pacientes", None))
        self.bt_Alertas.setText(QCoreApplication.translate("Profesionales", u"Alertas", None))
        self.label.setText(QCoreApplication.translate("Profesionales", u"UltimoReporte: 12-12-1234", None))
        self.bt_Buscar.setText(QCoreApplication.translate("Profesionales", u"Buscar", None))
        self.tit_DatosProfesional.setText(QCoreApplication.translate("Profesionales", u"Datos del Profesional", None))
        self.datos_Nombre.setText(QCoreApplication.translate("Profesionales", u"Nombre:  mmmm mmmmm", None))
        self.datos_Rut.setText(QCoreApplication.translate("Profesionales", u"Rut:  12.345.678-9", None))
        self.datos_Cargo.setText(QCoreApplication.translate("Profesionales", u"Cargo: cargo", None))
        self.datos_Area.setText(QCoreApplication.translate("Profesionales", u"Cuidados", None))
        self.datos_Coordinador.setText(QCoreApplication.translate("Profesionales", u"Coordinador:", None))
        self.datos_SIS.setText(QCoreApplication.translate("Profesionales", u"SIS:", None))
        self.datos_Contrato.setText(QCoreApplication.translate("Profesionales", u"Contrato", None))
        self.datos_Otro.setText(QCoreApplication.translate("Profesionales", u"Otro:", None))
        self.tit_Inasistencias.setText(QCoreApplication.translate("Profesionales", u"Inasistencias", None))
        self.n_Inasistencias.setText(QCoreApplication.translate("Profesionales", u"12", None))
        self.tit_Justificadas.setText(QCoreApplication.translate("Profesionales", u"Justificadas", None))
        self.n_Justificadas.setText(QCoreApplication.translate("Profesionales", u"13", None))
        self.tit_Horas.setText(QCoreApplication.translate("Profesionales", u"Horas Realizadas", None))
        self.n_Horas.setText(QCoreApplication.translate("Profesionales", u"12", None))
        self.tit_Extra.setText(QCoreApplication.translate("Profesionales", u"Horas Extras", None))
        self.n_Extra.setText(QCoreApplication.translate("Profesionales", u"13", None))
        self.bt_Remuneraciones.setText(QCoreApplication.translate("Profesionales", u"Remuneracion", None))
        self.bt_Historial.setText(QCoreApplication.translate("Profesionales", u"Asistencias", None))
        self.bt_Obtener.setText(QCoreApplication.translate("Profesionales", u"Obtener Reporte", None))
    # retranslateUi

