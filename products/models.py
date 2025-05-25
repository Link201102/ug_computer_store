from django.db import models


class Product(models.Model):
    name = models.CharField("Наименование", max_length=255, null=False, blank=False)
    description = models.TextField("Описание", null=False, blank=False)
    price = models.DecimalField(
        "Цена", max_digits=10, decimal_places=2, null=False, blank=False
    )
    image = models.ImageField(
        "Изображение", upload_to="products/", null=False, blank=False
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=False, blank=False
    )
    brand = models.ForeignKey(
        "Brand", on_delete=models.CASCADE, null=False, blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    name = models.CharField("Наименование", max_length=255, null=False, blank=False)
    description = models.TextField("Описание", null=False, blank=False)
    image = models.ImageField(
        "Изображение", upload_to="categories/", null=False, blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField("Наименование", max_length=255, null=False, blank=False)
    description = models.TextField("Описание", null=False, blank=False)
    image = models.ImageField(
        "Изображение", upload_to="brands/", null=False, blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
