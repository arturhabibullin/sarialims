from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(MaterialType)
admin.site.register(ProductType)
admin.site.register(Bruker)
admin.site.register(Color)
admin.site.register(WorkShift)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('sample', 'date_production', 'company', 'material_type','product', 'get_categorys', 'bb_from', 'bb_to', 'pallet_from', 'pallet_to', 'date_registration','repeate', 'comment')
    ordering = ['-date_registration']
    def get_categorys(self, obj):
        return "\n".join([p.name for p in obj.category.all()])
admin.site.register(Sample, SampleAdmin)

class FFAAdmin(admin.ModelAdmin):
    list_display = ('sample', 'sample_mass', 'titrant_volume', 'value', 'date_pub')
admin.site.register(FFA, FFAAdmin) 

class ProteinAdmin(admin.ModelAdmin):
    list_display = ('sample', 'sample_mass', 'titrant_volume', 'value', 'date_pub')
admin.site.register(Protein, ProteinAdmin)    

class FatAdmin(admin.ModelAdmin):
    list_display = ('sample', 'blank_cup_mass', 'sample_mass', 'final_cup_mass', 'value', 'date_pub')
admin.site.register(Fat, FatAdmin)

class AshAdmin(admin.ModelAdmin):
    list_display = ('sample', 'blank_cup_mass', 'sample_mass', 'final_cup_mass', 'value', 'date_pub')
admin.site.register(Ash, AshAdmin)

class MoistureAdmin(admin.ModelAdmin):
    list_display = ('sample', 'blank_cup_mass', 'sample_mass', 'final_cup_mass', 'value', 'date_pub')
admin.site.register(Moisture, MoistureAdmin)

class AoksAdmin(admin.ModelAdmin):
    list_display = ('sample', 'sample_mass', 'bha', 'bht', 'value', 'date_pub')
admin.site.register(Aoks, AoksAdmin)
