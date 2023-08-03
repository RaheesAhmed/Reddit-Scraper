import requests

def get_reddit_data(subreddit, num_posts):
    # Replace 'YOUR_REDDIT_API_KEY' with your actual Reddit API key
    headers = {'User-Agent': 'My Reddit Scraper', 'Authorization': 'bearer YOUR_REDDIT_API_KEY'}
    base_url = 'https://oauth.reddit.com'

    # API endpoint for listing top posts in a subreddit
    endpoint = f'{base_url}/r/{subreddit}/top?limit={num_posts}'

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data from the Reddit API. Status code: {response.status_code}")
        return None

def parse_reddit_data(data):
    if data and 'data' in data and 'children' in data['data']:
        posts = data['data']['children']
        parsed_data = []

        for post in posts:
            post_data = post['data']
            parsed_data.append({
                'title': post_data['title'],
                'score': post_data['score'],
                'author': post_data['author'],
                'created_utc': post_data['created_utc'],
                'num_comments': post_data['num_comments'],
                # Add more fields as needed
            })

        return parsed_data
    else:
        print("Error: Invalid data format or missing data.")
        return None

if __name__ == "__main__":
    subreddit = "Python"  # Replace this with the subreddit of your choice
    num_posts = 10        # Number of posts to retrieve

    data = get_reddit_data(subreddit, num_posts)
    if data:
        parsed_data = parse_reddit_data(data)
        print(parsed_data)
