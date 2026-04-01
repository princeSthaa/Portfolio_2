from django.contrib import admin
from .models import Profile,Trait, Value, Stats, SkillCategory, Skill, WorkExperience, Education, Project, ProjectCategory, ProjectTag, ProjectTechStack, Certification, Journey_Milestone, Interest, Current

admin.site.register(Current)
admin.site.register(Journey_Milestone)
admin.site.register(Profile)
admin.site.register(Trait)
admin.site.register(Value)
admin.site.register(Stats)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(ProjectTag)
admin.site.register(ProjectTechStack)
admin.site.register(Certification)
admin.site.register(Interest)