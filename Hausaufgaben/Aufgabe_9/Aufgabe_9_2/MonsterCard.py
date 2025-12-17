import os
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtGui import QRegion, QPainterPath
from PySide6.QtCore import Qt, QSize

from ui_MonsterCard import Ui_MonsterCard

class MonsterCard(QWidget):
    def __init__(self, card_name, image_filename, parent=None):
        super().__init__(parent)
        self.ui = Ui_MonsterCard()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.horizontalLayout.setContentsMargins(8, 8, 8, 0)

        self.ui.imageLabel.setScaledContents(True)

        self.ui.nameLabel.setText(card_name)
        self.ui.nameLabel.setWordWrap(True)
        self.ui.nameLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "!Media", image_filename)

        pixmap = QPixmap(image_path)

        if not pixmap.isNull():
            side_length = 200
            target_square = QSize(side_length, side_length)

            self.ui.imageLabel.setFixedSize(target_square)

            zoom_factor = 1.1
            zoomed_size = target_square * zoom_factor

            zoomed_pixmap = pixmap.scaled(
                zoomed_size,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )

            offset_x = (zoomed_pixmap.width() - side_length) // 2
            offset_y = (zoomed_pixmap.height() - side_length) // 2

            final_pixmap = self.get_rounded_square_pixmap(
                zoomed_pixmap,
                side_length,
                offset_x,
                offset_y,
                10
            )

            self.ui.imageLabel.setPixmap(final_pixmap)
        else:
            self.ui.imageLabel.setText("Bild fehlt")

    def get_rounded_square_pixmap(self, src_pixmap, size, x, y, radius):
        out_pixmap = QPixmap(QSize(size, size))
        out_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(out_pixmap)
        # Wichtig für Schärfe und glatte Kanten
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        # Den quadratischen Pfad mit Rundung definieren
        path = QPainterPath()
        path.addRoundedRect(0, 0, size, size, radius, radius)

        painter.setClipPath(path)
        # Zeichnet das große Bild verschoben (-x, -y), sodass nur die Mitte im Quadrat landet
        painter.drawPixmap(-x, -y, src_pixmap)
        painter.end()

        return out_pixmap
