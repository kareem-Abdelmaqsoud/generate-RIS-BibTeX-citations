#!/usr/bin/env python
"""Command line module"""
import argparse
from s23oa import Works

parser = argparse.ArgumentParser()

parser.add_argument(
    "-reftype",
    help="Specify reference format needed by typing: 'bibtex' or 'ris'"
)
parser.add_argument("doi", help="The DOI of the paper")

args = parser.parse_args()
doi = args.doi
work = Works(doi)

def main():
    if args.reftype == "bibtex":
        print(work.bibtex)
    elif args.reftype == "ris":
        print(work.ris)
    else:
        raise RuntimeError(
            "The citation format requested does not exist.")
    