from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .views import snippet_list, snippet_detail


# urlpatterns = [
#     path('snippets/', snippet_list),
#     path('snippets/<int:pk>/', snippet_detail),
# ]
from .views import SnippetList, SnippetDetail


urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
