import conf
import data
import requests


# создание заказа
def post_new_order(body):
    return requests.post(conf.URL_SERVICE + conf.ORDER, json=body)


# номер трека заказа
track = post_new_order(data.new_order).json()['track']


# запрос на получения заказа по треку заказа
def get_receive_order():
    return requests.get(conf.URL_SERVICE + conf.RECEIVE + str(track))