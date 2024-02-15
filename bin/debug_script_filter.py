# -*- coding: utf-8 -*-

import json
from automation.ops import path_bin_python, dir_workflow
from afwf_findref.handlers import (
    findref,
)
from rich import print as rprint

verbose = True
# verbose = False

handler = findref.handler
query = "boto3 s3 put object"

res = handler.run_script_command(path_bin_python, dir_workflow, query, verbose=verbose)
if res is None:
    print(f"res = {res}")
else:
    rprint(json.loads(res))
