"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wages):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    pass
    return list(wages)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    pass
    a, b ,*leftover=each_wagons_id
    corrected_wagon=[1]
    for wagon in missing_wagons:
        if wagon!=1:
            corrected_wagon.append(wagon)
    for wagon in leftover:
        if wagon!=1:
            corrected_wagon.append(wagon)
    corrected_wagon.extend([a,b])
    return corrected_wagon


def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    pass
    new_stops = {
        "stops": []
    }
    for destination in stops.values():
        new_stops["stops"].append(destination)
    new_routes={**route,**new_stops}
    return new_routes


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    pass
    full_route={**route,**more_route_information}
    return full_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    pass
    return [list(row) for row in zip(*wagons_rows)]
