def capital_case_filter(my_string):
    return my_string.capitalize()


class FilterModule(object):
    def filters(self):
        return {"filter3": capital_case_filter}

