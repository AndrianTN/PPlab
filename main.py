from camera import Camera
from digitalcamera import DigitalCamera
from professionalcamera import ProfessionalCamera
from videocamera import VideoCamera

camera1 = Camera("Canon", 15, "plastic")
digitalcamera1 = DigitalCamera("Nikon", 20, "metal", 24)
professionalcamera = ProfessionalCamera("Sony Alpha", 25, "metal", 36, "Lens Kit")
videocamera = VideoCamera("Panasonic", 30, "plastic", "4K")

print(camera1)
print(digitalcamera1)
print(professionalcamera.fulldescription())
print(videocamera)

print("Is camera expensive?", camera1.expensive())
print("Is digital camera expensive?", digitalcamera1.expensive())
print("Is professional camera expensive?", professionalcamera.expensive())
print("Is video camera expensive?", videocamera.expensive())

print("Total cameras:", Camera.countscameras())
