import requests
from bs4 import BeautifulSoup

def fetch_deloitte_info():
    url = "https://en.wikipedia.org/wiki/Deloitte"
    
    try:
        response = requests.get(url)
        print(f"HTTP Status Code: {response.status_code}") 
        response.raise_for_status()
        
        
        print("HTML Content Preview:\n", response.text[:500])  
        
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        paragraphs = soup.find_all('p')
        print(f"Number of paragraphs found: {len(paragraphs)}")  

        
        if paragraphs:
            full_text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
            return full_text
        else:
            print("No paragraphs found on the page.")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching information: {e}")
        return ""

# Test the function
if __name__ == "__main__":
    deloitte_info = fetch_deloitte_info()
    if deloitte_info:
        print("Deloitte Information:\n", deloitte_info)
    else:
        print("No information extracted.")
