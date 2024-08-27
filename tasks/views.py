from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import PersonTaskAssignment
def task_frequencies_view(request):

    search_query = request.GET.get('search', '')
    frequencies = PersonTaskAssignment.get_task_frequencies()
    
    if search_query:
        frequencies = [freq for freq in frequencies if search_query.lower() in freq['task_title'].lower() or search_query.lower() in freq['person_fullname'].lower()]

    paginator = Paginator(frequencies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'tasks/task_frequencies.html', context)
