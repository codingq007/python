# jinja2는 탭, 공백문자, 개행문자 제거하지 않고 그대로 둔다.
from jinja2 import Environment, FileSystemLoader
import os

# file_loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))

file_loader = FileSystemLoader('C:/m-study/python_flask/11_02/templates')
env = Environment(loader = file_loader)

template = env.get_template('white_space.html')
print(template.render(truth = True))



