from django.db import models

class Trait(models.Model):
    name = models.CharField(max_length=50)

class Value(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    emoji = models.CharField(max_length=10)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    tagline = models.TextField()
    location = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    studies = models.CharField(max_length=100)
    gmail = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=100)
    
    resume_pdf = models.FileField(upload_to='documents/', default='documents/default.pdf')

    about_short = models.TextField(blank=True, default=' ')
    about_long = models.TextField(blank=True, default=' ')
    about_long1 = models.TextField(blank=True, default=' ')
    about_long2 = models.TextField(blank=True, default=' ')

    avatar = models.ImageField(upload_to='images/', default='images/default.jpg')

    traits = models.ManyToManyField(Trait, related_name='profiles')
    values = models.ManyToManyField(Value, related_name='profiles')


class Stats(models.Model):  
    projects = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, default='fas fa-layer-group')

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50)  

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    description = models.TextField(blank=True)
    
    skills = models.ManyToManyField('Skill', related_name='experience', blank=True)
    
    def __str__(self):
        return f"{self.role} at {self.company}"
    
class Education(models.Model):
    institution = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.degree} - {self.institution}'

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'

class ProjectTag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ProjectTechStack(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    is_featured = models.BooleanField(default=False)

    category = models.ManyToManyField(
        ProjectCategory,
        related_name='projects',
        blank=True
    )

    thumbnail = models.ImageField(upload_to='images/', default='images/default.jpg')
    title = models.CharField(max_length=50)
    description = models.TextField()

    live_url = models.CharField(max_length=100, blank=True)
    github_url = models.CharField(max_length=100)

    tag = models.ManyToManyField(ProjectTag, related_name='projects', blank=True)
    tech_stack = models.ManyToManyField(ProjectTechStack, related_name='projects', blank=True)
    
    def save(self, *args, **kwargs):
        if self.is_featured:
            # Remove featured from all other projects
            Project.objects.exclude(pk=self.pk).update(is_featured=False)

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-is_featured', '-id']
        
class Certification(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=50)
    date = models.DateField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='images/default.jpg'
    )
    
    def __str__(self):
        return f'{self.title}-{self.issuer}'

class Journey_Milestone(models.Model):
    year = models.PositiveIntegerField(default=2026)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.title}:{self.year}'
    
    class Meta:
         ordering = ['year','id']

class Interest(models.Model):
    emoji = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.emoji} {self.name}'

class Current(models.Model):
    label = models.CharField(max_length=100)
    reading = models.CharField(max_length=100)
    reading_sub = models.TextField()
    
    def __str__(self):
        return f'{self.label}'
        
    
    
    
    

    