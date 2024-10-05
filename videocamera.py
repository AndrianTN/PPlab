from constants import ZOOMMIN, RESOLUTION
from camera import Camera

class VideoCamera(Camera):
    def __init__(self, model="Unknown", zoom=ZOOMMIN, material="plastic", resolution="1080p"):
        super().__init__(model, zoom, material)
        self._resolution = resolution

    def cost(self):
        base_cost = super().cost()
        if self._resolution == "4K":
            return base_cost * RESOLUTION
        return base_cost

    def __str__(self):
        return f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, Resolution: {self._resolution}, Cost: {self.cost()} $"
