import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習７－１
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_rct = kk_img.get_rect() #練習８－１（こうかとんrectを抽出）
    kk_rct.center = 300, 200 #練習８－２（中心座標）
    tmr = 0
    x_ziku = 0
    y_ziku = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y_ziku = -1
        if key_lst[pg.K_DOWN]:
            y_ziku = 1
        if key_lst[pg.K_RIGHT]:
            x_ziku = 2
        if key_lst[pg.K_LEFT]:
            x_ziku = -1  
        kk_rct.move_ip([x_ziku-1, y_ziku])  #練習８
        x_ziku = 0
        y_ziku = 0

        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg_img2, [-x+1600, 0]) #練習７－１
        screen.blit(bg_img, [-x+3200, 0]) #練習６
        screen.blit(bg_img2, [-x+4800, 0]) #練習７－１
        screen.blit(kk_img, kk_rct)  #練習４
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()