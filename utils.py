import json

path = "candidates.json"


def load_candidates_from_json(path):
    """которая покажет всех кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    list_candidates = []
    for candidate in data:
        list_candidates.append(candidate)
    return list_candidates


def get_candidate(candidate_id):
    """которая вернет кандидата по id"""
    list_candidates = load_candidates_from_json(path)
    for data in list_candidates:
        if data['id'] == candidate_id:
            return data


def get_candidates_by_name(candidate_name):
    """которая вернет кандидатов по имени"""
    list_candidates = load_candidates_from_json(path)
    list_name_candidates = []
    for data in list_candidates:
        if candidate_name in data['name'].lower():
            list_name_candidates.append(data)

    return list_name_candidates


def get_candidates_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    list_candidates = load_candidates_from_json(path)
    list_skills = []
    for data in list_candidates:
        for skill in data['skills'].split(", "):
            if skill_name.lower() == skill.lower() and data not in list_skills:
                list_skills.append(data)

    return list_skills
