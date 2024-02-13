from rest_framework.pagination import PageNumberPagination

class LessonCoursePaginator(PageNumberPagination):
    page_size = 10
