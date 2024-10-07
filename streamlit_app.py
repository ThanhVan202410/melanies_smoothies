# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.title('Check 2')

# Write directly to the app
st.title("Customize your smoothie !")
st.write(
    "Choose the fruits you want for your smoothie"
)

name_on_order = st.text_input('Name on smoothies : ')
st.write('The name of your smoothie is : ',name_on_order)

cnx=st.connection('snowflake')
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list = st.multiselect('Choose up to 5 ingredient'
                                 , my_dataframe
                                 , max_selections=5)

if ingredient_list : 
    st.write(ingredient_list)
    st.text(ingredient_list)
    ingredient_string = ''
    for fruit_choosen in ingredient_list:
        ingredient_string += fruit_choosen + ' '
    #st.write(ingredient_string)

    my_insert_stmt = """Insert into smoothies.public.orders (ingredients,name_on_order) values ('"""+ingredient_string+"""','"""+name_on_order+"""')"""
    #st.write (my_insert_stmt)

    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")















