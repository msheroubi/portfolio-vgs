import pandas as pd
from prettytable import PrettyTable

# Initialize dataframe
df = pd.read_csv('vgsales.csv', index_col='Rank')


# ========================================================
# Aggregates: get max, min and mean values for each
#  category defined.
# ========================================================

# Total Sales by region

total_na_sales = df['NA_Sales'].sum()
total_eu_sales = df['EU_Sales'].sum()
total_jp_sales = df['JP_Sales'].sum()
total_other_sales = df['Other_Sales'].sum()
total_global_sales = df['Global_Sales'].sum()

print(f"Total NA Sales: ${total_na_sales:.2f} (in millions)")
print(f"Total EU Sales: ${total_eu_sales:.2f} (in millions)")
print(f"Total JP Sales: ${total_jp_sales:.2f} (in millions)")
print(f"Total Other Sales: ${total_other_sales:.2f} (in millions)")
print(f"Total Sales: ${total_global_sales:.2f} (in millions)")

# Max and Min by region

max_na = df.iloc[df['NA_Sales'].idxmax()-1] #rank starts at 1, index starts at 0 so we -1 from idx
min_na = df.iloc[df['NA_Sales'].idxmin()-1]

max_eu = df.iloc[df['EU_Sales'].idxmax()-1]
min_eu = df.iloc[df['EU_Sales'].idxmin()-1]

max_jp = df.iloc[df['JP_Sales'].idxmax()-1]
min_jp = df.iloc[df['JP_Sales'].idxmin()-1]

max_other = df.iloc[df['Other_Sales'].idxmax()-1]
min_other = df.iloc[df['Other_Sales'].idxmin()-1]

max_global = df.iloc[df['Global_Sales'].idxmax()-1]
min_global = df.iloc[df['Global_Sales'].idxmin()-1]

# # Show results in an ASCII table
max_t = PrettyTable(['Region', 'Name', 'Publisher', 'Platform', 'Year'])
min_t = PrettyTable(['Region', 'Name', 'Publisher', 'Platform', 'Year'])

max_t.add_row(['NA', max_na['Name'], max_na['Publisher'], max_na['Platform'], f"{max_na['Year']:.0f}"])
max_t.add_row(['EU', max_eu['Name'], max_eu['Publisher'], max_eu['Platform'], f"{max_eu['Year']:.0f}"])
max_t.add_row(['JP', max_jp['Name'], max_jp['Publisher'], max_jp['Platform'], f"{max_jp['Year']:.0f}"])
max_t.add_row(['Other', max_other['Name'], max_other['Publisher'], max_other['Platform'], f"{max_other['Year']:.0f}"])
max_t.add_row(['Global', max_global['Name'], max_global['Publisher'], max_global['Platform'], f"{max_global['Year']:.0f}"])


print('')
print('Highest Grossing Games of All-time by Region')
print(max_t)

min_t.add_row(['NA', min_na['Name'], min_na['Publisher'], min_na['Platform'], f"{min_na['Year']:.0f}"])
min_t.add_row(['EU', min_eu['Name'], min_eu['Publisher'], min_eu['Platform'], f"{min_eu['Year']:.0f}"])
min_t.add_row(['JP', min_jp['Name'], min_jp['Publisher'], min_jp['Platform'], f"{min_jp['Year']:.0f}"])
min_t.add_row(['Other', min_other['Name'], min_other['Publisher'], min_other['Platform'], f"{min_other['Year']:.0f}"])
min_t.add_row(['Global', min_global['Name'], min_global['Publisher'], min_global['Platform'], f"{min_global['Year']:.0f}"])

print('Lowest Grossing Games of All-time by Region')
print(min_t)

# Get rest of stats

stat_t = PrettyTable(['Region', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
na_stats = df['NA_Sales'].describe()
eu_stats = df['EU_Sales'].describe()
jp_stats = df['JP_Sales'].describe()
other_stats = df['Other_Sales'].describe()
global_stats = df['Global_Sales'].describe()

stat_t.add_row(['NA', na_stats['count'],na_stats['mean'],na_stats['std'],na_stats['min'],na_stats['25%'],na_stats['50%'],na_stats['75%'], na_stats['max']])
stat_t.add_row(['EU', eu_stats['count'],eu_stats['mean'],eu_stats['std'],eu_stats['min'],eu_stats['25%'],eu_stats['50%'],eu_stats['75%'], eu_stats['max']])
stat_t.add_row(['JP', jp_stats['count'],jp_stats['mean'],jp_stats['std'],jp_stats['min'],jp_stats['25%'],jp_stats['50%'],jp_stats['75%'], jp_stats['max']])
stat_t.add_row(['Other', other_stats['count'],other_stats['mean'],other_stats['std'],other_stats['min'],other_stats['25%'],other_stats['50%'],other_stats['75%'], other_stats['max']])
stat_t.add_row(['Global', global_stats['count'],global_stats['mean'],global_stats['std'],global_stats['min'],global_stats['25%'],global_stats['50%'],global_stats['75%'], global_stats['max']])

print('Stat Distribution')
print(stat_t)


# ========================================================
# 
# 
# ========================================================