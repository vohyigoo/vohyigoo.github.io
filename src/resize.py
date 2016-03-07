import argparse

import PIL
from PIL import Image


def resize(input_file, output_file, hsize, vsize=None):
    img = Image.open(input_file)
    if vsize is None:
        vsize = int(hsize * img.size[1] / img.size[0])
    img = img.resize((hsize, vsize), PIL.Image.ANTIALIAS)
    img.save(output_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input-file', dest='input_file', action='store', type=str,
        help='input file', required=True
    )
    parser.add_argument(
        '-o', '--output-file', dest='output_file', action='store', type=str,
        help='output file', required=True
    )
    parser.add_argument(
        '-x', '--hsize', dest='hsize', action='store', type=int,
        help='output file', required=True
    )
    parser.add_argument(
        '-y', '--vsize', dest='vsize', action='store', type=int,
        help='output file', required=False, default=None
    )
    params, other_params = parser.parse_known_args()
    resize(params.input_file, params.output_file, params.hsize, params.vsize)
