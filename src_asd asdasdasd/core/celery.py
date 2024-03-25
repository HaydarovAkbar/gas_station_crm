# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# app.conf.enable_utc = False
# app.conf.timezone = "Asia/Tashkent"

app.conf.beat_schedule = {
    # "check_all_users_result": {
    #     "task": "bot.tasks.check_all_users_result",
    #     "schedule": 10.0,
    #     # 'every': 10.0,}
}


# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")