from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from src.config import Config


class PieCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=Config.CANVAS_WIDTH.value, height=Config.CANVAS_HEIGHT.value, dpi=Config.CANVAS_DPI.value):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.axis("off")
        super(PieCanvas, self).__init__(fig)
