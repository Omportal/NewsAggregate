from django.shortcuts import render
from django.views.generic import View
from apps.parse_app.models import ParseData
from repository.parser_app_repository import ParserAppRepository
# Create your views here.


class NewsView(View):
    template_name = 'parse_app/news.html'
    content = ParseData.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):

        # TODO добавить этот метод в celery
        ParserAppRepository.create_all_parsers_data()

        return render(request, self.template_name, context={'content': self.content})
