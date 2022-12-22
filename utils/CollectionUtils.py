class CollectionUtils:

    @staticmethod
    def sort_tuple_by_values(my_set):
        as_sorted = sorted(my_set, key=lambda l: l[1])
        return list(as_sorted)


    @staticmethod
    def sort_map_by_values(my_set):
        as_sorted = sorted(my_set, key=lambda v: my_set[v])
        return list(as_sorted)
