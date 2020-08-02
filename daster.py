# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/21 19:59
@Auth ： LuZheng
@E-mail: 466824111@qq.com
@IDE ：PyCharm
"""
from dagster import execute_pipeline, pipeline, solid


@solid
def get_name(_):
    return 'dagster'


@solid
def hello(context, name: str):
    context.log.info('Hello, {name}!'.format(name=name))


@pipeline
def hello_pipeline():
    hello(get_name())