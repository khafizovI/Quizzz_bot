from tortoise.models import Model
from tortoise import fields
from tortoise.models import Model
from tortoise import fields

class Quiz(Model):
    id = fields.IntField(pk=True)
    question = fields.TextField()  # Savol
    options = fields.JSONField()  # Variantlar (ro'yxat)
    correct_answer = fields.IntField()

class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255, null=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    score = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "users"

class QuizCategory(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)
    questions = fields.ReverseRelation["Question"]

class Question(Model):
    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField("models.QuizCategory", related_name="questions")
    question = fields.CharField(max_length=1024)
    options = fields.JSONField()
    correct_answer = fields.CharField(max_length=255)
    explanation = fields.TextField(null=True)

    class Meta:
        table = "questions"

class QuizResult(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='quiz_results')
    category = fields.CharField(max_length=100)
    score = fields.IntField()
    questions_total = fields.IntField()
    questions_correct = fields.IntField()
    completed_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "quiz_results"

class UserAchievement(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='achievements')
    achievement_type = fields.CharField(max_length=100)
    achieved_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "user_achievements"

class ShopItem(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.IntField()
    description = fields.TextField()
    image_url = fields.CharField(max_length=255)

    class Meta:
        table = "shop_items"

from tortoise.models import Model
from tortoise import fields

class UserLog(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    username = fields.CharField(max_length=255, null=True)
    query = fields.TextField()
    response = fields.TextField()
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_logs"
