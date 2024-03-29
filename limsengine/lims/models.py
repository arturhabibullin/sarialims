from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='место отбора пробы')
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('company_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компания'

class Material(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='e.g мука, жир, шквара')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид образца'
        verbose_name_plural = 'Вид образца'

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='e.g линия А, птичья')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='НП, ВП, Mix')
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

class Color(models.Model):
    color = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50,unique=True, verbose_name='цвет')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Цвет этикетки'
        verbose_name_plural = 'Цвет этикетки'

class WorkShift(models.Model):
    value = models.IntegerField('смена', unique=True)
    
    def __str__(self):
        return str(self.value)
        
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смена'

class Specification(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    ffa_min = models.FloatField(blank=True, null=True, verbose_name='кислотное число мин. значение')
    ffa_max = models.FloatField(blank=True, null=True, verbose_name='кислотное число макс. значение')
    protein_min = models.FloatField(blank=True, null=True, verbose_name='протеин мин. значение')
    protein_max = models.FloatField(blank=True, null=True, verbose_name='пртоеин макс. значение')
    fat_min = models.FloatField(blank=True, null=True, verbose_name='жир мин. значение')
    fat_max = models.FloatField(blank=True, null=True, verbose_name='жир макс. значение')
    ash_min = models.FloatField(blank=True, null=True, verbose_name='зола мин. значение')
    ash_max = models.FloatField(blank=True, null=True, verbose_name='зола макс. значение')
    pv_min = models.FloatField(blank=True, null=True, verbose_name=' перекисное число мин. значение')
    pv_max = models.FloatField(blank=True, null=True, verbose_name='перекисное число макс. значение')
    aoks_min = models.FloatField(blank=True, null=True, verbose_name='антиоксидант мин. значение')
    aoks_max = models.FloatField(blank=True, null=True, verbose_name='антиоксидант макс. значение')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификация'

class Sample(models.Model):
    sample = models.SlugField('образец', max_length=50, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, verbose_name='цвет этикетки')
    date_production = models.DateField('дата производства')
    work_shift = models.ForeignKey(WorkShift, on_delete=models.CASCADE, blank=True, null=True,verbose_name='смена')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='вид образца', help_text='e.g мука, жир, шквара')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', help_text='e.g A, C, птичья, мясо-костная')
    tags = models.ManyToManyField(Tag, blank=True, related_name='samples', verbose_name='категории, теги')
    bb_from = models.PositiveIntegerField('Б.Б с', blank=True, null=True)
    bb_to = models.PositiveIntegerField('Б.Б по', blank=True, null=True)
    pallet_from = models.PositiveIntegerField('паллеты с', blank=True, null=True)
    pallet_to = models.PositiveIntegerField('паллеты по', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='Описание')
    date_registration = models.DateTimeField('дата регистрации', auto_now_add=True)
    comment = models.TextField('комментарий', blank=True)
    photo = models.ImageField('фото', upload_to = 'magages/%Y/%m/%d/', blank=True)
   

    def get_absolute_url(self):
        return reverse('sample_detail_url', kwargs={'sample': self.sample})

    @property
    def isoweekday(self):
        return self.date_production.isoweekday()

    def __str__(self):
        return self.sample
    
    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'

class FFA(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='ffas')
    sample_mass = models.FloatField('масса навески', max_length=5, blank=True, null=True)
    titrant_volume = models.FloatField('объем 0.1 Н KOH',blank=True, null=True)
    value = models.FloatField('кислотное число',blank=True, null=True,max_length=4)
    date_pub = models.DateTimeField(auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')

    def __str__(self):
        return str(self.sample)
     
    def save(self, *args, **kwargs):
        if self.sample_mass != None and self.titrant_volume != None:
            self.value = ( self.titrant_volume * 5.61 ) / self.sample_mass
            self.value = round(self.value, 2)
            super(FFA, self).save(*args, **kwargs)
        else:
            super(FFA,self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Кислотное число'
        verbose_name_plural = 'Кислотное число'

class Protein(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='proteins')
    sample_mass = models.FloatField('масса навески', max_length=5, blank=True, null=True)
    titrant_volume = models.FloatField('объем 0.2 М серной кислоты',blank=True, null=True)
    value = models.FloatField('массовая доля сырого протеина',blank=True, null=True,max_length=4)
    date_pub = models.DateTimeField(auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')


    def __str__(self):
        return str(self.sample)
     
    def save(self, *args, **kwargs):
        if self.sample_mass != None and self.titrant_volume != None:
            self.value = ( self.titrant_volume * 1.75 ) / self.sample_mass
            self.value = round(self.value, 2)
            super(Protein, self).save(*args, **kwargs)
        else:
            super(Protein,self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Протеин'
        verbose_name_plural = 'Протеин'

class Fat(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='fats')
    blank_cup_mass = models.FloatField('масса пустого стакана', blank=True, null=True)
    sample_mass = models.FloatField('масса навески', blank=True, null=True)
    final_cup_mass = models.FloatField('масса стакана i', blank=True, null=True)
    value = models.FloatField('массовая доля сырого жира', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')
    
    def __str__(self):
        return str(self.sample)

    def save(self, *args, **kwargs):
        if self.blank_cup_mass != None and self.sample_mass != None and self.final_cup_mass != None:
            self.value = ( ( self.final_cup_mass - self.blank_cup_mass ) / self.sample_mass ) * 100
            self.value = round(self.value, 2)
            super(Fat, self).save(*args, **kwargs)
        else:
            super(Fat, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Жир'
        verbose_name_plural = 'Жир'

class Ash(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='ashs')
    blank_cup_mass = models.FloatField('масса пустого тигля', blank=True, null=True)
    sample_mass = models.FloatField('масса навески', blank=True, null=True)
    final_cup_mass = models.FloatField('масса тигля i', blank=True, null=True)
    value = models.FloatField('массовая доля сырой золы', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')

    
    def __str__(self):
        return str(self.sample)

    def save(self, *args, **kwargs):
        if self.blank_cup_mass != None and self.sample_mass != None and self.final_cup_mass != None:
            self.value = ( ( self.final_cup_mass - self.blank_cup_mass ) / self.sample_mass ) * 100
            self.value = round(self.value, 2)
            super(Ash, self).save(*args, **kwargs)
        else:
            super(Ash, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Зола'
        verbose_name_plural = 'Зола'

class Moisture(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='moistures')
    blank_cup_mass = models.FloatField('масса пустой бюксы', blank=True, null=True)
    sample_mass = models.FloatField('масса навески', blank=True, null=True)
    final_cup_mass = models.FloatField('масса бюксы i', blank=True, null=True)
    value = models.FloatField('массовая доля влаги', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')
    
    def __str__(self):
        return str(self.sample)

    def save(self, *args, **kwargs):
        if self.blank_cup_mass != None and self.sample_mass != None and self.final_cup_mass != None:
            self.value = ( (1 - ( self.final_cup_mass - self.blank_cup_mass ) / self.sample_mass) ) * 100
            self.value = round(self.value, 2)
            super(Moisture, self).save(*args, **kwargs)
        else:
            super(Moisture, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Влага'
        verbose_name_plural = 'Влага'

class Aoks(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='aoks')
    sample_mass = models.FloatField('масса навески', blank=True, null=True)
    bha = models.FloatField(blank=True, null=True)
    bht = models.FloatField(blank=True, null=True)
    value = models.FloatField('суммарно bha/bht', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    technical_information = models.CharField('тех. инфо', max_length=150, blank=True, help_text='для внутреннего использования')
    
    def __str__(self):
        return str(self.sample)

    def save(self, *args, **kwargs):
        if  self.bha != None and self.bht != None:
            self.value = self.bha + self.bht
            self.value = round(self.value, 2)
            super(Aoks, self).save(*args, **kwargs)
        else:
            super(Aoks, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Антиоксидант'
        verbose_name_plural = 'Антиоксидант'




class Bruker(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='brukers')
    ffa = models.FloatField('кислотное число', blank=True, null=True)
    protein = models.FloatField('протеин', blank=True, null=True)
    fat = models.FloatField('жир', blank=True, null=True)
    ash = models.FloatField('зола', blank=True, null=True)
    moisture = models.FloatField('влага', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)

    def __str__(self):
        return str(self.sample)

    class Meta:
        verbose_name = 'Спектрометр'
        verbose_name_plural = 'Спектрометр'

class Milling(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='millings')
    date_pub = models.DateTimeField('дата анализа', auto_now=True)
    value_5mm = models.FloatField('5 мм %', blank=True, null=True)
    value_4mm = models.FloatField('4 мм %', blank=True, null=True)
    value_3mm = models.FloatField('3 мм %', blank=True, null=True)
    value_2mm = models.FloatField('2 мм %', blank=True, null=True)
    value_1mm = models.FloatField('1 мм %', blank=True, null=True)
    free_meal = models.FloatField('чистая мука % ', blank=True, null=True)
    sample_mass = models.FloatField('масса образца г.', blank=True, null=True)
    mass_5mm = models.FloatField('масса 5 мм г.', default=0)
    mass_4mm = models.FloatField('масса 4 мм г.', blank=True, null=True, default=0)
    mass_3mm = models.FloatField('масса 3 мм г.', blank=True, null=True, default=0)
    mass_2mm = models.FloatField('масса 2 мм г.', blank=True, null=True, default=0)
    mass_1mm = models.FloatField('масса 1 мм г.', blank=True, null=True, default=0)
   
    def save(self, *args, **kwargs):
        if self.sample_mass != None :
            self.value_5mm = (self.mass_5mm * 100) / self.sample_mass
            self.value_5mm = round(self.value_5mm, 2)
            self.value_4mm = (self.mass_4mm * 100) / self.sample_mass
            self.value_4mm = round(self.value_4mm, 2)
            self.value_3mm = (self.mass_3mm * 100) / self.sample_mass
            self.value_3mm = round(self.value_3mm, 2)
            self.value_2mm = (self.mass_2mm * 100) / self.sample_mass
            self.value_2mm = round(self.value_2mm, 2)
            self.value_1mm = (self.mass_1mm * 100) / self.sample_mass
            self.value_1mm = round(self.value_1mm, 2)
            self.free_meal = 100 - (self.value_5mm + self.value_4mm + self.value_3mm + self.value_2mm + self.value_2mm + self.value_1mm)

            super(Milling, self).save(*args, **kwargs)
        else:
            super(Milling, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sample)
    class Meta:
        verbose_name = 'Крупность помола'
        verbose_name_plural = 'Крупность помола'

class MMP(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='mmps')
    sample_mass = models.FloatField('масса навески в г.', blank=True, null=True, default=500)
    mmp_mass = models.FloatField('масса ММП в г.', blank=True, null=True)
    value = models.FloatField('значение ММП в мг/кг.', blank=True, null=True)
    date_pub = models.DateTimeField('дата анализа', auto_now=True)

   
    def __str__(self):
        return str(self.sample)

    def save(self, *args, **kwargs):
        if self.sample_mass != None and self.mmp_mass != None:
            self.value = ((self.mmp_mass * 1000)  / self.sample_mass) * 1000
            # self.value = round(self.value, 1)
            super(MMP, self).save(*args, **kwargs)
        else:
            super(MMP, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'ММП'
        verbose_name_plural = 'ММП'

# class PeroxideValue(models.Model):
#     sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='образец', related_name='peroxideValue')
#     sample_mass = models.FloatField('масса навески', blank=True, null=True)
#     titrant_volume = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)
#     Na_Vol_for_work_sol = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)
#     vol_work_solution = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)
#     conc_work_solution = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)
#     K_vol_titr = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)
#     Na_con_vol_titr = models.FloatField('объем раб.Na2S2O3',blank=True, null=True)