from constants import ZOOMMIN, ZOOMMAX, PLASTIC, METAL, BASECOST

class Camera:
    countcameras = {
        "total": 0
    }
    
    def __init__(self, model="Unknown", zoom=ZOOMMIN, material="plastic"):
        self._model = model
        self._zoom = zoom
        self._material = material
        Camera.countcameras["total"] += 1
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        if ZOOMMIN <= value <= ZOOMMAX:
            self._zoom = value
        else:
            raise ValueError(f"Zoom must be between {ZOOMMIN} and {ZOOMMAX}")

    def cost(self):
        base_cost = (self._zoom + PLASTIC) * BASECOST
        if self._material == "metal":
            return base_cost * METAL
        return base_cost

    def expensive(self):
        return self.cost() > 2000
    
    def __str__(self):
        return f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, Cost: {self.cost()} $"

    @staticmethod
    def countscameras():
        return Camera.countcameras["total"]
