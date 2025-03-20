import pygame

# 初始化迷宫
ROW, COL = 6, 4
maze = [
    [0,  0,  0,  2],
    [0, -1, 0,  0],
    [0, -1, 0,  0],
    [0,  0,  0,  0],
    [0,  0, -1, 0],
    [3,  0,  0,  0]
]

# 设定起点与终点
START = (0, 3)
END = (5, 0)

# 计算可走的格子数量(所有格子数量 - 墙)
walkable_tiles = sum(1 for row in maze for cell in row if cell != -1)

# 颜色定义
BG_COLOUR = (231, 245, 255)
GRID_COLOUR = (91, 135, 227)
WALL_COLOUR = (0, 0, 57)
PLAYER_COLOUR = (255, 206, 227)
END_COLOUR = (175, 176, 255)
WIDTH,HEIGHT = 400,600
SIZE = 100

class Game:
    def __init__(self, maze):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ONE_LINE")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_pos = START
        self.visited = {START}
    
    def move_player(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        
        if 0 <= new_x < ROW and 0 <= new_y < COL:  # 边界检查
            if maze[new_x][new_y] != -1 and (new_x, new_y) not in self.visited:
                self.player_pos = (new_x, new_y)
                self.visited.add(self.player_pos)
            else:
                print("grid visted")
        
        # 游戏胜利条件
        if self.player_pos == END:
            if len(self.visited) == walkable_tiles:
                print("CONGRATS U PASSED")
            else:
                print("DIDN'T PASS ALL THE TILES")
            
    
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_player(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.move_player(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(0, 1)
    
    def render(self):
        self.window.fill(BG_COLOUR)
        font = pygame.font.SysFont("arial", 50)
        
        # 画网格
        for i in range(ROW + 1):
            pygame.draw.line(self.window, GRID_COLOUR, (0, i * (HEIGHT/ROW)), (COL * (HEIGHT/ROW), i * (HEIGHT/ROW)), 3)
        for j in range(COL + 1):
            pygame.draw.line(self.window, GRID_COLOUR, (j * (HEIGHT/ROW), 0), (j * (HEIGHT/ROW), ROW * (HEIGHT/ROW)), 3)
        
        # 画墙壁、起点和终点
        for i in range(ROW):
            for j in range(COL):
                if maze[i][j] == -1:
                    pygame.draw.rect(self.window, WALL_COLOUR, (j * (HEIGHT/ROW), i * (HEIGHT/ROW), (HEIGHT/ROW), (HEIGHT/ROW)))
                elif (i, j) == END:
                    end_text = font.render("E", True, END_COLOUR)
                    self.window.blit(end_text, ((j + 0.3) * (HEIGHT/ROW), (i + 0.2) * (HEIGHT/ROW)))
        
        # 画已访问路径
        for x, y in self.visited:
            pygame.draw.circle(self.window, (200, 195, 230), ((y + 0.5) * (HEIGHT/ROW), (x + 0.5) * (HEIGHT/ROW)), 10)
        
        # 画玩家
        x, y = self.player_pos
        pygame.draw.circle(self.window, PLAYER_COLOUR, ((y + 0.5) * (HEIGHT/ROW), (x + 0.5) * (HEIGHT/ROW)), 32)
        
        pygame.display.update()
    
    def run(self):
        while self.running:
            self.process_input()
            self.render()
            self.clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    game = Game(maze)
    game.run()
