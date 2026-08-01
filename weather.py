from tkinter import *
from tkinter import ttk
import requests


country_data = {
    "India": {
        "Uttar Pradesh": [
            "Lucknow", "Varanasi", "Kanpur", "Agra", "Prayagraj", "Ghaziabad", "Noida",
            "Meerut", "Bareilly", "Moradabad", "Saharanpur", "Aligarh", "Jhansi",
            "Gorakhpur", "Muzaffarnagar", "Mathura", "Shahjahanpur", "Rampur", "Firozabad",
            "Faizabad (Ayodhya)", "Etawah", "Fatehpur", "Hapur", "Raebareli", "Sultanpur",
            "Bijnor", "Ballia", "Barabanki", "Jaunpur", "Budaun", "Azamgarh", "Ghazipur",
            "Deoria", "Ambedkar Nagar", "Amroha", "Hathras", "Unnao"
        ],
        "Chhattisgarh": ["Raipur", "Bilaspur", "Korba", "Durg", "Jagdalpur"],
        "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar"],
        "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Panipat", "Ambala"],
        "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Mandi", "Solan"],
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Deoghar"],
        "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi"],
        "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Alappuzha"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "Manipur": ["Imphal", "Churachandpur", "Thoubal", "Bishnupur", "Ukhrul"],
        "Meghalaya": ["Shillong", "Tura", "Cherrapunjee", "Jowai", "Baghmara"],
        "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip", "Kolasib"],
        "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Wokha", "Zunheboto"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Berhampur"],
        "Punjab": ["Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda"],
        "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur", "Kota", "Ajmer"],
        "Sikkim": ["Gangtok", "Namchi", "Pelling", "Gyalshing", "Mangan"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
        "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam"],
        "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailashahar", "Belonia"],
        "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Rishikesh", "Haldwani"],
        "West Bengal": ["Kolkata", "Darjeeling", "Siliguri", "Asansol", "Durgapur"],
        "Andaman and Nicobar Islands": ["Port Blair", "Car Nicobar", "Diglipur", "Havelock Island", "Campbell Bay"],
        "Chandigarh": ["Chandigarh"],
        "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Silvassa", "Amli"],
        "Lakshadweep": ["Kavaratti", "Agatti", "Amini", "Androth", "Minicoy"],
        "Delhi": ["New Delhi"],
        "Puducherry": ["Pondicherry", "Karaikal", "Mahe", "Yanam"]
    },
    "USA": {
        "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "Fresno"],
        "Texas": ["Houston", "Dallas", "Austin", "San Antonio", "El Paso"],
        "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee"],
        "New York": ["New York City", "Buffalo", "Rochester", "Albany", "Syracuse"]
    },
    "UK": {
        "England": ["London", "Manchester", "Liverpool", "Birmingham", "Bristol"],
        "Scotland": ["Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Inverness"],
        "Wales": ["Cardiff", "Swansea", "Newport", "Bangor", "Wrexham"],
        "Northern Ireland": ["Belfast", "Derry", "Lisburn", "Newry", "Armagh"]
    },
    "China": {
        "Beijing Municipality": ["Beijing"],
        "Shanghai Municipality": ["Shanghai"],
        "Sichuan": ["Chengdu", "Mianyang", "Deyang", "Luzhou", "Yibin"],
        "Guangdong": ["Guangzhou", "Shenzhen", "Dongguan", "Foshan", "Zhuhai"]
    },
    "Nepal": {
        "Bagmati Province": ["Kathmandu", "Lalitpur", "Bhaktapur", "Hetauda", "Bidur"],
        "Province 1": ["Biratnagar", "Dharan", "Itahari", "Dhankuta", "Kakarvitta"],
        "Province 2": ["Janakpur", "Birgunj", "Rajbiraj", "Gaur", "Siraha"]
    }
}


def update_states(event):
    selected_country = country_name.get()
    if selected_country in country_data:
        state_dropdown["values"] = list(country_data[selected_country].keys())
        state_dropdown.set("Select State")
        city_dropdown.set("Select City")
        city_dropdown["values"] = []
    else:
        state_dropdown["values"] = []
        state_dropdown.set("No states available")
        city_dropdown.set("No cities available")
        city_dropdown["values"] = []


def update_cities(event):
    selected_country = country_name.get()
    selected_state = state_name.get()
    if selected_country in country_data and selected_state in country_data[selected_country]:
        city_dropdown["values"] = country_data[selected_country][selected_state]
        city_dropdown.set("Select City")
    else:
        city_dropdown["values"] = []
        city_dropdown.set("No cities available")


def data_get():
    city = city_name.get()
    if city == "Select City" or not city:
        weather_label.config(text="Please select a valid city!", fg="red")
        return

    api_key = "a6d430fa25356d057a1a6c4d227bf984"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url).json()
        if data.get("cod") != 200:
            weather_label.config(text="City not found! Please try again.", fg="red")
            return

        
        weather_label.config(text=f"Weather in {city}:", fg="black")
        climate_label.config(text=f"Climate: {data['weather'][0]['main']}")
        description_label.config(text=f"Description: {data['weather'][0]['description']}")
        temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
        temp_min_label.config(text=f"Temp Min: {data['main']['temp_min']}°C")
        temp_max_label.config(text=f"Temp Max: {data['main']['temp_max']}°C")
        pressure_label.config(text=f"Pressure: {data['main']['pressure']} hPa")
    except:
        weather_label.config(text="Error fetching data!", fg="red")


win = Tk()
win.title("Sunstorm Weather App")
win.geometry("500x750")
win.config(bg="sky blue")


Label(win, text="Sunstorm Weather App", font=("Times New Roman", 30, "bold"), bg="black", fg="white").place(relx=0.5, y=50, anchor=CENTER)


country_name = StringVar()
country_dropdown = ttk.Combobox(win, values=list(country_data.keys()), font=("Times New Roman", 15), textvariable=country_name)
country_dropdown.set("Select Country")
country_dropdown.bind("<<ComboboxSelected>>", update_states)
country_dropdown.place(relx=0.5, y=120, anchor=CENTER, height=50, width=300)

state_name = StringVar()
state_dropdown = ttk.Combobox(win, font=("Times New Roman", 15), textvariable=state_name)
state_dropdown.set("Select State")
state_dropdown.bind("<<ComboboxSelected>>", update_cities)
state_dropdown.place(relx=0.5, y=190, anchor=CENTER, height=50, width=300)

city_name = StringVar()
city_dropdown = ttk.Combobox(win, font=("Times New Roman", 15), textvariable=city_name)
city_dropdown.set("Select City")
city_dropdown.place(relx=0.5, y=260, anchor=CENTER, height=50, width=300)
Button(win, text="Fetch Weather", font=("Times New Roman", 15, "bold"), command=data_get).place(relx=0.5, y=330, anchor=CENTER, height=50, width=150)


weather_label = Label(win, text="Weather Details:", font=("Times New Roman", 20, "bold"), bg="sky blue")
weather_label.place(relx=0.5, y=400, anchor=CENTER)
climate_label = Label(win, text="Climate: ", font=("Times New Roman", 15), bg="sky blue")
climate_label.place(relx=0.5, y=450, anchor=CENTER)
description_label = Label(win, text="Description: ", font=("Times New Roman", 15), bg="sky blue")
description_label.place(relx=0.5, y=490, anchor=CENTER)
temp_label = Label(win, text="Temperature: ", font=("Times New Roman", 15), bg="sky blue")
temp_label.place(relx=0.5, y=530, anchor=CENTER)
temp_min_label = Label(win, text="Temp Min: ", font=("Times New Roman", 15), bg="sky blue")
temp_min_label.place(relx=0.5, y=570, anchor=CENTER)
temp_max_label = Label(win, text="Temp Max: ", font=("Times New Roman", 15), bg="sky blue")
temp_max_label.place(relx=0.5, y=610, anchor=CENTER)
pressure_label = Label(win, text="Pressure: ", font=("Times New Roman", 15), bg="sky blue")
pressure_label.place(relx=0.5, y=650, anchor=CENTER)


win.mainloop()