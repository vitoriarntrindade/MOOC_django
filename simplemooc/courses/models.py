from django.db import models
from django.db.models import Q
from django.urls import reverse


class CourseManager(models.Manager):

    def search(self, query):
        return super().get_queryset().filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Nome', max_length=80)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre', blank=True)
    start_date = models.DateField('Data de ínicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images',
                              verbose_name='Imagem',
                              null=True,
                              blank=True
                              )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em",  auto_now=True)

    objects = CourseManager()

    def get_absolute_url(self):
        return reverse('courses:details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']