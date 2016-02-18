import Populators

class Patent(object):
    """The baseline patent object, containing parameters common to all patents"""

    def __init__(self):

        #unique ids
        self.app_number = None
        self.pub_number = None
        self.grant_number = None

        #classifications
        self.app_type = None


        #relationships
        self.inventors = None
        self.original_assignees = None
        self.current_assignees = None
        self.prior_assignees = None
        self.joint_ownership = None

        #dates
        self.app_date = None
        self.pub_date = None
        self.grant_date = None

        #text fields
        self.title = None
        self.abstract = None
        self.claims = None
        self.specification = None

        #meta
        self.num_of_claims = None
        self.num_of_citations = None

    def populate(self):
        data = Populators.get_patent(self.grant_number)

        if data['total_patent_count'] != 1:
            print("Error: Unique Identifier is Ambiguous")
        else:
            self.app_number = data['patents'][0]['applications'][0]['app_number']
            self.title = data['patents'][0]['patent_title']
            self.grant_date = data['patents'][0]['patent_date']
            self.abstract = data['patents'][0]['patent_abstract']
            self.num_of_claims = data['patents'][0]['patent_num_claims']

            self.inventors = [{'last_name' : i['inventor_last_name'], 'first_name': i['inventor_first_name']}
                              for i in data['patents'][0]['inventors']]

            self.current_assignees = []
            for i in data['patents'][0]['assignees']:
                if i['assignee_type'] in [4,5,14,15]:
                    self.current_assignees.append({'last_name' : i['assignee_last_name'],
                                                   'first_name': i['assignee_first_name']})
                else:
                    self.current_assignees.append(i['assignee_organization'])


