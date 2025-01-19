from PyQt6 import QtCharts
from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime, QDate
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__line_series_CDU = QLineSeries()
        self.__line_series_CDU.setName("CDU")
        self.__line_series_CDU.setColor(QColor(18, 18, 18))
        self.__line_series_SPD = QLineSeries()
        self.__line_series_SPD.setName("SPD")
        self.__line_series_SPD.setColor(QColor(215, 31, 29))
        self.__line_series_GRÜNE = QLineSeries()
        self.__line_series_GRÜNE.setName("GRÜNE")
        self.__line_series_GRÜNE.setColor(QColor(120, 188, 27))
        self.__line_series_FDP = QLineSeries()
        self.__line_series_FDP.setName("FDP")
        self.__line_series_FDP.setColor(QColor(255, 204, 0))
        self.__line_series_AFD = QLineSeries()
        self.__line_series_AFD.setName("AFD")
        self.__line_series_AFD.setColor(QColor(0, 158, 224))
        self.__line_series_LINKE = QLineSeries()
        self.__line_series_LINKE.setName("LINKE")
        self.__line_series_LINKE.setColor(QColor(190, 48, 117))
        self.__line_series_BSW = QLineSeries()
        self.__line_series_BSW.setName("BSW")
        self.__line_series_BSW.setColor(QColor(105, 24, 64))
        self.__line_series_ANDERE = QLineSeries()
        self.__line_series_ANDERE.setName("ANDERE")
        self.__line_series_ANDERE.setColor(QColor(112, 113, 115))

        x_axis = QDateTimeAxis()
        curret_date_diff_ende = -66
        start_date = QDateTime.currentDateTime().addDays(curret_date_diff_ende)
        end_date = QDateTime.currentDateTime().addDays(-4)
        x_axis.setRange(start_date, end_date)
        x_axis.setFormat("dd.MM.yyyy")

        y_axis = QValueAxis()
        y_axis.setRange(0, 50)

        chart = QChart()

        chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)

        chart.setWindowTitle('Hier könnte Ihr Titel stehen')
        chart.addSeries(self.__line_series_CDU)
        chart.addSeries(self.__line_series_SPD)
        chart.addSeries(self.__line_series_GRÜNE)
        chart.addSeries(self.__line_series_FDP)
        chart.addSeries(self.__line_series_AFD)
        chart.addSeries(self.__line_series_LINKE)
        chart.addSeries(self.__line_series_BSW)
        chart.addSeries(self.__line_series_ANDERE)

        self.__line_series_CDU.attachAxis(x_axis)
        self.__line_series_CDU.attachAxis(y_axis)

        self.__line_series_SPD.attachAxis(x_axis)
        self.__line_series_SPD.attachAxis(y_axis)

        self.__line_series_GRÜNE.attachAxis(x_axis)
        self.__line_series_GRÜNE.attachAxis(y_axis)

        self.__line_series_FDP.attachAxis(x_axis)
        self.__line_series_FDP.attachAxis(y_axis)

        self.__line_series_AFD.attachAxis(x_axis)
        self.__line_series_AFD.attachAxis(y_axis)

        self.__line_series_LINKE.attachAxis(x_axis)
        self.__line_series_LINKE.attachAxis(y_axis)

        self.__line_series_BSW.attachAxis(x_axis)
        self.__line_series_BSW.attachAxis(y_axis)

        self.__line_series_ANDERE.attachAxis(x_axis)
        self.__line_series_ANDERE.attachAxis(y_axis)

        self.__line_series_CDU.append(QDateTime.currentDateTime().addDays(curret_date_diff_ende).toMSecsSinceEpoch(),
                                      34)
        self.__line_series_CDU.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 8).toMSecsSinceEpoch(), 33)
        self.__line_series_CDU.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 29).toMSecsSinceEpoch(), 32)
        self.__line_series_CDU.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 43).toMSecsSinceEpoch(), 33)
        self.__line_series_CDU.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 65).toMSecsSinceEpoch(), 31)

        self.__line_series_SPD.append(QDateTime.currentDateTime().addDays(curret_date_diff_ende).toMSecsSinceEpoch(),
                                      16)
        self.__line_series_SPD.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 8).toMSecsSinceEpoch(), 14)
        self.__line_series_SPD.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 29).toMSecsSinceEpoch(), 16)
        self.__line_series_SPD.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 43).toMSecsSinceEpoch(), 14)
        self.__line_series_SPD.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 65).toMSecsSinceEpoch(), 15)

        self.__line_series_GRÜNE.append(QDateTime.currentDateTime().addDays(curret_date_diff_ende).toMSecsSinceEpoch(),
                                        12)
        self.__line_series_GRÜNE.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 8).toMSecsSinceEpoch(), 14)
        self.__line_series_GRÜNE.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 29).toMSecsSinceEpoch(), 14)
        self.__line_series_GRÜNE.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 43).toMSecsSinceEpoch(), 14)
        self.__line_series_GRÜNE.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 65).toMSecsSinceEpoch(), 14)

        self.__line_series_FDP.append(QDateTime.currentDateTime().addDays(curret_date_diff_ende).toMSecsSinceEpoch(),
                                        5)
        self.__line_series_FDP.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 8).toMSecsSinceEpoch(), 4)
        self.__line_series_FDP.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 29).toMSecsSinceEpoch(), 4)
        self.__line_series_FDP.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 43).toMSecsSinceEpoch(), 14)
        self.__line_series_FDP.append(
            QDateTime.currentDateTime().addDays(curret_date_diff_ende + 65).toMSecsSinceEpoch(), 14)

        self.setChart(chart)
