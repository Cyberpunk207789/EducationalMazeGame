import pygame


class EventHandler:
    def __init__ (self):
        self.state = "Idle"

    def state_running (self):
        for event in pygame.event.get():
            #Выход из игры
            if event.type == pygame.QUIT:
                exit()

            #Управление челиком
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Вперед")
                if event.key == pygame.K_s:
                    print("Назад")
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_d:
                    pass

    def cycle(self):
        if self.state == "Running":
            self.state_running()




