init -10 python:
    # this class can generate a heart image based on their respective base images
    class HeartImage(renpy.display.im.ImageBase):
        images = {}

        def __init__(self, name, background, foreground, value = 0, secondary_foreground = None, secondary_value = 0, max_value = 20.0, **properties):
            super(HeartImage, self).__init__(name, **properties)
            self.name = name
            if background not in HeartImage.images:
                HeartImage.images[background] = Image(get_file_handle(background))
            if foreground not in HeartImage.images:
                HeartImage.images[foreground] = Image(get_file_handle(foreground))
            if not secondary_foreground is None and secondary_foreground not in HeartImage.images:
                HeartImage.images[secondary_foreground] = Image(get_file_handle(secondary_foreground))

            self.background = background
            self.foreground = foreground
            self.secondary_foreground = secondary_foreground
            self.value = value
            self.secondary_value = secondary_value
            self.max_value = max_value

        def _repr_info(self):
            return repr(self.name)

        def get_hash(self):
            return renpy.loader.get_hash(self.name)

        def load(self, unscaled=False):
            surface = renpy.display.im.cache.get(HeartImage.images[self.background])
            size = surface.get_size()
            image = pygame_sdl2.Surface(size, pygame_sdl2.SRCALPHA)
            image.blit(surface, (0, 0))

            width = size[0] * min(self.value / self.max_value, 1)
            surface2 = renpy.display.im.cache.get(HeartImage.images[self.foreground])
            image.blit(surface2.subsurface(0,0,width,size[1]), (0, 0))

            if self.secondary_foreground:
                secondary_width = size[0] * min(self.secondary_value / self.max_value, 1)
                surface3 = renpy.display.im.cache.get(HeartImage.images[self.secondary_foreground])
                image.blit(surface3.subsurface(width, 0, secondary_width, size[1]), (width, 0))

            return image

        def predict_files(self):
            return self.name
