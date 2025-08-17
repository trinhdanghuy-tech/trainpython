# Global queue
q = []

# Add a customer to the queue
def add(name):
    q.append(name)

# Serve the next customer and return their name
def next():
    if len(q) > 0:
        return q.pop(0)  # Remove and return the first customer in the queue
    else:
        return "No customers in the queue."

# Show all customers currently waiting
def show():
    if len(q) > 0:
        print("Currently waiting customers:", ", ".join(q))
    else:
        print("No customers in the queue.")

# Return the number of customers currently waiting
def length():
    return len(q)

add("Alice")
add("Bob")
add("Charlie")
next()  # Serve the first customer
show()  # Show all customers