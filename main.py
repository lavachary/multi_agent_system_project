from Research_agent.research_agent import fetch_deloitte_info
from Use_case_agent.usecase_agent import generate_use_cases  # Make sure you have this function defined
from Resource_collection_agent.resource_agent import fetch_datasets_for_use_case  # Same here
from Report_agent.report_agent import generate_report

def main():
    # Step 1: Research Agent
    deloitte_info = fetch_deloitte_info()
    print("Fetched Deloitte Information:\n", deloitte_info)
    
    # Step 2: Generate AI/ML Use Cases (Assuming you have an industry data or similar)
    use_cases = generate_use_cases(deloitte_info)  # This function should be defined in your Use case agent
    print("Generated Use Cases:\n", use_cases)
    
    # Step 3: Collect Datasets for Each Use Case
    datasets = [fetch_datasets_for_use_case(use_case) for use_case in use_cases]  # Assuming this function is defined
    print("Fetched Datasets:\n", datasets)
    
    # Step 4: Generate Report
    generate_report(use_cases, datasets)
    print("Report generated as final_report.md")

if __name__ == "__main__":
    main()
