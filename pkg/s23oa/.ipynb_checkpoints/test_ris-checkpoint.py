"""A test for the RIS entry output"""

from s23oa import Works


REF_RIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -"""


def test_ris():
    """Testing the output of a works class"""
    works_object = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_RIS == works_object.ris
