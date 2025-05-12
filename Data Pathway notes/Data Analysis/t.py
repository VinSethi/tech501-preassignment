import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
import matplotlib.ticker as mtick
import os

# Set the aesthetic style for our plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# ===============================================================
# PART 1: DATA LOADING AND CLEANING
# ===============================================================

def load_and_clean_data(file_path):
    """
    Load the CSV file and perform initial data cleaning.
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Cleaned dataframe
    """
    print("Loading and cleaning data...")
    
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from: {file_path}")
        
        # Display basic information about the dataset
        print(f"Dataset dimensions: {df.shape[0]} rows and {df.shape[1]} columns")
        
        # Check for missing values
        missing_values = df.isnull().sum()
        print("\nMissing values per column:")
        print(missing_values)
        
        # Standardize column names (lowercase, replace spaces with underscores)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Check for duplicates and remove them
        duplicates = df.duplicated().sum()
        print(f"\nNumber of duplicate rows: {duplicates}")
        if duplicates > 0:
            df.drop_duplicates(inplace=True)
            print(f"Duplicates removed. New shape: {df.shape}")
        
        # Convert year to integer if it's not already
        df['year'] = df['year'].astype(int)
        
        return df
    
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        print("Please check if the file exists at the specified location.")
        print("Current working directory: {0}".format(os.getcwd()))
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

# ===============================================================
# PART 2: EXPLORATORY DATA ANALYSIS
# ===============================================================

def perform_eda(df):
    """
    Perform exploratory data analysis on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataframe to analyze
    """
    print("\n" + "="*50)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Display basic statistics
    print("\nSummary statistics for numerical columns:")
    print(df.describe().round(2))
    
    # Display counts for categorical columns
    print("\nCounts for categorical columns:")
    
    # For Country
    print("\nCountry distribution:")
    country_counts = df['country'].value_counts()
    print(country_counts)
    
    # For Industry
    print("\nIndustry distribution:")
    industry_counts = df['industry'].value_counts()
    print(industry_counts)
    
    # For Regulation Status
    print("\nRegulation Status distribution:")
    regulation_counts = df['regulation_status'].value_counts()
    print(regulation_counts)
    
    # For Top AI Tools
    print("\nTop AI Tools Used distribution:")
    tools_counts = df['top_ai_tools_used'].value_counts()
    print(tools_counts)
    
    # Distribution of years
    print("\nDistribution of years:")
    year_counts = df['year'].value_counts().sort_index()
    print(year_counts)
    
    # Calculate correlations between numerical variables
    print("\nCorrelation matrix for numerical variables:")
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = df[numerical_cols].corr().round(2)
    print(correlation_matrix)

# ===============================================================
# PART 3: DATA VISUALIZATION FUNCTIONS
# ===============================================================

def create_visualizations(df):
    """
    Create various visualizations to explore the data.
    
    Parameters:
    df (pd.DataFrame): The dataframe to visualize
    """
    print("\n" + "="*50)
    print("CREATING VISUALIZATIONS")
    print("="*50)
    
    # Create a directory to save visualizations if it doesn't exist
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
        print("Created 'visualizations' directory to save the charts")
    
    # Call each visualization function
    visualize_ai_adoption_by_country(df)
    visualize_ai_adoption_by_industry(df)
    visualize_job_loss_vs_revenue(df)
    visualize_ai_tools_distribution(df)
    visualize_ai_adoption_trend(df)
    visualize_correlation_heatmap(df)
    visualize_human_ai_collaboration_vs_trust(df)
    visualize_content_volume_by_country_year(df)
    visualize_regulation_impact(df)
    
    print("\nAll visualizations created and saved in the 'visualizations' folder.")

def visualize_ai_adoption_by_country(df):
    """Create a horizontal bar chart of average AI adoption rate by country."""
    print("Creating AI adoption by country visualization...")
    
    # Calculate average adoption rate by country
    country_adoption = df.groupby('country')['ai_adoption_rate_(%)'].mean().sort_values(ascending=False)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=country_adoption.values, y=country_adoption.index, palette='viridis')
    
    # Add labels and title
    plt.title('Average AI Adoption Rate by Country', fontsize=16)
    plt.xlabel('AI Adoption Rate (%)', fontsize=14)
    plt.ylabel('Country', fontsize=14)
    
    # Add percentage signs to x-axis labels
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Add value labels to the bars
    for i, v in enumerate(country_adoption.values):
        ax.text(v + 1, i, f"{v:.1f}%", va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('visualizations/ai_adoption_by_country.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_ai_adoption_by_industry(df):
    """Create a horizontal bar chart of average AI adoption rate by industry."""
    print("Creating AI adoption by industry visualization...")
    
    # Calculate average adoption rate by industry
    industry_adoption = df.groupby('industry')['ai_adoption_rate_(%)'].mean().sort_values(ascending=False)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=industry_adoption.values, y=industry_adoption.index, palette='mako')
    
    # Add labels and title
    plt.title('Average AI Adoption Rate by Industry', fontsize=16)
    plt.xlabel('AI Adoption Rate (%)', fontsize=14)
    plt.ylabel('Industry', fontsize=14)
    
    # Add percentage signs to x-axis labels
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Add value labels to the bars
    for i, v in enumerate(industry_adoption.values):
        ax.text(v + 1, i, f"{v:.1f}%", va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('visualizations/ai_adoption_by_industry.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_job_loss_vs_revenue(df):
    """Create a scatter plot of job loss vs revenue increase with industry encoding."""
    print("Creating job loss vs revenue increase visualization...")
    
    # Create the plot
    plt.figure(figsize=(14, 10))
    
    # Get unique industries for color mapping
    industries = df['industry'].unique()
    
    # Create a color palette with enough colors
    palette = sns.color_palette("husl", len(industries))
    industry_colors = dict(zip(industries, palette))
    
    # Create the scatter plot
    scatter = plt.scatter(
        df['job_loss_due_to_ai_(%)'], 
        df['revenue_increase_due_to_ai_(%)'],
        c=df['industry'].map(lambda x: industries.tolist().index(x)),
        s=df['ai_adoption_rate_(%)'] * 5,  # Scale the point size by adoption rate
        alpha=0.7,
        cmap=ListedColormap(palette)
    )
    
    # Add labels and title
    plt.title('Job Loss vs Revenue Increase Due to AI by Industry', fontsize=16)
    plt.xlabel('Job Loss Due to AI (%)', fontsize=14)
    plt.ylabel('Revenue Increase Due to AI (%)', fontsize=14)
    
    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add a legend for industries
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=industry) 
               for industry, color in zip(industries, palette)]
    legend1 = plt.legend(handles=handles, title="Industry", loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.gca().add_artist(legend1)
    
    # Add a legend for the size scale
    size_legend_sizes = [20, 40, 60, 80]
    size_legend_labels = ['20%', '40%', '60%', '80%']
    handles = [plt.Line2D([0], [0], marker='o', color='gray', markersize=np.sqrt(size/2), linestyle='None') 
               for size in size_legend_sizes]
    legend2 = plt.legend(handles=handles, labels=size_legend_labels, title="AI Adoption Rate", 
                         loc='upper left', bbox_to_anchor=(1.05, 0.6))
    
    # Add correlation line
    x = df['job_loss_due_to_ai_(%)']
    y = df['revenue_increase_due_to_ai_(%)']
    
    # Calculate correlation
    correlation = x.corr(y)
    
    # Add correlation coefficient text
    plt.annotate(f'Correlation: {correlation:.2f}', 
                 xy=(0.05, 0.95), 
                 xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    # Add best fit line
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, 'r--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('visualizations/job_loss_vs_revenue.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_ai_tools_distribution(df):
    """Create a pie chart showing the distribution of top AI tools used."""
    print("Creating AI tools distribution visualization...")
    
    # Count the occurrences of each AI tool
    tools_counts = df['top_ai_tools_used'].value_counts()
    
    # Create a pie chart
    plt.figure(figsize=(12, 10))
    
    # Use a visually pleasing color palette
    colors = sns.color_palette('bright', len(tools_counts))
    
    # Create the pie chart
    plt.pie(
        tools_counts, 
        labels=tools_counts.index, 
        autopct='%1.1f%%',
        startangle=90, 
        colors=colors,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
        textprops={'fontsize': 12}
    )
    
    # Add a title
    plt.title('Distribution of Top AI Tools Used', fontsize=16)
    
    # Add a circle at the center to make it look like a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    
    plt.tight_layout()
    plt.savefig('visualizations/ai_tools_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_ai_adoption_trend(df):
    """Create a line plot showing the trend of AI adoption rate over years."""
    print("Creating AI adoption trend visualization...")
    
    # Calculate average adoption rate by year
    year_adoption = df.groupby('year')['ai_adoption_rate_(%)'].mean()
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Create the line plot
    plt.plot(
        year_adoption.index, 
        year_adoption.values,
        marker='o', 
        linewidth=3, 
        markersize=10,
        color='#1f77b4'
    )
    
    # Add labels and title
    plt.title('Trend of AI Adoption Rate Over Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average AI Adoption Rate (%)', fontsize=14)
    
    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add value labels to the data points
    for x, y in zip(year_adoption.index, year_adoption.values):
        plt.annotate(
            f"{y:.1f}%", 
            (x, y), 
            textcoords="offset points",
            xytext=(0, 10), 
            ha='center',
            fontweight='bold'
        )
        
    # Format y-axis as percentage
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Set x-axis to only show the years in the dataset
    plt.xticks(year_adoption.index)
    
    plt.tight_layout()
    plt.savefig('visualizations/ai_adoption_trend.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_correlation_heatmap(df):
    """Create a heatmap of correlations between numerical variables."""
    print("Creating correlation heatmap...")
    
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Calculate the correlation matrix
    correlation = df[numerical_cols].corr()
    
    # Create the heatmap
    plt.figure(figsize=(14, 12))
    
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    
    # Create the heatmap with a diverging colormap
    sns.heatmap(
        correlation, 
        annot=True,  # Show correlation values
        fmt='.2f',   # Format to 2 decimal places
        cmap='coolwarm',  # Use a diverging colormap
        mask=mask,   # Use the mask to show only the lower triangle
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )
    
    # Add a title
    plt.title('Correlation Matrix of Numerical Variables', fontsize=16)
    
    plt.tight_layout()
    plt.savefig('visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_human_ai_collaboration_vs_trust(df):
    """Create a scatter plot of human-AI collaboration vs consumer trust."""
    print("Creating human-AI collaboration vs consumer trust visualization...")
    
    # Create the figure
    plt.figure(figsize=(14, 10))
    
    # Get unique regulation statuses for color mapping
    regulations = df['regulation_status'].unique()
    
    # Create a color palette with enough colors
    palette = sns.color_palette("Set2", len(regulations))
    reg_colors = dict(zip(regulations, palette))
    
    # Create the scatter plot
    for reg in regulations:
        subset = df[df['regulation_status'] == reg]
        plt.scatter(
            subset['human-ai_collaboration_rate_(%)'],
            subset['consumer_trust_in_ai_(%)'],
            s=subset['market_share_of_ai_companies_(%)'] * 10,  # Scale by market share
            c=[reg_colors[reg]] * len(subset),
            alpha=0.7,
            label=reg
        )
    
    # Add labels and title
    plt.title('Human-AI Collaboration vs Consumer Trust by Regulation Status', fontsize=16)
    plt.xlabel('Human-AI Collaboration Rate (%)', fontsize=14)
    plt.ylabel('Consumer Trust in AI (%)', fontsize=14)
    
    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add a legend for regulation status
    plt.legend(title="Regulation Status", fontsize=12)
    
    # Format axes as percentage
    plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter())
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Calculate and add the overall correlation line
    x = df['human-ai_collaboration_rate_(%)']
    y = df['consumer_trust_in_ai_(%)']
    
    # Calculate correlation
    correlation = x.corr(y)
    
    # Add correlation coefficient text
    plt.annotate(f'Correlation: {correlation:.2f}', 
                 xy=(0.05, 0.95), 
                 xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    # Add best fit line
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, 'r--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('visualizations/collaboration_vs_trust.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_content_volume_by_country_year(df):
    """Create a grouped bar chart showing AI-generated content volume by country and year."""
    print("Creating content volume by country and year visualization...")
    
    # Prepare data: average content volume by country and year
    content_by_country_year = df.pivot_table(
        index='country', 
        columns='year', 
        values='ai-generated_content_volume_(tbs_per_year)',
        aggfunc='mean'
    ).fillna(0)
    
    # Select top countries by total content volume for readability
    top_countries = df.groupby('country')['ai-generated_content_volume_(tbs_per_year)'].sum().nlargest(8).index
    content_top = content_by_country_year.loc[top_countries]
    
    # Create the grouped bar chart
    plt.figure(figsize=(14, 10))
    
    # Plot the data
    content_top.plot(kind='bar', figsize=(14, 10), width=0.8)
    
    # Add labels and title
    plt.title('AI-Generated Content Volume by Country and Year (Top 8 Countries)', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('AI-Generated Content Volume (TBs per year)', fontsize=14)
    plt.legend(title='Year', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    plt.tight_layout()
    plt.savefig('visualizations/content_volume_by_country_year.png', dpi=300, bbox_inches='tight')
    plt.close()

def visualize_regulation_impact(df):
    """Create a multi-faceted visualization showing the impact of regulation status on various metrics."""
    print("Creating regulation impact visualization...")
    
    # Prepare data: average metrics by regulation status
    metrics = [
        'ai_adoption_rate_(%)', 
        'job_loss_due_to_ai_(%)', 
        'revenue_increase_due_to_ai_(%)', 
        'consumer_trust_in_ai_(%)'
    ]
    
    metric_names = [
        'AI Adoption Rate (%)', 
        'Job Loss Due to AI (%)', 
        'Revenue Increase Due to AI (%)', 
        'Consumer Trust in AI (%)'
    ]
    
    regulation_impact = df.groupby('regulation_status')[metrics].mean()
    
    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    # Create a color palette
    colors = sns.color_palette("Set3", len(regulation_impact))
    
    # Create bar plots for each metric
    for i, (metric, name) in enumerate(zip(metrics, metric_names)):
        ax = axes[i]
        
        # Create the bar plot
        bars = ax.bar(
            regulation_impact.index,
            regulation_impact[metric],
            color=colors,
            width=0.6
        )
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.1,
                f"{height:.1f}%",
                ha='center',
                fontsize=10,
                fontweight='bold'
            )
        
        # Customize the plot
        ax.set_title(name, fontsize=14)
        ax.set_ylabel('Percentage (%)', fontsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Format y-axis as percentage
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Add an overall title
    plt.suptitle('Impact of Regulation Status on AI Metrics', fontsize=18, y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to make room for suptitle
    plt.savefig('visualizations/regulation_impact.png', dpi=300, bbox_inches='tight')
    plt.close()

# ===============================================================
# PART 4: ADVANCED ANALYSIS FUNCTIONS
# ===============================================================

def perform_advanced_analysis(df):
    """
    Perform more complex analyses on the dataset.
    
    Parameters:
    df (pd.DataFrame): The dataframe to analyze
    """
    print("\n" + "="*50)
    print("ADVANCED ANALYSIS")
    print("="*50)
    
    # Analyze the relationship between AI adoption and revenue increase
    analyze_adoption_revenue_relationship(df)
    
    # Analyze job displacement vs human-AI collaboration
    analyze_job_displacement_vs_collaboration(df)
    
    # Analyze the impact of regulation status
    analyze_regulation_impact(df)
    
    # Analyze trends over time
    analyze_time_trends(df)
    
    # Analyze industry-specific patterns
    analyze_industry_patterns(df)

def analyze_adoption_revenue_relationship(df):
    """Analyze the relationship between AI adoption rate and revenue increase."""
    print("\n1. RELATIONSHIP BETWEEN AI ADOPTION AND REVENUE INCREASE")
    
    # Calculate correlation
    correlation = df['ai_adoption_rate_(%)'].corr(df['revenue_increase_due_to_ai_(%)'])
    print(f"Correlation between AI adoption rate and revenue increase: {correlation:.2f}")
    
    # Group by adoption rate ranges and calculate average revenue increase
    df['adoption_range'] = pd.cut(
        df['ai_adoption_rate_(%)'], 
        bins=[0, 25, 50, 75, 100], 
        labels=['0-25%', '25-50%', '50-75%', '75-100%']
    )
    
    adoption_revenue = df.groupby('adoption_range')['revenue_increase_due_to_ai_(%)'].agg(['mean', 'count'])
    print("\nAverage revenue increase by AI adoption rate range:")
    print(adoption_revenue)
    
    # Find industries with highest and lowest ROI (revenue increase / adoption rate)
    df['roi'] = df['revenue_increase_due_to_ai_(%)'] / df['ai_adoption_rate_(%)']
    
    industry_roi = df.groupby('industry')['roi'].mean().sort_values(ascending=False)
    print("\nIndustries ranked by AI ROI (Revenue Increase / Adoption Rate):")
    print(industry_roi)
    
    # Find countries with highest and lowest ROI
    country_roi = df.groupby('country')['roi'].mean().sort_values(ascending=False)
    print("\nCountries ranked by AI ROI (Revenue Increase / Adoption Rate):")
    print(country_roi)

def analyze_job_displacement_vs_collaboration(df):
    """Analyze the relationship between job displacement and human-AI collaboration."""
    print("\n2. JOB DISPLACEMENT VS HUMAN-AI COLLABORATION")
    
    # Calculate correlation
    correlation = df['job_loss_due_to_ai_(%)'].corr(df['human-ai_collaboration_rate_(%)'])
    print(f"Correlation between job loss and human-AI collaboration rate: {correlation:.2f}")
    
    # Group by collaboration rate ranges and calculate average job loss
    df['collaboration_range'] = pd.cut(
        df['human-ai_collaboration_rate_(%)'], 
        bins=[0, 25, 50, 75, 100], 
        labels=['0-25%', '25-50%', '50-75%', '75-100%']
    )
    
    collaboration_job_loss = df.groupby('collaboration_range')['job_loss_due_to_ai_(%)'].agg(['mean', 'count'])
    print("\nAverage job loss by human-AI collaboration rate range:")
    print(collaboration_job_loss)
    
    # Find the best and worst industries for balancing job preservation with AI adoption
    df['job_preservation_score'] = df['ai_adoption_rate_(%)'] - df['job_loss_due_to_ai_(%)']
    
    industry_job_preservation = df.groupby('industry')[['job_preservation_score', 'ai_adoption_rate_(%)', 'job_loss_due_to_ai_(%)']].mean().sort_values(by='job_preservation_score', ascending=False)
    print("\nIndustries ranked by job preservation score (adoption rate - job loss):")
    print(industry_job_preservation)

def analyze_regulation_impact(df):
    """Analyze the impact of regulation status on various metrics."""
    print("\n3. IMPACT OF REGULATION STATUS")
    
    # Calculate average metrics by regulation status
    metrics = [
        'ai_adoption_rate_(%)', 
        'job_loss_due_to_ai_(%)', 
        'revenue_increase_due_to_ai_(%)', 
        'human-ai_collaboration_rate_(%)',
        'consumer_trust_in_ai_(%)', 
        'market_share_of_ai_companies_(%)'
    ]
    
    regulation_impact = df.groupby('regulation_status')[metrics].mean()
    print("\nAverage metrics by regulation status:")
    print(regulation_impact)
    
    # ANOVA test to check if differences are statistically significant
    try:
        from scipy import stats
        
        print("\nANOVA tests for statistical significance of regulation impact:")
        for metric in metrics:
            groups = [df[df['regulation_status'] == status][metric] for status in df['regulation_status'].unique()]
            f_val, p_val = stats.f_oneway(*groups)
            
            significance = "Significant" if p_val < 0.05 else "Not significant"
            print(f"{metric}: F={f_val:.2f}, p={p_val:.4f} - {significance}")
    except ImportError:
        print("\nNote: scipy is not installed. Skipping ANOVA tests.")
    except Exception as e:
        print(f"\nError performing ANOVA tests: {str(e)}")
    
    # Analyze which tools are most common in different regulatory environments
    regulation_tools = pd.crosstab(
        df['regulation_status'], 
        df['top_ai_tools_used'], 
        normalize='index'
    ) * 100  # Convert to percentage
    
    print("\nPercentage distribution of AI tools by regulation status:")
    print(regulation_tools.round(1))

def analyze_time_trends(df):
    """Analyze trends over time for various metrics."""
    print("\n4. TRENDS OVER TIME")
    
    # Calculate average metrics by year
    metrics = [
        'ai_adoption_rate_(%)', 
        'job_loss_due_to_ai_(%)', 
        'revenue_increase_due_to_ai_(%)', 
        'human-ai_collaboration_rate_(%)',
        'consumer_trust_in_ai_(%)', 
        'market_share_of_ai_companies_(%)'
    ]
    
    time_trends = df.groupby('year')[metrics].mean()
    print("\nAverage metrics by year:")
    print(time_trends)
    
    # Calculate compound annual growth rate (CAGR) for each metric
    min_year = df['year'].min()
    max_year = df['year'].max()
    years_diff = max_year - min_year
    
    print("\nCompound Annual Growth Rate (CAGR) for key metrics:")
    for metric in metrics:
        try:
            initial_value = time_trends.loc[min_year, metric]
            final_value = time_trends.loc[max_year, metric]
            
            if initial_value > 0:  # Avoid division by zero
                cagr = (final_value / initial_value) ** (1 / years_diff) - 1
                print(f"{metric}: {cagr:.2%}")
        except Exception as e:
            print(f"Error calculating CAGR for {metric}: {str(e)}")
    
    # Analyze changing popularity of AI tools over time
    tools_by_year = pd.crosstab(
        df['year'], 
        df['top_ai_tools_used'], 
        normalize='index'
    ) * 100  # Convert to percentage
    
    print("\nPercentage distribution of AI tools by year:")
    print(tools_by_year.round(1))

def analyze_industry_patterns(df):
    """Analyze industry-specific patterns in AI adoption and impact."""
    print("\n5. INDUSTRY-SPECIFIC PATTERNS")
    
    # Calculate average metrics by industry
    metrics = [
        'ai_adoption_rate_(%)', 
        'ai-generated_content_volume_(tbs_per_year)',
        'job_loss_due_to_ai_(%)', 
        'revenue_increase_due_to_ai_(%)', 
        'human-ai_collaboration_rate_(%)',
        'consumer_trust_in_ai_(%)', 
        'market_share_of_ai_companies_(%)'
    ]
    
    industry_metrics = df.groupby('industry')[metrics].mean().sort_values(by='ai_adoption_rate_(%)', ascending=False)
    print("\nAverage metrics by industry (sorted by adoption rate):")
    print(industry_metrics.round(2))
    
    # Find which industries have the highest content volume per adoption rate
    df['content_efficiency'] = df['ai-generated_content_volume_(tbs_per_year)'] / df['ai_adoption_rate_(%)']
    
    industry_content_efficiency = df.groupby('industry')[['content_efficiency']].mean().sort_values(by='content_efficiency', ascending=False)
    print("\nIndustries ranked by content generation efficiency (volume / adoption rate):")
    print(industry_content_efficiency.round(2))
    
    # Analyze which tools are preferred in different industries
    industry_tools = pd.crosstab(
        df['industry'], 
        df['top_ai_tools_used'], 
        normalize='index'
    ) * 100  # Convert to percentage
    
    print("\nPercentage distribution of AI tools by industry:")
    print(industry_tools.round(1))
    
    # Find the most profitable industries (revenue increase - job loss)
    df['net_benefit'] = df['revenue_increase_due_to_ai_(%)'] - df['job_loss_due_to_ai_(%)']
    
    industry_net_benefit = df.groupby('industry')[['net_benefit', 'revenue_increase_due_to_ai_(%)', 'job_loss_due_to_ai_(%)']].mean().sort_values(by='net_benefit', ascending=False)
    print("\nIndustries ranked by net benefit (revenue increase - job loss):")
    print(industry_net_benefit.round(2))

# ===============================================================
# PART 5: MAIN FUNCTION
# ===============================================================

def main():
    """
    Main function to run the entire analysis pipeline.
    """
    # Your specific file path
    file_path = r'C:\Users\vinee\OneDrive\Documents\Github\tech501-preassignment\Data Pathway notes\Global_AI_Content_Impact_Dataset.csv'
    
    print("\n" + "="*50)
    print("GLOBAL AI CONTENT IMPACT ANALYSIS")
    print("="*50)
    print(f"\nAnalyzing data from: {file_path}")
    
    # Load and clean data
    df = load_and_clean_data(file_path)
    
    if df is None:
        print("\nError: Unable to proceed with analysis due to issues with the dataset.")
        return
    
    # Perform exploratory data analysis
    perform_eda(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Perform advanced analysis
    perform_advanced_analysis(df)
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE")
    print("="*50)
    print("\nAll analyses and visualizations have been successfully completed.")
    print("Visualizations are saved in the 'visualizations' folder.")

# Run the main function
if __name__ == "__main__":
    main()