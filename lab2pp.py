class Camera:
    countcameras = 0
    
    def __init__(self, model="Unknown", zoom=1.0, material="plastic"):
        self._model = model
        self._zoom = zoom
        self._material = material
        Camera.countcameras += 1
    
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
    def countscameras():
        return Camera.countcameras


class Accessory:
    def __init__(self, accessorytype="Unknown"):
        self._accessorytype = accessorytype
    
    def description(self):
        return f"Accessory type: {self._accessorytype}"


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


class ProfessionalCamera(DigitalCamera, Accessory):
    def __init__(self, model="Unknown", zoom=1.0, material="plastic", megapixels=24, accessory_type="Tripod"):
        DigitalCamera.__init__(self, model, zoom, material, megapixels)
        Accessory.__init__(self, accessory_type)

    def fulldescription(self):
        return f"{self.__str__()} and comes with {self.description()}"

    def cost(self):
        return super().cost() + 500


class VideoCamera(Camera):
    def __init__(self, model="Unknown", zoom=1.0, material="plastic", resolution="1080p"):
        super().__init__(model, zoom, material)
        self._resolution = resolution

    def cost(self):
        base_cost = super().cost()
        if self._resolution == "4K":
            return base_cost * 1.5
        return base_cost

    def __str__(self):
        return f"Model: {self._model}, Zoom: {self._zoom}x, Body: {self._material}, Resolution: {self._resolution}, Cost: {self.cost()} $"


camera1 = Camera("Canon", 15, "plastic")
digital_camera = DigitalCamera("Nikon", 20, "metal", 24)
professional_camera = ProfessionalCamera("Sony Alpha", 25, "metal", 36, "Lens Kit")
video_camera = VideoCamera("Panasonic", 30, "plastic", "4K")

print(camera1)
print(digital_camera)
print(professional_camera.fulldescription())
print(video_camera)

print("Is camera expensive?", camera1.expensive())
print("Is digital camera expensive?", digital_camera.expensive())
print("Is professional camera expensive?", professional_camera.expensive())
print("Is video camera expensive?", video_camera.expensive())

print("Total cameras:", Camera.countscameras())
