from decouple import config

env = config("ENVIRONMENT", default="local")

if env == "local":
    from .local import *
elif env == "test":
    from .test import *
elif env == "production":
    from .production import *
else:
    raise ValueError("Invalid environment")