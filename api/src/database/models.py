from boltons.strutils import camel2under
from sqlalchemy.ext.declarative import declared_attr


class TableNameMixin:
    @declared_attr
    def __tablename__(self):
        return camel2under(self.__name__)