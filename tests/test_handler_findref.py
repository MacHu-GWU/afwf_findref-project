# -*- coding: utf-8 -*-

from afwf_findref.handlers.findref import handler
from rich import print as rprint


def test():
    sf = handler.main(dataset="airflow", query="aws")
    data = sf.to_script_filter()
    rprint(data)


if __name__ == "__main__":
    from afwf_findref.tests import run_cov_test

    run_cov_test(__file__, "afwf_findref.handlers.findref", preview=False)
