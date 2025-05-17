from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.topic


class NewsText(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"News for {self.topic.topic}"
    #    return f"News for {self.topic.topic}: {self.text} (Published on {self.pub_date.strftime('%Y-%m-%d %H:%M')})"