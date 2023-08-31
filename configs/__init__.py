from .extra import Extra

class Configs:
    def __init__(self,extra:Extra=None):
        self.extra = extra

configs = Configs(
    extra=Extra()
)