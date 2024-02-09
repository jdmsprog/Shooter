#모듈 불러오기
import pygame
import random

# Pygame 실행
pygame.init()

# 해상도, 설정값
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3

# 색 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 창 정의
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KokeonShooter")

# 발사장치
player_img = pygame.image.load("kokeon.png")
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 20

# 탄환 설정
bullets = []

# 적군 설정
enemies = []
enemy_spawn_timer = 100  # 100프레임마다 적군 등장

# 서체설정
font = pygame.font.Font(None, 36)

# 변수정의
score = 0

# 반복문
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 스페이스바를 눌러 발사
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = pygame.Rect(player_rect.centerx, player_rect.top, 5, 10)
            bullets.append(bullet)

    keys = pygame.key.get_pressed()
    player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED

    # 탄환상태변경
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # 적군소환
    if enemy_spawn_timer <= 0:
        enemy_rect = pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30)
        enemies.append(enemy_rect)
        enemy_spawn_timer = 100

    # 적군상태변경
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # 충돌 / 꼬임 오류 감지
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # PyGame 창 표시부분 (렌더링 요소)
    screen.fill(WHITE)
    screen.blit(player_img, player_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    enemy_spawn_timer -= 1
    clock.tick(60)

# 게임끝내기
pygame.quit()
