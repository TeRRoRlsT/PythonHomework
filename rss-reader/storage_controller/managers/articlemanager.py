"""
Module manager of database model Article.

"""
from storage_controller.models import Article, DB_HANDLE

__all__ = ['ArticleManager']


class ArticleManager:
    def __init__(self):
        Article.create_table()

    @staticmethod
    def create_and_return(structs, source):
        """
        Method for creating articles in list in db. Return count of created objects

        :param structs: list of articles structs
        :param source: model Source object of feeds source
        :type structs: list
        :type source: Source
        :return: count of new created objects
        :rtype: int
        """
        count = 0
        for struct in structs:
            if Article.from_dict(struct, source) is not None:
                count += 1
        return count