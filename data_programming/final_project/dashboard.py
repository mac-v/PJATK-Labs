import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

st.title("Predicting Stock Price: S&P 500")

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(start="1957-03-04", period="max")

sp500.index = sp500.index.tz_localize(None)
start_date = st.sidebar.date_input("Start date", sp500.index.min())
end_date = st.sidebar.date_input("End date", sp500.index.max())
sp500 = sp500.loc[start_date:end_date]

st.header("S&P 500 Closing Prices Over Time")
fig, ax = plt.subplots()
sp500.plot.line(y="Close", use_index=True, color='blue', ax=ax)
ax.set_title("S&P 500 Closing Prices Over Time")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_xlabel('Year')
st.pyplot(fig)

sp500['Daily_Return'] = (sp500['Close'].pct_change() * 100).round(2)

st.header("S&P 500 Daily Returns Over the Years")
fig, ax = plt.subplots()
ax.plot(sp500.index, sp500['Daily_Return'], color='blue')
ax.set_xlabel('Year')
ax.set_ylabel('Daily Return %')
ax.set_title('S&P 500 Index Daily Returns Over the Years')
st.pyplot(fig)

st.header("Distribution of S&P 500 Daily Returns")
bins = st.sidebar.slider("Number of bins in histogram", min_value=10, max_value=500, value=100)

fig, ax = plt.subplots()
ax.hist(sp500['Daily_Return'].dropna(), bins=bins, alpha=0.7, edgecolor='blue')
ax.set_title("S&P 500 Daily Returns")
ax.set_xlabel("Daily Return %")
ax.set_ylabel("Frequency")
ax.grid(True)
st.pyplot(fig)

sp500['Weekday'] = sp500.index.day_name()
sp500['Day_of_Month'] = sp500.index.month

weekday_avg = sp500.groupby('Weekday')['Daily_Return'].mean()
weekdays_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekday_avg = weekday_avg[weekdays_order]

st.header("Average Return % by Weekday")
fig, ax = plt.subplots()
weekday_avg.plot(kind='bar', color='blue', ax=ax)
ax.set_title('Average Return % by Weekday')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Average Return %')
ax.set_xticklabels(weekdays_order, rotation=45)
st.pyplot(fig)

month_avg = sp500.groupby('Day_of_Month')['Daily_Return'].mean()

st.header("Average Return % by Month")
fig, ax = plt.subplots()
month_avg.plot(kind='bar', color='blue', ax=ax)
ax.set_title('Average Return % by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Average Return %')
ax.set_xticklabels(range(1, 13), rotation=0)
st.pyplot(fig)
