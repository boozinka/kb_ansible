def upper_case_filter(my_string):
    return my_string.upper()


class FilterModule(object):
    def filters(self):
        return {"filter1": upper_case_filter}

