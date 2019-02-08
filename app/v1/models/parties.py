parties = []

class PoliticalParty:

    def save_party(self, party):
        parties.append(party)
        return ({
            "id":party['id'],
            "name":party['name']
        })

    def get_party(self,id):
        for party in parties:
            if party['id'] == id
            return party
        return {}