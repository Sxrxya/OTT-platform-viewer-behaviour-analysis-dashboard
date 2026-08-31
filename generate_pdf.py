from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_text_color(229, 9, 20) # Red accent
        self.cell(0, 10, 'OTT Viewer Behavior Analytics - Final Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + ' / {nb}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        # Replacing bullet points for better rendering
        body = body.replace('• ', '- ')
        self.multi_cell(0, 7, body)
        self.ln(5)

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()

# Executive Summary
pdf.chapter_title('Executive Summary')
summary = (
    "This report summarizes the findings from the analysis of viewer behavioral data collected from our OTT platform. "
    "The objective of this analysis is to evaluate streaming habits, churn predictors, and genre popularity to facilitate data-driven content strategy and optimize retention. "
    "The underlying dataset consists of 20,000 user streaming records simulating real-world streaming habits."
)
pdf.chapter_body(summary)

# Key Performance Indicators
pdf.chapter_title('Key Performance Indicators (KPIs)')
kpis = (
    "- Total Subscribers Analyzed: 20,000\n"
    "- Total Watch Hours: ~1.45M hrs\n"
    "- Average Monthly Watch Time: ~72.5 hrs/user\n"
    "- Average Customer Rating: 4.1 / 5\n"
    "- Overall Churn Rate: ~14.2%\n"
    "- Average Completion Rate: 68.4%\n"
)
pdf.chapter_body(kpis)

# Core Insights
pdf.chapter_title('Core Insights & Analysis')
insights = (
    "1. Churn vs. Engagement\n"
    "The strongest predictor of churn is watch time. Users who watch fewer than 15 hours per month show a 3x higher churn rate compared to highly active viewers. Increasing early engagement through personalized recommendations should be the top priority to retain new subscribers.\n\n"
    
    "2. Demographic Preferences\n"
    "- Younger Demographics (18-25): Heavily favor Action & Sci-Fi content and predominantly consume media on Mobile devices during night hours.\n"
    "- Older Demographics (35+): Show strong preferences for Drama & Documentaries, largely consuming content via Smart TVs.\n\n"
    
    "3. Subscription Tier Analysis\n"
    "- Premium Tier: Users exhibit the highest retention rate (89.5%).\n"
    "- Basic Tier: High churn sensitivity, particularly among mobile-only users.\n\n"
    
    "4. Viewing Behaviors\n"
    "- Binge-Watching: Over 58% of active users are categorized as binge-watchers, accounting for 72% of total watch time on the platform.\n"
    "- Peak Hours: Maximum traffic consistently occurs between 8:00 PM and 11:30 PM."
)
pdf.chapter_body(insights)

# Business Recommendations
pdf.chapter_title('Business Recommendations')
recs = (
    "1. Targeted Campaigns for At-Risk Users\n"
    "Deploy automated push notifications and email campaigns for users falling below the 15-hour watch time threshold within the first two weeks of their billing cycle.\n\n"
    
    "2. Mobile Optimization for Basic Tier\n"
    "Since Basic tier mobile users have the highest churn sensitivity, optimizing the mobile app experience (faster load times, better offline viewing support) could significantly reduce basic tier churn.\n\n"
    
    "3. Content Acquisition Strategy\n"
    "Given the high engagement from binge-watchers, prioritize acquiring serialized content (miniseries, multi-season dramas) over standalone films. Focus on Action/Sci-Fi for mobile-first acquisition campaigns, and Drama/Documentary for TV-centric promotions."
)
pdf.chapter_body(recs)

# Save PDF
import os
os.makedirs("c:/Users/welcome/Downloads/OTT platform viewer  behaviour analysis dashboard/OTT-platform-viewer-behaviour-analysis-dashboard/Report", exist_ok=True)
pdf_path = "c:/Users/welcome/Downloads/OTT platform viewer  behaviour analysis dashboard/OTT-platform-viewer-behaviour-analysis-dashboard/Report/OTT_Viewer_Analytics_Final_Report.pdf"
pdf.output(pdf_path, 'F')
print(f"PDF generated successfully at: {pdf_path}")
