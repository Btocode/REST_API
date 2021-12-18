from django.db import models

# Create your models here.

class User(models.Model):
  userId = models.AutoField(primary_key=True)
  email  = models.EmailField(max_length=200,null=True)
  password = models.CharField(max_length=30,null = True)

  GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
  )
  firstName = models.CharField(max_length = 20, null=True)
  lastName = models.CharField(max_length = 20, null=True)
  gender = models.CharField(max_length = 10, null=True,choices=GENDER)
  age = models.IntegerField(null=True)
  
  jobTitle = models.CharField(max_length = 50, null=True)
  programming = models.CharField(max_length = 200, null=True)
  languageKnown = models.CharField(max_length = 200, null=True)
  linkedIn = models.CharField(max_length = 200, null=True)
  resume = models.CharField(max_length = 200, null=True)
  github = models.CharField(max_length = 200, null=True)
  def __str__(self):
    return self.firstName



class Idea(models.Model):
  ideaId = models.AutoField(primary_key=True)
  ideaDesc = models.CharField(max_length=2000,null=True)
  ideatitle = models.CharField(max_length=200,default='Provide a title here')
  ideatags = models.CharField(max_length=200,default='#tags')
  upVotes = models.IntegerField(null=True)
  downVotes = models.IntegerField(null=True)
  collaborators = models.IntegerField(null=True)
  postingTime = models.DateTimeField(auto_now_add=True, null=True)

  user = models.ForeignKey(User, on_delete=models.CASCADE, 
  related_name="idea")
  # comment = models.ForeignKey(Suggestion,on_delete=models.CASCADE)
  def __str__(self):
    return self.ideatitle

class Notification(models.Model):
  notiId = models.AutoField(primary_key=True)
  NOTIFICATION = (
      ("Upvote",1),
      ("Downvote",2),
      ("Followed",3),
      ("Suggested",4),
      ("Friend",5),
      ("Collaboration",6),
  )
  notiType = models.CharField(max_length=20, null=True,choices=NOTIFICATION)
  notiTime = models.TimeField(auto_now_add=True,null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="notification")
  def __str__(self):
    return self.notiType

class Suggestion(models.Model):
  ideaId = models.ForeignKey(Idea, on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  content = models.CharField(max_length=300,default=None)
  def __str__(self):
    return self.user
  