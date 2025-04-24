"""
Prehľad verejných funkcií modulu scratch.py:

Trieda Stage:
  - set_background(file_path): Nastaví obrázok pozadia.
  - add_sprite(sprite): Pridá sprite do hry.
  - get_mouse_position() -> (x, y): Vráti pozíciu myši.
  - is_mouse_down() -> bool: Vráti True, ak je stlačené tlačidlo myši.
  - is_key_pressed(key) -> bool: Vráti True, ak je daný kláves stlačený.
  - start(): Spustí hlavnú slučku hry.

Trieda Sprite:
  - move_to(x, y): Presunie sprite na nové súradnice.
  - change_x(dx): Posunie sprite o dx pixelov vodorovne.
  - change_y(dy): Posunie sprite o dy pixelov zvisle.
  - set_rotation(deg): Otočí sprite na daný uhol.
  - show(): Zobrazí sprite.
  - hide(): Skryje sprite.
  - set_size(percent): Zmení veľkosť sprite.
  - set_costume(file_path): Zmení obrázok sprite.
  - on_click(callback): Priradí funkciu, ktorá sa spustí pri kliknutí.
  - is_touching_sprite(other) -> bool: Skontroluje, či sa dotýka iného sprite.
  - bring_to_front(): Presunie sprite pred ostatné.
  - send_to_back(): Presunie sprite za ostatné.

Voľná funkcia:
  - play_sound(file_path): Prehrá zvuk zo súboru.
"""
# Prehľad verejných funkcií (API) modulu scratch.py
#
# Trieda Stage:
#   - set_background(file_path): Nastaví obrázok pozadia.
#   - add_sprite(sprite): Pridá sprite do hry.
#   - get_mouse_position() -> (x, y): Vráti pozíciu myši.
#   - is_mouse_down() -> bool: Vráti True, ak je myš stlačená.
#   - is_key_pressed(key) -> bool: Vráti True, ak je daný kláves stlačený.
#   - start(): Spustí herný cyklus.
#
# Trieda Sprite:
#   - move_to(x, y): Presunie sprite na súradnice (x,y).
#   - change_x(dx): Posunie sprite o dx pixelov doprava.
#   - change_y(dy): Posunie sprite o dy pixelov nahor.
#   - set_rotation(deg): Otočí sprite na daný uhol.
#   - show(): Zobrazí sprite.
#   - hide(): Skryje sprite.
#   - set_size(percent): Zmení veľkosť sprite na percent%.
#   - set_costume(file_path): Zmení obrázok sprite.
#   - on_click(callback): Nastaví funkciu na kliknutie.
#   - is_touching_sprite(other) -> bool: Skontroluje, či sa sprite dotýka iného sprite.
#   - bring_to_front(): Posunie sprite navrch.
#   - send_to_back(): Posunie sprite dozadu.
#
# Voľná funkcia:
#   - play_sound(file_path): Prehrá zvuk zo súboru.

import tkinter as tk
from PIL import Image, ImageTk
import pygame


# Spustíme zvuky
pygame.mixer.init()

# Trieda Stage je miesto, kde prebieha hra
class Stage:
    def __init__(self):
        """
        Vytvorí herné okno a prázdne plátno.
        Príklad:
            stage = Stage()
        -> otvorí sa okno s plátnom na kreslenie.
        """
        self.root = tk.Tk()
        self.root.title("Scratch Stage")
        self.canvas = tk.Canvas(self.root, width=480, height=360)
        self.canvas.pack()

        self.sprites = []          # sem pridáme postavy
        self.background = None     # obrázok pozadia
        self.background_file = None

        # Udalosti myši a kláves
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_down = False
        self.keys_pressed = set()

        # Spojíme klikanie a pohyb s metódami
        self.root.bind("<Motion>", self._on_mouse_move)
        self.root.bind("<ButtonPress>", lambda e: setattr(self, 'mouse_down', True))
        self.root.bind("<ButtonRelease>", lambda e: setattr(self, 'mouse_down', False))
        self.root.bind("<KeyPress>", self._on_key_press)
        self.root.bind("<KeyRelease>", self._on_key_release)

    def _on_mouse_move(self, event):
        """
        Sleduje, kde je myš.
        Nepoužívate to priamo.
        """
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _on_key_press(self, event):
        """
        Spomenie si, že sme stlačili klávesu.
        """
        self.keys_pressed.add(event.keysym)

    def _on_key_release(self, event):
        """
        Spomenie si, že sme pustili klávesu.
        """
        self.keys_pressed.discard(event.keysym)

    def set_background(self, file_path):
        """
        Nastaví obrázok za všetky postavy.
        Príklad:
            stage.set_background('pozadie.jpg')
        -> pozadie.jpg sa ukáže pod postavami.
        """
        self.background_file = file_path
        img = Image.open(file_path).resize((480, 360))
        self.background = ImageTk.PhotoImage(img)
        bg_id = self.canvas.create_image(0, 0, anchor="nw", image=self.background)
        self.canvas.tag_lower(bg_id)

    def add_sprite(self, sprite):
        """
        Pridá postavu do hry.
        Príklad:
            stage.add_sprite(sprite1)
        -> sprite1 sa zobrazí a bude reagovať.
        """
        self.sprites.append(sprite)

    def get_mouse_position(self):
        """
        Povie, kde je myš.
        Príklad:
            x, y = stage.get_mouse_position()
        """
        return self.mouse_x, self.mouse_y

    def is_mouse_down(self):
        """
        Povie, či držíme myš.
        Príklad:
            if stage.is_mouse_down():
                print('Klik!')
        """
        return self.mouse_down

    def is_key_pressed(self, key):
        """
        Povie, či je klávesa stlačená.
        key je napr. 'w' alebo 'space'.
        Príklad:
            if stage.is_key_pressed('w'):
                sprite.move_to(10,10)
        """
        return key in self.keys_pressed

    def start(self):
        """
        Spustí hru a čaká na stlačenia.
        Príklad:
            stage.start()
        -> okno ostane otvorené.
        """
        self.root.mainloop()

# Trieda Sprite je postava v hre
class Sprite:
    def __init__(self, stage, image_file, x=0, y=0, size=100, rotation=0):
        """
        Vytvorí postavu s obrázkom.
        Príklad:
            sprite = Sprite(stage, 'char.png', x=50, y=50)
        -> char.png sa ukáže na súradniciach (50,50).
        """
        self.stage = stage
        self.x = x
        self.y = y
        self.size = size
        self.rotation = rotation
        self.visible = True
        self.callback = None
        self.image_file = image_file

        self._load_image()
        self.id = self.stage.canvas.create_image(self.x, self.y, image=self.tk_image)
        self.stage.canvas.tag_bind(self.id, "<Button-1>", self._on_click)

    def _load_image(self):
        """
        Načíta obrázok, zmení veľkosť a otočí ho.
        Nepoužívate to priamo.
        """
        img = Image.open(self.image_file).convert("RGBA")
        img = img.resize((int(img.width * self.size / 100), int(img.height * self.size / 100)))
        img = img.rotate(-self.rotation, expand=True)
        self._raw_image = img
        self.tk_image = ImageTk.PhotoImage(img)

    def _get_mask_and_position(self):
        """
        Pripraví čiernobielu masku pre kolízie.
        Príklad:
            mask, x0, y0 = sprite._get_mask_and_position()
        """
        mask = self._raw_image.split()[-1].point(lambda a: 255 if a > 0 else 0)
        return mask, self.x - self._raw_image.width // 2, self.y - self._raw_image.height // 2

    def move_to(self, x, y):
        """
        Posunie postavu na nové miesto.
        Príklad:
            sprite.move_to(100,200)
        -> postava sa presunie na (100,200).
        """
        self.x = x
        self.y = y
        self.stage.canvas.coords(self.id, self.x, self.y)

    def change_x(self, dx):
        """
        Posunie postavu vodorovne.
        Príklad:
            sprite.change_x(10)
        -> posunie sa o 10 pixelov doprava.
        """
        self.move_to(self.x + dx, self.y)

    def change_y(self, dy):
        """
        Posunie postavu zvisle.
        Príklad:
            sprite.change_y(-5)
        -> posunie sa o 5 pixelov nahor.
        """
        self.move_to(self.x, self.y + dy)

    def set_rotation(self, degrees):
        """
        Otočí postavu.
        Príklad:
            sprite.set_rotation(90)
        -> postava sa natočí o 90°.
        """
        self.rotation = degrees
        self._reload()

    def show(self):
        """
        Ukáže skrytú postavu.
        Príklad:
            sprite.show()
        """
        self.visible = True
        self.stage.canvas.itemconfigure(self.id, state='normal')

    def hide(self):
        """
        Skryje postavu.
        Príklad:
            sprite.hide()
        """
        self.visible = False
        self.stage.canvas.itemconfigure(self.id, state='hidden')

    def set_size(self, percent):
        """
        Zmení veľkosť postavy.
        Príklad:
            sprite.set_size(50)
        -> postava bude polovičná.
        """
        self.size = percent
        self._reload()

    def set_costume(self, file_path):
        """
        Zmení obrázok postavy.
        Príklad:
            sprite.set_costume('new.png')
        """
        self.image_file = file_path
        self._reload()

    def _reload(self):
        """
        Znovu upraví obrázok, keď sa zmení veľkosť alebo rotácia.
        """
        self._load_image()
        self.stage.canvas.itemconfig(self.id, image=self.tk_image)
        self.stage.canvas.coords(self.id, self.x, self.y)

    def on_click(self, callback):
        """
        Keď kliknete na postavu, spustí sa táto funkcia.
        Príklad:
            sprite.on_click(lambda: print('Ahoj'))
        """
        self.callback = callback

    def _on_click(self, event):
        if self.callback:
            self.callback()

    def is_touching_sprite(self, other):
        """
        Skontroluje, či sa dve postavy dotýkajú.
        Príklad:
            if sprite1.is_touching_sprite(sprite2):
                print('Dotyk!')
        """
        if not self.visible or not other.visible:
            return False
        mask1, x1, y1 = self._get_mask_and_position()
        mask2, x2, y2 = other._get_mask_and_position()

        x_overlap_start = max(x1, x2)
        y_overlap_start = max(y1, y2)
        x_overlap_end = min(x1 + mask1.width, x2 + mask2.width)
        y_overlap_end = min(y1 + mask1.height, y2 + mask2.height)

        if x_overlap_start >= x_overlap_end or y_overlap_start >= y_overlap_end:
            return False

        mask1_crop = mask1.crop((x_overlap_start - x1, y_overlap_start - y1,
                                 x_overlap_end - x1, y_overlap_end - y1))
        mask2_crop = mask2.crop((x_overlap_start - x2, y_overlap_start - y2,
                                 x_overlap_end - x2, y_overlap_end - y2))

        for px1, px2 in zip(mask1_crop.getdata(), mask2_crop.getdata()):
            if px1 > 0 and px2 > 0:
                return True
        return False

    def bring_to_front(self):
        """
        Položí postavu navrch.
        Príklad:
            sprite.bring_to_front()
        """
        self.stage.canvas.tag_raise(self.id)

    def send_to_back(self):
        """
        Položí postavu dozadu.
        Príklad:
            sprite.send_to_back()
        """
        self.stage.canvas.tag_lower(self.id)

# Prehrá zvuk

def play_sound(file_path):
    """
    Prehrá zvuk zo súboru.
    Príklad:
        play_sound('meow.wav')
    """
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
