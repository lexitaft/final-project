import streamlit as st
import pandas as pd

#Heading of the Coaster Facts
st.markdown("<h1 style='color: #FF69B4; text-align: center;'> Roller Coaster Fun Facts </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #FF69B4; text-align: center;'>Use the widgets below to learn more about the Roller Coasters in the U.S.A.</h2>", unsafe_allow_html=True)

#Radio Widget
st.markdown("<h4 style='color: #1E90FF; text-align: left;'>Select a category to learn a FUN fact about roller coasters</h4>", unsafe_allow_html=True)
label = st.radio(" ",('Top Speed', 'Longest Length', 'Highest Drop'))

#Create the IF statements to find the Top speed, longest length, and the highest drop
if label == 'Top Speed':
    coasters = pd.read_csv('RollerCoasters-Geo.csv')
                        #Create an empty dictionary to store coaster names and their top speeds
    coaster_top_speeds = {}
                        #Loop through each row of the DataFrame and add the coaster name and its top speed to the dictionary
    for index, row in coasters.iterrows():
        name = row['Coaster']
        location = row['Park']
        top_speed = row['Top_Speed']
        if not pd.isna(top_speed):  # ignore rows where 'Top Speed (mph)' is NaN
            coaster_top_speeds[name] = top_speed
                        #Find the name and location of the coaster with the highest top speed
    max_speed_coaster = max(coaster_top_speeds, key=coaster_top_speeds.get)
    max_speed_location = coasters.loc[coasters['Coaster'] == max_speed_coaster, 'Park'].iloc[0]
    st.write(f"The coaster with the highest top speed is '{max_speed_coaster}' at '{max_speed_location}' with a top speed of {coaster_top_speeds[max_speed_coaster]} mph.")
    thrill = "maxresdefault.jpg"
    st.image(thrill, use_column_width=True)


if label == 'Longest Length':
    coasters = pd.read_csv('RollerCoasters-Geo.csv')
    coaster_lengths = {} #define the dictionary
    #Loop through each row of the DataFrame and add the coaster name and its length to the dictionary
    for index, row in coasters.iterrows():
        name = row['Coaster']
        location = row['Park']
        length = row['Length']
        if not pd.isna(length):  # ignore rows where 'Length (feet)' is NaN
            coaster_lengths[name] = length
    #Find the name and location of the coaster with the highest length
    max_length_coaster = max(coaster_lengths, key=coaster_lengths.get)
    max_length_location = coasters.loc[coasters['Coaster'] == max_length_coaster, 'Park'].iloc[0]
    st.write(f"The coaster with the longest length is '{max_length_coaster}' at '{max_length_location}' with a length of {coaster_lengths[max_length_coaster]} feet.")
    beast = "PKI-Son_of_Beast.jpg"
    st.image(beast, use_column_width=True)


if label == 'Highest Drop':
     #Read the CSV file into a pandas DataFrame
    coasters = pd.read_csv('RollerCoasters-Geo.csv')
    # Create an empty dictionary to store coaster names and their drop heights
    drop_heights = {}
    #Loop through each row of the DataFrame and add the coaster name and its drop height to the dictionary
    for index, row in coasters.iterrows():
        name = row['Coaster']
        location = row['Park']
        drop = row['Drop']
        if not pd.isna(drop):  # ignore rows where 'Drop' is NaN
            drop_heights[name] = drop

    #Find the name and location of the coaster with the highest drop height
    max_drop_coaster = max(drop_heights, key=drop_heights.get)
    max_drop_location = coasters.loc[coasters['Coaster'] == max_drop_coaster, 'Park'].iloc[0]
    st.write(f"The coaster with the highest drop height is '{max_drop_coaster}' at '{max_drop_location}' with a drop height of {drop_heights[max_drop_coaster]} feet.")
    thrill = "maxresdefault.jpg"
    st.image(thrill, use_column_width=True)



#Slider Function

#takes the data frame and number of inversions
def filter_coasters_by_inversions(df, num_of_inversions):
    #this will display the filtered data frame by the name of coaster, the name of the park, and the state it is located in.
    return df[df['Num_of_Inversions'] == num_of_inversions][['Coaster', 'Park', 'State']]

data = pd.read_csv('RollerCoasters-Geo.csv')
st.markdown("<h4 style='color: #1E90FF; text-align: left;'>Use the Slider to see the coasters with that number of inversions</h4>", unsafe_allow_html=True)
#create the slider based on number of inversions
num_of_inversions = st.slider('', min_value=0, max_value=8, step=1)

# Filter data based on selected number of inversions
filtered_data = filter_coasters_by_inversions(data, num_of_inversions)

#Display the data
if not filtered_data.empty:
    st.write('Coasters with', num_of_inversions, 'inversions:')
    st.write(filtered_data)
else:
    st.write('No coasters found with', num_of_inversions, 'inversions.')

st.markdown("<h4 style='color: #1E90FF; text-align: left;'>Select a Coaster Design</h4>", unsafe_allow_html=True)
data = pd.read_csv('RollerCoasters-Geo.csv')

# Define function to split data into separate DataFrames based on a column
def split_data_by_column(df, column):
    split_data = {}
    options = df[column].unique()
    for option in options:
        split_data[option] = df[df[column] == option].reset_index(drop=True)
    return split_data
    #keys are the unique values and the values are the separate DataFrames corresponding to each unique value.

# Add a selectbox to select the coaster design & allow the user to select a specific coaster design
selection = st.selectbox(' ', ('Sit Down','Stand Up', 'Pipeline', 'Inverted','4th Dimension', 'Flying', 'Wing'))

# Split data into separate DataFrames based on selected coaster design
split_data = split_data_by_column(data, 'Design')
if selection in split_data:
    st.write(f"{selection} coasters:")
    st.write(split_data[selection])