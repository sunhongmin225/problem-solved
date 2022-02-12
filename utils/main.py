from itertools import combinations
from collections import deque
import argparse
from pathlib import Path

from distinctipy import distinctipy
import igraph as ig


MEMBERS = deque(["MSH","SDO","JSY","LHS","PJS"])
DEGREE = 2


def main(members=MEMBERS, degree=DEGREE, filename='random-graph'):
    fp = f'graphs/{filename}.png'
    if Path(fp).exists():
        raise FileExistsError(f'{filename}.png already exists!')

    size = len(members)
    dg = ig.Graph().K_Regular(size, degree, directed=True)
    layout = dg.layout("circle")
    dg.vs['name'] = members

    vertex_colors = distinctipy.get_colors(size, pastel_factor=0.7)
    edge_colors = [c for c, degree in zip(vertex_colors, [degree]*size) for _ in range(degree)]

    ig.plot(
        dg,
        target=fp,
        layout=layout,
        bbox=(350,350),
        vertex_color=vertex_colors,
        edge_color=edge_colors,
        vertex_label=dg.vs["name"],
        vertex_size=40
    )


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--name', type=str, default='random-graph', help='Define PNG filename')
    parser.add_argument('-d','--degree', type=int, default=2, help='Define number of reviews for each person')
    args = parser.parse_args()
    main(degree=args.degree, filename=args.name)

