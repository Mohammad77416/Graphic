import arcade
import random
from arcade import Sound

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 3
        self.bird_image = arcade.load_texture("bird_image.png")

    def update(self):
        self.x -= self.velocity
        if self.x < 0:
            self.x = 1400 
            
    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.bird_image.width, self.bird_image.height, self.bird_image)
    
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.player_image = arcade.load_texture("player_image.png")

    def update(self, key):
        if key == arcade.key.LEFT:
            self.x -= self.speed
        elif key == arcade.key.RIGHT:
            self.x += self.speed
        elif key == arcade.key.UP:
            self.y += self.speed
        elif key == arcade.key.DOWN:
            self.y -= self.speed

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.player_image.width, self.player_image.height, self.player_image)

class Farm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.farm_image = arcade.load_texture("farm_image.png")

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.farm_image.width, self.farm_image.height, self.farm_image)

class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sheep_image = arcade.load_texture("sheep_image.png")

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.sheep_image.width, self.sheep_image.height, self.sheep_image)

class RainDrop:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = random.uniform(5, 10)

    def update(self):
        self.y -= self.velocity

    def draw(self):
        arcade.draw_line(self.x, self.y, self.x, self.y + self.size, arcade.color.BLUE, 2)
          
class TractorGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Tractor Game")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.tractor_speed = 20
        self.tractor_x = 600
        self.tractor_y = 350
        self.cloud_x = 100
        self.tractor_sound = arcade.load_sound("tractor_sound.wav")
        self.is_tractor_sound_playing = False
        self.player = Player(200, 200)
        self.farm = Farm(500,375)
        self.sheep_list = []
        self.add_sheep()
        self.bird_list = []
        self.add_bird()
        self.rain_sound = arcade.load_sound("rain_sound.wav")
        self.is_rain_sound_playing = False
        self.sheep_sound = arcade.load_sound("sheep_sound.wav")
        self.is_sheep_sound_playing = False

    def add_sheep(self):
        sheep1 = Sheep(1300, 300)
        sheep2 = Sheep(1350,350)
        sheep3 = Sheep(1400,400)
        self.sheep_list.append(sheep3)
        self.sheep_list.append(sheep2)
        self.sheep_list.append(sheep1)
        
    def add_bird(self):
        bird1 = Bird(1300, 500)
        bird2 = Bird(1350,550)
        bird3 = Bird(1400,600)
        self.bird_list.append(bird3)
        self.bird_list.append(bird2)
        self.bird_list.append(bird1)

    def setup(self):
        self.player_sound = arcade.load_sound("player_sound.wav")
        self.player_sound.play(volume=0.5) 
        self.raindrops = []
        for _ in range(100):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.uniform(5, 10)
            raindrop = RainDrop(x, y, size)
            self.raindrops.append(raindrop)
        self.play_rain_sound()
        self.play_sheep_sound()

    def on_draw(self):
        arcade.start_render()
        self.draw_grass()
        self.draw_road()
        self.draw_sun()
        self.draw_mountain()
        self.farm.draw()
        self.draw_barn()
        self.draw_tractor()
        self.draw_trees()
        self.draw_cloud(200, 500)
        self.player.draw()
        for sheep in self.sheep_list:
            sheep.draw()
        for raindrop in self.raindrops:
            raindrop.draw()
        for bird in self.bird_list:
            bird.draw()
     
    def play_rain_sound(self):
        if not self.is_rain_sound_playing:
            arcade.play_sound(self.rain_sound)
            self.is_rain_sound_playing = True
            
    def play_sheep_sound(self):
        if not self.is_sheep_sound_playing:
            arcade.play_sound(self.sheep_sound)
            self.is_sheep_sound_playing = True
            
    def draw_sun(self):
        # Draw the sun
        arcade.draw_circle_filled(900, 650, 60, arcade.color.YELLOW)

    def draw_cloud(self, x, y):
        
        x += self.cloud_x
        #1
        arcade.draw_circle_filled(x, y+100, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 60, y+100, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x - 60, y+100, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 30, y + 140, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x - 30, y + 140, 40, arcade.color.WHITE)
        #2
        arcade.draw_circle_filled(x+220, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 280, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 170, y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 200, y + 50, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 250, y + 50, 40, arcade.color.WHITE)
        #2
        arcade.draw_circle_filled(x+250, y+140, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 300, y+140, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 200, y+140, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 220, y + 180, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(x + 280, y + 180, 40, arcade.color.WHITE)

    def draw_grass(self):
        arcade.draw_lrtb_rectangle_filled(
            0, self.width, self.height / 2, 0, arcade.color.BITTER_LIME)

    def draw_road(self):
        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height / 4, 0, arcade.color.DARK_GRAY)
        
        #خط جاده
        arcade.draw_line(0,70,90,70,arcade.color.WHITE,10)
        arcade.draw_line(140,70,230,70,arcade.color.WHITE,10)
        arcade.draw_line(280,70,370,70,arcade.color.WHITE,10)
        arcade.draw_line(420,70,510,70,arcade.color.WHITE,10)
        arcade.draw_line(560,70,650,70,arcade.color.WHITE,10)
        arcade.draw_line(700,70,790,70,arcade.color.WHITE,10)
        arcade.draw_line(840,70,930,70,arcade.color.WHITE,10)
        arcade.draw_line(980,70,1070,70,arcade.color.WHITE,10)
        arcade.draw_line(1120,70,1210,70,arcade.color.WHITE,10) 
        arcade.draw_line(1260,70,1350,70,arcade.color.WHITE,10)  
        arcade.draw_line(1400,70,1490,70,arcade.color.WHITE,10) 
             
    def draw_mountain(self):
        # Draw the mountain
        arcade.draw_triangle_filled(
            700, 380, 1024, 380, 890, 600, arcade.color.DARK_BROWN)
        
        #snow
        arcade.draw_triangle_filled(
            785, 480, 963, 480, 890, 600, arcade.color.WHITE)
        
        #1
        arcade.draw_triangle_filled(
            690, 380, 1000, 380, 800, 500, arcade.color.DARK_BROWN)
        #2
        arcade.draw_triangle_filled(
            700, 380, 1000, 380, 850, 500, arcade.color.DARK_BROWN)
        #3
        arcade.draw_triangle_filled(
            700, 380, 1000, 380, 890, 500, arcade.color.DARK_BROWN)
        #4
        arcade.draw_triangle_filled(
            700, 380, 1000, 380, 930, 500, arcade.color.DARK_BROWN)
        #5
        arcade.draw_triangle_filled(
            700, 380, 1020, 380, 952, 500, arcade.color.DARK_BROWN)
        
        
        
        # Draw the small  mountain
        arcade.draw_triangle_filled(
            550, 380, 750, 380, 680, 550, arcade.color.DARK_BROWN)
        
        #snow
        arcade.draw_triangle_filled(
            626, 480, 710, 480, 680, 550, arcade.color.WHITE)
        
        #1
        arcade.draw_triangle_filled(
            550, 380, 730, 380, 640, 500, arcade.color.DARK_BROWN)
        #2
        arcade.draw_triangle_filled(
            550, 380, 740, 380, 665, 500, arcade.color.DARK_BROWN)
        
        #3
        arcade.draw_triangle_filled(
             550, 380, 750, 380, 685, 500, arcade.color.DARK_BROWN)
        #3
        arcade.draw_triangle_filled(
             550, 380, 760, 380, 702, 500, arcade.color.DARK_BROWN)
        
    def draw_trees(self):
        # Draw the trees
        arcade.draw_triangle_filled(
            450, 200, 350, 200, 400, 300, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(400, 180, 20, 40, arcade.color.BROWN)

        arcade.draw_triangle_filled(
            550, 200, 450, 200, 500, 300, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(500, 180, 20, 40, arcade.color.BROWN)

        arcade.draw_triangle_filled(
            650, 200, 550, 200, 600, 300, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(600, 180, 20, 40, arcade.color.BROWN)

    def draw_barn(self):
        # Barn cement base
        arcade.draw_lrtb_rectangle_filled(
            30, 350, 210, 170, arcade.color.BISQUE)

        # Bottom half
        arcade.draw_lrtb_rectangle_filled(
            30, 350, 350, 210, arcade.color.BROWN)

        # Left-bottom window
        arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

        # Right-bottom window
        arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

        # Barn door
        arcade.draw_rectangle_filled(
            190, 230, 100, 100, arcade.color.BLACK_BEAN)

        # Rail above the door
        arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)

        # Draw second level of barn
        arcade.draw_polygon_filled(
            [[20, 350], [100, 470], [280, 470], [360, 340]], arcade.color.BROWN)

        # Draw loft of barn
        arcade.draw_triangle_filled(
            100, 470, 280, 470, 190, 500, arcade.color.BROWN)

        # Left-top window
        arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

        # Right-top window
        arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)

        # Draw 2nd level door
        arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.BONE, 5)

    def draw_tractor(self):
        # Draw the engine
        arcade.draw_rectangle_filled(
            self.tractor_x, self.tractor_y, 140, 70, arcade.color.GRAY)
        arcade.draw_rectangle_filled(
            self.tractor_x - 10, self.tractor_y - 15, 90, 40, arcade.color.BLACK)

        # Draw the smoke stack
        arcade.draw_rectangle_filled(
            self.tractor_x - 20, self.tractor_y + 45, 10, 40, arcade.color.BLACK)

        # Back wheel
        arcade.draw_circle_filled(
            self.tractor_x - 110, self.tractor_y - 10, 50, arcade.color.BLACK)
        arcade.draw_circle_filled(
            self.tractor_x - 110, self.tractor_y - 10, 45, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(
            self.tractor_x - 110, self.tractor_y - 10, 35, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(
            self.tractor_x - 110, self.tractor_y - 10, 10, arcade.color.RED)

        # Front wheel
        arcade.draw_circle_filled(
            self.tractor_x + 50, self.tractor_y - 30, 30, arcade.color.BLACK)
        arcade.draw_circle_filled(
            self.tractor_x + 50, self.tractor_y - 30, 25, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(
            self.tractor_x + 50, self.tractor_y - 30, 18, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(
            self.tractor_x + 50, self.tractor_y - 30, 5, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.tractor_x -= self.tractor_speed
        elif key == arcade.key.RIGHT:
            self.tractor_x += self.tractor_speed
        elif key == arcade.key.UP:
            self.tractor_y += self.tractor_speed
        elif key == arcade.key.DOWN:
            self.tractor_y -= self.tractor_speed
            
        # پخش صدای تراکتور
        if not self.is_tractor_sound_playing:
            arcade.play_sound(self.tractor_sound)
            self.is_tractor_sound_playing = True
            
    def on_key_release(self, key, modifiers):
        # توقف پخش صدای تراکتور
        if self.is_tractor_sound_playing:
            arcade.stop_sound(self.tractor_sound)
            self.is_tractor_sound_playing = False
    
    def on_update(self, delta_time):
        
        # به متغیر موقعیت افقی ابرها تغییر دهید
        self.cloud_x += 1  # می‌توانید سرعت حرکت ابرها را تغییر دهید

        # بررسی اگر ابرها به انتهای تصویر رسیدند، موقعیت افقی را صفر کنید
        if self.cloud_x > self.width:
            self.cloud_x = 0
            
        for raindrop in self.raindrops:
            raindrop.update()
            if raindrop.y < 0:
                raindrop.y = self.height
        
        self.play_rain_sound()
        
        for bird in self.bird_list:
            bird.update()

def main():
    window = TractorGame(1500, 759)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
