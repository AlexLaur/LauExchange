import os

def load_style_sheet(script_path=None):
    """This function load the style sheet

    :param script_path: The path of the app, defaults to None
    :type script_path: str, optional
    :return: The style content
    :rtype: str
    """
    style = open(os.path.join(script_path, 'style/style.qss')).read()
    style = style.replace('@res', script_path)
    return style


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


def filter_listwidget(all_items=None, finding_item=None, text=None):
    """This function is a filter for a listwidgetitem

    :param all_items: all items in the listwidgetitem, defaults to None
    :type all_items: list, optional
    :param finding_item: all finding items with the text, defaults to None
    :type finding_item: list, optional
    :param text: the text in the lineedit, defaults to None
    :type text: str, optional
    """
    if not text:
        for item in all_items:
            item.setHidden(False)
    else:
        for item in all_items:
            item.setHidden(True)
        # If we have an item found
        if not finding_item:
            return
        for item in finding_item:
            # show only item
            item.setHidden(False)
