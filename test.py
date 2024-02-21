import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Припускаємо, що `df` це ваш DataFrame
df = pd.DataFrame({
    "Career": ["Career"] * 5,
    "G": [1168, 33, 1043, 1086, 1168],
    "PTS": [12.7, 0.6, 15.2, 20.4, 12.7],
    "TRB": [5.1, 0.8, 2.9, 6.1, 5.1],
    "AST": [1.3, 0.1, 5.4, 5.6, 1.3],
    "FG%": [49.5, 46.7, 41.5, 47.2, 49.5],
    "FG3%": [4.8, "-", 38.7, 31.8, 4.8],
    "FT%": [69.8, 46.2, 89.4, 78.8, 69.8],
    "eFG%": [49.5, 46.7, 49.5, 49.5, 49.5],
    "PER": [14.7, 3.9, 18.8, 21.1, 14.7],
    "WS": [59.7, 0.0, 120.8, 135.6, 59.7]
})

# Заголовок веб-додатку
st.title("Візуалізація даних кар'єри баскетболіста")

# Відображення DataFrame у додатку
st.write("Дані кар'єри:")
st.dataframe(df)

# Візуалізація кількості ігор та очок
fig, ax = plt.subplots()
ax2 = ax.twinx()
df.plot(kind='bar', x='Career', y='G', ax=ax, color='blue', position=0)
df.plot(kind='bar', x='Career', y='PTS', ax=ax2, color='red', position=1, alpha=0.5)
ax.set_ylabel('Кількість ігор (G)')
ax2.set_ylabel('Очки (PTS)')
plt.title("Кількість ігор та очки за кар'єру")

# Показати графік у Streamlit
st.pyplot(fig)
