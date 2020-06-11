def get_all_list_items(list_widget):
    items = []
    for index in range(list_widget.count()):
        items.append(list_widget.item(index))
    return items