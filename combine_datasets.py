""" append, merge """
""" Append data frames
In this exercise, you’ll practice appending records by creating a dataset of the 100 highest-rated cafes in New York City according to Yelp.

APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. 
The Yelp Business Search API limits the results returned in a call to 50 records. 
However, the offset parameter lets a user retrieve results starting after a specified number. 
By modifying the offset, we can get results 1-50 in one call and 51-100 in another. Then, we can append the data frames.

pandas (as pd), requests, and json_normalize() have been imported. The 50 top-rated cafes are already in a data frame, top_50_cafes.
"""

# Add an offset parameter to get cafes 51-100
# If using an offset of 0 gets results 1-50, what offset will get results starting at 51?
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)




# Example 2
# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on='location_zip_code', right_on='zipcode')


# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on='puma')

# View the data
print(cafes_with_pop.head())



