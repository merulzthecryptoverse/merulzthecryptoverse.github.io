import requests
from bs4 import BeautifulSoup

# URL of the Dimsum Daily homepage
url = 'https://www.dimsumdaily.hk/'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <h3> tags (headlines are in <h3>)
headlines = soup.find_all('h3')

# Prepare markdown content
markdown_content = '# Latest Headlines from Dimsum Daily HK\n\n'

# Limit to the first 10 headlines
for h in headlines[:10]:
    if h.a:  # Ensure it has a link
        title = h.a.text.strip()
        link = h.a['href']
        
        # Get the next sibling, which should be the date and description text
        next_sibling = h.next_sibling
        if next_sibling and isinstance(next_sibling, str):
            date_desc = next_sibling.strip()
        else:
            # If not direct text, try the next element's text
            next_elem = h.find_next_sibling()
            date_desc = next_elem.text.strip() if next_elem else ''
        
        # Add to markdown (truncate description for brevity)
        markdown_content += f'- [{title}]({link}) - {date_desc[:100]}...\n'

# Print the markdown (you can copy this to your GitHub README.md)
print(markdown_content)

# Optionally, write to a file for easy inclusion in GitHub
with open('headlines.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("Markdown file 'headlines.md' generated. You can add this to your GitHub repository's README or a GitHub Pages site.")
print("To automate updates, consider setting up a GitHub Actions workflow to run this script periodically and commit the updated headlines.md.")