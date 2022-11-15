import requests
import os


def download_data(url, target_path):
    if not os.path.exists(target_path):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'cookie': 'session=add your session id here'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(target_path, 'w') as f:
                f.write(response.text)
            print('Data downloaded')
            return True
        else:
            print('Download failed with status code:', response.status_code)
            return False
    else:
        print('File already exist. Skipping download')
        return True
    

def get_data(day):
    target_path = f'data/d{day}_data.txt'
    if not os.path.exists(target_path):
        url = f'https://adventofcode.com/2021/day/{day}/input'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'cookie': 'session=add your session id here'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(target_path, 'w') as f:
                f.write(response.text)
            print('Data downloaded')
        else:
            print('Download failed with status code:', response.status_code)
            return False
    else:
        print('File already exist. Skipping download')
    with open(target_path, 'r') as f:
        lines = f.readlines()
    return lines