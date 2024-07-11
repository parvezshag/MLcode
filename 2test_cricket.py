import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('D:\Conda Env\MLcode\list of test player of india.csv')

# Convert columns to appropriate data types
numeric_columns = ['First match', 'Last Match', 'Matchs Played', 'Runs Scored', 'Highest score', 
                   'Batting Average', '100s', '50s', 'Total Wickets', 'Average', '5 Wickets ', 
                   '10 Wickets', 'Catches', 'Stumping']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate career span
df['Career Span'] = df['Last Match'] - df['First match']

# 1. Centuries vs Half-centuries
plt.figure(figsize=(10, 6))
plt.scatter(df['50s'], df['100s'], alpha=0.5)
plt.title('Centuries vs Half-centuries')
plt.xlabel('Number of Half-centuries')
plt.ylabel('Number of Centuries')
plt.tight_layout()
plt.savefig('centuries_vs_half_centuries.png')
plt.close()

# 2. Batting Average vs Bowling Average
plt.figure(figsize=(10, 6))
plt.scatter(df['Batting Average'], df['Average'], alpha=0.5)
plt.title('Batting Average vs Bowling Average')
plt.xlabel('Batting Average')
plt.ylabel('Bowling Average')
plt.tight_layout()
plt.savefig('batting_vs_bowling_average.png')
plt.close()

# 3. Career Span Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Career Span'].dropna(), kde=True, bins=20)
plt.title('Distribution of Career Spans')
plt.xlabel('Career Span (years)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('career_span_distribution.png')
plt.close()

# 4. Wickets vs Catches
plt.figure(figsize=(10, 6))
plt.scatter(df['Total Wickets'], df['Catches'], alpha=0.5)
plt.title('Wickets vs Catches')
plt.xlabel('Total Wickets')
plt.ylabel('Catches')
plt.tight_layout()
plt.savefig('wickets_vs_catches.png')
plt.close()

# 5. Top 10 Players by Batting Strike Rate
df['Strike Rate'] = (df['Runs Scored'] / df['Matchs Played']) * 100
top_strike_rate = df.nlargest(10, 'Strike Rate')
plt.figure(figsize=(12, 6))
sns.barplot(x='Name', y='Strike Rate', data=top_strike_rate)
plt.title('Top 10 Players by Batting Strike Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_strike_rate.png')
plt.close()

print("All new visualizations have been saved as PNG files.")

# Display some additional statistics
print("\
Additional Statistics:")
print(f"Player with highest batting average: {df.loc[df['Batting Average'].idxmax(), 'Name']} ({df['Batting Average'].max():.2f})")
print(f"Player with most centuries: {df.loc[df['100s'].idxmax(), 'Name']} ({df['100s'].max()})")
print(f"Player with longest career span: {df.loc[df['Career Span'].idxmax(), 'Name']} ({df['Career Span'].max():.2f} years)")
print(f"Player with most catches: {df.loc[df['Catches'].idxmax(), 'Name']} ({df['Catches'].max()})")
print(f"Player with highest strike rate: {df.loc[df['Strike Rate'].idxmax(), 'Name']} ({df['Strike Rate'].max():.2f})")