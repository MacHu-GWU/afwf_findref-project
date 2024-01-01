# -*- coding: utf-8 -*-

import pytest
from afwf_findref.handlers.error import handler


def test():
    with pytest.raises(Exception):
        handler.main()


if __name__ == "__main__":
    from afwf_findref.tests import run_cov_test

    run_cov_test(__file__, "afwf_findref.handlers.error", preview=False)
