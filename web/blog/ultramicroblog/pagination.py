from rest_framework.pagination import PageNumberPagination
from rest_framework.compat import OrderedDict
from rest_framework.response import Response

class PageNumberDetailedPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        #import pdb 
        #pdb.set_trace()

        has_next = self.page.has_next()
        has_prev = self.page.has_previous()
        next_page_number = previous_page_number = self.page.number

        if has_next: 
            next_page_number = self.page.next_page_number()
        if has_prev: 
            previous_page_number = self.page.previous_page_number()

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('has_next', has_next),
            ('has_prev', has_prev),
            ('next_page_number', next_page_number),
            ('previous_page_number', previous_page_number),
            ('results', data)
        ]))
