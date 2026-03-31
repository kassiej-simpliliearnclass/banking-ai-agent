import re
from banking_ai_agent.database import get_ticket_status

def handle_query(message):
    match = re.search(r"\b\d{6}\b", message)

    if not match:
        return "Please provide a valid 6-digit ticket number."

    ticket_id = match.group()
    status = get_ticket_status(ticket_id)

    if status:
        return f"Your ticket #{ticket_id} is currently marked as: {status}."
    else:
        return f"Sorry, I could not find any ticket with number #{ticket_id}."
