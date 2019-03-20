# # -*- coding: utf-8 -*-
import pytest
import json
import os.path
import importlib
#import jsonpickle
#файл создания фикстур

from fixture.application import Application
#from fixture.db import DbFixture
fixture = None
target =None


def load_config(file): # выполняется загрузка конфигурации
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request): #через request получаем доступ к опциям
    global fixture
    global target
    browser = request.config.getoption("--browser")  # передаем опц значение в конструктор application
    web_config = load_config(request.config.getoption("--target"))['web'] #загрузка конфигурации фикстуры из файла
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])   # если фикстура сломалась, запускаем новую
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture
def adminka(request): #через request получаем доступ к опциям
    global fixture
    global target
    browser = request.config.getoption("--browser")  # передаем опц значение в конструктор application
    web_config = load_config(request.config.getoption("--target"))['webadmin'] #загрузка конфигурации фикстуры из файла
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])   # если фикстура сломалась, запускаем новую
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)  #scope session чтобы логаут был после прохождения всех тестов, autouse чтобы автоматом завершил сессию
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser): #опции для фикстуры перед запуском тестов
    parser.addoption("--browser", action="store", default="firefox") #store значит сохранить значение параметра