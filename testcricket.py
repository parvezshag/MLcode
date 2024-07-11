import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('D:\Conda Env\MLcode\list of test player of india.csv')

# Convert columns to appropriate data types
df['First match'] = pd.to_numeric(df['First match'], errors='coerce')
df['Last Match'] = pd.to_numeric(df['Last Match'], errors='coerce')
df['Matchs Played'] = pd.to_numeric(df['Matchs Played'], errors='coerce')
df['Runs Scored'] = pd.to_numeric(df['Runs Scored'], errors='coerce')
df['Total Wickets'] = pd.to_numeric(df['Total Wickets'], errors='coerce')
df['Batting Average'] = pd.to_numeric(df['Batting Average'], errors='coerce')

# Calculate career span
df['Career Span'] = df['Last Match'] - df['First match']

# 1. Top 10 Run Scorers
plt.figure(figsize=(12, 6))
top_runs = df.nlargest(10, 'Runs Scored')
sns.barplot(x='Name', y='Runs Scored', data=top_runs)
plt.title('Top 10 Run Scorers in Indian Test Cricket')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_run_scorers.png')
plt.close()

# 2. Top 10 Wicket Takers
plt.figure(figsize=(12, 6))
top_wickets = df.nlargest(10, 'Total Wickets')
sns.barplot(x='Name', y='Total Wickets', data=top_wickets)
plt.title('Top 10 Wicket Takers in Indian Test Cricket')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_wicket_takers.png')
plt.close()

# 3. Career Span vs Matches Played
plt.figure(figsize=(10, 6))
plt.scatter(df['Career Span'], df['Matchs Played'])
plt.title('Career Span vs Matches Played')
plt.xlabel('Career Span (years)')
plt.ylabel('Matches Played')
plt.tight_layout()
plt.savefig('career_span_vs_matches.png')
plt.close()

# 4. Batting Average Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Batting Average'].dropna(), kde=True)
plt.title('Distribution of Batting Averages')
plt.xlabel('Batting Average')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('batting_average_distribution.png')
plt.close()

# 5. Correlation Heatmap
numeric_cols = ['Matchs Played', 'Runs Scored', 'Batting Average', 'Total Wickets', 'Career Span']
corr_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap of Key Statistics')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

print("All visualizations have been saved as PNG files.")

# Display some key statistics
print("\
Key Statistics:")
print(f"Total number of players: {len(df)}")
print(f"Average career span: {df['Career Span'].mean():.2f} years")
print(f"Average matches played: {df['Matchs Played'].mean():.2f}")
print(f"Average runs scored: {df['Runs Scored'].mean():.2f}")
print(f"Average batting average: {df['Batting Average'].mean():.2f}")
print(f"Average wickets taken: {df['Total Wickets'].mean():.2f}")