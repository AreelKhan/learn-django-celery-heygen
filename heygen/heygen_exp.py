import requests
import json
import os

def generate_video(
        api_key,
        input_text,
        avatar_id="Vanessa-insuit-20220722",
        voice_id="1bd001e7e50f421d891986aad5158bc8",
        background_color="#008000"
        ):
    url = 'https://api.heygen.com/v2/video/generate'
    
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": input_text,
                    "voice_id": voice_id
                },
                "background": {
                    "type": "color",
                    "value": background_color
                }
            }
        ],
        "dimension": {
            "width": 1280,
            "height": 720
        },
        "aspect_ratio": "16:9",
        "test": True,
        "caption": True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_video_status(api_key, video_id):
    url = f'https://api.heygen.com/v1/video_status.get?video_id={video_id}'
    
    headers = {
        'X-Api-Key': api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data['data']['status'] == 'completed':
            return {
                'status': 'completed',
                'video_url': response_data['data']['video_url'],
                'caption_url': response_data['data']['caption_url'],
                'thumbnail_url': response_data['data']['thumbnail_url'],
                'duration': response_data['data']['duration'],
                'video_id': response_data['data']['id']
            }
        else:
            return {
                'status': response_data['data']['status'],
                'message': 'Video is not available.'
            }
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    heygen_api_key = os.getenv('heygen-trial-token')
    
    # video_response = generate_video(
    #     api_key=heygen_api_key,
    #     input_text="Welcome to the HeyGen API!",
    #     avatar_id="Daisy-inskirt-20220818",
    #     voice_id="2d5b0e6cf36f460aa7fc47e3eee4ba54"
    # )
    
    # print(video_response)

    video_id = "5925ddef813b4125b84050a63870b1ee"
    video_status = get_video_status(heygen_api_key, video_id)
    print(video_status)


