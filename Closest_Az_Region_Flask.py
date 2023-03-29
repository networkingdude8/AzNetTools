from flask import Flask, request
from geopy.geocoders import Nominatim
from geopy.distance import distance

app = Flask(__name__)

# Azure region map with corresponding coordinates
region_map = {
    "centralus": (41.8781, -87.6298),
    "eastus": (40.7128, -74.0060),
    "eastus2": (47.6062, -122.3321),
    "northcentralus": (44.9778, -93.2650),
    "southcentralus": (29.4241, -98.4936),
    "westus": (37.7749, -122.4194),
    "westus2": (47.6149, -122.1941),
    "Canada Central": (45.5016889, -73.567256),
    "Canada East": (45.5016889, -73.567256),
    "Brazil South": (-23.5505205, -46.6333094),
    "UK South": (51.5073509, -0.1277583),
    "UK West": (51.5073509, -0.1277583),
    "France Central": (48.8566969, 2.3514616),
    "France South": (43.296482, 5.36978),
    "Germany North": (52.5200066, 13.404954),
    "Germany West Central": (50.1109221, 8.6821267),
    "Norway East": (59.9138688, 10.7522454),
    "Norway West": (60.3912636, 5.3220544),
    "Switzerland North": (47.3768866, 8.541694),
    "Switzerland West": (46.2043907, 6.1431577),
    "Netherlands West": (52.370216, 4.895168),
    "Netherlands North": (53.2170445, 6.5503734),
    "Italy North": (45.4642035, 9.189982),
    "Italy South": (40.8517746, 14.2681244),
    "Spain Central": (40.4167047, -3.7035825),
    "Spain East": (39.4699075, -0.3762881),
    "Poland Central": (52.237049, 21.017532),
    "Poland North": (54.351209, 18.646638),
    "UAE Central": (24.466667, 54.366669),
    "UAE North": (25.0750095, 55.1887609),
    "South Africa North": (-26.1715045, 27.9699836),
    "South Africa West": (-33.9248685, 18.4240553),
    "Japan East": (35.6894875, 139.6917064),
    "Japan West": (34.6937252, 135.5022535),
    "Korea Central": (37.566535, 126.9779692),
    "Korea South": (35.907757, 127.766)
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city_name']
        country_name = request.form['country_name']
        # Use geopy to get the latitude and longitude of the city
        geolocator = Nominatim(user_agent="azure_regions")
        location = geolocator.geocode(city_name + "," + country_name)
        city_coords = (location.latitude, location.longitude)

        # Calculate the distance between the city and each Azure region
        min_distance = float("inf")
        closest_region = ""
        for region, region_coords in region_map.items():
            dist = distance(city_coords, region_coords).km
            if dist < min_distance:
                min_distance = dist
                closest_region = region

        # Output the closest Azure region to the user
        return f"The closest Azure region to {city_name} is {closest_region}."
    else:
        return '''
            <form method="post">
                <p>Enter the name of the city: <input type="text" name="city_name"></p>
                <p>Enter the name of the country: <input type="text" name="country_name"></p>
                <p><input type="submit" value="Submit"></p>
            </form>
        '''

if __name__ == '__main__':
    app.run()
