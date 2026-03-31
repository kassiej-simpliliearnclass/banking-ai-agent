from banking_ai_agent.utils import generate_ticket_id
from banking_ai_agent.database import insert_ticket

def handle_positive_feedback(customer_name="Customer"):
    return f"Thank you for your kind words, {customer_name}! We're delighted to assist you."

def handle_negative_feedback(message, customer_name="Customer"):
    ticket_id = generate_ticket_id()

    insert_ticket(ticket_id, customer_name, message)

    return f"We apologize for the inconvenience. A new ticket #{ticket_id} has been generated, and our team will follow up shortly."
