class Camera:
    total_cameras = 0
    
    def __init__(self, model="Unknown", zoom=1.0, material="plastic"):
        self._model = model
        self._zoom = zoom
        self._material = material
        Camera.total_cameras += 1
    
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
        if 1.0 <= value <= 35.0:
            self._zoom = value
        else:
            raise ValueError("Zoom must be between 1 and 35")

    def cost(self):
        base_cost = (self._zoom + 2) * 100
        if self._material == "metal":
            return base_cost * 2
        return base_cost

    def expensive(self):
        return self.cost() > 2000
    
    def __str__(self):
        return f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, Cost: {self.cost()} $"

    @staticmethod
    def get_total_cameras():
        return Camera.total_cameras


class DigitalCamera(Camera):
    def __init__(self, model="Unknown", zoom=1.0, material="plastic", megapixels=12):
        super().__init__(model, zoom, material)
        self._megapixels = megapixels

    def cost(self):
        return super().cost() * self._megapixels

    def updatemodel(self):
        self._megapixels += 2
    
    @property
    def megapixels(self):
        return self._megapixels
    
    @megapixels.setter
    def megapixels(self, value):
        self._megapixels = value

    def __str__(self):
        return (f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, "
                f"Megapixels: {self._megapixels}MP, Cost: {self.cost()} $")


camera1 = Camera("Canon", 15, "plastic")
print(camera1)
print(camera1.expensive())

digital_camera = DigitalCamera("Nikon", 20, "metal", 24)
print(digital_camera)
print(digital_camera.expensive())

digital_camera.updatemodel()
print(digital_camera)

print("Total cameras:", Camera.get_total_cameras())
