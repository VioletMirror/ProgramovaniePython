from scratch import Stage, Sprite, play_sound
import math

# Vytvoríme hlavné herné javisko
stage = Stage()
stage.set_background("background.jpg")  # Pridáme pozadie

# Pridáme dve postavy (sprite1 a sprite2)
sprite1 = Sprite(stage, "char1.png", x=100, y=100)
sprite2 = Sprite(stage, "char2.png", x=300, y=150)

# Keď kliknem na sprite1, vypíše sa správa
sprite1.on_click(lambda: print("Klikol si na sprite1!"))

# Zoznam projektilov, ktoré vypálime
projectiles = []


def game_loop():
    # --- Otáčanie smerom k myši ---
    mx, my = stage.get_mouse_position()  # kde je myš?
    dx = mx - sprite1.x  # rozdiel vodorovne
    dy = my - sprite1.y  # rozdiel zvisle
    angle = math.atan2(dy, dx)  # uhol v radiánoch
    sprite1.set_rotation(math.degrees(angle))  # otočíme na myš

    # --- Pohyb podľa kláves (WASD) ---
    speed = 5  # rýchlosť pohybu
    if stage.is_key_pressed("w"):  # vpred k myši
        sprite1.change_x(math.cos(angle) * speed)
        sprite1.change_y(math.sin(angle) * speed)
    if stage.is_key_pressed("s"):  # dozadu od myši
        sprite1.change_x(-math.cos(angle) * speed)
        sprite1.change_y(-math.sin(angle) * speed)
    if stage.is_key_pressed("a"):  # doľava (perpendicularne)
        sprite1.change_x(-5)  # jednoduchšie strafe
    if stage.is_key_pressed("d"):  # doprava
        sprite1.change_x(5)

    # --- Zmena veľkosti (Space a Shift) ---
    if stage.is_key_pressed("space"):      sprite1.set_size(max(10, sprite1.size - 1))  # zmenší sa
    if stage.is_key_pressed("Shift_L"):    sprite1.set_size(min(300, sprite1.size + 1))  # zväčší sa

    # --- Poradie vrstiev (1 a 2) ---
    if stage.is_key_pressed("1"): sprite1.bring_to_front()  # sprite1 navrch
    if stage.is_key_pressed("2"): sprite2.bring_to_front()  # sprite2 navrch

    # --- Vypálenie projektilu (klik myšou) ---
    if stage.is_mouse_down():
        # vytvoríme malý projektil na pozícii sprite1
        proj = Sprite(stage, "char2.png", x=sprite1.x, y=sprite1.y, size=10)
        projectiles.append((proj, mx, my))  # pamätáme cieľ (myš)
        stage.mouse_down = False  # aby sa nestrieľalo nonstop

    # --- Pohyb a kolízia projektilov ---
    for proj, tx, ty in projectiles[:]:
        dx = tx - proj.x
        dy = ty - proj.y
        dist = math.hypot(dx, dy)  # vzdialenosť ku cieľu

        # Ak dorazil blízko cieľa, zmizne projektil
        if dist < 5:
            projectiles.remove((proj, tx, ty))
            stage.canvas.delete(proj.id)
            continue

        # Ak sa projektil stretne so sprite2, sprite2 zmizne a hrá sa zvuk
        if proj.is_touching_sprite(sprite2) and sprite2.visible:
            sprite2.hide()  # schováme sprite2
            play_sound("sound.wav")  # zahráme zvuk
            projectiles.remove((proj, tx, ty))
            stage.canvas.delete(proj.id)
            continue

        # Inak projektil pokračuje k cieľu
        proj.change_x(dx / dist * speed)
        proj.change_y(dy / dist * speed)

    # Zavoláme sa znova o 30 ms
    stage.root.after(30, game_loop)


# Spustíme hlavnú slučku
game_loop()
stage.start()
