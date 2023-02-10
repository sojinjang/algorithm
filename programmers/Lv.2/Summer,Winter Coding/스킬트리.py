def check_possibility(skill, skill_tree):
    skill_order = list(skill)
    skill_tree_list = list(skill_tree)

    if skill_order[0] not in skill_tree_list:
        if set(skill_order) & set(skill_tree_list) == set():
            return True
        return False

    for (idx, target_skill) in enumerate(skill_order):
        if idx == 0: continue
        if target_skill not in skill_tree_list: continue
        target_skill_location = skill_tree_list.index(target_skill)
        if set(skill_tree_list[:target_skill_location]) & set(skill_order[:idx]) != set(skill_order[:idx]):
            return False
    return True


def solution(skill, skill_trees):
    is_possible_list = []
    for skill_tree in skill_trees:
        is_possible_list.append(check_possibility(skill, skill_tree))

    return is_possible_list.count(True)
