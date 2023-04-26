"""A test for the Bibtex entry output"""

from s23oa import Works


REF_BIBTEX = """@journal-article{Kitchin2015,
    author = {John R. Kitchin},
    doi = {https://doi.org/10.1021/acscatal.5b00538},
    journal = {ACS Catalysis},
    pages = {3894-3899},
    title = {Examples of Effective Data Sharing in Scientific Publishing},
    volume = {5},
    year = {2015}
}
"""


def test_bibtex():
    """Testing function for the bibtex entry"""
    works_object = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_BIBTEX == works_object.bibtex()
