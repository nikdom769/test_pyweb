from django.db import models

# Create your models here.


class Booking(models.Model):

    book_ref = models.CharField(max_length=100, primary_key=True)
    book_date = models.DateField(auto_now=True)
    total_amount = models.FloatField()

    def __str__(self):
        return f"{self.book_date}, {self.total_amount}"


class Ticket(models.Model):

    ticket_no = models.AutoField(primary_key=True)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=100,)
    contact_data = models.CharField(max_length=100,)
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger_id}, {self.passenger_name}, {self.contact_data}"


class Airport(models.Model):

    airport_code = models.CharField(max_length=5, primary_key=True)
    airport_name = models.CharField(max_length=10,)
    city = models.CharField(max_length=100,)
    coordinates = models.CharField(max_length=100,)
    timezone = models.IntegerField()

    def __str__(self):
        return f"{self.airport_name}, {self.city}"


class Aircraft(models.Model):

    aircraft_code = models.IntegerField(primary_key=True)
    model_aircraft = models.CharField(max_length=100,)
    range_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.aircraft_code}, {self.model_aircraft}, {self.range_seats}"


class Seat(models.Model):

    seat_no = models.CharField(max_length=100,)
    fare_conditions = models.CharField(max_length=100,)  # класс места
    aircraft_code = models.ForeignKey('Aircraft', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['seat_no', 'aircraft_code'], ]

    def __str__(self):
        return f"{self.seat_no}, {self.fare_conditions}"

"""
class Flight(models.Model):

    flight_id = models.IntegerField(primary_key=True)
    flight_no = models.CharField(max_length=100,)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey('Airport', related_name='departure_airport', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airport', related_name='arrival_airport', on_delete=models.CASCADE)
    status = models.CharField(max_length=100,)
    actual_departure = models.CharField(max_length=100,)
    actual_arrival = models.CharField(max_length=100,)
    aircraft_code = models.ForeignKey('Aircraft', related_name='aircraft_code', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight_id}, {self.scheduled_departure}, {self.scheduled_arrival},{self.departure_airport},\
         {self.arrival_airport},{self.status}"


class TicketFlight(models.Model):

    fare_conditions = models.CharField(max_length=10,)  # тариф
    amount = models.PositiveIntegerField()
    ticket_no = models.ForeignKey('Tickets', related_name='ticket_no', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', related_name='flight_id', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return f"{self.fare_conditions}, {self.amount}"


class BoardingPass(models.Model):

    boarding_no = models.PositiveIntegerField()
    seat_no = models.CharField(max_length=5)
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return f"{self.boarding_no}, {self.seat_no}"
"""
