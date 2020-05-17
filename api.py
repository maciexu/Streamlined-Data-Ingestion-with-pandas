""" Get data from an API
In this exercise, you'll use requests.get() to query the Yelp Business Search API for cafes in New York City. 
requests.get() needs a URL to get data from. 
The Yelp API also needs search parameters and authorization headers passed to the params and headers keyword arguments, respectively.

You'll need to extract the data from the response with its json() method, 
and pass it to pandas's DataFrame() function to make a data frame. Note that the necessary data is under the dictionary key "businesses".
"""

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)



""" Set API parameters
Formatting parameters to get the data you need is an integral part of working with APIs. 
These parameters can be passed to the get() function's params keyword argument as a dictionary.

The Yelp API requires the location parameter be set. It also lets users supply a term to search for. 
You'll use these parameters to get data about cafes in NYC, then process the result to create a data frame.

pandas (as pd) and requests have been loaded. The API endpoint is stored in the variable api_url. 
Authorization data is stored in the dictionary headers
"""
# Create dictionary to query API for cafes in NYC
parameters = {"term": "cafe",
          	  "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())




""" Set request headers
Many APIs require users provide an API key, obtained by registering for the service. 
Keys typically are passed in the request header, rather than as parameters.

The Yelp API documentation says "To authenticate API calls with the API Key, set the Authorization HTTP header value as Bearer API_KEY."

You'll set up a dictionary to pass this information to get(), call the API for the highest-rated cafes in NYC, and parse the response.

pandas (as pd) and requests have been loaded. The API endpoint is stored as api_url, and the key is api_key. 
Parameters are in the dictionary params.
"""
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)

