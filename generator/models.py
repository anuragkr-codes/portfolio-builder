from django.db import models
import uuid

class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='template_previews/')
    
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    social_github = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)
    social_twitter = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}'s Portfolio"
    
    def get_absolute_url(self):
        return f"/portfolio/{self.unique_id}/"

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework'),
        ('tool', 'Tool'),
        ('soft', 'Soft Skill'),
        ('other', 'Other'),
    ]
    
    portfolio = models.ForeignKey(Portfolio, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=50)  # 0-100 scale
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    
    class Meta:
        ordering = ['-start_date']
        
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Education'
        
    def __str__(self):
        return f"{self.degree} at {self.institution}"
