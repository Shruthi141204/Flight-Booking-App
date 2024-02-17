import sys
import math
import tkinter as tk
from tkinter import ttk
from queue import Queue
from tkinter import *
from tkinter import Tk, Label
from PIL import ImageTk, Image

class Airport:
    def __init__(self, code, name, latitude, longitude):
        self.code = code
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class Flight:
    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost
        self.next = None

class FlightSystem:
    def __init__(self):
        self.airports = {}
        self.flights = {}

    def add_airport(self, code, name, latitude, longitude):
        airport = Airport(code, name, latitude, longitude)
        self.airports[code] = airport

    def add_flight(self, source, destination, cost):
        flight = Flight(destination, cost)
        if source in self.flights:
            current_flight = self.flights[source]
            while current_flight.next:
                current_flight = current_flight.next
            current_flight.next = flight
        else:
            self.flights[source] = flight

    def get_flights_from_airport(self, source):
        if source in self.flights:
            return self.flights[source]
        else:
            return None

    def calculate_distance(self, source_code, destination_code):
        if source_code not in self.airports or destination_code not in self.airports:
            return None

        source = self.airports[source_code]
        destination = self.airports[destination_code]
        radius = 6371  # Radius of the Earth in kilometers

        lat_diff = math.radians(destination.latitude - source.latitude)
        lon_diff = math.radians(destination.longitude - source.longitude)
        lat1 = math.radians(source.latitude)
        lat2 = math.radians(destination.latitude)

        a = math.sin(lat_diff / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = radius * c
        return distance

    def find_all_paths(self, source_code, destination_code):
        if source_code not in self.airports or destination_code not in self.airports:
            print("Invalid source or destination airport.")
            return None

        all_paths = []
        visited = set()
        queue = Queue()
        queue.put([source_code])

        while not queue.empty():
            path = queue.get()
            current_code = path[-1]

            if current_code == destination_code:
                all_paths.append(path)
            elif current_code not in visited:
                visited.add(current_code)
                current_flight = self.flights.get(current_code)
                while current_flight:
                    next_code = current_flight.destination
                    new_path = list(path)
                    new_path.append(next_code)
                    queue.put(new_path)
                    current_flight = current_flight.next

        return all_paths

    def get_distance(self, source_code, destination_code):
        return self.calculate_distance(source_code, destination_code)

class FlightBookingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flight Availability and Booking System")
        self.flight_system = FlightSystem()
        self.create_widgets()

    def create_widgets(self):
        self.flight_system.add_airport("MAA", "Chennai International Airport", 13.0827, 80.2707)                    #Chennai
        self.flight_system.add_airport("BLR", "Kempegowda International Airport", 12.9716, 77.5946)                 #Bangalore
        self.flight_system.add_airport("HYD", "Rajiv Gandhi International Airport",17.3850, 78.4867)                #Hyderabad
        self.flight_system.add_airport("DEL", "Indira Gandhi International Airport", 28.7041, 77.1025)              #Delhi
        self.flight_system.add_airport("BOM","Chhatrapati Shivaji International Airport",19.0760, 72.8777)          #Mumbai        
        self.flight_system.add_airport("ATQ","Sri Guru Ramdas Jee International Airport",31.6340,74.8723)           #Amritsar
        self.flight_system.add_airport("AMD","Sardar Vallabhai Patel International Airport",23.0225, 72.5714)       #Ahmedabad
        self.flight_system.add_airport("LKO","Chaudary Charan Singh International Airport", 26.8467, 80.9462)       #Lucknow 
        self.flight_system.add_airport("PNQ","Pune Airport", 18.5204, 73.8567)                                      #Pune
        self.flight_system.add_airport("SXR","Sheikh ul Alam Airport",34.0837,74.7973)                              #Srinagar
        self.flight_system.add_airport("IXZ","Vir Savarkar International Airport",11.6234,92.7265)                  #Port Blair
        self.flight_system.add_airport("IXR","Birsa Munda Airport",23.3441,85.3096)                                 #Ranchi
        self.flight_system.add_airport("GOI","Dobolim Airport",15.2993,74.1240)                                     #Goa
        self.flight_system.add_airport("AJL","Lengpui Airport",23.1645,92.9376)                                     #Mizoram
        self.flight_system.add_airport("AGX","Agatti Airport",10.5667,72.6417)                                      #Lakshadweep
        self.flight_system.add_airport("CCU","Netaji Subhash Chandra Bose Airport",22.5726, 88.3639)                 #Kolkata

        
        # Add flights to the flight system
        self.flight_system.add_flight("MAA", "DEL", 6938)
        self.flight_system.add_flight("MAA", "BLR", 2730)
        self.flight_system.add_flight("MAA", "HYD", 2449)
        self.flight_system.add_flight("MAA", "BOM", 3000)
        self.flight_system.add_flight("MAA", "ATQ", 7504)
        self.flight_system.add_flight("MAA", "AMD", 4705)
        self.flight_system.add_flight("MAA", "LKO", 4217)
        self.flight_system.add_flight("MAA", "PNQ", 4784)
        self.flight_system.add_flight("MAA", "SXR", 7468)
        self.flight_system.add_flight("MAA", "IXZ", 5936)
        self.flight_system.add_flight("MAA", "IXR", 3940)
        self.flight_system.add_flight("MAA", "GOI", 4084)
        self.flight_system.add_flight("MAA", "AJL", 5459)
        self.flight_system.add_flight("MAA", "AGX", 3999)
        self.flight_system.add_flight("MAA", "CCU", 3999)
           
        self.flight_system.add_flight("BLR", "DEL", 5354)
        self.flight_system.add_flight("BLR", "MAA", 2847)
        self.flight_system.add_flight("BLR", "HYD", 2468)
        self.flight_system.add_flight("BLR", "BOM", 2500)
        self.flight_system.add_flight("BLR", "ATQ", 6407)
        self.flight_system.add_flight("BLR", "AMD", 4279)
        self.flight_system.add_flight("BLR", "LKO", 3706)
        self.flight_system.add_flight("BLR", "PNQ", 2925)
        self.flight_system.add_flight("BLR", "SXR", 8368)
        self.flight_system.add_flight("BLR", "IXZ", 7415)
        self.flight_system.add_flight("BLR", "IXR", 5831)
        self.flight_system.add_flight("BLR", "GOI", 2400)
        self.flight_system.add_flight("BLR", "AJL", 3459)
        self.flight_system.add_flight("BLR", "AGX", 4599)
        self.flight_system.add_flight("BLR", "CCU", 4599)
        
        self.flight_system.add_flight("HYD", "DEL", 5257)
        self.flight_system.add_flight("HYD", "MAA", 3247)
        self.flight_system.add_flight("HYD", "BLR", 3159)
        self.flight_system.add_flight("HYD", "BOM", 3939)
        self.flight_system.add_flight("HYD", "ATQ", 6063)
        self.flight_system.add_flight("HYD", "AMD", 3999)
        self.flight_system.add_flight("HYD", "LKO", 4479)
        self.flight_system.add_flight("HYD", "PNQ", 4212)
        self.flight_system.add_flight("HYD", "SXR", 6465)
        self.flight_system.add_flight("HYD", "IXZ", 8445)
        self.flight_system.add_flight("HYD", "IXR", 4478)
        self.flight_system.add_flight("HYD", "GOI", 2749)
        self.flight_system.add_flight("HYD", "AJL", 3699)
        self.flight_system.add_flight("HYD", "AGX", 4891)
        self.flight_system.add_flight("HYD", "CCU", 4599)
        
        self.flight_system.add_flight("DEL", "HYD", 4798)
        self.flight_system.add_flight("DEL", "MAA", 5370)
        self.flight_system.add_flight("DEL", "BLR", 5236)
        self.flight_system.add_flight("DEL", "BOM", 5299)
        self.flight_system.add_flight("DEL", "ATQ", 3014)
        self.flight_system.add_flight("DEL", "AMD", 2961)
        self.flight_system.add_flight("DEL", "LKO", 3013)
        self.flight_system.add_flight("DEL", "PNQ", 4200)
        self.flight_system.add_flight("DEL", "SXR", 5271)
        self.flight_system.add_flight("DEL", "IXZ", 7438)
        self.flight_system.add_flight("DEL", "IXR", 3635)
        self.flight_system.add_flight("DEL", "GOI", 5638)
        self.flight_system.add_flight("DEL", "AJL", 6785)
        self.flight_system.add_flight("DEL", "AGX", 8200)
        self.flight_system.add_flight("DEL", "CCU", 4599)
        
        self.flight_system.add_flight("BOM", "HYD", 3224)
        self.flight_system.add_flight("BOM", "MAA", 2979)
        self.flight_system.add_flight("BOM", "BLR", 2300)
        self.flight_system.add_flight("BOM", "DEL", 4456)
        self.flight_system.add_flight("BOM", "ATQ", 5513)
        self.flight_system.add_flight("BOM", "AMD", 2320)
        self.flight_system.add_flight("BOM", "LKO", 4638)
        self.flight_system.add_flight("BOM", "PNQ", 2800)
        self.flight_system.add_flight("BOM", "SXR", 6981)
        self.flight_system.add_flight("BOM", "IXZ", 8333)
        self.flight_system.add_flight("BOM", "IXR", 6239)
        self.flight_system.add_flight("BOM", "GOI", 3399)
        self.flight_system.add_flight("BOM", "AJL", 7000)
        self.flight_system.add_flight("BOM", "AGX", 8459)
        self.flight_system.add_flight("BOM", "CCU", 4599)

        self.flight_system.add_flight("ATQ", "HYD", 3224)
        self.flight_system.add_flight("ATQ", "MAA", 2979)
        self.flight_system.add_flight("ATQ", "BLR", 2300)
        self.flight_system.add_flight("ATQ", "DEL", 4456)
        self.flight_system.add_flight("ATQ", "BOM", 5513)
        self.flight_system.add_flight("ATQ", "AMD", 2320)
        self.flight_system.add_flight("ATQ", "LKO", 4638)
        self.flight_system.add_flight("ATQ", "PNQ", 2800)
        self.flight_system.add_flight("ATQ", "SXR", 6981)
        self.flight_system.add_flight("ATQ", "IXZ", 8333)
        self.flight_system.add_flight("ATQ", "IXR", 6239)
        self.flight_system.add_flight("ATQ", "GOI", 3399)
        self.flight_system.add_flight("ATQ", "AJL", 7000)
        self.flight_system.add_flight("ATQ", "AGX", 8459)
        self.flight_system.add_flight("ATQ", "CCU", 4599)

        self.flight_system.add_flight("AMD", "HYD", 3224)
        self.flight_system.add_flight("AMD", "MAA", 2979)
        self.flight_system.add_flight("AMD", "BLR", 2300)
        self.flight_system.add_flight("AMD", "DEL", 4456)
        self.flight_system.add_flight("AMD", "ATQ", 5513)
        self.flight_system.add_flight("AMD", "BOM", 2320)
        self.flight_system.add_flight("AMD", "LKO", 4638)
        self.flight_system.add_flight("AMD", "PNQ", 2800)
        self.flight_system.add_flight("AMD", "SXR", 6981)
        self.flight_system.add_flight("AMD", "IXZ", 8333)
        self.flight_system.add_flight("AMD", "IXR", 6239)
        self.flight_system.add_flight("AMD", "GOI", 3399)
        self.flight_system.add_flight("AMD", "AJL", 7000)
        self.flight_system.add_flight("AMD", "AGX", 8459)
        self.flight_system.add_flight("AMD", "CCU", 4599)

        self.flight_system.add_flight("LKO", "HYD", 3224)
        self.flight_system.add_flight("LKO", "MAA", 2979)
        self.flight_system.add_flight("LKO", "BLR", 2300)
        self.flight_system.add_flight("LKO", "DEL", 4456)
        self.flight_system.add_flight("LKO", "ATQ", 5513)
        self.flight_system.add_flight("LKO", "AMD", 2320)
        self.flight_system.add_flight("LKO", "BOM", 4638)
        self.flight_system.add_flight("LKO", "PNQ", 2800)
        self.flight_system.add_flight("LKO", "SXR", 6981)
        self.flight_system.add_flight("LKO", "IXZ", 8333)
        self.flight_system.add_flight("LKO", "IXR", 6239)
        self.flight_system.add_flight("LKO", "GOI", 3399)
        self.flight_system.add_flight("LKO", "AJL", 7000)
        self.flight_system.add_flight("LKO", "AGX", 8459)
        self.flight_system.add_flight("LKO", "CCU", 4599)

        self.flight_system.add_flight("PNQ", "HYD", 3224)
        self.flight_system.add_flight("PNQ", "MAA", 2979)
        self.flight_system.add_flight("PNQ", "BLR", 2300)
        self.flight_system.add_flight("PNQ", "DEL", 4456)
        self.flight_system.add_flight("PNQ", "ATQ", 5513)
        self.flight_system.add_flight("PNQ", "AMD", 2320)
        self.flight_system.add_flight("PNQ", "LKO", 4638)
        self.flight_system.add_flight("PNQ", "BOM", 2800)
        self.flight_system.add_flight("PNQ", "SXR", 6981)
        self.flight_system.add_flight("PNQ", "IXZ", 8333)
        self.flight_system.add_flight("PNQ", "IXR", 6239)
        self.flight_system.add_flight("PNQ", "GOI", 3399)
        self.flight_system.add_flight("PNQ", "AJL", 7000)
        self.flight_system.add_flight("PNQ", "AGX", 8459)
        self.flight_system.add_flight("PNQ", "CCU", 4599)

        self.flight_system.add_flight("SXR", "HYD", 3224)
        self.flight_system.add_flight("SXR", "MAA", 2979)
        self.flight_system.add_flight("SXR", "BLR", 2300)
        self.flight_system.add_flight("SXR", "DEL", 4456)
        self.flight_system.add_flight("SXR", "ATQ", 5513)
        self.flight_system.add_flight("SXR", "AMD", 2320)
        self.flight_system.add_flight("SXR", "LKO", 4638)
        self.flight_system.add_flight("SXR", "PNQ", 2800)
        self.flight_system.add_flight("SXR", "BOM", 6981)
        self.flight_system.add_flight("SXR", "IXZ", 8333)
        self.flight_system.add_flight("SXR", "IXR", 6239)
        self.flight_system.add_flight("SXR", "GOI", 3399)
        self.flight_system.add_flight("SXR", "AJL", 7000)
        self.flight_system.add_flight("SXR", "AGX", 8459)
        self.flight_system.add_flight("SXR", "CCU", 4599)

        self.flight_system.add_flight("IXZ", "HYD", 3224)
        self.flight_system.add_flight("IXZ", "MAA", 2979)
        self.flight_system.add_flight("IXZ", "BLR", 2300)
        self.flight_system.add_flight("IXZ", "DEL", 4456)
        self.flight_system.add_flight("IXZ", "ATQ", 5513)
        self.flight_system.add_flight("IXZ", "AMD", 2320)
        self.flight_system.add_flight("IXZ", "LKO", 4638)
        self.flight_system.add_flight("IXZ", "PNQ", 2800)
        self.flight_system.add_flight("IXZ", "BOM", 6981)
        self.flight_system.add_flight("IXZ", "SXR", 8333)
        self.flight_system.add_flight("IXZ", "IXR", 6239)
        self.flight_system.add_flight("IXZ", "GOI", 3399)
        self.flight_system.add_flight("IXZ", "AJL", 7000)
        self.flight_system.add_flight("IXZ", "AGX", 8459)
        self.flight_system.add_flight("IXZ", "CCU", 4599)

        self.flight_system.add_flight("IXR", "HYD", 3224)
        self.flight_system.add_flight("IXR", "MAA", 2979)
        self.flight_system.add_flight("IXR", "BLR", 2300)
        self.flight_system.add_flight("IXR", "DEL", 4456)
        self.flight_system.add_flight("IXR", "ATQ", 5513)
        self.flight_system.add_flight("IXR", "AMD", 2320)
        self.flight_system.add_flight("IXR", "PNQ", 2800)
        self.flight_system.add_flight("IXR", "BOM", 6981)
        self.flight_system.add_flight("IXR", "IXZ", 8333)
        self.flight_system.add_flight("IXR", "SXR", 6239)
        self.flight_system.add_flight("IXR", "GOI", 3399)
        self.flight_system.add_flight("IXR", "AJL", 7000)
        self.flight_system.add_flight("IXR", "AGX", 8459)
        self.flight_system.add_flight("IXR", "CCU", 4599)

        self.flight_system.add_flight("GOI", "HYD", 3224)
        self.flight_system.add_flight("GOI", "MAA", 2979)
        self.flight_system.add_flight("GOI", "BLR", 2300)
        self.flight_system.add_flight("GOI", "DEL", 4456)
        self.flight_system.add_flight("GOI", "ATQ", 5513)
        self.flight_system.add_flight("GOI", "AMD", 2320)
        self.flight_system.add_flight("GOI", "LKO", 4638)
        self.flight_system.add_flight("GOI", "PNQ", 2800)
        self.flight_system.add_flight("GOI", "BOM", 6981)
        self.flight_system.add_flight("GOI", "IXZ", 8333)
        self.flight_system.add_flight("GOI", "IXR", 6239)
        self.flight_system.add_flight("GOI", "SXR", 3399)
        self.flight_system.add_flight("GOI", "AJL", 7000)
        self.flight_system.add_flight("GOI", "AGX", 8459)
        self.flight_system.add_flight("GOI", "CCU", 4599)

        self.flight_system.add_flight("AJL", "HYD", 3224)
        self.flight_system.add_flight("AJL", "MAA", 2979)
        self.flight_system.add_flight("AJL", "BLR", 2300)
        self.flight_system.add_flight("AJL", "DEL", 4456)
        self.flight_system.add_flight("AJL", "ATQ", 5513)
        self.flight_system.add_flight("AJL", "AMD", 2320)
        self.flight_system.add_flight("AJL", "LKO", 4638)
        self.flight_system.add_flight("AJL", "PNQ", 2800)
        self.flight_system.add_flight("AJL", "BOM", 6981)
        self.flight_system.add_flight("AJL", "IXZ", 8333)
        self.flight_system.add_flight("AJL", "IXR", 6239)
        self.flight_system.add_flight("AJL", "GOI", 3399)
        self.flight_system.add_flight("AJL", "SXR", 7000)
        self.flight_system.add_flight("AJL", "AGX", 8459)
        self.flight_system.add_flight("AJL", "CCU", 4599)

        self.flight_system.add_flight("AGX", "HYD", 3224)
        self.flight_system.add_flight("AGX", "MAA", 2979)
        self.flight_system.add_flight("AGX", "BLR", 2300)
        self.flight_system.add_flight("AGX", "DEL", 4456)
        self.flight_system.add_flight("AGX", "ATQ", 5513)
        self.flight_system.add_flight("AGX", "AMD", 2320)
        self.flight_system.add_flight("AGX", "LKO", 4638)
        self.flight_system.add_flight("AGX", "PNQ", 2800)
        self.flight_system.add_flight("AGX", "BOM", 6981)
        self.flight_system.add_flight("AGX", "IXZ", 8333)
        self.flight_system.add_flight("AGX", "IXR", 6239)
        self.flight_system.add_flight("AGX", "GOI", 3399)
        self.flight_system.add_flight("AGX", "AJL", 7000)
        self.flight_system.add_flight("AGX", "SXR", 8459)
        self.flight_system.add_flight("AGX", "CCU", 4599)

        self.flight_system.add_flight("CCU", "HYD", 3224)
        self.flight_system.add_flight("CCU", "MAA", 2979)
        self.flight_system.add_flight("CCU", "BLR", 2300)
        self.flight_system.add_flight("CCU", "DEL", 4456)
        self.flight_system.add_flight("CCU", "ATQ", 5513)
        self.flight_system.add_flight("CCU", "AMD", 2320)
        self.flight_system.add_flight("CCU", "LKO", 4638)
        self.flight_system.add_flight("CCU", "PNQ", 2800)
        self.flight_system.add_flight("CCU", "BOM", 6981)
        self.flight_system.add_flight("CCU", "IXZ", 8333)
        self.flight_system.add_flight("CCU", "IXR", 6239)
        self.flight_system.add_flight("CCU", "GOI", 3399)
        self.flight_system.add_flight("CCU", "AJL", 7000)
        self.flight_system.add_flight("CCU", "AGX", 8459)
        self.flight_system.add_flight("CCU", "SXR", 4599)

        
        self.source_label = ttk.Label(self.root, text="Source Airport:")
        self.source_label.grid(row=0, column=0, padx=10, pady=5)
        self.source_combo = ttk.Combobox(self.root, values=list(self.flight_system.airports.keys()))
        self.source_combo.grid(row=0, column=1, padx=10, pady=5)

        self.destination_label = ttk.Label(self.root, text="Destination Airport:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=5)
        self.destination_combo = ttk.Combobox(self.root, values=list(self.flight_system.airports.keys()))
        self.destination_combo.grid(row=1, column=1, padx=10, pady=5)

        self.root.title("Flight Booking App")
        self.root.configure(background="peachpuff")
        style = ttk.Style()
        style.configure("Color.TButton", foreground="black", background="aquamarine")

        self.search_button = ttk.Button(self.root, text="Search Flights", command=self.search_flights, style="Color.TButton")
        self.search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def search_flights(self):
        source_code = self.source_combo.get()
        destination_code = self.destination_combo.get()

        if source_code and destination_code:
            paths = self.flight_system.find_all_paths(source_code, destination_code)
            if paths:
                shortest_path = None
                shortest_distance = float('inf')
                
                for path in paths:
                    total_cost = 0
                    total_distance = 0
                    
                    for i in range(len(path) - 1):
                        source = path[i]
                        destination = path[i + 1]
                        flight = self.flight_system.get_flights_from_airport(source)
                        
                        while flight:
                            if flight.destination == destination:
                                total_cost += flight.cost
                                total_distance += self.flight_system.get_distance(source, destination)
                                break
                            flight = flight.next
                    
                    if total_distance < shortest_distance:
                        shortest_distance = total_distance
                        shortest_path = path
                
                result_text = "Available Flights:\n\n"
                
                for path in paths:
                    total_cost = 0
                    total_distance = 0
                    
                    for i in range(len(path) - 1):
                        source = path[i]
                        destination = path[i + 1]
                        flight = self.flight_system.get_flights_from_airport(source)
                        
                        while flight:
                            if flight.destination == destination:
                                total_cost += flight.cost
                                total_distance += self.flight_system.get_distance(source, destination)
                                break
                            flight = flight.next
                    
                    if path == shortest_path:
                        result_text += f"Path: {' -> '.join(path)} (Shortest distance and Least cost)\n"
                    else:
                        result_text += f"Path: {' -> '.join(path)}\n"
                        
                    result_text += f"Total Cost: {total_cost}\n"
                    result_text += f"Total Distance: {total_distance} km\n\n"
                
                self.result_label.configure(text=result_text)
            else:
                self.result_label.configure(text="No flights available between the selected airports.")
        else:
            self.result_label.configure(text="Please select source and destination airports.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FlightBookingApp()
    app.run()


