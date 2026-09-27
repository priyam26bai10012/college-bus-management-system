from file_manager import load_data, save_data, get_next_id
from validators import required_text, read_id, find_by_id


class RouteManager:
    filename = "routes.json"

    def __init__(self):
        self.routes = load_data(self.filename)

    def save(self):
        save_data(self.filename, self.routes)

    def add_route(self):
        print("\nAdd Route")
        name = required_text("Route name: ")
        stops_text = required_text("Stops (separate with commas): ")
        stops = [stop.strip() for stop in stops_text.split(",") if stop.strip()]

        if any(r["name"].lower() == name.lower() for r in self.routes):
            print("A route with this name already exists.")
            return

        route = {
            "id": get_next_id(self.routes),
            "name": name,
            "stops": stops
        }
        self.routes.append(route)
        self.save()
        print("Route added successfully.")

    def view_routes(self):
        if not self.routes:
            print("No routes found.")
            return
        for r in self.routes:
            print(f'\nID: {r["id"]}')
            print(f'Route: {r["name"]}')
            print("Stops:", " -> ".join(r["stops"]))

    def update_route(self):
        route_id = read_id("Enter route ID: ")
        route = find_by_id(self.routes, route_id)
        if not route:
            print("Route not found.")
            return

        name = input(f'Route name [{route["name"]}]: ').strip()
        stops_text = input("New stops (comma separated, blank to keep): ").strip()

        if name:
            route["name"] = name
        if stops_text:
            route["stops"] = [s.strip() for s in stops_text.split(",") if s.strip()]

        self.save()
        print("Route updated successfully.")

    def remove_route(self):
        route_id = read_id("Enter route ID: ")
        route = find_by_id(self.routes, route_id)
        if not route:
            print("Route not found.")
            return
        self.routes.remove(route)
        self.save()
        print("Route removed successfully.")
