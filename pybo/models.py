from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문글의 제목
    content = models.TextField()  # 질문 내용
    create_date = models.DateTimeField()  # 질문 작성 일시

    def __str__(self):
        return self.subject  # 이렇게 하면 괴랄한 id를 출력해주는게 아니라 subject를 출력시켜줌


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question 클래스를 참조. 질문이 삭제되면 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()




