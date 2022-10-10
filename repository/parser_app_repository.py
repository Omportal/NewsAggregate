from .repository import Repository
from apps.parse_app.models import ParseData
from parsers import it_proger_parser, habr_parser, tproger_parser


class ParserAppRepository(Repository):

    @staticmethod
    def create_content(*dto):
        for i in dto:
            if not ParseData.objects.filter(link=i['link']).exists():
                ParseData.objects.create(
                    title=i['title'],
                    link=i['link'],
                    description=i['description'],
                    img_link=i['img_link'],
                    site_name=i['site_name'])

    @staticmethod
    def create_all_parsers_data():
        dto_habr = habr_parser.main_habr()
        dto_tproger = tproger_parser.main()
        dto_itproger = it_proger_parser.main_it_proger()
        all_news_content = dto_habr.content + dto_itproger.content + dto_tproger.content
        ParserAppRepository.create_content(*all_news_content)


            
