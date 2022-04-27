from django.contrib import admin
from . models import Recipe, RecipeIngredient
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Register your models here.



class RecipeIngredientInline(admin.TabularInline):  #!
    model = RecipeIngredient                         
    #fields = ['name','quantity','unit','directions']
    extra = 0
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']

class RecipeIngredientStackedInline(admin.StackedInline): #!
    model = RecipeIngredient
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']
    fields = ['name', 'quantity','unit','directions']
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    #inlines = [RecipeIngredientInline]              #!
    inlines = [RecipeIngredientStackedInline]       #!
    list_display=['name', 'user']
    readonly_fields = ['timestamp','updated']      #!
    #raw_id_fields = ['user']                        #!



admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
