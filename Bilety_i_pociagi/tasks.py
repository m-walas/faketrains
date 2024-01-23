from .models import Ticket
from django.utils import timezone
from logger import colored_logger as logger

def cancel_reservation(ticket_id):
    try:
        logger.info("Rozpoczęto anulowanie rezerwacji biletu o ID: " + str(ticket_id))
        ticket = Ticket.objects.get(id=ticket_id, status='reserved')
        # 1 minute and 58 seconds to cancel reservation
        if ticket.reservation_time + timezone.timedelta(minutes=1, seconds=58) < timezone.now():
            ticket.delete()
            logger.warning(f"Rezerwacja biletu {ticket_id} została anulowana.")
    except Ticket.DoesNotExist:
        logger.error(f"Bilet o ID {ticket_id} nie istnieje lub jego rezerwacja została już anulowana.")
