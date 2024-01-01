# -*- coding: utf-8 -*-

import uuid
from afwf_findref.handlers.write_file import handler, path_file


def test():
    content = uuid.uuid4().hex
    sf = handler.handler(content)
    assert len(sf.items) == 1
    assert content in sf.items[0].title


if __name__ == "__main__":
    from afwf_findref.tests import run_cov_test

    run_cov_test(__file__, "afwf_findref.handlers.write_file", preview=False)
