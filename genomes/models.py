from django.db import models

class Genome(models.Model):
    sequence_id = models.CharField(max_length=100)
    description = models.TextField()
    a_percent = models.FloatField()
    t_percent = models.FloatField()
    c_percent = models.FloatField()
    g_percent = models.FloatField()
    gc_percent = models.FloatField()
    at_gc_ratio = models.FloatField()

    def __str__(self):
        return self.sequence_id
