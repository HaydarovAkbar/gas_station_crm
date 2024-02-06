try:
    from .base import start
    from .leader import leader
    from .admin import admin, get_users, settings
except ImportError:
    from base import start
    from leader import leader
    from admin import admin, get_users, settings
    print('ImportError')
