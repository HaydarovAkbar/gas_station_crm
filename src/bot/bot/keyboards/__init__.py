try:
    from .base import KeyboardsAdmin
except ImportError:
    from base import KeyboardsAdmin
    print('ImportError in keyboards/__init__.py')