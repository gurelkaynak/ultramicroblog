from django.contrib import admin
from django import forms
from .models import Post
from .models import Category


class PostAdminForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        Category.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('categories', False),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['categories'] = self.instance.categories.values_list('pk', flat=True)

    def save(self, *args, **kwargs):
        kwargs['commit'] = True
        return super(PostAdminForm, self).save(*args, **kwargs)

    def save_m2m(self):
        self.instance.categories.clear()
        self.instance.categories.add(*self.cleaned_data['categories'])

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
