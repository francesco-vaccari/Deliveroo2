import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class Graphics:
    def __init__(self, game, width=600, height=600):
        self.screen = pygame.display.set_mode((width, height),flags = pygame.RESIZABLE)
        self.game = game
        self.font_path = 'server_dir/font/Pixeltype.ttf'
        
        self.CELL_SIZE = 45
        self.SPACE_BETWEEN_CELLS = 5
        self.TEXT_FONT_SIZE = 15
        self.INFO_TEXT_FONT_SIZE = 35
        self.font = pygame.font.Font(self.font_path, int(self.TEXT_FONT_SIZE))
        self.font_info = pygame.font.Font(self.font_path, int(self.INFO_TEXT_FONT_SIZE))

        self.x_offset = 0
        self.y_offset = 0
        self.mouse_start_pos = (0, 0)
        self.display_info_pos = (0, 0)

        self.id_agent_to_draw = -1

    def get_pos(self, x, y):
        return x + self.x_offset, y + self.y_offset

    def draw_environment(self):
        self.screen.fill('Black')

        self.tl_cell = (self.CELL_SIZE + self.SPACE_BETWEEN_CELLS)

        for x, row in enumerate(self.game.map.grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(self.screen, 'cornsilk', pygame.Rect(self.get_pos(y * self.tl_cell, x * self.tl_cell), (self.CELL_SIZE, self.CELL_SIZE)))
                if cell == 2:
                    pygame.draw.rect(self.screen, 'firebrick1', pygame.Rect(self.get_pos(y * self.tl_cell, x * self.tl_cell), (self.CELL_SIZE, self.CELL_SIZE)))
                if cell == 3:
                    pygame.draw.rect(self.screen, 'firebrick4', pygame.Rect(self.get_pos(y * self.tl_cell, x * self.tl_cell), (self.CELL_SIZE, self.CELL_SIZE)))
                if cell == 4:
                    pygame.draw.rect(self.screen, 'lightgoldenrod', pygame.Rect(self.get_pos(y * self.tl_cell, x * self.tl_cell), (self.CELL_SIZE, self.CELL_SIZE)))
                if cell == 5:
                    pygame.draw.rect(self.screen, 'chartreuse4', pygame.Rect(self.get_pos(y * self.tl_cell, x * self.tl_cell), (self.CELL_SIZE, self.CELL_SIZE)))
        
        # can draw max 12 elements on the border of a cell (4 on each side)
        self.elements = [
            (self.game.parcels, 'darkgoldenrod3'),
            (self.game.batteries, 'green'),
            (self.game.keys, 'gray42'),
            (self.game.doors, 'saddlebrown'),
            # (self.game.parcels, 'Orange'),
            # (self.game.parcels, 'Blue'),
            # (self.game.parcels, 'Pink'),
            # (self.game.parcels, 'Purple'),
            # (self.game.parcels, 'Orange'),
            # (self.game.parcels, 'Green'),
            # (self.game.parcels, 'Red'),
            # (self.game.parcels, 'Brown'),
            # (self.game.parcels, 'Pink')
            ]
        self.draw_elements_in_cell()
        
        self.draw_agents()
    
    def draw_agents(self):
        agent_size = self.CELL_SIZE / 1.9
        tl_agent = (self.CELL_SIZE - agent_size) / 2

        for agent in self.game.agents:
            coords = self.get_pos(agent.y * self.tl_cell + tl_agent, agent.x * self.tl_cell + tl_agent)
            pygame.draw.rect(self.screen, 'blue4', pygame.Rect(coords, (agent_size, agent_size)))
            text_surf = self.font.render(str(agent.id), False, 'Yellow')
            text_rect = text_surf.get_rect(center = (self.get_pos(self.tl_cell * agent.y + tl_agent + agent_size / 2, self.tl_cell * agent.x + tl_agent + agent_size / 2)))
            self.screen.blit(text_surf, text_rect)

        self.draw_elements_on_agent(agent_size)
    
    def draw_elements_on_agent(self, agent_size):
        n_objects_drawn = 0
        for list in self.elements:
            objects = list[0]
            color = list[1]
            obj_square_space = agent_size / 4
            obj_in_square_space = obj_square_space / 4
            obj_size = obj_square_space - obj_in_square_space
            
            for object in objects:
                if object.to_draw_on_agent:
                    tl_agent = (self.tl_cell * object.y + (self.CELL_SIZE - agent_size) / 2, self.tl_cell * object.x + (self.CELL_SIZE - agent_size) / 2)
                    tl_cell = (tl_agent[0] - obj_in_square_space / 2, tl_agent[1] - obj_in_square_space / 2)

                    if n_objects_drawn < 4:
                        top_left_coord = (tl_cell[0] + obj_square_space * n_objects_drawn, tl_cell[1])
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))

                    elif n_objects_drawn < 8:
                        pos = n_objects_drawn - 4
                        top_left_coord = (tl_cell[0] + obj_square_space * 3 * (pos % 2), tl_cell[1] + obj_square_space * ((pos // 2) + 1))
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))

                    elif n_objects_drawn < 12:
                        pos = n_objects_drawn - 8
                        top_left_coord = (tl_cell[0] + obj_square_space * pos, tl_cell[1] + obj_square_space * 3)
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))
            
            n_objects_drawn += 1
    
    def draw_elements_in_cell(self):
        n_objects_drawn = 0
        for list in self.elements:
            objects = list[0]
            color = list[1]
            obj_square_space = self.CELL_SIZE / 4
            obj_in_square_space = obj_square_space / 4
            obj_size = obj_square_space - obj_in_square_space
            
            for object in objects:
                if object.to_draw:
                    tl_cell = (self.tl_cell * object.y - obj_in_square_space / 2, self.tl_cell * object.x - obj_in_square_space / 2)

                    if n_objects_drawn < 4:
                        top_left_coord = (tl_cell[0] + obj_square_space * n_objects_drawn, tl_cell[1])
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))

                    elif n_objects_drawn < 8:
                        pos = n_objects_drawn - 4
                        top_left_coord = (tl_cell[0] + obj_square_space * 3 * (pos % 2), tl_cell[1] + obj_square_space * ((pos // 2) + 1))
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))

                    elif n_objects_drawn < 12:
                        pos = n_objects_drawn - 8
                        top_left_coord = (tl_cell[0] + obj_square_space * pos, tl_cell[1] + obj_square_space * 3)
                        pygame.draw.rect(self.screen, color, pygame.Rect(self.get_pos(top_left_coord[0] + obj_in_square_space, top_left_coord[1] + obj_in_square_space), (obj_size, obj_size)))
            
            n_objects_drawn += 1

    def display_info(self):
        y, x = self.display_info_pos
        if self.id_agent_to_draw != -1:
            for agent in self.game.agents:
                if agent.id == self.id_agent_to_draw:
                    y, x = agent.y, agent.x
        
        drawing_pos = self.game.map.width * (self.CELL_SIZE + self.SPACE_BETWEEN_CELLS) + self.INFO_TEXT_FONT_SIZE

        if x < len(self.game.map.grid) and y < len(self.game.map.grid[0]) and x >= 0 and y >= 0:
            text = "Cell (" + str(x) + ", " + str(y) + "): "
            if self.game.map.grid[x][y] == 0:
                text += "Non-Walkable Cell"
            elif self.game.map.grid[x][y] == 1:
                text += "Walkable Cell"
            elif self.game.map.grid[x][y] == 2:
                text += "Delivery Cell"
            elif self.game.map.grid[x][y] == 3:
                text += "Double Delivery Cell"
            elif self.game.map.grid[x][y] == 4:
                text += "Parcels Spawn Cell"
            text_surf = self.font_info.render(text, False, 'White')
            text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE)))
            self.screen.blit(text_surf, text_rect)

            vert_offset = self.INFO_TEXT_FONT_SIZE * 2

            text_surf = self.font_info.render("Agents in this cell:", False, 'White')
            text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
            self.screen.blit(text_surf, text_rect)
            vert_offset += self.INFO_TEXT_FONT_SIZE
            for agent in self.game.agents:
                if agent.x == x and agent.y == y:
                    text = "       " + agent.print_agent()
                    text_surf = self.font_info.render(text, False, 'White')
                    text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
                    self.screen.blit(text_surf, text_rect)
                    vert_offset += self.INFO_TEXT_FONT_SIZE
            
            vert_offset += self.INFO_TEXT_FONT_SIZE

            text_surf = self.font_info.render("Parcels in this cell:", False, 'White')
            text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
            self.screen.blit(text_surf, text_rect)
            vert_offset += self.INFO_TEXT_FONT_SIZE
            for parcel in self.game.parcels:
                if parcel.x == x and parcel.y == y:
                    text = "       " + parcel.print_parcel()
                    text_surf = self.font_info.render(text, False, 'White')
                    text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
                    self.screen.blit(text_surf, text_rect)
                    vert_offset += self.INFO_TEXT_FONT_SIZE
            
            if self.id_agent_to_draw != -1:
                vert_offset += self.INFO_TEXT_FONT_SIZE
                text_surf = self.font_info.render("Locked onto agent: " + str(self.id_agent_to_draw), False, 'White')
                text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
                self.screen.blit(text_surf, text_rect)
                # vert_offset += self.INFO_TEXT_FONT_SIZE
                # for agent in self.game.agents:
                #     if agent.id == self.id_agent_to_draw:
                #         text = "       " + agent.print_agent()
                #         text_surf = self.font_info.render(text, False, 'White')
                #         text_rect = text_surf.get_rect(topleft = (self.get_pos(drawing_pos, self.INFO_TEXT_FONT_SIZE + vert_offset)))
                #         self.screen.blit(text_surf, text_rect)
                #         break
    
    def scale_sizes(self, event_y):
        if event_y > 0:
            scaling_factor = 1.05
        else :
            scaling_factor = 0.95
        self.CELL_SIZE *= scaling_factor
        self.SPACE_BETWEEN_CELLS *= scaling_factor
        self.TEXT_FONT_SIZE *= scaling_factor
        self.INFO_TEXT_FONT_SIZE *= scaling_factor
        self.font = pygame.font.Font(self.font_path, int(self.TEXT_FONT_SIZE))
        self.font_info = pygame.font.Font(self.font_path, int(self.INFO_TEXT_FONT_SIZE))
    
    def show_cell_info(self):
        mouse_pos = pygame.mouse.get_pos()
        x = int((mouse_pos[1] - self.y_offset) // (self.CELL_SIZE + self.SPACE_BETWEEN_CELLS))
        y = int((mouse_pos[0] - self.x_offset) // (self.CELL_SIZE + self.SPACE_BETWEEN_CELLS))
        self.display_info_pos = (y, x)
        for agent in self.game.agents:
            if agent.x == x and agent.y == y:
                self.id_agent_to_draw = agent.id
                break
        else:
            self.id_agent_to_draw = -1
    
    def lmb_pressed(self):
        self.mouse_start_pos = pygame.mouse.get_pos()
    
    def move_screen(self):
        mouse_end_pos = pygame.mouse.get_pos()
        self.x_offset += mouse_end_pos[0] - self.mouse_start_pos[0]
        self.y_offset += mouse_end_pos[1] - self.mouse_start_pos[1]
        self.mouse_start_pos = mouse_end_pos
    
    def display_fps(self, fps):
        pygame.font.init()
        font = pygame.font.SysFont(None, 15)
        fps_text = font.render(f"{int(fps)}", True, pygame.Color('white'))
        screen_width, screen_height = self.screen.get_size()
        text_rect = fps_text.get_rect()
        text_rect.topright = (screen_width - 10, 10)
        self.screen.blit(fps_text, text_rect)
