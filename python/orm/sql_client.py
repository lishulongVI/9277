import pymysql 
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:123456@192.168.91.129/tornado',
                       encoding='utf8', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(2000), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(2000), nullable=False)
    author = Column(String(2000), nullable=False)
    created_at = Column(DateTime,)
    is_valid = Column(Boolean,)


if __name__ == '__main__':
    # News.metadata.create_all(engine)

    s = Session()

    # insert

    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))
    # s.add(News(title='lishulong',content='this is content',types = 'types',author = 'author'))

    # query
    print(s.query(News).get(1))
    print(s.query(News).get(2).title)


    # update

    obj = s.query(News).filter_by(title='lishulong').first()

    print(obj.content)

    obj.content = 'good'

    s.add(obj)

    s.commit()



    # delete
    # print(s.delete(s.query(News).get(1)))
    # s.commit()

    # s.commit()

