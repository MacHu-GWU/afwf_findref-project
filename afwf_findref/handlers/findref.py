# -*- coding: utf-8 -*-

"""
"""

import attrs
import afwf.api as afwf
from findref.models import (
    create_sayt_dataset,
)
from findref.ui import (
    search,
    preprocess_query,
)

from ..paths import dir_cache, dir_index


@attrs.define
class Handler(afwf.Handler):
    def main(self, dataset: str, query: str) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()

        ds = create_sayt_dataset(dataset, dir_index, dir_cache)
        new_query = preprocess_query(query)

        url_item_list = search(
            dataset=dataset,
            ds=ds,
            query=new_query,
            limit=20,
        )
        for url_item in url_item_list:
            item = afwf.Item(
                uid=url_item.uid,
                title=url_item.title,
                subtitle=url_item.subtitle,
                autocomplete=url_item.autocomplete,
                arg=url_item.arg,
            ).open_url(url_item.arg)
            sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        dataset, search_query = query.split(" ", 1)
        return dict(
            dataset=dataset,
            query=search_query,
        )


handler = Handler(id="findref")
