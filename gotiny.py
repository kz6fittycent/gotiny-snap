#!/usr/bin/env python3

import argparse
import re
import requests
import sys

def shorten_url(url):
    # Set up API endpoint and payload
    api_url = 'https://tinyurl.com/api-create.php'
    payload = {'url': url}

    # Send POST request to API endpoint
    response = requests.post(api_url, data=payload)

    # Extract the shortened URL from the response
    match = re.search(r'(https?://tinyurl\.com/\S+)', response.text)
    if match:
        short_url = match.group(1)
        return short_url
    else:
        print(f'Error: Could not extract short URL from response: {response.text}', file=sys.stderr)
        return None

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A tiny URL generator')
    parser.add_argument('url', nargs='?', help='URL to shorten')
    parser.add_argument('--menu', '-m', action='store_true', help='Display a menu')
    args = parser.parse_args()

    if args.menu:
        print('Gotiny Help Menu:')
        print('------------------')
        print('h - Display this help menu')
        print('n - Add another URL to shorten')
        print('q - Quit the program')
        return

    while True:
        if not args.url:
            url = input('Enter a URL to shorten: ')
        else:
            url = args.url

        # Check if the user wants to quit
        if url == 'q':
            print('Quitting Gotiny...')
            break

        # Check if the user wants to display the help menu
        if url == 'h':
            print('Gotiny Help Menu:')
            print('------------------')
            print('h - Display this help menu')
            print('n - Add another URL to shorten')
            print('q - Quit the program')
            continue

        # Shorten the URL
        short_url = shorten_url(url)
        if short_url:
            print(f'{short_url}')

        # Ask the user if they want to add another URL
        choice = input('Add another URL to shorten? (y/n): ')
        if choice.lower() != 'y':
            break
        args.url = input('Enter a URL to shorten: ')

if __name__ == '__main__':
    main()

