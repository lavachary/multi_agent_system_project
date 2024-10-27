# Define fetch_datasets_for_use_case function to retrieve dataset links
def fetch_datasets_for_use_case(use_case):
    # This generates a search link on Kaggle for the use case
    kaggle_link = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    return kaggle_link

# Function to generate a report in Markdown format
def generate_report(use_cases, datasets):
    with open("final_report.md", "w") as file:
        file.write("# AI Use Case Proposal Report for Deloitte\n\n")
        for use_case, dataset in zip(use_cases, datasets):
            file.write(f"- **{use_case}**\n  - [Dataset]({dataset})\n")

# Test the function
if __name__ == "__main__":
    use_cases = ["Customer Segmentation", "Predictive Analytics for Risk Management"]
    datasets = [fetch_datasets_for_use_case(use_case) for use_case in use_cases]
    generate_report(use_cases, datasets)
    print("Report generated as final_report.md")
