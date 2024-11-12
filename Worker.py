class Worker:
    def __init__(self, company, position):
        self.company = company
        self.position = position
    def get_info(self):
        return f"Company: {self.company}, Position: {self.position}"