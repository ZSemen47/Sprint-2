class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls):
        if cls.hours == None:
            cls.hours = (7 - cls.rest_days) * 8
            return cls(cls.name, cls.hours, cls.rest_days, cls.email)
        
    @classmethod
    def get_email(cls):
        if cls.email == None:
            cls.email = f"{cls.name}@email.com"
            return cls(cls.name, cls.hours, cls.rest_days, cls.email)
        
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary