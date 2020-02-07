from django.db import models


class Results(models.Model):
    query = models.CharField(max_length=25)
    row_number = models.IntegerField()

    def __str__(self):
        return self.query

    class Meta:
        verbose_name_plural = "Результаты"
        verbose_name = "Результат"