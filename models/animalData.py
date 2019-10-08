from django.db import models
from django.contrib import admin
from django.utils import timezone


# The model imports.
from .farm import Farm
from .task import Task

# The definitions

class AnimalGroup(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animalGroup = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.animalGroup


class AnimalGroupAdmin(admin.ModelAdmin):
    list_display = ('farm', 'animalGroup', 'active')
    search_fields = ('farm', 'animalGroup')
    list_filter = ('active',)
    ordering = ('farm', 'animalGroup')


class Breed(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('animalGroup', 'breed')

    def __str__(self):
        return self.breed


class BreedAdmin(admin.ModelAdmin):
    list_display = ('farm', 'breed', 'active', 'animalGroup')
    search_fields = ('farm', 'breed')
    list_filter = ('active',)
    ordering = ('farm', 'breed')


class SubGroup(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    subGroup = models.CharField(max_length=50)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('farm', 'animalGroup', 'subGroup')

    def __str__(self):
        return self.subGroup


class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('farm', 'subGroup', 'active', 'animalGroup')
    search_fields = ('farm', 'subGroup')
    list_filter = ('active',)
    ordering = ('farm', 'subGroup')


class Origin(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.origin


class OriginAdmin(admin.ModelAdmin):
    list_display = ('farm', 'origin', 'active')
    search_fields = ('farm', 'origin')
    list_filter = ('active',)
    ordering = ('farm', 'origin')


class Animal(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    mother = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    markings = models.CharField(max_length=200)
    filename = models.FileField()
    alive = models.BooleanField(default=True)
    comments = models.TextField()
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('farm')
    search_fields = ('farm', 'name')
    list_filter = ('active',)
    ordering = ('farm', 'name')


class Reason(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.reason


class Vet(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    care_date = models.DateField(blank=True)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    symptoms = models.TextField(blank=True)
    temperature = models.SmallIntegerField(blank=True)
    care = models.TextField(blank=True)
    weight = models.SmallIntegerField(blank=True)
    vet = models.CharField(max_length=100, blank=True)
    contact = models.IntegerField(blank=True)
    assistants = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.reason


class Medication(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.medication


class Meds_given(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    units = models.SmallIntegerField
    units_given = models.FloatField
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE)

    def __str__(self):
        return self.medication


class Egg_Log(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    collection_date = models.DateField()
    number = models.IntegerField()
    comments = models.TextField(max_length=300)

    def __str__(self):
        return self.collection_date


class Wormer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    wormer = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.wormer


class Sheep_care(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    care_date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    eye = models.SmallIntegerField()
    body = models.SmallIntegerField()
    tail = models.CharField(max_length=6)
    nose = models.CharField(max_length=100)
    coat = models.CharField(max_length=100)
    jaw = models.SmallIntegerField()
    wormer = models.CharField(max_length=100)
    wormer_quantity = models.IntegerField
    hoof = models.CharField(max_length=3)
    weight = models.IntegerField()
    estimated = models.CharField(max_length=9)
    comments = models.TextField()

    def __str__(self):
        return self.animal


class Forage(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    forage = models.CharField(max_length=100)
    density = models.FloatField()
    active = models.BooleanField()


class Paddock(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    size = models.FloatField()
    forage = models.ForeignKey(Forage, on_delete=models.CASCADE)
    active = models.BooleanField()


# The move table has been omitted

class Note(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    note_date = models.DateField()
    note = models.TextField()
    filename = models.FileField(blank=True)
    created_by = models.CharField(max_length=50)


class Destination(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.destination


class Sale(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    sale_tag = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    weight = models.SmallIntegerField()
    estimated = models.CharField(max_length=9)
    price_lb = models.DecimalField(max_digits=8, decimal_places=2)
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField()
    sale_date = models.DateField(auto_created=timezone.now)

    def __str__(self):
        return self.animal


class Slay_House(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    slay_house = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.slay_house


class Slaughter(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    sale_tag = models.CharField(max_length=50)  # I suspect this should be a foreign key with the table sale
    slay_house = models.ForeignKey(Slay_House, on_delete=models.CASCADE)
    hauler = models.CharField(max_length=200)
    haul_equip = models.CharField(max_length=200)
    slay_date = models.DateField()
    weight = models.PositiveSmallIntegerField
    estimated = models.CharField(max_length=9)
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()

    def __str__(self):
        return self.animal


class Other_Dest(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.reason


class Other_Reason(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        self.reason


class Other_Remove(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    remove_date = models.DateField()
    reason = models.ForeignKey(Other_Reason, on_delete=models.CASCADE)
    destination = models.ForeignKey(Other_Dest, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.reason


class Feed_Type(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Feed_Subtype(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.ForeignKey(Feed_Type, on_delete=models.CASCADE)
    subtype = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Feed_Unit(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Vendor(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


class Feed_Purchase(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    type = models.ForeignKey(Feed_Type, on_delete=models.CASCADE)
    subtype = models.ForeignKey(Feed_Subtype, on_delete=models.CASCADE)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    units = models.ForeignKey(Feed_Unit, on_delete=models.CASCADE)
    price_unit = models.DecimalField(max_digits=8, decimal_places=2)
    weight_unit = models.DecimalField(max_digits=8, decimal_places=2)


class Task_Master(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comments = models.TextField()
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    workers = models.IntegerField()
    minutes = models.IntegerField()
    complete = models.BooleanField(default=False)


class Task_Recurring(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    comments = models.TextField()
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    workers = models.IntegerField()
    minutes = models.IntegerField()
    recur = models.CharField(max_length=15)
