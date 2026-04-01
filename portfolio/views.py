from django.shortcuts import redirect, render

from profiling import settings
from .models import Profile   # ✅ add this
from .models import SkillCategory, WorkExperience, Education, Project, ProjectTechStack, Certification, Journey_Milestone, Interest, Current, Stats
from django.core.mail import send_mail

def about(request):
    profile = Profile.objects.first()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = f"""
        You have a new message from your portfolio:
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        send_mail(
            subject=subject or "No Subject",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["shresthaprince222@gmail.com"],  # your email
            fail_silently=False,
        )
    
    return render(request, 'portfolio/about.html',
                  {
                      'profile' : profile,
                      'certifications': Certification.objects.all(),
                      'journey_milestones' : Journey_Milestone.objects.all(),
                      'interests': Interest.objects.all(),
                      'current': Current.objects.all()
                  })

def index(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills')
    work_experiences = WorkExperience.objects.prefetch_related('skills')
    education = Education.objects.all()
    projects = Project.objects.all()
    tech_stack = ProjectTechStack.objects.all()
    
    skills = ["Python", "Django", "REST APIs", "PostgreSQL"]

    return render(request, "portfolio/index.html", {
        "skills": skills,
        "profile": profile,
        "skill_categories": skill_categories,
        "work_experiences": work_experiences,
        "education_list": education,
        "projects" : projects,
        "tech_stack" : tech_stack,
        "stats":Stats.objects.first()
    })

def base(request):
    return render(request, 'portfolio/base.html')