def on_a_pressed():
    global bullet
    if direction == 0:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 4 4 . . . . . . .
                . . . . . . 4 5 5 4 . . . . . .
                . . . . . . 2 5 5 2 . . . . . .
                . . . . . . . 2 2 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            mySprite,
            0,
            -50)
    elif direction == 90:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 4 4 . . . . . . .
                . . . . . . 4 5 5 4 . . . . . .
                . . . . . . 2 5 5 2 . . . . . .
                . . . . . . . 2 2 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            mySprite,
            50,
            0)
    elif direction == 180:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 4 4 . . . . . . .
                . . . . . . 4 5 5 4 . . . . . .
                . . . . . . 2 5 5 2 . . . . . .
                . . . . . . . 2 2 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            mySprite,
            0,
            50)
    elif direction == 270:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . 4 4 . . . . . . .
                . . . . . . 4 5 5 4 . . . . . .
                . . . . . . 2 5 5 2 . . . . . .
                . . . . . . . 2 2 . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            mySprite,
            -50,
            0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def spawnEnemy():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . f f f . . . . . . . . f f f
            . f f c c . . . . . . f c b b c
            f f c c . . . . . . f c b b c .
            f c f c . . . . . . f b c c c .
            f f f c c . c c . f c b b c c .
            f f c 3 c c 3 c c f b c b b c .
            f f b 3 b c 3 b c f b c c b c .
            . c b b b b b b c b b c c c . .
            . c 1 b b b 1 b b c c c c . . .
            c b b b b b b b b b c c . . . .
            c b c b b b c b b b b f . . . .
            f b 1 f f f 1 b b b b f c . . .
            f b b b b b b b b b b f c c . .
            . f b b b b b b b b c f . . . .
            . . f b b b b b b c f . . . . .
            . . . f f f f f f f . . . . . .
            """),
        SpriteKind.enemy)
    mySprite2.set_position(0, 0)
    animation.run_image_animation(mySprite2,
        [img("""
                . . f f f . . . . . . . . f f f
                . f f c c . . . . . . f c b b c
                f f c c . . . . . . f c b b c .
                f c f c . . . . . . f b c c c .
                f f f c c . c c . f c b b c c .
                f f c 3 c c 3 c c f b c b b c .
                f f b 3 b c 3 b c f b c c b c .
                . c b b b b b b c b b c c c . .
                . c 1 b b b 1 b b c c c c . . .
                c b b b b b b b b b c c . . . .
                c b c b b b c b b b b f . . . .
                f b 1 f f f 1 b b b b f c . . .
                f b b b b b b b b b b f c c . .
                . f b b b b b b b b c f . . . .
                . . f b b b b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                """),
            img("""
                . . f f f . . . . . . . . . . .
                f f f c c . . . . . . . . f f f
                f f c c . . c c . . . f c b b c
                f f c 3 c c 3 c c f f b b b c .
                f f b 3 b c 3 b c f b b c c c .
                . c b b b b b b c f b c b c c .
                . c b b b b b b c b b c b b c .
                c b 1 b b b 1 b b b c c c b c .
                c b b b b b b b b c c c c c . .
                f b c b b b c b b b b f c . . .
                f b 1 f f f 1 b b b b f c c . .
                . f b b b b b b b b c f . . . .
                . . f b b b b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . c c . . c c . . . . . . . .
                . . c 3 c c 3 c c c . . . . . .
                . c b 3 b c 3 b c c c . . . . .
                . c b b b b b b b b f f . . . .
                c c b b b b b b b b f f . . . .
                c b 1 b b b 1 b b c f f f . . .
                c b b b b b b b b f f f f . . .
                f b c b b b c b c c b b b . . .
                f b 1 f f f 1 b f c c c c . . .
                . f b b b b b b f b b c c . . .
                c c f b b b b b c c b b c . . .
                c c c f f f f f f c c b b c . .
                . c c c . . . . . . c c c c c .
                . . c c c . . . . . . . c c c c
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . f f f . . . . . . . . . . .
                f f f c c . . . . . . . . f f f
                f f c c . . c c . . . f c b b c
                f f c 3 c c 3 c c f f b b b c .
                f f b 3 b c 3 b c f b b c c c .
                . c b b b b b b c f b c b c c .
                . c b b b b b b c b b c b b c .
                c b 1 b b b 1 b b b c c c b c .
                c b b b b b b b b c c c c c . .
                f b c b b b c b b b b f c . . .
                f b 1 f f f 1 b b b b f c c . .
                . f b b b b b b b b c f . . . .
                . . f b b b b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . f f f . . . . . . . . f f f .
                f f c . . . . . . . f c b b c .
                f c c . . . . . . f c b b c . .
                c f . . . . . . . f b c c c . .
                c f f . . . . . f f b b c c . .
                f f f c c . c c f b c b b c . .
                f f f c c c c c f b c c b c . .
                . f c 3 c c 3 b c b c c c . . .
                . c b 3 b c 3 b b c c c c . . .
                c c b b b b b b b b c c . . . .
                c b 1 b b b 1 b b b b f c . . .
                f b b b b b b b b b b f c c . .
                f b c b b b c b b b b f . . . .
                . f 1 f f f 1 b b b c f . . . .
                . . f b b b b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                """)],
        200,
        True)
    mySprite2.follow(mySprite, 60)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.fire, 500)
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    pause(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
bullet: Sprite = None
direction = 0
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . f f f f f f . . . . .
        . . . f f e e e e f 2 f . . . .
        . . f f e e e e f 2 2 2 f . . .
        . . f e e e f f e e e e f . . .
        . . f f f f e e 2 2 2 2 e f . .
        . . f e 2 2 2 f f f f e 2 f . .
        . f f f f f f f e e e f f f . .
        . f f e 4 4 e b f 4 4 e e f . .
        . f e e 4 d 4 1 f d d e f . . .
        . . f e e e e e d d d f . . . .
        . . . . f 4 d d e 4 e f . . . .
        . . . . f e d d e 2 2 f . . . .
        . . . f f f e e f 5 5 f f . . .
        . . . f f f f f f f f f f . . .
        . . . . f f . . . f f f . . . .
        """),
    SpriteKind.player)
mySprite.set_position(75, 54)
controller.move_sprite(mySprite)
info.set_life(3)
scene.camera_follow_sprite(mySprite)
gamePhase = 0
direction = 90

def on_update_interval():
    global direction
    if controller.right.is_pressed():
        direction = 90
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f f f . . . .
                    . . . . f f e e e e f 2 f . . .
                    . . . f f e e e e f 2 2 2 f . .
                    . . . f e e e f f e e e e f . .
                    . . . f f f f e e 2 2 2 2 e f .
                    . . . f e 2 2 2 f f f f e 2 f .
                    . . f f f f f f f e e e f f f .
                    . . f f e 4 4 e b f 4 4 e e f .
                    . . f e e 4 d 4 1 f d d e f . .
                    . . . f e e e 4 d d d d f . . .
                    . . . . f f e e 4 4 4 e f . . .
                    . . . . . 4 d d e 2 2 2 f . . .
                    . . . . . e d d e 2 2 2 f . . .
                    . . . . . f e e f 4 5 5 f . . .
                    . . . . . . f f f f f f . . . .
                    . . . . . . . f f f . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f f f . . . .
                    . . . . f f e e e e f 2 f . . .
                    . . . f f e e e e f 2 2 2 f . .
                    . . . f e e e f f e e e e f . .
                    . . . f f f f e e 2 2 2 2 e f .
                    . . . f e 2 2 2 f f f f e 2 f .
                    . . f f f f f f f e e e f f f .
                    . . f f e 4 4 e b f 4 4 e e f .
                    . . f e e 4 d 4 1 f d d e f . .
                    . . . f e e e e e d d d f . . .
                    . . . . . f 4 d d e 4 e f . . .
                    . . . . . f e d d e 2 2 f . . .
                    . . . . f f f e e f 5 5 f f . .
                    . . . . f f f f f f f f f f . .
                    . . . . . f f . . . f f f . . .
                    """),
                img("""
                    . . . . . . f f f f f f . . . .
                    . . . . f f e e e e f 2 f . . .
                    . . . f f e e e e f 2 2 2 f . .
                    . . . f e e e f f e e e e f . .
                    . . . f f f f e e 2 2 2 2 e f .
                    . . . f e 2 2 2 f f f f e 2 f .
                    . . f f f f f f f e e e f f f .
                    . . f f e 4 4 e b f 4 4 e e f .
                    . . f e e 4 d 4 1 f d d e f . .
                    . . . f e e e 4 d d d d f . . .
                    . . . . f f e e 4 4 4 e f . . .
                    . . . . . 4 d d e 2 2 2 f . . .
                    . . . . . e d d e 2 2 2 f . . .
                    . . . . . f e e f 4 5 5 f . . .
                    . . . . . . f f f f f f . . . .
                    . . . . . . . f f f . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f f f . . . .
                    . . . . f f e e e e f 2 f . . .
                    . . . f f e e e e f 2 2 2 f . .
                    . . . f e e e f f e e e e f . .
                    . . . f f f f e e 2 2 2 2 e f .
                    . . . f e 2 2 2 f f f f e 2 f .
                    . . f f f f f f f e e e f f f .
                    . . f f e 4 4 e b f 4 4 e e f .
                    . . f e e 4 d 4 1 f d d e f . .
                    . . . f e e e 4 d d d d f . . .
                    . . . . 4 d d e 4 4 4 e f . . .
                    . . . . e d d e 2 2 2 2 f . . .
                    . . . . f e e f 4 4 5 5 f f . .
                    . . . . f f f f f f f f f f . .
                    . . . . . f f . . . f f f . . .
                    """)],
            100,
            True)
    elif controller.left.is_pressed():
        direction = 270
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . f f f f f f . . . . . .
                    . . . f 2 f e e e e f f . . . .
                    . . f 2 2 2 f e e e e f f . . .
                    . . f e e e e f f e e e f . . .
                    . f e 2 2 2 2 e e f f f f . . .
                    . f 2 e f f f f 2 2 2 e f . . .
                    . f f f e e e f f f f f f f . .
                    . f e e 4 4 f b e 4 4 e f f . .
                    . . f e d d f 1 4 d 4 e e f . .
                    . . . f d d d d 4 e e e f . . .
                    . . . f e 4 4 4 e e f f . . . .
                    . . . f 2 2 2 e d d 4 . . . . .
                    . . . f 2 2 2 e d d e . . . . .
                    . . . f 5 5 4 f e e f . . . . .
                    . . . . f f f f f f . . . . . .
                    . . . . . . f f f . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . f f f f f f . . . . . .
                    . . . f 2 f e e e e f f . . . .
                    . . f 2 2 2 f e e e e f f . . .
                    . . f e e e e f f e e e f . . .
                    . f e 2 2 2 2 e e f f f f . . .
                    . f 2 e f f f f 2 2 2 e f . . .
                    . f f f e e e f f f f f f f . .
                    . f e e 4 4 f b e 4 4 e f f . .
                    . . f e d d f 1 4 d 4 e e f . .
                    . . . f d d d e e e e e f . . .
                    . . . f e 4 e d d 4 f . . . . .
                    . . . f 2 2 e d d e f . . . . .
                    . . f f 5 5 f e e f f f . . . .
                    . . f f f f f f f f f f . . . .
                    . . . f f f . . . f f . . . . .
                    """),
                img("""
                    . . . . f f f f f f . . . . . .
                    . . . f 2 f e e e e f f . . . .
                    . . f 2 2 2 f e e e e f f . . .
                    . . f e e e e f f e e e f . . .
                    . f e 2 2 2 2 e e f f f f . . .
                    . f 2 e f f f f 2 2 2 e f . . .
                    . f f f e e e f f f f f f f . .
                    . f e e 4 4 f b e 4 4 e f f . .
                    . . f e d d f 1 4 d 4 e e f . .
                    . . . f d d d d 4 e e e f . . .
                    . . . f e 4 4 4 e e f f . . . .
                    . . . f 2 2 2 e d d 4 . . . . .
                    . . . f 2 2 2 e d d e . . . . .
                    . . . f 5 5 4 f e e f . . . . .
                    . . . . f f f f f f . . . . . .
                    . . . . . . f f f . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . f f f f f f . . . . . .
                    . . . f 2 f e e e e f f . . . .
                    . . f 2 2 2 f e e e e f f . . .
                    . . f e e e e f f e e e f . . .
                    . f e 2 2 2 2 e e f f f f . . .
                    . f 2 e f f f f 2 2 2 e f . . .
                    . f f f e e e f f f f f f f . .
                    . f e e 4 4 f b e 4 4 e f f . .
                    . . f e d d f 1 4 d 4 e e f . .
                    . . . f d d d d 4 e e e f . . .
                    . . . f e 4 4 4 e d d 4 . . . .
                    . . . f 2 2 2 2 e d d e . . . .
                    . . f f 5 5 4 4 f e e f . . . .
                    . . f f f f f f f f f f . . . .
                    . . . f f f . . . f f . . . . .
                    """)],
            100,
            True)
    elif controller.down.is_pressed():
        direction = 180
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . . f e 2 f f f f f f 2 e f . .
                    . . f f f f e e e e f f f f . .
                    . f f e f b f 4 4 f b f e f f .
                    . f e e 4 1 f d d f 1 4 e e f .
                    . . f e e d d d d d d e e f . .
                    . . . f e e 4 4 4 4 e e f . . .
                    . . e 4 f 2 2 2 2 2 2 f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . f f e 2 f f f f f f 2 e f f .
                    . f f f f f e e e e f f f f f .
                    . . f e f b f 4 4 f b f e f . .
                    . . f e 4 1 f d d f 1 4 e f . .
                    . . . f e 4 d d d d 4 e f e . .
                    . . f e f 2 2 2 2 e d d 4 e . .
                    . . e 4 f 2 2 2 2 e d d e . . .
                    . . . . f 4 4 5 5 f e e . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . f f f . . . . . . . . .
                    """),
                img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . . f e 2 f f f f f f 2 e f . .
                    . . f f f f e e e e f f f f . .
                    . f f e f b f 4 4 f b f e f f .
                    . f e e 4 1 f d d f 1 4 e e f .
                    . . f e e d d d d d d e e f . .
                    . . . f e e 4 4 4 4 e e f . . .
                    . . e 4 f 2 2 2 2 2 2 f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f e e 2 2 2 2 2 2 e f f . .
                    . f f e 2 f f f f f f 2 e f f .
                    . f f f f f e e e e f f f f f .
                    . . f e f b f 4 4 f b f e f . .
                    . . f e 4 1 f d d f 1 4 e f . .
                    . . e f e 4 d d d d 4 e f . . .
                    . . e 4 d d e 2 2 2 2 f e f . .
                    . . . e d d e 2 2 2 2 f 4 e . .
                    . . . . e e f 5 5 4 4 f . . . .
                    . . . . . f f f f f f f . . . .
                    . . . . . . . . . f f f . . . .
                    """)],
            100,
            True)
    elif controller.up.is_pressed():
        direction = 0
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f e e e e f f . . . .
                    . . . f e e e f f e e e f . . .
                    . . f f f f f 2 2 f f f f f . .
                    . . f f e 2 e 2 2 e 2 e f f . .
                    . . f e 2 f 2 f f 2 f 2 e f . .
                    . . f f f 2 2 e e 2 2 f f f . .
                    . f f e f 2 f e e f 2 f e f f .
                    . f e e f f e e e e f e e e f .
                    . . f e e e e e e e e e e f . .
                    . . . f e e e e e e e e f . . .
                    . . e 4 f f f f f f f f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f e e e e f f . . . .
                    . . . f e e e f f e e e f . . .
                    . . . f f f f 2 2 f f f f . . .
                    . . f f e 2 e 2 2 e 2 e f f . .
                    . . f e 2 f 2 f f f 2 f e f . .
                    . . f f f 2 f e e 2 2 f f f . .
                    . . f e 2 f f e e 2 f e e f . .
                    . f f e f f e e e f e e e f f .
                    . f f e e e e e e e e e e f f .
                    . . . f e e e e e e e e f . . .
                    . . . e f f f f f f f f 4 e . .
                    . . . 4 f 2 2 2 2 2 e d d 4 . .
                    . . . e f f f f f f e e 4 . . .
                    . . . . f f f . . . . . . . . .
                    """),
                img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f e e e e f f . . . .
                    . . . f e e e f f e e e f . . .
                    . . f f f f f 2 2 f f f f f . .
                    . . f f e 2 e 2 2 e 2 e f f . .
                    . . f e 2 f 2 f f 2 f 2 e f . .
                    . . f f f 2 2 e e 2 2 f f f . .
                    . f f e f 2 f e e f 2 f e f f .
                    . f e e f f e e e e f e e e f .
                    . . f e e e e e e e e e e f . .
                    . . . f e e e e e e e e f . . .
                    . . e 4 f f f f f f f f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f e e e e f f . . . .
                    . . . f e e e f f e e e f . . .
                    . . . f f f f 2 2 f f f f . . .
                    . . f f e 2 e 2 2 e 2 e f f . .
                    . . f e f 2 f f f 2 f 2 e f . .
                    . . f f f 2 2 e e f 2 f f f . .
                    . . f e e f 2 e e f f 2 e f . .
                    . f f e e e f e e e f f e f f .
                    . f f e e e e e e e e e e f f .
                    . . . f e e e e e e e e f . . .
                    . . e 4 f f f f f f f f e . . .
                    . . 4 d d e 2 2 2 2 2 f 4 . . .
                    . . . 4 e e f f f f f f e . . .
                    . . . . . . . . . f f f . . . .
                    """)],
            100,
            True)
game.on_update_interval(400, on_update_interval)
