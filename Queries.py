from DBConnectivity import conn, cursor
def add_customer():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    cursor.execute("""
        INSERT INTO Customers (FullName, Email, Phone)
        VALUES (%s, %s, %s)
    """, (name, email, phone))

    conn.commit()
    print("Customer added.")
    
def add_event():
    name = input("Event name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    org = input("Organizer ID: ")
    venue = input("Venue ID: ")
    cat = input("Category ID: ")

    cursor.execute("""
        INSERT INTO Events (EventName, EventDate, EventTime, OrganizerID, VenueID, CategoryID)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, date, time, org, venue, cat))

    conn.commit()
    print("Event added.")

def show_events():
    cursor.execute('SELECT * FROM Events')
    rows = cursor.fetchall()

    for r in rows:
        print(r)

def buy_ticket():
    event_id = input("Event ID: ")
    customer_id = input("Customer ID: ")
    ticket_type = input("Ticket Type: ")
    price = input("Price: ")
    seat = input("Seat number: ")

    cursor.execute("""
        INSERT INTO Tickets (EventID, CustomerID, TicketType, Price, SeatNumber)
        VALUES (%s, %s, %s, %s, %s)
    """, (event_id, customer_id, ticket_type, price, seat))

    conn.commit()
    print("Ticket purchased.")

def show_tickets():
    cursor.execute("""
        SELECT t.TicketID, c.FullName, e.EventName, t.Price
        FROM Tickets t
        JOIN Customers c ON t.CustomerID = c.CustomerID
        JOIN Events e ON t.EventID = e.EventID
    """)

    rows = cursor.fetchall()

    for r in rows:
        print(r)

def show_customers():
    cursor.execute("""
        SELECT * FROM Customers
    """)

    rows = cursor.fetchall()

    print("\n=== CUSTOMERS ===")

    for r in rows:
        print(r)

def show_reviews():
    cursor.execute("""
        SELECT * FROM Reviews
    """)

    rows = cursor.fetchall()

    print("\n=== REVIEWS ===")

    for r in rows:
        print(r)

def show_reviews():
    cursor.execute("""
        SELECT * FROM Reviews
    """)

    rows = cursor.fetchall()

    print("\n=== REVIEWS ===")

    for r in rows:
        print(r)

def update_event_status():
    event_id = input("Event ID: ")
    new_status = input("New Status: ")

    cursor.execute("""
        UPDATE Events
        SET Status = %s
        WHERE EventID = %s
    """, (new_status, event_id))

    conn.commit()

    print("Event updated successfully.")

def update_customer_phone():
    customer_id = input("Customer ID: ")
    new_phone = input("New phone: ")

    cursor.execute("""
        UPDATE Customers
        SET Phone = %s
        WHERE CustomerID = %s
    """, (new_phone, customer_id))

    conn.commit()

    print("Customer updated successfully.")

def delete_review():
    review_id = input("Review ID to delete: ")

    cursor.execute("""
        DELETE FROM Reviews
        WHERE ReviewID = %s
    """, (review_id,))

    conn.commit()

    print("Review deleted successfully.")

def delete_ticket():
    ticket_id = input("Ticket ID to delete: ")

    cursor.execute("""
        DELETE FROM Tickets
        WHERE TicketID = %s
    """, (ticket_id,))

    conn.commit()

    print("Ticket deleted successfully.")

def add_review():
    customer = input("Customer ID: ")
    event = input("Event ID: ")
    rating = input("Rating (1-5): ")
    comment = input("Comment: ")

    cursor.execute("""
        INSERT INTO Reviews (CustomerID, EventID, Rating, Comment)
        VALUES (%s, %s, %s, %s)
    """, (customer, event, rating, comment))

    conn.commit()
    print("Review added.")