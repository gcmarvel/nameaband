from django.db import models


class Bandmate(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Groupname(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name



class Vote(models.Model):
    bandmate = models.ForeignKey(Bandmate, on_delete=models.CASCADE, related_name='votes')
    groupname = models.ForeignKey(Groupname, on_delete=models.CASCADE, related_name='votes')
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.groupname.name