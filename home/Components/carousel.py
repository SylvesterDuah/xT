# carousel.py
import requests

class Carousel:
    def __init__(self, user_location=''):
        self.user_location = user_location

    def fetch_news(self):
        # Define API endpoints for different news sources
        api_endpoints = {
            'Bloomberg': 'https://example.com/bloomberg-api',
            'WallStreet': 'https://example.com/wallstreet-api',
            'WashingtonPost': 'https://example.com/washingtonpost-api',
        }

        # Fetch news based on the user's location
        selected_api = api_endpoints.get(self.user_location, None)

        if selected_api:
            try:
                response = requests.get(selected_api)
                data = response.json()
                # Extract and return relevant news information
                news_items = self.extract_news(data)
                return news_items
            except requests.RequestException as e:
                print(f"Error fetching news: {e}")

        return []

    def extract_news(self, data):
        # Extract relevant information from the API response
        # Modify this based on the actual API response structure
        news_items = []
        for item in data.get('articles', []):
            title = item.get('title', '')
            description = item.get('description', '')
            news_items.append({'title': title, 'description': description})

        return news_items
    

    def deals_of_the_week(self):
        # Define API endpoint for deals of the week
        deals_endpoint = 'https://example.com/deals-of-the-week-api'

        try:
            response = requests.get(deals_endpoint)
            data = response.json()
            # Extract and return relevant deals information
            deals_items = self.extract_deals(data)
            return deals_items
        except requests.RequestException as e:
            print(f"Error fetching deals of the week: {e}")

        return []

    def extract_deals(self, data):
        # Extract relevant information from the API response for deals
        # Modify this based on the actual API response structure
        deals_items = []
        for item in data.get('deals', []):
            product_name = item.get('product_name', '')
            discount_percentage = item.get('discount_percentage', '')
            deals_items.append({'product_name': product_name, 'discount_percentage': discount_percentage})

        return deals_items
        