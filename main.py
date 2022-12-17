from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

main = Flask(__name__)
path = "candidates.json"


@main.route("/")
def page_index():
    candidates = load_candidates_from_json(path)
    return render_template("list.html", candidates=candidates)


@main.route("/candidates/<int:x>")
def profile(x):
    candidate = get_candidate(x)
    return render_template("single.html", candidate=candidate)


@main.route("/search/<candidate_name>.lower()")
def search_profile(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    len_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, len_candidates=len_candidates)


@main.route("/skill/<skill_name>")
def qq(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    len_candidates = len(candidates)
    return render_template("skill.html", candidates=candidates, skill_name=skill_name, len_candidates=len_candidates)


main.run(port=1000, debug=True)
