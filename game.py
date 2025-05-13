import pygame
import math

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Солнечная система")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SUN_COLOR = (255, 255, 0)
PLANET_COLOR = (0, 0, 255)

# Солнце
sun_radius = 50
sun_pos = (width // 2, height // 2)

# Планеты (положение и радиус орбит)
planets = [
    {'name': 'Меркурий', 'distance': 60, 'radius': 8, 'speed': 1.59},  # Меркурий
    {'name': 'Венера', 'distance': 100, 'radius': 12, 'speed': 1.18},    # Венера
    {'name': 'Земля', 'distance': 150, 'radius': 15, 'speed': 1},       # Земля
    {'name': 'Марс', 'distance': 200, 'radius': 10, 'speed': 0.53},     # Марс
]

# Инициализация времени
clock = pygame.time.Clock()

def draw_planet(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def draw_orbit(x, y, distance):
    pygame.draw.circle(screen, WHITE, (x, y), distance, 1)

def main():
    running = True
    angle = 0  # Начальный угол для движения планет
    while running:
        screen.fill(BLACK)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Рисуем Солнце
        draw_planet(sun_pos[0], sun_pos[1], sun_radius, SUN_COLOR)

        # Рисуем орбиты планет
        for planet in planets:
            draw_orbit(sun_pos[0], sun_pos[1], planet['distance'])
        
        # Рисуем планеты
        for planet in planets:
            planet_x = sun_pos[0] + planet['distance'] * math.cos(math.radians(angle * planet['speed']))
            planet_y = sun_pos[1] + planet['distance'] * math.sin(math.radians(angle * planet['speed']))
            draw_planet(planet_x, planet_y, planet['radius'], PLANET_COLOR)

        # Увеличиваем угол для анимации
        angle += 1
        if angle >= 360:
            angle = 0

        # Обновляем экран
        pygame.display.flip()
        clock.tick(60)  # 60 кадров в секунду

    pygame.quit()

if __name__ == "__main__":
    main()
