#ifndef GUITEST_H
#define GUITEST_H

#include <QMainWindow>
#include <QLabel>
#include <QSpinBox>
namespace Ui {
class GuiTest;
}

class GuiTest : public QMainWindow
{
    Q_OBJECT

public:
    explicit GuiTest(QWidget *parent = 0);
    ~GuiTest();

private slots:
    void setLabelsVisible(int index, bool visible);
    void setSpinrightVisible(int index, bool visible);
    void setSpinleftVisible(int index, bool visible);

    void getSpinrightValue(int index);
    void getSpinleftValue(int index);

    void on_toolButton_clicked();
    void on_toolButton_2_clicked();
    void on_toolButton_3_clicked();
    void on_toolButton_4_clicked();
    void on_actionExit_triggered();
    void on_pushButton_13_clicked();
    void on_pushButton_clicked();
    void spinboxWrite(int arg1, int index);


private:
    Ui::GuiTest *ui;
};

#endif // GUITEST_H
