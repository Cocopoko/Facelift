import os
import logging
from PIL import Image
import pwnagotchi.plugins as plugins
import pwnagotchi.ui.faces as faces
from pwnagotchi.ui.components import Widget
from pwnagotchi.ui import fonts

FACE_DIR = '/root/coco2-faces'
PASTE_XY = (0, 14)


class FaceImage(Widget):
    def __init__(self, value='', position=(0, 14), color=0):
        super().__init__(position, color)
        self.value = value
        self._cache = {}
        self._rev = None

    def _name_for(self, glyph):
        if self._rev is None:
            rev = {}
            for n in dir(faces):
                if n.isupper():
                    try:
                        rev[getattr(faces, n)] = n
                    except Exception:
                        pass
            self._rev = rev
        return self._rev.get(glyph)

    def draw(self, canvas, drawer):
        try:
            name = self._name_for(self.value)
            if name:
                path = os.path.join(FACE_DIR, name + '.png')
                if os.path.exists(path):
                    if path not in self._cache:
                        self._cache[path] = Image.open(path).convert('1')
                    canvas.paste(self._cache[path], PASTE_XY)
                    return
        except Exception as e:
            logging.error('[facelift] draw failed: %s' % e)
        if self.value:
            drawer.text((0, 40), self.value, font=fonts.Huge, fill=self.color)


class Facelift(plugins.Plugin):
    __author__ = 'Kira'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Picture faces for the pwnagotchi web UI'

    def on_loaded(self):
        logging.info('[facelift] loaded, face dir: %s' % FACE_DIR)

    def on_ui_setup(self, ui):
        ui.add_element('face', FaceImage(value=faces.SLEEP))
        logging.info('[facelift] face widget swapped for picture face')
