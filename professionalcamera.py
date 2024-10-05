from constants import ZOOMMIN, PROFESSIONALCAMERACOST
from digitalcamera import DigitalCamera
from accesyar import Accessory

class ProfessionalCamera(DigitalCamera, Accessory):
    def __init__(self, model="Unknown", zoom=ZOOMMIN, material="plastic", megapixels=24, accessory_type="Tripod"):
        DigitalCamera.__init__(self, model, zoom, material, megapixels)
        Accessory.__init__(self, accessory_type)

    def fulldescription(self):
        return f"{self.__str__()} and comes with {self.description()}"

    def cost(self):
        return super().cost() + PROFESSIONALCAMERACOST