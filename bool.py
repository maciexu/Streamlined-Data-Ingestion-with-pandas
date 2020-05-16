# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())


# Set dtype to load appropriate column(s) as Boolean data
# dtype takes a dictionary, where keys are column names as strings and values are the data types they should be.
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())


""" Set custom true/false values --->>> true_values and false_values arguments. """
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values=["Yes"],
                              false_values=["No"])

# View the data
print(survey_subset.head())

