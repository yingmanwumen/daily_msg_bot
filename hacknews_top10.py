import requests


def fetch_top_stories():
    # Fetch top story IDs
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()[:10]  # Get top 10 story IDs

    stories = []
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story_data = story_response.json()
        stories.append(story_data)

    return stories


def format_stories_to_markdown(stories):
    markdown_output = "# Top 10 Hacker News Stories\n\n"
    for story in stories:
        title = story.get("title", "No Title")
        url = story.get("url", "No URL")
        author = story.get("by", "Unknown Author")
        score = story.get("score", "No Score")
        markdown_output += f"- [{title}]({url})\n"
        markdown_output += f"**Author:** {author}  \n"
        markdown_output += f"**Score:** {score}  \n\n"

    return markdown_output


if __name__ == "__main__":
    stories = fetch_top_stories()
    markdown = format_stories_to_markdown(stories)
    print(markdown)
