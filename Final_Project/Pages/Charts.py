#Pie Chart for the type of coaster
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
df = pd.read_csv("RollerCoasters-Geo.csv")


#Heading of Charts Page
st.markdown("<h1 style='color: #FF69B4; text-align: center;'>Charts</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #BF3EFF; text-align: center;'>Check our some of the charts below to get a better visual about the roller coasters!</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #1E90FF; text-align: center;'>Wooden vs. Steel</h3>", unsafe_allow_html=True)


#Images for WOODEN VS STEEL
col1, col2 = st.columns(2)
with col1:
    st.image("WoodenCoaster.jpg")
with col2:
    st.image("Steelcoaster.jpg")


#CREATE THE PIE CHART
def statisticchart(selection):
    df = pd.read_csv("RollerCoasters-Geo.csv")
    df = df[['Type']] #selects the "Type" column
    df = df[df['Type'].isin(['Wooden', 'Steel'])] #filters the data to only include roller coasters that are either "Wooden" or "Steel"
    d = df['Type'].value_counts().to_dict() #creates a dictionary of value counts for the "Type" column

    label = []
    values = []
    for key in d:          #creates two lists, label and values, to store the keys and values of the dictionary

        label.append(key)
        values.append(d[key])
    EXPLODE_VALUE = 0.1 #used to "explode" the slice of the pie chart corresponding to the largest percentage.
    max_percentage = max(d.values()) #determines which slice to explode by finding the maximum value
    max_percentage_index = values.index(max_percentage)
    explode_values = [0] * len(label)
    explode_values[max_percentage_index] = EXPLODE_VALUE
    colors = ['#FFB6C1', '#FF69B4']

    fig = plt.figure()
    plt.pie(values, labels=label, colors=colors, explode=explode_values, autopct="%1.1f%%", startangle=90,
            textprops={"fontsize": 10})
    plt.rcParams.update({"font.size": 7}) #updates the font.size parameter
    plt.legend(loc="lower right", bbox_to_anchor=(1.5, 0))
    st.pyplot(fig)
    st.markdown(
        "<p style='color: #BF3EFF; text-align: center;'>With this data we can see that there are many more roller coasters that are made with steel compared to wood.</p>",
        unsafe_allow_html=True)


#PRESS BUTTON TO SEE PIE CHART
if st.button('Click to see Pie Chart'):
    st.markdown("<h2 style='color: #FF69B4; text-align: center;'>Pie Chart</h2>", unsafe_allow_html=True)
    statisticchart(None)
st.markdown("<h3 style='color: #1E90FF; text-align: center;'>Duration (in seconds) of coaster ride in your selected State</h3>", unsafe_allow_html=True)



#CREATE BAR CHART
def load_data():
    df = pd.read_csv("RollerCoasters-Geo.csv")
    return df #returns a pandas data frame

def main():

    df = load_data()
    st.markdown("<h4 style='color: #1E90FF; text-align: left;'>Select a State below:</h4>", unsafe_allow_html=True)

    state = st.selectbox(" ", sorted(df['State'].unique())) #selectbox

    #Press button to see bar chart
    if st.button("Click to see Bar Chart"):
        st.markdown("<h2 style='color: #FF69B4; text-align: center;'>Bar Chart</h2>", unsafe_allow_html=True)
        state_df = df[df['State'] == state] #creates a new data frame containing only the data for the selected state

        fig, ax = plt.subplots() ##create a figure and axis objects
        ax.bar(state_df['Coaster'], state_df['Duration'], color="cyan")
        plt.xticks(rotation=90, color="hotpink")
        ax.set_xlabel("Coaster Name", color="hotpink")
        ax.set_ylabel("Duration (seconds)", color="hotpink")
        ax.set_title(f"Roller Coasters in {state}", color="hotpink")

        st.pyplot(fig)
        st.markdown("<p style='color: #BF3EFF; text-align: center;'>**Please note that if there is no Bar above a coaster name than there is no data for that specific coasters duration time**</p>", unsafe_allow_html=True)

#function is only executed if the Python script is run as the main program
if __name__ == '__main__':
    main()


#CREATE SCATTERPLOT
def load_data():
    df = pd.read_csv("RollerCoasters-Geo.csv")
    return df   #returns a pandas data frame

def main():
    st.markdown(
        "<h3 style='color: #1E90FF; text-align: center;'>Correlation between drop height and year coaster opened</h3>",
        unsafe_allow_html=True)

    df = load_data()
                                    #click button to see the scatter plot
    if st.button("Click to see Scatter Plot"):
        st.markdown("<h2 style='color: #FF69B4; text-align: center;'>Scatter Plot</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots() #create a figure and axis objects
        ax.scatter(df['Year_Opened'], df['Drop'], color="cyan", alpha=0.5) #create the scatter plot
        ax.set_xlabel("Year Opened", color="HotPink")
        ax.set_ylabel("Drop Height (feet)", color="HotPink")
        ax.set_title("Roller Coasters Scatter Plot", color="HotPink") #set the labels and title of the scatter plot.
        st.pyplot(fig) #display the plot
        st.markdown("<p style='color: #BF3EFF; text-align: center;'>Here we see there is somewhat of a strong positive correlation between the drop height and the year the coaster opened. The drop height of the roller coasters seems to increase as the years move closer to the present. With this data we are also able to see that there was a boom in roller coasters around the 2000s. During this boom it seems that a lot of the coasters drop heights were between 50-200 feet.</p>", unsafe_allow_html=True)

if __name__ == '__main__': # checks if the script is being run as the main program
    main()



