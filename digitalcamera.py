from constants import ZOOMMIN, MEGAPIXEL
from camera import Camera

class DigitalCamera(Camera):
    def __init__(self, model="Unknown", zoom=ZOOMMIN, material="plastic", megapixels=12):
        super().__init__(model, zoom, material)
        self._megapixels = megapixels

    def cost(self):
        return super().cost() * self._megapixels

    def updatemodel(self):
        self._megapixels += MEGAPIXEL
    
    @property
    def megapixels(self):
        return self._megapixels
    
    @megapixels.setter
    def megapixels(self, value):
        self._megapixels = value

    def __str__(self):
        return (f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, "
                f"Megapixels: {self._megapixels}MP, Cost: {self.cost()} $")
