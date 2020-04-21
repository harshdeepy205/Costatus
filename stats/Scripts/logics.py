class Calculations:

    def __init__(self,content):
       self.content = content


    def s_no(self):
        self.s_no = self.content['s_no']
        return self.s_no

    def index(self,content):
        self.index=[*range(0, len(self.s_no))]
        return self.index


    def state_ut(self):
        self.state_ut = self.content['States_UT']
        return self.state_ut

    def confirmed(self):
        self.confirmed = self.content['Confirmed']
        return self.confirmed

    def recovered(self):
        self.recovered = self.content['Recovered']
        return self.recovered

    def deceased(self):
        self.deceased = self.content['Deceased']
        return self.deceased

    def total_confirmed(self):
        self.total_confirmed = sum(self.content['Confirmed'])
        return self.total_confirmed

    def total_recovered(self):
        self.total_recovered =sum(self.content['Recovered'])
        return self.total_recovered

    def total_death(self):
        self.total_death = sum(self.content['Deceased'])
        return self.total_death

    def total_active(self):
        self.total_active = sum(self.confirmed) - (sum(self.recovered)+sum(self.deceased))
        return self.total_active



