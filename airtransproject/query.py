
# список рейсов между двумя аэропортами
air_trip = Flight.objects.all().filter(departure_airport__airport_code="AAQ", arrival_airport__airport_code="AAU")


# список мест для выбранного самолета
seats = Seat.objects.all().filter(aircraft_code__aircraft_code="AB3 ")
for i in seats:
    print(i.seat_no)


# список выданных посадочных таллонов для выбранного перелета
pas = BoardingPass.objects.all().filter(flight_id__flight_id__flight_id='111111')
for val in pas:
    print(val)


#список имен пасажиров данного рейса
ticket = TicketFlight.objects.all().filter(flight_id__flight_id='111111')
for val in ticket:
    print(val.ticket_no.passenger_name)

