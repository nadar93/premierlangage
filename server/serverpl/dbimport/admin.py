from django.contrib import admin

# Register your models here.

from dbimport.models import *

admin.site.register(AuthorizedDomainNames)
admin.site.register(Category)
admin.site.register(CategoryTranslation)
admin.site.register(Configuration)
admin.site.register(Exercise)
admin.site.register(ExerciseAuthor)
admin.site.register(ExerciseComment)
admin.site.register(ExerciseIsWrong)
admin.site.register(ExercisesCategoryVote)
admin.site.register(ExercisesKeywordsVote)
admin.site.register(ExercisesLevelsVote)
admin.site.register(ExercisesScoreVote)
admin.site.register(Keyword)
admin.site.register(KeywordTranslation)
admin.site.register(Levels)
admin.site.register(NextCategoryForExercise)
admin.site.register(PreviousCategoryForExercise)
admin.site.register(Users)
admin.site.register(UserSelectedCategory)
admin.site.register(Worksheet)
admin.site.register(WorksheetExercises)