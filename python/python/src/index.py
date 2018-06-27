import datetime


def returnN():
    a = {'name':"翰博",'age':25}
    b = 2018
    return a, b


if __name__ == '__main__':
    print('hello my world {}'.format(datetime.datetime.now()))


    a,b = returnN()

    print(a)
    print(b)
