# -*- coding: utf-8 -*-

import random

ENABLE = 1
NEWS_ID = 31
NEWS_DEBUG = False

DEFAULT_WEIGHT = 10


def random_by_weight(p):
    choice_id = []
    for i in range(len(p)):
        choice_id += [i for _ in range(DEFAULT_WEIGHT + p[i]["news_weight"])]

    return p[random.choice(choice_id)]


def random_news():
    news_list = [
         {
            "news_title": "Dcard coming soon",
            "news_image": "http://i.imgur.com/wDNlEaU.jpg",
            "news_url": "https://www.facebook.com/events/186383611572196/",
            "news_content": "",
            "news_weight": 0
        },
        {
            "news_title": "2015高應大校園歌唱大賽",
            "news_image": "http://i.imgur.com/oRRaM6H.jpg",
            "news_url": "https://www.facebook.com/pages/2015%E9%AB%98%E6%87%89%E5%A4%A7%E6%A0%A1%E5%9C%92%E6%AD%8C%E5%94%B1%E5%A4%A7%E8%B3%BD/503404693131297",
            "news_content": "",
            "news_weight": 0

        },
        {
            "news_title": "航海王奪寶 模咒逃走中",
            "news_image": "http://i.imgur.com/LVcpWi9.jpg",
            "news_url": "http://goo.gl/forms/6BbIyZXHdd",
            "news_content": "",
            "news_weight": 0
        },
        {
            "news_title": "高應大資訊研習社",
            "news_image": "http://i.imgur.com/cSHCYfZ.png",
            "news_url": "https://www.facebook.com/KUASITC/photos/a.750277898402920.1073741828.735951703168873/759733750790668/?type=1",
            "news_content": "",
            "news_weight": 0
        }

    ]

    if NEWS_DEBUG:
        return news_list[0]
    else:
        return random_by_weight(news_list)


def news_status():
    return [ENABLE, NEWS_ID]


def news():
    """
    News for kuas.

    return [enable, news_id, news_title, news_template, news_url]
        enable: bool
        news_id: int
        news_title: string
        news_tempalte: string
        news_url: string
    """

    # Get news from random news
    news = random_news()

    news_title = news["news_title"]
    news_template = (
            "<div style='text-align:center;'>"
            "<div><img style='display:block;margin-left:auto;margin-right:auto;max-width:80%;min-height:150px;height:auto;' src='"
            + news["news_image"] + "'></img>" + news["news_content"] + "</div>" +
            "</div>"

        )
    news_url = news["news_url"]

    return [ENABLE, NEWS_ID, news_title, news_template, news_url]
