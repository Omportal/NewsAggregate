from typing import Dict, List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from apps.parse_app.models import ParseData
from parsers.dto import TprogerDTO, HabrDTO
from parsers.tproger_parser import main
from parsers.habr_parser import main_habr
from parsers.it_proger_parser import main_it_proger
# Create your views here.


class NewsView(View):
    template_name = 'parse_app/news.html'

    def get(self, request, *args, **kwargs):
        dto = main()
        dto_habr = main_habr()
        dto_itproger = main_it_proger()
        habr_content = self.create_content_habr(*dto_habr.habr)
        content = self.create_content_data(*dto.tproger)
        it_proger = self.create_content_it_proger(*dto_itproger.it_proger)
        return render(request, self.template_name, context={'content': content})

    @staticmethod
    def create_content_data(*dto) -> ParseData:
        for i in dto:
            if not ParseData.objects.filter(link=i['link']).exists():
                ParseData.objects.create(
                    title=i['title'],
                    link=i['link'],
                    description=i['description'],
                    img_link=i['img_link'])
        return ParseData.objects.all()

    @staticmethod
    def create_content_habr(*dto) -> ParseData:
        for i in dto:
            if not ParseData.objects.filter(link=i['link']).exists():
                ParseData.objects.create(
                    title=i['title'],
                    link=i['link'],
                    description=i['description'],
                    img_link=i['img_link'])
        return ParseData.objects.all()

    @staticmethod
    def create_content_it_proger(*dto) -> ParseData:
        for i in dto:
            if not ParseData.objects.filter(link=i['link']).exists():
                ParseData.objects.create(
                    title=i['title'],
                    link=i['link'],
                    description=i['description'],
                    img_link=i['img_link'])
        return ParseData.objects.all()
