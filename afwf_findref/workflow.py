# -*- coding: utf-8 -*-

import afwf

from .handlers import (
    findref,
)

wf = afwf.Workflow()
wf.register(findref.handler)
