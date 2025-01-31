from api_v1.models import Source

__all__ = ['SourceManager']


class SourceManager:
    @staticmethod
    def get_or_create(url, title):
        """
        Method for safe getting a Source model object.

        :param url: string link for init object
        :param title: title of feeds source
        :type url: str
        :type title: str
        :return: Source object. If object with such data is founded return it,
            else created new object and return it.
        :rtype: Source
        """
        return Source.get_or_create(url, title=title)

    @staticmethod
    def get_articles_with_data_from(url, date):
        """
        Method to getting articles with date after a given date.

        :param url: URL-key for getting Source object
        :param date: date for query
        :type url: str
        :type date: str
        :return: dict with title of a rss source and founded articles
        :rtype dict
        """
        source = Source.get_or_create(url)

        articles = source.sort_by_date(date)
        return {
            'title': source.title,
            'articles': articles,
        }
