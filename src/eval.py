# -*- coding: utf-8 -*-

import argparse
import codecs
import copy
import os

from jinja2 import FileSystemLoader
from jinja2 import Environment
import yaml


class Evaluator(object):
    def __init__(self, template_dir, render_dir, data_file):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.render_dir = render_dir
        with open(data_file) as f:
            self.data = yaml.load(f.read())

    def render(self, template, data):
        template = self.env.get_template(template)
        with codecs.open(os.path.join(self.render_dir, data['file']),
                         'w', encoding="utf-8") as f:
            f.write(template.render(data))

    def render_all(self):
        data = copy.deepcopy(self.data)
        self.render(data['template'], data)
        for room in data['rooms']:
            data.update(room)
            self.render(data['template'], data)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--data-file', dest='data_file', action='store', type=str,
        help='yaml data file', default=None
    )
    parser.add_argument(
        '-t', '--template-dir', dest='template_dir', action='store', type=str,
        help='template directory', default=None
    )
    parser.add_argument(
        '-r', '--render-dir', dest='render_dir', action='store', type=str,
        help='render directory', default=None
    )
    params, other_params = parser.parse_known_args()

    evaluator = Evaluator(
        template_dir=params.template_dir,
        render_dir=params.render_dir,
        data_file=params.data_file,
    ).render_all()
