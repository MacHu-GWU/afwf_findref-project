# -*- coding: utf-8 -*-

from afwf_findref.workflow import wf
from afwf_findref.handlers import (
    findref,
)
from rich import print as rprint


def test():
    sf = wf._run(arg=f"{findref.handler.id} airflow aws")


if __name__ == "__main__":
    from afwf_findref.tests import run_cov_test

    run_cov_test(__file__, "afwf_findref.workflow", preview=False)
