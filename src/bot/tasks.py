from ..core import celery_app
from .models import User


@celery_app.task
def check_user_result(groupmember_id):
    print("Hello")
    user = User.objects.get(id=groupmember_id)
    print(user)


@celery_app.task
def check_all_users_result():
    print("Hello")
    groupmembers = User.objects.all()
    for groupmember in groupmembers:
        check_user_result.delay(groupmember.id)
