def expand_list(nested_list):
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            for sub_item in expand_list(item):
                print ('sub_item:' + str(sub_item))
                yield sub_item
        else:
            print ('item:' + str(item))
            yield item
