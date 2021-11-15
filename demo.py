import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.instagram.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.instagram.com/',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6,ar;q=0.5',
    'cookie': 'mid=YYWhrwALAAF8YjzUDSj18rNanRRv; ig_did=C5BE9DB6-58B2-4016-9669-8E1ADC1D09AB; fbm_124024574287414=base_domain=.instagram.com; datr=vvCMYaETZqIUJsKlAMXcyd3Y; ig_direct_region_hint="CLN\\0542951722125\\0541668197163:01f71d81d25c9fd0ea8707bb5f9bea199ef6a9ff4c4cb0a7d856e05f0f1a3c513ebc1ccf"; shbid="8160\\0542951722125\\0541668243020:01f7657d8ca0e3b043526ef989d42699133fa571837c0018c56d19b409ae77454bcd0087"; shbts="1636707020\\0542951722125\\0541668243020:01f72a71b235986df858df18d21b1b1ee18e9f357bdaeb9391a0e173431e7cd092149160"; fbsr_124024574287414=jYE-5PNhXYvGXISkzoRnM-UoJbk8aQX4Gn-a2pX4aS8.eyJ1c2VyX2lkIjoiMTAwMDAzMjE1ODQ0Njk1IiwiY29kZSI6IkFRQ2ViTWpZTzB1RmJQbENXNDllV2tfSjNfcUtjeDVqOE85VF9QOG0tNHgwczY0NGM0R3U0ZTlxR194YWlyTjJPNXZXZTRQT05yYS1PY3l0Ukd1YlZjV1pUd1dxVmczZFNfREh5YkxXOVBfNUY5OEt3MEdTSThBUnpqVXdfZHg4Y3pkdGlEb2hEaXBhNHhJejdGaWpoM1FkZkVJaE5EcFdrdTZxeWg2V2Y1aEJVTjdwWTF2VTliVHd1ZTgzN2hiUEFaQkdnNHQybHlXV1d0eTdSYmpYOVJuR2xGS0UwUk1lb1VYcEFRdFB2MFBzdy14QzNhNWVFaWVIY18ySmFWNE1acTQ2QWc1R1JyR0JpM0ZsT3ZkTUxXUHdkRmdDSTNUQ1JmNlpkU190aDhzTHFDdFJoby1BYW1KSWhHZmo4emZaSzRYanY5VzE3dGdvVExheGJzT0RvOGlJIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFtbVhFZXR4ejgxaERMdzVPd3VycVpDbzY4aGpaQkdaQVdYM2gwZ2JOU2xIakFNQm9IOVk1NWptRE5OUVhEYlB6VnFjOVYwMUNMUmpGNXJlck5VS1FCdUNSUXpTTEZtdzMzamZscVpCUUtKdHU4Y1ZYRlF5ZUc5aGxOUGNJb1BQVXJQQU9FcDNQanJla0VkdE5VUFRXbmRsWEJaQVJiaEJ0RHVDc3oyayIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjM2NzEwNzI2fQ; fbsr_124024574287414=jYE-5PNhXYvGXISkzoRnM-UoJbk8aQX4Gn-a2pX4aS8.eyJ1c2VyX2lkIjoiMTAwMDAzMjE1ODQ0Njk1IiwiY29kZSI6IkFRQ2ViTWpZTzB1RmJQbENXNDllV2tfSjNfcUtjeDVqOE85VF9QOG0tNHgwczY0NGM0R3U0ZTlxR194YWlyTjJPNXZXZTRQT05yYS1PY3l0Ukd1YlZjV1pUd1dxVmczZFNfREh5YkxXOVBfNUY5OEt3MEdTSThBUnpqVXdfZHg4Y3pkdGlEb2hEaXBhNHhJejdGaWpoM1FkZkVJaE5EcFdrdTZxeWg2V2Y1aEJVTjdwWTF2VTliVHd1ZTgzN2hiUEFaQkdnNHQybHlXV1d0eTdSYmpYOVJuR2xGS0UwUk1lb1VYcEFRdFB2MFBzdy14QzNhNWVFaWVIY18ySmFWNE1acTQ2QWc1R1JyR0JpM0ZsT3ZkTUxXUHdkRmdDSTNUQ1JmNlpkU190aDhzTHFDdFJoby1BYW1KSWhHZmo4emZaSzRYanY5VzE3dGdvVExheGJzT0RvOGlJIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFtbVhFZXR4ejgxaERMdzVPd3VycVpDbzY4aGpaQkdaQVdYM2gwZ2JOU2xIakFNQm9IOVk1NWptRE5OUVhEYlB6VnFjOVYwMUNMUmpGNXJlck5VS1FCdUNSUXpTTEZtdzMzamZscVpCUUtKdHU4Y1ZYRlF5ZUc5aGxOUGNJb1BQVXJQQU9FcDNQanJla0VkdE5VUFRXbmRsWEJaQVJiaEJ0RHVDc3oyayIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjM2NzEwNzI2fQ; csrftoken=UaZsui656PCtugfgEl9d7kcouiNVcEWv; ds_user_id=2951722125; sessionid=2951722125%3APcKvN4NAlInGAH%3A7; rur="RVA\\0542951722125\\0541668247129:01f7a1c07b8562d0657cee8c5ea1b192b9abe5d1d8c2f818b6d205e82a8c9744af9a5725"',
    'username': 'ziad_ouchary01',
    'password': '18072001Ouchary.01'
}

try:
    response = requests.get('https://www.instagram.com/', headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(soup)


except Exception as ex:
    print(ex)
