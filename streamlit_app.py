import streamlit
import pandas
streamlit.title('My Parents New Healty Diner')
streamlit.header('Breakfast Menu')
streamlit.text('1.🥗 Idli, Dosa')
streamlit.text ('2. 🥣 Vada, Poori, Chapathi')
streamlit.text('3. 🍞 Panipoori, vadapaav, sandwich')
streamlit.header(' Fruit Juices Menu')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
