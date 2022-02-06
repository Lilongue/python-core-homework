def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    roles_tree = dict()
    roles_tree["categories"] = [build_category_dict(mapping, id) for id in mapping.get("categoryIdsSorted")]
    return roles_tree

def build_category_dict(mapping, category_id):
    """
    :params 
        mapping: маппинг ролей в категории
        category_id: id категории
    :return: словарь для указанной категории
    """
    if category_id not in mapping.get("categories"):
        return dict()
    category_dict = {}
    category_dict["id"] = "category-{0}".format(category_id)
    category_dict["text"] = mapping.get("categories").get(category_id).get("name")
    category_dict["items"] = [build_item_dict(mapping.get("roles"), id) for id in mapping.get("categories").get(category_id).get("roleIds")]
    return category_dict

def build_item_dict(mapping, role_id):
    """
    :params 
        mapping: маппинг ролей в категории
        role_id: id роли
    :return: словарь для указанной роли
    """
    if role_id not in mapping:
        return dict()
    role_dict = dict()
    role_dict["id"] = mapping.get(role_id).get("id")
    role_dict["text"] = mapping.get(role_id).get("name")
    return role_dict
