from django.db import models

# Create your models here.


class Booking(models.Model):

    book_ref = models.CharField(max_length=6, primary_key=True) # номер бронирования
    book_date = models.DateField(auto_now=True)
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.book_ref}, {self.book_date}, {self.total_amount}"


class Ticket(models.Model):

    ticket_no = models.CharField(max_length=13, primary_key=True)
    passenger_id = models.CharField(max_length=20,)
    passenger_name = models.TextField(max_length=100,)
    contact_data = models.CharField(max_length=100,)
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger_id}, {self.passenger_name}, {self.contact_data}"


class Airport(models.Model):
    
    TIMEZONE = [('ACST ', 'UTC+9:30'), ('AEST ', 'UTC+10'), ('AKT ', 'UTC−9'),
                ('ART ', 'UTC-3'), ('AST ', 'UTC-4'), ('AWST ', 'UTC+8'),
                ('BDT ', 'UTC+6'), ('BTT ', 'UTC+6'), ('CAT ', 'UTC+2'), ('CET ', 'UTC+1'),
                ('CST ', 'UTC−6'), ('CXT ', 'UTC+7'), ('ChT ', 'UTC−4'), ('EAT ', 'UTC+3'),
                ('EET ', 'UTC+2'), ('EST ', 'UTC−5'), ('FET ', 'UTC+3'), ('GALT ', 'UTC+6'),
                ('GMT ', 'UTC'), ('HAST ', 'UTC−10'), ('HKT ', 'UTC+8'), ('IRST ', 'UTC+3:30'),
                ('IST ', 'UTC+2'), ('IST ', 'UTC+5:30'), ('JST ', 'UTC+9'), ('MT ', 'UTC−7'),
                ('MSK ', 'UTC+3'), ('MST ', 'UTC+6:30'), ('NFT ', 'UTC+11'), ('NST ', 'UTC-3:30'),
                ('PET ', 'UTC-5'), ('PHT ', 'UTC+8'), ('PKT ', 'UTC+5'), ('PMST ', 'UTC-3'),
                ('PST ', 'UTC-8'), ('SLT ', 'UTC+5:30'), ('SST ', 'UTC+8'), ('ST ', 'UTC−11'),
                ('THA ', 'UTC+7'), ('UTC ', 'UTC'), ('WAT ', 'UTC+1'), ('WET ', 'UTC')]

    airport_code = models.CharField(max_length=5, primary_key=True) # код IATA 
    airport_name = models.TextField()
    city = models.TextField()
    coordinates = models.CharField(max_length=30, null=True) # координаты
    timezone = models.CharField(max_length=5, choices=TIMEZONE, default='UTC')

    def __str__(self):
        return f"{self.airport_code}, {self.city}, {self.timezone}"


class Aircraft(models.Model):

    aircraft_code = models.CharField(max_length=3, primary_key=True) # IATA
    model_aircraft = models.CharField(max_length=100,)
    distance = models.PositiveIntegerField(default=1000) # дальность перелета

    def __str__(self):
        return f"{self.aircraft_code}, {self.model_aircraft}, {self.distance}"


class Seat(models.Model):

    STATUS_FARE = [('ECON', 'Economy'), ('COMF', 'Comfort'), ('BUSI', 'Business')]

    seat_no = models.CharField(max_length=100,)
    fare_conditions = models.CharField(max_length=10, choices=STATUS_FARE, default='Economy')  # класс места
    aircraft_code = models.ForeignKey('Aircraft', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('seat_no', 'aircraft_code'), )

    def __str__(self):
        return f"{self.aircraft_code}, {self.seat_no}, {self.fare_conditions}"


class Flight(models.Model):

    STATUS_TRIP = [('SCHED','Scheduled'),
                   ('TIME', 'On Time'),
                   ('DELA', 'Delayed'),
                   ('DEPAR', 'Departed'),
                   ('ARR', 'Arrived'),
                   ('CANC', 'Cancelled'),
                   ]

    flight_id = models.CharField(max_length=100, primary_key=True)
    flight_no = models.CharField(max_length=10,)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey('Airport', related_name='departure', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airport', related_name='arrival', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_TRIP, default='Scheduled')
    actual_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField()
    aircraft_code = models.ForeignKey('Aircraft', on_delete=models.CASCADE)

    def check_time_departure_arrival(self):
        if scheduled_departure > scheduled_arrival:
            raise ValueError("Scheduled_departure must be < scheduled_arrival")

    class Meta:
        unique_together = (('flight_no', 'scheduled_departure'))

    def __str__(self):
        return f"{self.flight_id}, {self.scheduled_departure}, {self.scheduled_arrival},{self.departure_airport},\
         {self.arrival_airport},{self.status}"


class TicketFlight(models.Model):

    STATUS_FARE = [('ECON', 'Economy'), ('COMF', 'Comfort'), ('BUSI', 'Business')]

    fare_conditions = models.CharField(max_length=10, choices=STATUS_FARE, default='Economy')  # класс места
    amount = models.FloatField()
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return f"{self.fare_conditions}, {self.amount}"


class BoardingPass(models.Model):

    boarding_no = models.PositiveIntegerField()
    seat_no = models.CharField(max_length=5)
    #ticket_no = models.PositiveIntegerField() 
    #flight_id = models.PositiveIntegerField()
    ticket_no = models.ForeignKey('TicketFlight',related_name='idTicket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('TicketFlight', related_name='idFlight', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'), ('flight_id', 'seat_no'))

    def __str__(self):
        return f"{self.boarding_no}, {self.seat_no}"

