init -2 python:
    class Hint():
        def __init__( self, title, description, start_condition, complete_condition, description_func_string = None):
            self._title = title
            self._description = description
            self._start_condition = start_condition
            self._complete_condition = complete_condition
            self._description_func_string = description_func_string

        # Return the text for the actual stage.
        @property
        def is_active( self ):
            try:
                return eval(self._start_condition)
            except NameError:
                return False    # on error it's not active

        # Return the (human understandable) number of the actual stage. 
        @property
        def is_complete( self ):
            try:
                return eval(self._complete_condition)
            except NameError:
                return True     # on error it's complete

        @property
        def title(self):
            return self._title

        @property
        def description(self):
            if self._description_func_string:
                parts = self._description_func_string.split(".")
                if parts > 1:
                    return getattr(globals()[parts[0]], parts[1])()
                else:
                    return globals()[self._description_func_string]()
            else:
                return self._description
