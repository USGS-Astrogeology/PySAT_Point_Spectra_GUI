#include "guitest.h"
#include "ui_guitest.h"
#include <QString>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QFileDialog>
#include <QDebug>
#include <QRect>
#include <QDesktopWidget>
#include <QSignalMapper>
#include <QFile>
#include <QTextStream>


int normSize = 0;
int normPushValue = 0;
int isNormFilled = 0;
int isSpinBoxFilled = 0;
int normalizationBtnCnt = 0;
int spinArray[16] = {0,0,0,0,0,0,0,0,0,0,0,0};

QString pythonProgrmaFile = "";
QString outputDirectory = "";
QFile file("pls_sm_output.py");
QTextStream output(&file);

GuiTest::GuiTest (QWidget *parent):
    QMainWindow(parent), ui(new Ui::GuiTest){
    ui->setupUi(this);
    setSizeOfWindow();
    setupQSpinWidgets();
    setupOutFile();
}


GuiTest::~GuiTest(){
    delete ui;
}




void GuiTest::setSizeOfWindow(){
    QRect currentWindowSize = QApplication::desktop()->screenGeometry();
    int height = currentWindowSize.height();
    this->resize(this->width(), height*0.9);
    for (int i = 0; i < 7; i++){
        setLabelAndSpinVisible(i, false);
    }
}

void GuiTest::setupQSpinWidgets(){
    QList<QSpinBox*> allChildSpinBoxes = findChildren<QSpinBox*>();
    QSignalMapper* signalMapper = new QSignalMapper(this);
    QSpinBox oneChildSpinbox;
    foreach(oneChildSpinbox, allChildSpinBoxes){
        connect(oneChildSpinbox, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
        signalMapper->setMapping(oneChildSpinbox, oneChildSpinbox);
    }
    connect(signalMapper, SIGNAL(mapped(QWidget*)), this, SLOT(getSpinboxValue(QWidget*)));
}

void GuiTest::setupOutFile(){
    output << "from pysat.spectral.spectral_data import spectral_data\n";
    output << "from pysat.regression.pls_sm import pls_sm\n";
    output << "import pandas as pd\n";
}

void GuiTest::setLabelAndSpinVisible(int index, bool visible){
    int arraySize = 7;
    QLabel* labels[arraySize] = {ui->norm_label_2,
                                 ui->norm_label_3,
                                 ui->norm_label_4,
                                 ui->norm_label_5,
                                 ui->norm_label_6,
                                 ui->norm_label_7,
                                 ui->norm_label_8};
    QSpinBox* spinBoxR[arraySize] = {ui->norm_spinBox_2,
                                     ui->norm_spinBox_3,
                                     ui->norm_spinBox_4,
                                     ui->norm_spinBox_5,
                                     ui->norm_spinBox_6,
                                     ui->norm_spinBox_7,
                                     ui->norm_spinBox_8};
    QSpinBox* spinBoxL[arraySize] = {ui->norm_spinBox_10,
                                     ui->norm_spinBox_11,
                                     ui->norm_spinBox_12,
                                     ui->norm_spinBox_13,
                                     ui->norm_spinBox_14,
                                     ui->norm_spinBox_15,
                                     ui->norm_spinBox_16
                                    };
    labels[index]->setVisible(visible);
    spinBoxL[index]->setVisible(visible);
    spinBoxR[index]->setVisible(visible);
}

void GuiTest::on_maskFileButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Maskfile", QDir::homePath());
    ui->lineEdit->setText(file_name);
    output << "maskfile = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_unknownDataButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Unknwon Data File", QDir::homePath());
    ui->lineEdit_2->setText(file_name);
    output << "unknowndatacsv = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_fullDataBaseButton_clicked(){
    const QString &file_name = QFileDialog::getOpenFileName(this, "Select Database File", QDir::homePath());
    ui->lineEdit_3->setText(file_name);
    output << "db = \"" << file_name << "\"\n";
    isNormFilled++;
}

void GuiTest::on_outPutLocation_clicked(){
    outputDirectory = QFileDialog::getExistingDirectory(this, "Select Output Directory", QDir::homePath());
    ui->lineEdit_4->setText(outputDirectory);
    output << "outpath = \"" << outputDirectory << "\"\n";
    isNormFilled++;
}

void GuiTest::on_pythonButton_clicked(){
    pythonProgrmaFile = QFileDialog::getOpenFileName(this, "Python .exe File", QDir::rootPath());
    ui->lineEdit_6->setText(pythonProgrmaFile);
}

void GuiTest::on_NormAddValuebutton_clicked(){
    if (normPushValue >= normSize){
        QMessageBox::critical(this, "Warning", "Cannot add anymore values");
    } else {
        setLabelAndSpinVisible(normPushValue, true);
        normPushValue++;
    }
}

int GuiTest::getSpinValue(){
    QSpinBox* spinValue = (QSpinBox*)widgetSpinValue;
    int valueofSpin = spinValue->value();
    return value;
}

void GuiTest::getSpinboxValue(QWidget* e){
    int spinNum = SpinBoxChanged(e);
    QString spinboxObjectName = e->objectName();
    if (isNormFilled < 4){
        QMessageBox::critical(this, "Error", "Please add all Files");
        return;
    } else {
        output << "data = pd.read_csv(db, header=[0, 1])\n";
        output << "data = spectral_data(data)\n";
        output << "unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])\n";
        output << "unknown_data = spectral_data(unknown_data)\n";
        output << "unknown_data.interp(data.df['wvl'].columns)\n";
        output << "data.mask(maskfile)\n";
        output << "unknown_data.mask(maskfile)\n";
    }
    if ((value == QString::fromStdString("norm_spinBox"))){           ui->norm_spinBox_10->setMinimum(spinNum); spinArray1[0] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_2"))){  ui->norm_spinBox_11->setMinimum(spinNum); spinArray1[1] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_3"))){  ui->norm_spinBox_12->setMinimum(spinNum); spinArray1[2] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_4"))){  ui->norm_spinBox_13->setMinimum(spinNum); spinArray1[3] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_5"))){  ui->norm_spinBox_14->setMinimum(spinNum); spinArray1[4] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_6"))){  ui->norm_spinBox_15->setMinimum(spinNum); spinArray1[5] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_7"))){  ui->norm_spinBox_16->setMinimum(spinNum); spinArray1[6] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_8"))){                                            spinArray1[7] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_9"))){  ui->norm_spinBox->setMinimum(spinNum);    spinArray1[8] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_10"))){ ui->norm_spinBox_2->setMinimum(spinNum);  spinArray1[9] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_11"))){ ui->norm_spinBox_3->setMinimum(spinNum);  spinArray1[10] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_12"))){ ui->norm_spinBox_4->setMinimum(spinNum);  spinArray1[11] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_13"))){ ui->norm_spinBox_5->setMinimum(spinNum);  spinArray1[12] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_14"))){ ui->norm_spinBox_6->setMinimum(spinNum);  spinArray1[13] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_15"))){ ui->norm_spinBox_7->setMinimum(spinNum);  spinArray1[14] = spinNum;
    } else if ((value == QString::fromStdString("norm_spinBox_16"))){ ui->norm_spinBox_8->setMinimum(spinNum);  spinArray1[15] = spinNum;
    }
}


void GuiTest::on_okButton_clicked(){
    file.close();
    //    system(qPrintable(python_file + " " + output_location+"pls_sm_test"));
    system(qPrintable(python_file + " " + "out.py"));
}

