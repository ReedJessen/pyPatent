import requests
import json
def get_patent(patent_number):
    """Given a unique patent identifier, returns json object from PatentViews.org"""


    #prep message
    endpoint = "http://www.patentsview.org/api/patents/query"

    q_val = "{\"patent_number\":\"%s\"}" % str(patent_number)
    f_val = "[\"app_number\"," \
            "\"patent_number\"," \
            "\"patent_title\"," \
            "\"patent_date\"," \
            "\"inventor_first_name\"," \
            "\"inventor_last_name\"," \
            "\"patent_abstract\"," \
            "\"patent_num_claims\"," \
            "\"assignee_type\"," \
            "\"assignee_organization\"," \
            "\"assignee_first_name\"," \
            "\"assignee_last_name\"]"
    payload = {'q': q_val, 'f':f_val}

    r = requests.get(endpoint, params=payload)

    content = json.loads(r.text)

    return content


if __name__ == "__main__":
    get_patent(6857069)

