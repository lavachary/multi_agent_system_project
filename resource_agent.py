def fetch_datasets_for_use_case(use_case):
    # Construct a search link for each use case to Kaggle
    kaggle_link = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    return kaggle_link

# Test the function
if __name__ == "__main__":
    use_cases = ["Customer Segmentation", "Predictive Analytics for Risk Management"]
    for use_case in use_cases:
        print(f"Dataset link for {use_case}: {fetch_datasets_for_use_case(use_case)}")
