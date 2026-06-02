"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    pass
    seat_alphabets=["A","B","C","D"]
    for num in range(number):
        num=num%4
        yield seat_alphabets[num%4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    pass
    seat_alphabets=["A","B","C","D"]
    for num in range(1,number+1):
        if num%4==0:
            seat_number=str(int(num/4) if num<=48 else int(num/4 +1))
        else:
            seat_number=str(int(num/4+1) if num<=48 else int(num/4 +2))
        yield seat_number+seat_alphabets[(num-1)%4]


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    pass
    passengers_allotment={}
    seat_allotment=generate_seats(len(passengers))
    for passenger in passengers:
        passengers_allotment[passenger]=next(seat_allotment)
    return passengers_allotment


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    pass
    
    for seat in seat_numbers:
        zero=""
        zeros_times=12-len(flight_id)-len(seat)
        for time in range(zeros_times):
            zero+="0"
        yield seat+flight_id+zero
