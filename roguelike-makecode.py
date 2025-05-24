def on_overlap_tile(sprite, location):
    global myLocation2
    if controller.B.is_pressed():
        myLocation2 += -1
        # Set up the initial room
        tiles.set_current_tilemap(tilemap("""
            level
            """))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
        checkSurroundingRooms(myLocation2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door_left
        """),
    on_overlap_tile)

# A function to destroy the enemy and the projectile when they collide

def on_on_overlap(sprite3, otherSprite):
    sprites.destroy(otherSprite, effects.fire, 500)
    sprites.destroy(sprite3)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

# A function for shooting a projectile

def on_a_pressed():
    global bullet
    if direction2 == 0:
        bullet = sprites.create_projectile_from_sprite(assets.image("""
            bullet
            """), mySprite, 0, -50)
    elif direction2 == 90:
        bullet = sprites.create_projectile_from_sprite(assets.image("""
            bullet
            """), mySprite, 50, 0)
    elif direction2 == 180:
        pass
    elif direction2 == 270:
        bullet = sprites.create_projectile_from_sprite(assets.image("""
            bullet
            """), mySprite, -50, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    global myLocation2
    if controller.B.is_pressed():
        myLocation2 += -10
        # Set up the initial room
        tiles.set_current_tilemap(tilemap("""
            level
            """))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
        checkSurroundingRooms(myLocation2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door_up
        """),
    on_overlap_tile2)

# Modified initialization - replace the existing map generation
def initializeDungeon():
    global myLocation2
    # Generate the dungeon layout
    generateDungeon()
    # Set starting location
    myLocation2 = 44
    # Set up the initial room
    tiles.set_current_tilemap(tilemap("""
        level
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
    checkSurroundingRooms(myLocation2)

def on_overlap_tile3(sprite4, location3):
    global myLocation2
    if controller.B.is_pressed():
        myLocation2 += 1
        # Set up the initial room
        tiles.set_current_tilemap(tilemap("""
            level
            """))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
        checkSurroundingRooms(myLocation2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door_right
        """),
    on_overlap_tile3)

# A function to lose a life when player gets hit by an enemy

def on_on_overlap2(sprite22, otherSprite2):
    info.change_life_by(-1)
    pause(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

# A function for losing when life at zero

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_overlap_tile4(sprite5, location4):
    global myLocation2
    if controller.B.is_pressed():
        myLocation2 += 10
        # Set up the initial room
        tiles.set_current_tilemap(tilemap("""
            level
            """))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
        checkSurroundingRooms(myLocation2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door_down
        """),
    on_overlap_tile4)

def checkSurroundingRooms(myLocation: number):
    if newmap[myLocation + 1] == 1:
        tiles.set_tile_at(tiles.get_tile_location(14, 8),
            assets.tile("""
                door_right
                """))
        tiles.set_wall_at(tiles.get_tile_location(14, 8), False)
    if newmap[myLocation - 1] == 1:
        tiles.set_tile_at(tiles.get_tile_location(0, 8),
            assets.tile("""
                door_left
                """))
        tiles.set_wall_at(tiles.get_tile_location(0, 8), False)
    if newmap[myLocation - 10] == 1:
        tiles.set_tile_at(tiles.get_tile_location(8, 0),
            assets.tile("""
                door_up
                """))
        tiles.set_wall_at(tiles.get_tile_location(8, 0), False)
    if newmap[myLocation + 10] == 1:
        tiles.set_tile_at(tiles.get_tile_location(8, 14),
            assets.tile("""
                door_down
                """))
        tiles.set_wall_at(tiles.get_tile_location(8, 14), False)
# A function to spawn in an enemy
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
    mySprite2.set_position(randint(5, 145), randint(5, 110))
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

def on_overlap_tile5(sprite6, location5):
    if controller.B.is_pressed():
        initializeDungeon()
        spawnEnemy()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_north,
    on_overlap_tile5)

# Clear the existing map
def generateDungeon():
    global minRooms, maxRooms, branchChance, maxBranches, startPos, directions, walkers, roomsCreated, isolatedRooms
    for index in range(100):
        newmap.append(0)
    # Configuration
    minRooms = 7
    # Minimum number of rooms to generate
    maxRooms = 15
    # Maximum number of rooms to generate
    branchChance = 30
    # Percentage chance to create a branch (0-100)
    maxBranches = 3
    # Maximum number of active branches at once
    # Starting position (center of 10x10 grid)
    startPos = 44
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    # Position 4,4 in the grid (row 4, col 4)
    newmap[startPos] = 1
    # Directions: up, right, down, left
    directions = [-10, 1, 10, -1]
    # Grid movement values
    # Initialize walkers list with starting position
    walkers = [startPos]
    roomsCreated = 1
    # Keep generating until we have enough rooms
    while roomsCreated < minRooms or roomsCreated < maxRooms and len(walkers) > 0:
        newWalkers = []
        # Process each active walker
        for currentWalker in walkers:
            # Get current position coordinates
            currentRow = Math.floor(currentWalker / 10)
            currentCol = currentWalker % 10
            # Get valid directions (don't go out of bounds)
            validDirections = []
            # Check up
            if currentRow > 0:
                validDirections.append(-10)
            # Check right
            if currentCol < 9:
                validDirections.append(1)
            # Check down
            if currentRow < 9:
                validDirections.append(10)
            # Check left
            if currentCol > 0:
                validDirections.append(-1)
            # If no valid directions, remove this walker
            if len(validDirections) == 0:
                continue
            # Choose a random valid direction
            direction = validDirections[randint(0, len(validDirections) - 1)]
            newPos = currentWalker + direction
            # Create room at new position
            if newmap[newPos] == 0:
                newmap[newPos] = 1
                roomsCreated += 1
            # Continue this walker
            newWalkers.append(newPos)
            # Chance to create a branch
            if len(newWalkers) < maxBranches and randint(1, 100) <= branchChance:
                # Try to create a branch in a different direction
                branchDirections = []
                for dir2 in validDirections:
                    if dir2 != direction:
                        # Don't branch in the same direction
                        branchPos = currentWalker + dir2
                        # Only branch to empty spaces or existing rooms
                        if branchPos >= 0 and branchPos < 100:
                            branchDirections.append(dir2)
                if len(branchDirections) > 0:
                    branchDir = branchDirections[randint(0, len(branchDirections) - 1)]
                    branchPos = currentWalker + branchDir
                    # Create room at branch position
                    if newmap[branchPos] == 0:
                        newmap[branchPos] = 1
                        roomsCreated += 1
                    # Add branch walker
                    newWalkers.append(branchPos)
        # Remove some walkers randomly to prevent overcrowding
        if len(newWalkers) > maxBranches:
            # Keep only a random selection of walkers
            shuffledWalkers = []
            for walker in newWalkers:
                shuffledWalkers.append(walker)
            i = 0
            while i < len(shuffledWalkers):
                j = randint(0, len(shuffledWalkers) - 1)
                temp = shuffledWalkers[i]
                shuffledWalkers[i] = shuffledWalkers[j]
                shuffledWalkers[j] = temp
                i += 1
            # Keep only the first maxBranches walkers
            walkers = []
            i = 0
            while i < min(maxBranches, len(shuffledWalkers)):
                walkers.append(shuffledWalkers[i])
                i += 1
        else:
            walkers = newWalkers
        # Sometimes remove a random walker to create more branching
        if len(walkers) > 1 and randint(1, 100) <= 20:
            removeIndex = randint(0, len(walkers) - 1)
            walkers.splice(removeIndex, 1)
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    # Ensure we always have the starting room
    newmap[44] = 1
    # Optional: Add some isolated rooms for variety
    isolatedRooms = randint(1, 3)
    i = 0
    while i < isolatedRooms:
        pos = randint(0, 99)
        if newmap[pos] == 0:
            # Check if it's not adjacent to existing rooms (truly isolated)
            row = Math.floor(pos / 10)
            col = pos % 10
            isolated = True
            # Check all adjacent positions
            adjacentPositions = []
            if row > 0:
                adjacentPositions.append(pos - 10)
            # up
            if col < 9:
                adjacentPositions.append(pos + 1)
            # right
            if row < 9:
                adjacentPositions.append(pos + 10)
            # down
            if col > 0:
                adjacentPositions.append(pos - 1)
            # left
            for adjPos in adjacentPositions:
                if newmap[adjPos] == 1:
                    isolated = False
                    break
            if isolated:
                newmap[pos] = 1
        i += 1
isolatedRooms = 0
roomsCreated = 0
directions: List[number] = []
startPos = 0
maxBranches = 0
branchChance = 0
maxRooms = 0
minRooms = 0
mySprite2: Sprite = None
bullet: Sprite = None
myLocation2 = 0
direction2 = 0
mySprite: Sprite = None
newmap: List[number] = []
gamePhase = 0
walkers: List[number] = []
newmap = []
tiles.set_current_tilemap(tilemap("""
    start
    """))
mySprite = sprites.create(assets.image("""
    player
    """), SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(8, 8))
controller.move_sprite(mySprite)
info.set_life(3)
scene.camera_follow_sprite(mySprite)
direction2 = 90
# A function to animate player movement

def on_update_interval():
    global direction2
    if controller.right.is_pressed():
        direction2 = 90
        animation.run_image_animation(mySprite,
            assets.animation("""
                player_right
                """),
            100,
            False)
    elif controller.left.is_pressed():
        direction2 = 270
        animation.run_image_animation(mySprite,
            assets.animation("""
                player_left
                """),
            100,
            False)
    elif controller.down.is_pressed():
        direction2 = 180
        animation.run_image_animation(mySprite,
            assets.animation("""
                player_down
                """),
            100,
            False)
    elif controller.up.is_pressed():
        direction2 = 0
        animation.run_image_animation(mySprite,
            assets.animation("""
                player_up
                """),
            100,
            False)
game.on_update_interval(400, on_update_interval)
