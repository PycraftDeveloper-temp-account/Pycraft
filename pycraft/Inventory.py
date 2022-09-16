if __name__ != "__main__":
    import pygame
    import os
    import pyautogui
    from PIL import Image, ImageFilter
    import traceback

    base_folder = os.path.dirname(__file__)

    if ("site-packages" in base_folder or
            "dist-packages" in base_folder):

        import LoggingUtils
        import DisplayUtils
        import ImageUtils
        import SoundUtils
        import ErrorUtils

    else:
        from pycraft import LoggingUtils
        from pycraft import DisplayUtils
        from pycraft import ImageUtils
        from pycraft import SoundUtils
        from pycraft import ErrorUtils
            
    class GenerateInventory:
        def __init__(self):
            pass

        def set_display():
            try:
                try:
                    fullscreen_x = pyautogui.size()[0]
                    fullscreen_y = pyautogui.size()[1]

                    if fullscreen:
                        if opengl:
                            if vsync:
                                display = pygame.display.set_mode(
                                    (saved_window_width,
                                        saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)

                            else:
                                display = pygame.display.set_mode(
                                    (saved_window_width,
                                        saved_window_height),
                                    pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)
                        else:
                            display = pygame.display.set_mode(
                                (saved_window_width,
                                    saved_window_height),
                                pygame.RESIZABLE)

                    elif fullscreen is False:
                        if opengl:
                            if vsync:
                                display = pygame.display.set_mode(
                                    (fullscreen_x,
                                        fullscreen_y),
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=0)

                            else:
                                display = pygame.display.set_mode(
                                    (fullscreen_x,
                                        fullscreen_y),
                                    pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF,
                                    vsync=1)
                        else:
                            display = pygame.display.set_mode(
                                (fullscreen_x,
                                    fullscreen_y),
                                pygame.FULLSCREEN)

                except Exception as Message:
                    log_message = "display_utils > display_utils > set_display:", Message
                    
                    if output_log:
                        print(log_message)
                    
                    saved_window_width = 1280
                    saved_window_height = 720
                    pygame.display.quit()
                    pygame.init()
                    display = pygame.display.set_mode(
                        (saved_window_width, saved_window_height))

                pygame.display.set_icon(window_icon)
            
            except Exception as Message:
                error_message = "display_utils > display_utils > set_display: "+str(Message)
                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

        def Inventory(display, background_color, platform, title_font, base_folder, aa, font_color):
            try:
                DisplayUtils.display_utils.set_display(self)
                display.fill(background_color)
                pygame.display.update()

                if platform == "Linux":
                    title_font = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 60)

                else:
                    title_font = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 60)

                PycraftTitle = title_font.render(
                    "Pycraft",
                    aa,
                    font_color).convert_alpha()
                title_width = PycraftTitle.get_width()

                real_window_width = pygame.display.get_window_size()[0]
                real_window_height = pygame.display.get_window_size()[1]

                AlphaSurface = pygame.Surface(
                    (real_window_width, real_window_height),
                    pygame.HWSURFACE|
                    pygame.SRCALPHA).convert_alpha()
                AlphaSurface.set_alpha(204)
                AlphaSurface.fill(background_color)

                if platform == "Linux":
                    selector = pygame.image.load(
                        os.path.join(
                            base_folder,
                            (f"resources//general resources//selectorICON{self.theme}.jpg")))

                    selector.convert()

                else:
                    selector = pygame.image.load(
                        os.path.join(
                            base_folder,
                            (f"resources\\general resources\\selectorICON{self.theme}.jpg")))

                    selector.convert()

                selector_width = selector.get_width()

                hover1 = False
                hover2 = False
                hover3 = False
                hover4 = False
                hover5 = False
                hover6 = False
                hover7 = False
                hover8 = False

                if platform == "Linux":
                    ButtonFont1 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont2 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont3 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont4 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont5 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont6 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont7 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                    ButtonFont8 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts//Book Antiqua.ttf")), 30)

                else:
                    ButtonFont1 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont2 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont3 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont4 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont5 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont6 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont7 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                    ButtonFont8 = pygame.font.Font(
                        os.path.join(
                            base_folder,
                            ("fonts\\Book Antiqua.ttf")), 30)

                WeaponsText = ButtonFont1.render(
                    "Weapons",
                    aa,
                    font_color).convert_alpha()
                WeaponsTextWidth = WeaponsText.get_width()

                RangedWeaponsText = ButtonFont2.render(
                    "Ranged Weapons",
                    aa,
                    font_color).convert_alpha()
                RangedWeaponsTextWidth = RangedWeaponsText.get_width()

                ShieldsText = ButtonFont3.render(
                    "Shields",
                    aa,
                    font_color).convert_alpha()
                ShieldsTextWidth = ShieldsText.get_width()

                ArmourText = ButtonFont4.render(
                    "Armour",
                    aa,
                    font_color).convert_alpha()
                ArmourTextWidth = ArmourText.get_width()

                FoodText = ButtonFont5.render(
                    "Food",
                    aa,
                    font_color).convert_alpha()
                FoodTextWidth = FoodText.get_width()

                ItemsText = ButtonFont6.render(
                    "Items",
                    aa,
                    font_color).convert_alpha()
                ItemsTextWidth = ItemsText.get_width()

                SpecialItemsText = ButtonFont7.render(
                    "Special Items",
                    aa,
                    font_color).convert_alpha()
                SpecialItemsTextWidth = SpecialItemsText.get_width()

                OptionsText = ButtonFont7.render(
                    "Options",
                    aa,
                    font_color).convert_alpha()
                OptionsTextWidth = OptionsText.get_width()

                fullscreen_x, fullscreen_y = pyautogui.size()

                mouse_x = real_window_width/2
                mouse_y = real_window_height/2

                if aa:
                    if platform == "Linux":
                        pilImage = Image.open(
                            os.path.join(
                                base_folder,
                                ("resources//general resources//PauseIMG.png"))).resize(
                                    (real_window_width,
                                     real_window_height),
                                    Image.ANTIALIAS)
                    else:
                        pilImage = Image.open(
                            os.path.join(
                                base_folder,
                                ("resources\\general resources\\PauseIMG.png"))).resize(
                                    (real_window_width,
                                     real_window_height),
                                    Image.ANTIALIAS)

                else:
                    if platform == "Linux":
                        pilImage = Image.open(
                            os.path.join(
                                base_folder,
                                ("resources//general resources//PauseIMG.png"))).resize(
                                    (real_window_width,
                                     real_window_height))

                    else:
                        pilImage = Image.open(
                            os.path.join(
                                base_folder,
                                ("resources\\general resources\\PauseIMG.png"))).resize(
                                    (real_window_width,
                                     real_window_height))

                BLURRED_pilImage = pilImage.filter(ImageFilter.BoxBlur(4))

                PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                    self,
                    BLURRED_pilImage)

                display.blit(
                    PauseImg,
                    (0, 0))

                display.blit(
                    AlphaSurface,
                    (0, 0))

                while True:
                    self.mod_caption_utils__.generate_captions.get_normal_caption(
                        self,
                        "Inventory")

                    display.fill(background_color)

                    display.blit(
                        PauseImg,
                        (0, 0))

                    display.blit(
                        AlphaSurface,
                        (0, 0))

                    display.blit(
                        PycraftTitle,
                        ((real_window_width-title_width)/2, 0))

                    DisplayUtils.display_functionality.core_display_functions(
                        self, checkEvents=False)

                    if joystick_exit:
                        break

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                                (event.type == pygame.KEYDOWN and
                                    event.key == pygame.K_ESCAPE) or
                                (event.type == pygame.KEYDOWN and
                                    event.key == pygame.K_e)):
                            
                            break

                        if event.type == pygame.WINDOWFOCUSLOST:
                            window_in_focus = False
                        elif event.type == pygame.WINDOWFOCUSGAINED:
                            window_in_focus = True

                        if event.type == pygame.WINDOWSIZECHANGED:
                            real_window_width = pygame.display.get_window_size()[0]
                            real_window_height = pygame.display.get_window_size()[1]

                            AlphaSurface = pygame.Surface(
                                (real_window_width, real_window_height),
                                pygame.HWSURFACE|
                                pygame.SRCALPHA).convert_alpha()
                            AlphaSurface.set_alpha(204)
                            AlphaSurface.fill(background_color)

                            if platform == "Linux":
                                if aa:
                                    pilImage = Image.open(
                                        os.path.join(
                                            base_folder,
                                            ("resources//general resources//PauseIMG.png"))).resize(
                                                (real_window_width,
                                                 real_window_height),
                                                Image.ANTIALIAS)

                                else:
                                    pilImage = Image.open(
                                        os.path.join(
                                            base_folder,
                                            ("resources//general resources//PauseIMG.png"))).resize(
                                                (real_window_width,
                                                 real_window_height))

                            else:
                                if aa:
                                    pilImage = Image.open(
                                        os.path.join(
                                            base_folder,
                                            ("resources\\general resources\\PauseIMG.png"))).resize(
                                                (real_window_width,
                                                 real_window_height),
                                                Image.ANTIALIAS)

                                else:
                                    pilImage = Image.open(
                                        os.path.join(
                                            base_folder,
                                            ("resources\\general resources\\PauseIMG.png"))).resize(
                                                (real_window_width,
                                                 real_window_height))

                            BLURRED_pilImage = pilImage.filter(ImageFilter.BoxBlur(4))

                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_F11:
                                DisplayUtils.display_utils.update_display(self)

                                AlphaSurface = pygame.Surface(
                                    (fullscreen_x,
                                     fullscreen_y),
                                    pygame.HWSURFACE|
                                    pygame.SRCALPHA).convert_alpha()
                                AlphaSurface.set_alpha(204)
                                AlphaSurface.fill(background_color)

                    if (mouse_y >= 202*y_scale_factor and
                                mouse_y <= 247*y_scale_factor and
                                mouse_x >= 1155):

                        hover1 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)

                            mouse_button_down = False
                    else:
                        hover1 = False

                    if (mouse_y >= 252*y_scale_factor and
                                mouse_y <= 297*y_scale_factor and
                                mouse_x >= 1105):

                        hover2 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover2 = False

                    if (mouse_y >= 302*y_scale_factor and
                                mouse_y <= 347*y_scale_factor and
                                mouse_x >= 865):

                        hover3 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover3 = False

                    if (mouse_y >= 402*y_scale_factor and
                                mouse_y <= 447*y_scale_factor and
                                mouse_x >= 1035):

                        hover4 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover4 = False

                    if (mouse_y >= 352*y_scale_factor and
                                mouse_y <= 397*y_scale_factor and
                                mouse_x >= 880):

                        hover5 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover5 = False

                    if (mouse_y >= 502*y_scale_factor and
                                mouse_y <= 547*y_scale_factor and
                                mouse_x >= 1095):

                        hover6 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover6 = False

                    if (mouse_y >= 452*y_scale_factor and
                                mouse_y <= 497*y_scale_factor and
                                mouse_x >= 1095):

                        hover7 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover7 = False

                    if (mouse_y >= 552*y_scale_factor and
                                mouse_y <= 597*y_scale_factor and mouse_x >= 1095):

                        hover8 = True
                        if mouse_button_down:
                            PauseImg = ImageUtils.ConvertImage.pilImageToSurface(
                                self,
                                BLURRED_pilImage)

                            if sound:
                                SoundUtils.play_sound.play_click_sound(self)
                            mouse_button_down = False
                    else:
                        hover8 = False

                    ButtonFont1.set_underline(hover1)
                    ButtonFont2.set_underline(hover2)
                    ButtonFont3.set_underline(hover3)
                    ButtonFont4.set_underline(hover4)
                    ButtonFont5.set_underline(hover5)
                    ButtonFont6.set_underline(hover6)
                    ButtonFont7.set_underline(hover7)
                    ButtonFont8.set_underline(hover8)
                    AlphaSurface.fill(background_color)

                    display.blit(
                        WeaponsText,
                        ((real_window_width-WeaponsTextWidth)-2,
                         200*y_scale_factor))
                    if hover1:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(WeaponsTextWidth+selector_width)-2,
                             200*y_scale_factor))

                    display.blit(
                        RangedWeaponsText,
                        ((real_window_width-RangedWeaponsTextWidth)-2,
                         250*y_scale_factor))
                    if hover2:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(RangedWeaponsTextWidth+selector_width)-2,
                             250*y_scale_factor))

                    display.blit(
                        ShieldsText,
                        ((real_window_width-ShieldsTextWidth)-2,
                         300*y_scale_factor))
                    if hover3:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(ShieldsTextWidth+selector_width)-2,
                             300*y_scale_factor))

                    display.blit(
                        ArmourText,
                        ((real_window_width-ArmourTextWidth)-2,
                         350*y_scale_factor))
                    if hover4:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(FoodTextWidth+selector_width)-2,
                             400*y_scale_factor))

                    display.blit(
                        FoodText,
                        ((real_window_width-FoodTextWidth)-2,
                         400*y_scale_factor))
                    if hover5:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(ArmourTextWidth+selector_width)-2,
                             350*y_scale_factor))

                    display.blit(
                        ItemsText,
                        ((real_window_width-ItemsTextWidth)-2,
                         450*y_scale_factor))
                    if hover6:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(SpecialItemsTextWidth+selector_width)-2,
                             500*y_scale_factor))

                    display.blit(
                        SpecialItemsText,
                        ((real_window_width-SpecialItemsTextWidth)-2,
                         500*y_scale_factor))
                    if hover7:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(ItemsTextWidth+selector_width)-2,
                             450*y_scale_factor))

                    display.blit(
                        OptionsText,
                        ((real_window_width-OptionsTextWidth)-2,
                         550*y_scale_factor))
                    if hover8:
                        AlphaSurface.blit(
                            selector,
                            (real_window_width-(OptionsTextWidth+selector_width)-2,
                             550*y_scale_factor))

                    pygame.display.flip()
                    clock.tick(
                        DisplayUtils.display_utils.get_play_status(self))

                    if error_message is not None:
                        error_message = "".join(("Inventory > GenerateInventory ",
                                                     f"> Inventory: {str(error_message)}"))

                        print(error_message)
                        break
                    
            except Exception as Message:
                error_message = "Inventory > GenerateInventory > Inventory: "+str(Message)

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                ErrorUtils.generate_error_screen.error_screen(self)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "Startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
