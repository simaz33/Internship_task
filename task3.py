import requests
import sys

url = 'https://api.github.com/emojis'

def get_emoji_image(emoji_name):
    emojis = requests.get(url).json()

    if emoji_name not in emojis.keys():
        print('The image was not found')
        exit()

    emoji_url = emojis[emoji_name]

    emoji_response = requests.get(emoji_url, stream=True)

    with open(sys.argv[1] + '.png', 'wb') as image:
        for chunk in emoji_response.iter_content(chunk_size=512):
            image.write(chunk)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No image specified')
        exit()

    get_emoji_image(sys.argv[1])
