def braceyourself(MainWindow):
    MainWindow.setStyleSheet("QGroupBox {\n"
                             "  border: 2px solid gray;\n"
                             "  border-radius: 6px;\n"
                             "  margin-top: 0.5em;\n"
                             "}\n"
                             "\n"
                             "QGroupBox::title {\n"
                             "  padding-top: -10px;\n"
                             "  padding-left: 8px;\n"
                             " padding-right: 8px;\n"
                             "}")


def default(MainWindow):
    MainWindow.setStyleSheet('')
