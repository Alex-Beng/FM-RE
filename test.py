from MyCube import *
from Visualizer import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer


if __name__ == "__main__":
    mycube = MyCube()
    mycube("r U R' U R' r2 U' R' U R' r2 U2 r'")
    mycube("U")

    print(mycube)
    svg_bytes = GetSvgBytes("r U R' U R' r2 U' R' U R' r2 U2 r'")
    app = QApplication(sys.argv)
    svgWidget = QSvgWidget()
    svgWidget.renderer().load(svg_bytes)
    svgWidget.setGeometry(100,100,300,300)
    svgWidget.show()
    sys.exit(app.exec_())

