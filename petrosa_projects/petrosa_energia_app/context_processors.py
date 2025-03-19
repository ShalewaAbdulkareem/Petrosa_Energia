from petrosa_energia_app.models import Category

def navbar_context(request):
    categories = Category.objects.filter(parent=None).prefetch_related('subcategories')
    return {'categories': categories}
