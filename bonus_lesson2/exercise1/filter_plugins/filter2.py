def lower_case_filter(my_string):
    return my_string.lower()


class FilterModule(object):
    def filters(self):
        return {"filter2": lower_case_filter}

