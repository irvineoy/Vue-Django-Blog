## Model structure:
- id = models.AutoField(primary_key=True)
- title = models.CharField(blank=False, max_length=255, )
- content = models.TextField()
- updataTime = models.DateTimeField(default=timezone.now())
- timesOfReply = models.IntegerField()
- timesOfRead = models.IntegerField()