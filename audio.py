from pygame._sdl2 import *
from pygame import mixer
mixer.init()
print([get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))])
mixer.quit()