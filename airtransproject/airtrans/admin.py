from django.contrib import admin
from .models import Booking, Airport, Ticket, Aircraft, Seat, Flight, TicketFlight, BoardingPass


# Register your models here.

admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Seat)
admin.site.register(Flight)
admin.site.register(TicketFlight)
admin.site.register(BoardingPass)
