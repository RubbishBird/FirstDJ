from django.db import models


# Create your models here.

class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length = 200)   #属性text是一个CharField.由字符或文本组成的数据
    # DateTimeField：记录日期和时间的数据      实参auto_now_add=True,每当用户创建新主题时，Django将这个属性自动设置成当前的日期和时间
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text


class Entry(models.Model):
    '''学到的有关某主题的具体知识'''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            '''返回模型的字符串表示'''
            return self.text[:50] + '...'