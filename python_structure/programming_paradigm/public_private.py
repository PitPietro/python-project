class PublicPrivate:
    """
    Python does not have private variables or methods.
    There is just a naming convention: the variables
    and methods that should be considered as private,
    starts whit an underscore.
    """
    def __init__(self):
        self.public = "public"
        self._private = "private"

    def public_method(self):
        return self.public

    def private_method(self):
        return self._private
