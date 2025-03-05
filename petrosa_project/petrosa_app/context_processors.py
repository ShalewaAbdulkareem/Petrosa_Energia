from petrosa_app.models import Category

def navbar_context(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    return {'categories': categories}
