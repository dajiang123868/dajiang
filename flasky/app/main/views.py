# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app, request
from flask.json import jsonify
import requests
from .. import db
# from ..models import User
# from ..email import send_email
from . import main
# from .forms import NameForm
from lxml import etree


@main.route('/article', methods=['GET', 'POST'])
def index():
    index = request.args.get('p')
    item_list = []
    url = 'https://www.jianshu.com/u/05f416aefbe1?order_by=shared_at&page={}'.format(index)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res = etree.HTML(res.content.decode())
    nodes = res.xpath('//ul[@class="note-list"]/li')
    for node in nodes:
        item = {}
        title = node.xpath('.//a[@class="title"]/text()')[0]
        time = node.xpath('.//span[@class="time"]/@data-shared-at')[0]
        abstract = node.xpath('.//p[@class="abstract"]/text()')[0].replace('\n','').replace(' ','')
        img = node.xpath('./a/img/@src')
        url = 'https://www.jianshu.com' + node.xpath('.//a/@href')[0]
        item['title'] = title
        item['time'] = time
        item['url'] = url
        item['abstract'] = abstract
        item['img'] = img
        item_list.append(item)

    return jsonify(item_list)

