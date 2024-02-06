try:
    from .base import start
    from .leader import leader
    from .admin import admin
except ImportError:
    from base import start
    from leader import leader
    from admin import admin
    print('ImportError')
