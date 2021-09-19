import pygame
import sys

pygame.init()

def run(version, BackgroundCol, ShapeCol):
    FPSlistX = []
    FPSlistY = []

    FPSlistX2 = []
    FPSlistY2 = []

    clock = pygame.time.Clock()

    Display = pygame.display.set_mode((1280, 720))

    iteration = 0
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 15 FPS")
    while not iteration == 500:
        if not clock.get_fps() == 0:
            FPSlistX.append(iteration)
            FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(15)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 30 FPS")
    while not iteration == 1000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(30)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 45 FPS")
    while not iteration == 1500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(45)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 60 FPS")
    while not iteration == 2000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(60)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 75 FPS")
    while not iteration == 2500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(75)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 90 FPS")
    while not iteration == 3000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(90)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 105 FPS")
    while not iteration == 3500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(105)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 120 FPS")
    while not iteration == 4000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(120)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 135 FPS")
    while not iteration == 4500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(135)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 150 FPS")
    while not iteration == 5000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(150)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 200 FPS")
    while not iteration == 5500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(200)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 250 FPS")
    while not iteration == 6000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(250)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 300 FPS")
    while not iteration == 6500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(300)
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 350 FPS")
    while not iteration == 7000:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(350)
   
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Blank Window Benchmark @ 500 FPS")
    while not iteration == 7500:
        FPSlistX.append(iteration)
        FPSlistY.append(clock.get_fps())
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(500)

    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Preparing Animated Benchmark")

    iteration = 0
    run = 0
    y = 10

    while not iteration == 500:
        Display.fill(BackgroundCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(60)

            
    iteration = 0
    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 15 FPS")
    while not iteration == 500:
        run += 1
        if iteration == 0:
            linePoints = [(0,10),(300,10)]
        if not (clock.get_fps() == 0 or clock.get_fps() >= 15):
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(15)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10

    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 30 FPS")
    while not iteration == 1000:
        run += 1
        if iteration == 500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(30)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 45 FPS")
    while not iteration == 1500:
        run += 1
        if iteration == 1000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(45)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 60 FPS")
    while not iteration == 2000:
        run += 1
        if iteration == 1500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(60)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 70 FPS")
    while not iteration == 2500:
        run += 1
        if iteration == 2000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(75)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 90 FPS")
    while not iteration == 3000:
        run += 1
        if iteration == 2500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(90)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 105 FPS")
    while not iteration == 3500:
        run += 1
        if iteration == 3000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(105)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 120 FPS")
    while not iteration == 4000:
        run += 1
        if iteration == 3500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(120)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 135 FPS")
    while not iteration == 4500:
        run += 1
        if iteration == 4000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(135)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 150 FPS")
    while not iteration == 5000:
        run += 1
        if iteration == 4500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(150)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10

    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 200 FPS")
    while not iteration == 5500:
        run += 1
        if iteration == 5000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(200)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 250 FPS")
    while not iteration == 6000:
        run += 1
        if iteration == 5000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(250)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 300 FPS")
    while not iteration == 6500:
        run += 1
        if iteration == 5500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(300)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 350 FPS")
    while not iteration == 7000:
        run += 1
        if iteration == 6000:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(350)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10


    run = 0
    y = 10
    
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Running Animated Window Benchmark @ 500 FPS")
    while not iteration == 7500:
        run += 1
        if iteration == 6500:
            linePoints = [(0,10),(300,10)]
        if not clock.get_fps() == 0:
            FPSlistX2.append(iteration)
            FPSlistY2.append(clock.get_fps())
        Display.fill(BackgroundCol)
        pygame.draw.aalines(Display, ShapeCol, False, linePoints)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (not event.key == pygame.K_SPACE)):
                return False

        pygame.display.flip()
        iteration += 1
        clock.tick(500)
        linePoints.append((run*200,y))
        if run*200 >= 1280:
            y += 30
            run = -10
        
    pygame.display.set_caption(f"Pycraft: v{version}: Benchmark | Finished Animated Benchmark")

    return FPSlistX, FPSlistY, FPSlistX2, FPSlistY2