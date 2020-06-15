def get_all_list_items(list_widget):
    items = []
    for index in range(list_widget.count()):
        items.append(list_widget.item(index))
    return items


def get_all_tree_items(tree_widget):
    items = []
    root = tree_widget.invisibleRootItem()
    child_count = root.childCount()
    for row in range(child_count):
        item = root.child(row)
        items.append(item)
    return items