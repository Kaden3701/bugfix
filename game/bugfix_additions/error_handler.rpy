init -5 python:
    class LabelNotFountErrorHandler(object):
        """
        Handles error in game when return label not found.
        Mostly caused by loading a save game that was taken during an crisis event
        """

        def __init__(self):
            self.target_depth = renpy.call_stack_depth()

        def __call__(self, short, full, traceback_fn):
            print(short)
            if "Could not find return label" in short:
                renpy.jump("game_loop")
                return True
            return False

    renpy.config.exception_handler = LabelNotFountErrorHandler()
