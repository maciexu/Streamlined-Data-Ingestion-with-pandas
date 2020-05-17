""" Correctly modeling datetimes is easy when they are in a standard format -- 
we can use the parse_dates argument to tell read_excel() to read columns as datetime data.
"""
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())


"""
the survey data has been split so that dates are in one column, Part2StartDate, and times are in another, Part2StartTime. 
"""
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", 
                                "Part2StartTime"]}

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())


""" Parse non-standard date formats --->>> pd.to_datetime() to convert strings to dates after import.
https://strftime.org/
"""




