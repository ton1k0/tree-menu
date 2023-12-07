

def build_menu_tree(items, parent=None):
    menu_tree = []
    for item in items:
        if item.parent == parent:
            children = build_menu_tree(items, item)
            menu_tree.append((item, children))
    return menu_tree
