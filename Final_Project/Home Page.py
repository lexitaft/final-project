import streamlit as st
import pandas as pd

#set the Page Configurations
st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None, )
df = pd.read_csv("RollerCoasters-Geo.csv")


#Main page heading with the data

st.markdown("<h1 style='color: #FF69B4; text-align: center;'> Roller Coaster Final Project </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #BF3EFF; text-align: center;'> Welcome to the Main Page</h2>", unsafe_allow_html=True)
main = "Coaster.jpg"
st.image(main, use_column_width=True)
st.markdown("<h3 style='color: #FF69B4; text-align: center;'>On this page I have included the original data set as well as a data set you can filter</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #FF69B4; text-align: center;'> Please use the sidebar to find the other pages on this application!</h4>", unsafe_allow_html=True)
st.markdown("<p style='color: #BF3EFF; text-align: center;'>This data set below contains all of the data used for this project</p>", unsafe_allow_html=True)

st.dataframe(df)


#Created columns of images to represent the different filters
st.markdown("<h2 style='color: #1E90FF; text-align: center;'>You can filter through this data using the sidebar on the left. You can filter the data based on...</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3) # Streamlit func allows you to divide the page width into columns so you can put multiple widgets/elements side by side

with col1:
    st.markdown("<h2 style='color: #1E90FF; text-align: center;'>Location</h2>",
                unsafe_allow_html=True)
    st.image("Location.jpg")

with col2:
    st.markdown("<h2 style='color: #1E90FF; text-align: center;'>Age</h2>",
                unsafe_allow_html=True)
    st.image("Age.jpg")

with col3:
    st.markdown("<h2 style='color: #1E90FF; text-align: center;'>Type</h2>",
                unsafe_allow_html=True)
    st.image("Type.jpg")


#streamlits adding widgets to your sidebar
st.sidebar.header("Filter out rollercoasters here!") #heading
st.sidebar.write("You can filter the coasters by their location(state), age, and the type.") #writing under heading

#above df = pd.read_csv("RollerCoasters-Geo.csv") was created making the variable df the dataframe

#multiselect widget for the location of coaster and assignment of variable
state_coaster = st.sidebar.multiselect(
    "Select the State:",
    options=df["State"].unique(), # parameter specifies the list of available options for the widget
    default=df["State"].unique() #parameter is used to set the default selected options for the widget
) #use both parameters to make the widget more user-friendly
# use the unique func to ensure that users only see each state once in the multiselect widget


#multiselect for the age of coaster
age_coaster = st.sidebar.multiselect(
    "Select the Age:",
    options=df["Age_Group"].unique(),
    default=df["Age_Group"].unique()
)
#multiselect widget for type of coaster
type_coaster = st.sidebar.multiselect(
    "Select the Type:",
    options=df["Type"].unique(),
    default=df["Type"].unique()
)
#below is method in pandas that allows you to filter a DataFrame by specifying a query expression as a string
#query() method replaces the @variable syntax with the actual value of the widget variable at the time the query is executed.
#ex)State == @state_coaster: this condition checks if the "State" column in the DataFrame matches
#any of the selected options from the state_coaster widget

df_selection = df.query(
    "State == @state_coaster & Age_Group == @age_coaster & Type == @type_coaster"
)

#filters the dataframe based on the user's selections from the sidebar widgets
#"@" symbol is used to refer to the variables created by the sidebar widgets in the query string

#a styled markdown heading: Color is purple, text is centerted in a paragraph sized writing
st.markdown("<p style='color: #BF3EFF; text-align: center;'>Here is the filtered data that only shows what you selected from the sidebar on the left</p>", unsafe_allow_html=True)
st.dataframe(df_selection) #the new dataframe with the filtered data




