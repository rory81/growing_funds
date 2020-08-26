from .models import Category


def categories(request):
    """
    show the categories on all templates dynamically
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return context
