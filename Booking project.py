#movie  ticket booking
import smtplib

#function to send email confirmation
def send_gmail(name,gmail,movie,ticket_type,quantity,price):
        sender_gmail="nakkadivya951@gmail.com"
        message=f""" subject:movie ticket confirmation 
        Hello {name},
        your movie ticket booking is confirmed!
        movie:{movie}
        ticket type:{ticket_type}
        quantity:{quantity} total price:{price}
        Enjoy your movie!"""
try:
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("nakkadivya951@gmail.com","vism jqxf azjp ufxb")
    server.quit()
    print("your gmail sent succesfully")
except:
    print("error sending email")
#function to book a movie ticket
def book_ticket():
    name=input("enter your name:")
    gmail=input("enter your email:")
    movie=input("enter movie name:")
    ticket_type=input("enter ticket type(regular/premium/VIP):")
    quantity=int(input("enter number of tickets you want:"))
    prices={"Regular":150,"Premium":300,"VIP":500}
    total_price=prices.get(ticket_type,150)*quantity
    print(f"Booking confirmed: {quantity} {ticket_type} tickets for {movie} -{total_price}")
#call the send_mail function after defing it
    send_gmail(name,gmail,movie,ticket_type,quantity,total_price)
book_ticket()