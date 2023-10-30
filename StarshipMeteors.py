import pygame
import random
import time

FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
WHITE = (255, 255, 255)
BACKGROUND = (0, 0, 0)
INITIAL_METEOR_Y_LOCATION = 10
INITIAL_NUMBER_OF_METEORS = 8
MAX_METEOR_SPEED = 5
STARSHIP_SPEED = 10
MAX_NUMBER_OF_CYCLES = 1000
NEW_METEOR_CYCLE_INTERVAL = 40


class GameObject:
    def __init__(self, game, image_filename):
        self.game = game
        self.load_image(image_filename)

    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.width, self.height = self.image.get_size()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.game.display_surface.blit(self.image, (self.x, self.y))


class Starship(GameObject):
    def __init__(self, game):
        super().__init__(game, 'starship.png')
        self.x = DISPLAY_WIDTH // 2
        self.y = DISPLAY_HEIGHT - 40

    def move(self, dx, dy):
        self.x = max(0, min(self.x + dx, DISPLAY_WIDTH - self.width))
        self.y = max(0, min(self.y + dy, DISPLAY_HEIGHT - self.height))


class Meteor(GameObject):
    def __init__(self, game):
        super().__init__(game, 'meteor.png')
        self.x = random.randint(0, DISPLAY_WIDTH)
        self.y = INITIAL_METEOR_Y_LOCATION
        self.speed = random.randint(1, MAX_METEOR_SPEED)

    def move(self):
        self.y = (self.y + self.speed) % DISPLAY_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption('Starship Meteors')
        self.clock = pygame.time.Clock()
        self.starship = Starship(self)
        self.meteors = [Meteor(self) for _ in range(INITIAL_NUMBER_OF_METEORS)]

    def check_for_collision(self):
        return any(self.starship.rect().colliderect(meteor.rect()) for meteor in self.meteors)

    def display_message(self, message):
        text_font = pygame.font.Font('freesansbold.ttf', 48)
        text_surface = text_font.render(message, True, WHITE)
        text_rect = text_surface.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        self.display_surface.fill(WHITE)
        self.display_surface.blit(text_surface, text_rect)

    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False

    def play(self):
        is_running = True
        starship_collided = False
        cycle_count = 0

        while is_running and not starship_collided:
            cycle_count += 1

            if cycle_count == MAX_NUMBER_OF_CYCLES:
                self.display_message('WINNER!')
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.starship.move(STARSHIP_SPEED, 0)
                    elif event.key == pygame.K_LEFT:
                        self.starship.move(-STARSHIP_SPEED, 0)
                    elif event.key == pygame.K_UP:
                        self.starship.move(0, -STARSHIP_SPEED)
                    elif event.key == pygame.K_DOWN:
                        self.starship.move(0, STARSHIP_SPEED)
                    elif event.key == pygame.K_p:
                        self.pause()
                    elif event.key == pygame.K_q:
                        is_running = False

            for meteor in self.meteors:
                meteor.move()

            self.display_surface.fill(BACKGROUND)
            self.starship.draw()
            for meteor in self.meteors:
                meteor.draw()

            if self.check_for_collision():
                starship_collided = True
                self.display_message('Collision: Game Over')

            if cycle_count % NEW_METEOR_CYCLE_INTERVAL == 0:
                self.meteors.append(Meteor(self))

            pygame.display.update()
            self.clock.tick(FRAME_REFRESH_RATE)
            time.sleep(1)

        pygame.quit()


def main():
    print('Starting Game')
    game = Game()
    game.play()
    print('Game Over')


if __name__ == '__main__':
    main()
