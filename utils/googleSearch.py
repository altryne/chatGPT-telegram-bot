from serpapi import GoogleSearch
import os
import json
import dotenv
dotenv.load_dotenv()

def googleSearch(query):
  # results = get_test_response()
  # return parse_response(query, results)


  params = {
    "q": query,
    "hl": "en",
    "gl": "us",
    "api_key": os.getenv("SERP_API_KEY")
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  print(f"Got google search results for {query}")
  print(json.dumps(results, indent=2))

  parsed_response = parse_response(query, results)
  print(parsed_response)
  return parsed_response


def get_test_response():
  json_string = {
  "search_metadata": {
    "id": "638bc233d5ecf4de2dc0ff46",
    "status": "Success",
    "json_endpoint": "https://serpapi.com/searches/95fb0952cce08a03/638bc233d5ecf4de2dc0ff46.json",
    "created_at": "2022-12-03 21:40:03 UTC",
    "processed_at": "2022-12-03 21:40:03 UTC",
    "google_url": "https://www.google.com/search?q=+summarize+the+outcome+of+world+cup+games+in+the+last+two+days&oq=+summarize+the+outcome+of+world+cup+games+in+the+last+two+days&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
    "raw_html_file": "https://serpapi.com/searches/95fb0952cce08a03/638bc233d5ecf4de2dc0ff46.html",
    "total_time_taken": 1.99
  },
  "search_parameters": {
    "engine": "google",
    "q": " summarize the outcome of world cup games in the last two days",
    "google_domain": "google.com",
    "hl": "en",
    "gl": "us",
    "device": "desktop"
  },
  "search_information": {
    "organic_results_state": "Results for exact spelling",
    "query_displayed": "summarize the outcome of world cup games in the last two days",
    "total_results": 56100000,
    "time_taken_displayed": 0.67
  },
  "related_questions": [
    {
      "question": "Which team is eliminated from World Cup 2022?",
      "snippet": "The U.S. men's national soccer team was eliminated from the World Cup after a thrilling 3-1 loss to The Netherlands on Saturday, ending the team's hopes of advancing past the round of 16\u2014as the team continues its decades-long search for its first World Cup victory.",
      "title": "U.S. Men's Team Eliminated From World Cup In 3-1 Loss To ... - Forbes",
      "date": "5 hours ago",
      "link": "https://www.forbes.com/sites/brianbushard/2022/12/03/us-mens-team-eliminated-from-world-cup-in-3-1-loss-to-netherlands/",
      "displayed_link": "https://www.forbes.com \u203a sites \u203a brianbushard \u203a 2022/12/03",
      "next_page_token": "eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hpY2ggdGVhbSBpcyBlbGltaW5hdGVkIGZyb20gV29ybGQgQ3VwIDIwMjI/IiwibGsiOiJHaXgzYUdsamFDQjBaV0Z0SUdseklHVnNhVzFwYm1GMFpXUWdabkp2YlNCM2IzSnNaQ0JqZFhBZ01qQXlNZyIsImJzIjoiYzJYTXNRckNNQlJHWVZ3ek9YWnctRjFjUkpDQWkwc1JvZFFueU9yRnBDYVE1SmJtbG03T0RrNi1tSzhrT0FqaWV2ZzRTcXVOOGVIaUlZNFNRb0dMSVlWTTRpeTZnUk1NRDlIaU9QYlFXNjNyNm41VFM3VXduakZ4Um5OcURuX2sxYXE5MmhsUGdpbkVDRTk5N3pLRUlkNmhDTmt3cGdMcXhBMmY5QjNVMWRPcnRWcTFQQ0Z5dnNLeUs3OEVWMG9Pa1lyVTFlTThuNzBCIn0=",
      "serpapi_link": "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hpY2ggdGVhbSBpcyBlbGltaW5hdGVkIGZyb20gV29ybGQgQ3VwIDIwMjI%2FIiwibGsiOiJHaXgzYUdsamFDQjBaV0Z0SUdseklHVnNhVzFwYm1GMFpXUWdabkp2YlNCM2IzSnNaQ0JqZFhBZ01qQXlNZyIsImJzIjoiYzJYTXNRckNNQlJHWVZ3ek9YWnctRjFjUkpDQWkwc1JvZFFueU9yRnBDYVE1SmJtbG03T0RrNi1tSzhrT0FqaWV2ZzRTcXVOOGVIaUlZNFNRb0dMSVlWTTRpeTZnUk1NRDlIaU9QYlFXNjNyNm41VFM3VXduakZ4Um5OcURuX2sxYXE5MmhsUGdpbkVDRTk5N3pLRUlkNmhDTmt3cGdMcXhBMmY5QjNVMWRPcnRWcTFQQ0Z5dnNLeUs3OEVWMG9Pa1lyVTFlTThuNzBCIn0%3D"
    },
    {
      "question": "Who won FIFA World Cup 2022?",
      "snippet": "FULL TIME | ARGENTINA 2 - 1 AUSTRALIA Australia gave it their all and came very close to equalising right at the death but the Argentinian defence stood tall and ensured safe passage to the last-8.",
      "title": "FIFA World Cup 2022, Argentina vs Australia Live Updates",
      "date": "16 mins ago",
      "link": "https://www.cnbctv18.com/sports/fifa-world-cup-qatar-live-updates-netherlands-vs-usa-argentina-vs-australia-15324771.htm",
      "displayed_link": "https://www.cnbctv18.com \u203a sports \u203a fifa-world-cup-qatar...",
      "next_page_token": "eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hvIHdvbiBGSUZBIFdvcmxkIEN1cCAyMDIyPyIsImxrIjoiR2h0M2FHOGdkMjl1SUdacFptRWdkMjl5YkdRZ1kzVndJREl3TWpJIiwiYnMiOiJjMlhNc1FyQ01CUkdZVnd6T1hady1GMWNSSkNBaTBzUm9kUW55T3JGcENhUTVKYm1sbTdPRGs2LW1LOGtPQWppZXZnNFNxdU44ZUhpSVk0U1FvR0xJWVZNNGl5NmdSTU1EOUhpT1BiUVc2M3I2bjVUUzdVd25qRnhSbk5xRG5fazFhcTkyaGxQZ2luRUNFOTk3ektFSWQ2aENOa3dwZ0xxeEEyZjlCM1UxZE9ydFZxMVBDRnl2c0t5Szc4RVYwb09rWXJVMWVNOG43MEIifQ==",
      "serpapi_link": "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hvIHdvbiBGSUZBIFdvcmxkIEN1cCAyMDIyPyIsImxrIjoiR2h0M2FHOGdkMjl1SUdacFptRWdkMjl5YkdRZ1kzVndJREl3TWpJIiwiYnMiOiJjMlhNc1FyQ01CUkdZVnd6T1hady1GMWNSSkNBaTBzUm9kUW55T3JGcENhUTVKYm1sbTdPRGs2LW1LOGtPQWppZXZnNFNxdU44ZUhpSVk0U1FvR0xJWVZNNGl5NmdSTU1EOUhpT1BiUVc2M3I2bjVUUzdVd25qRnhSbk5xRG5fazFhcTkyaGxQZ2luRUNFOTk3ektFSWQ2aENOa3dwZ0xxeEEyZjlCM1UxZE9ydFZxMVBDRnl2c0t5Szc4RVYwb09rWXJVMWVNOG43MEIifQ%3D%3D"
    },
    {
      "question": "What will happen to the stadiums after the World Cup?",
      "snippet": "Accordingly, the tournament organizers have pledged to build stadiums with modular elements, which will be reconfigured after the tournament to provide a lasting legacy for the FIFA World Cup 2022 far beyond Qatar's borders.",
      "title": "World Cup Stadiums in Qatar 2022 - Hukoomi",
      "link": "https://hukoomi.gov.qa/en/article/world-cup-stadiums",
      "displayed_link": "https://hukoomi.gov.qa \u203a article \u203a world-cup-stadiums",
      "next_page_token": "eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hhdCB3aWxsIGhhcHBlbiB0byB0aGUgc3RhZGl1bXMgYWZ0ZXIgdGhlIFdvcmxkIEN1cD8iLCJsayI6ImM1TXlLYzlJTEZFb3o4ekpVY2hJTENoSXpWTW95VmNveVVoVktDNUpUTWtzelMxV1NFd3JTUzBDQzVYbkYtV2tLQ1NYRmdBQSIsImJzIjoiYzJYTXNRckNNQlJHWVZ3ek9YWnctRjFjUkpDQWkwc1JvZFFueU9yRnBDYVE1SmJtbG03T0RrNi1tSzhrT0FqaWV2ZzRTcXVOOGVIaUlZNFNRb0dMSVlWTTRpeTZnUk1NRDlIaU9QYlFXNjNyNm41VFM3VXduakZ4Um5OcURuX2sxYXE5MmhsUGdpbkVDRTk5N3pLRUlkNmhDTmt3cGdMcXhBMmY5QjNVMWRPcnRWcTFQQ0Z5dnNLeUs3OEVWMG9Pa1lyVTFlTThuNzBCIn0=",
      "serpapi_link": "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiV2hhdCB3aWxsIGhhcHBlbiB0byB0aGUgc3RhZGl1bXMgYWZ0ZXIgdGhlIFdvcmxkIEN1cD8iLCJsayI6ImM1TXlLYzlJTEZFb3o4ekpVY2hJTENoSXpWTW95VmNveVVoVktDNUpUTWtzelMxV1NFd3JTUzBDQzVYbkYtV2tLQ1NYRmdBQSIsImJzIjoiYzJYTXNRckNNQlJHWVZ3ek9YWnctRjFjUkpDQWkwc1JvZFFueU9yRnBDYVE1SmJtbG03T0RrNi1tSzhrT0FqaWV2ZzRTcXVOOGVIaUlZNFNRb0dMSVlWTTRpeTZnUk1NRDlIaU9QYlFXNjNyNm41VFM3VXduakZ4Um5OcURuX2sxYXE5MmhsUGdpbkVDRTk5N3pLRUlkNmhDTmt3cGdMcXhBMmY5QjNVMWRPcnRWcTFQQ0Z5dnNLeUs3OEVWMG9Pa1lyVTFlTThuNzBCIn0%3D"
    },
    {
      "question": "How long does the World Cup game last?",
      "snippet": "How long is a World Cup match? Soccer games are 90 minutes, not accounting for stoppage time. World Cup matches have two 45-minute halves, but games have regularly been stretching past 100 minutes because of added time from referees.",
      "title": "How long is a soccer game in the World Cup? - 10TV",
      "date": "7 hours ago",
      "link": "https://www.10tv.com/article/news/nation-world/how-long-is-a-world-cup-soccer-game-stoppages-extra-time-no-ties/507-bc237ca7-6748-48a1-9615-1f9bacf30a7f",
      "displayed_link": "https://www.10tv.com \u203a article \u203a news \u203a nation-world \u203a h...",
      "next_page_token": "eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiSG93IGxvbmcgZG9lcyB0aGUgV29ybGQgQ3VwIGdhbWUgbGFzdD8iLCJsayI6IkdpVm9iM2NnYkc5dVp5QmtiMlZ6SUhSb1pTQjNiM0pzWkNCamRYQWdaMkZ0WlNCc1lYTjAiLCJicyI6ImMyWE1zUXJDTUJSR1lWd3pPWFp3LUYxY1JKQ0FpMHNSb2RRbnlPckZwQ2FRNUpibWxtN09EazYtbUs4a09Bamlldmc0U3F1TjhlSGlJWTRTUW9HTElZVk00aXk2Z1JNTUQ5SGlPUGJRVzYzcjZuNVRTN1V3bmpGeFJuTnFEbl9rMWFxOTJobFBnaW5FQ0U5OTd6S0VJZDZoQ05rd3BnTHF4QTJmOUIzVTFkT3J0VnExUENGeXZzS3lLNzhFVjBvT2tZclUxZU04bjcwQiJ9",
      "serpapi_link": "https://serpapi.com/search.json?device=desktop&engine=google_related_questions&google_domain=google.com&next_page_token=eyJvbnMiOiI2MjAiLCJmYyI6IkVxQUJDbUpCUVhSV2JHSkVUa1pvVXpKeE9HbHFUbEoyV2tNM2FuSldTa2hETUZsQlVVVTFjVmhIWlZKalppMVRUM2hzYW5GdGEyRkVNbWxrVGtGbk5VODNZa0UxWDBGRFlsTTBiRmxFUldoT2VUZEhTMEl5V2pSb1VHWlZUR0owYkhoTk9IaEtaeElXVGsxTFRGazRaalZPYzI0MmQxRlBaMTgwUkRSQlVSb2lRVVJWZVVWSFl6SldTVzVYVEZkMWNFSmxXVUYzV0daek1FSmZRbFZIUkZkRFp3IiwiZmN2IjoiMyIsImVpIjoiTk1LTFk4ZjVOc242d1FPZ180RDRBUSIsInFjIjoiYy1PeUxTN056VTBzeXF4S1ZTakpTRlhJTHkxSnpzOEYwbWtLNWZsRk9Ta0t5YVVGQ3VtSnVhbkZDcGw1WUJVNWljVWxDaVhsLVFvcGlaWEZBZ3kxUHJiSzlnQSIsInF1ZXN0aW9uIjoiSG93IGxvbmcgZG9lcyB0aGUgV29ybGQgQ3VwIGdhbWUgbGFzdD8iLCJsayI6IkdpVm9iM2NnYkc5dVp5QmtiMlZ6SUhSb1pTQjNiM0pzWkNCamRYQWdaMkZ0WlNCc1lYTjAiLCJicyI6ImMyWE1zUXJDTUJSR1lWd3pPWFp3LUYxY1JKQ0FpMHNSb2RRbnlPckZwQ2FRNUpibWxtN09EazYtbUs4a09Bamlldmc0U3F1TjhlSGlJWTRTUW9HTElZVk00aXk2Z1JNTUQ5SGlPUGJRVzYzcjZuNVRTN1V3bmpGeFJuTnFEbl9rMWFxOTJobFBnaW5FQ0U5OTd6S0VJZDZoQ05rd3BnTHF4QTJmOUIzVTFkT3J0VnExUENGeXZzS3lLNzhFVjBvT2tZclUxZU04bjcwQiJ9"
    }
  ],
  "organic_results": [
    {
      "position": 1,
      "title": "World Cup 2022 summary: 1 December 2022 - AS USA",
      "link": "https://en.as.com/soccer/world-cup-2022-live-online-game-and-team-updates-n-3/",
      "displayed_link": "https://en.as.com \u203a Soccer",
      "date": "2 days ago",
      "snippet": "World Cup headlines: Thursday, 1 December 2022. - Madness in Group E as Japan and Spain go through, Germany go home. - Match summaries of ...",
      "snippet_highlighted_words": [
        "World Cup",
        "Match"
      ],
      "about_this_result": {
        "source": {
          "description": "Diario AS is a Spanish daily sports newspaper that concentrates particularly on football.",
          "source_info_link": "https://en.as.com/soccer/world-cup-2022-live-online-game-and-team-updates-n-3/",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df904b65583ce5079c51611afeb3b541c6c7a195da1b545dc3b19662fa211783acc.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://en.as.com/soccer/world-cup-2022-live-online-game-and-team-updates-n-3/&tbm=ilp&ilps=ADNMCi0xJRUxd1Z2mnyyEWFj2bHUWIhf2w",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi0xJRUxd1Z2mnyyEWFj2bHUWIhf2w&q=About+https%3A%2F%2Fen.as.com%2Fsoccer%2Fworld-cup-2022-live-online-game-and-team-updates-n-3%2F",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:YmAmSt8JFPoJ:https://en.as.com/soccer/world-cup-2022-live-online-game-and-team-updates-n-3/&cd=1&hl=en&ct=clnk&gl=us",
      "related_results": [
        {
          "position": 1,
          "title": "What are the results from World Cup opening games? - AS USA",
          "link": "https://en.as.com/soccer/what-are-the-results-from-world-cup-opening-games-n/",
          "displayed_link": "https://en.as.com \u203a Soccer",
          "date": "Nov 20, 2022",
          "snippet": "Cameroon vs Brazil summary: Aboubakar winner and red card, score, goals, highlights 1-0 | Qatar World Cup 2022 \u00b7 Follow the final game of Group ...",
          "snippet_highlighted_words": [
            "summary",
            "winner",
            "score",
            "World Cup",
            "final game"
          ],
          "about_this_result": {
            "source": {
              "description": "Diario AS is a Spanish daily sports newspaper that concentrates particularly on football.",
              "source_info_link": "https://en.as.com/soccer/what-are-the-results-from-world-cup-opening-games-n/",
              "security": "secure",
              "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df92ac11d8818ae14271fb48db4917d92a0e90d37a8a481cfc6a1d2263af8b54c39fdf6dd8fb76b69f03dc626f490319adc3c107dc5e5f0bbe1.png"
            }
          },
          "about_page_link": "https://www.google.com/search?q=About+https://en.as.com/soccer/what-are-the-results-from-world-cup-opening-games-n/&tbm=ilp&ilps=ADNMCi2Dlkvhd14kmM8grjktP8Gw8eU89w",
          "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi2Dlkvhd14kmM8grjktP8Gw8eU89w&q=About+https%3A%2F%2Fen.as.com%2Fsoccer%2Fwhat-are-the-results-from-world-cup-opening-games-n%2F",
          "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:E9DWRevhRhgJ:https://en.as.com/soccer/what-are-the-results-from-world-cup-opening-games-n/&cd=2&hl=en&ct=clnk&gl=us"
        }
      ]
    },
    {
      "position": 2,
      "title": "FIFA World Cup Qatar 2022\u2122",
      "link": "https://www.fifa.com/tournaments/mens/worldcup/qatar2022",
      "displayed_link": "https://www.fifa.com \u203a tournaments \u203a mens \u203a qatar2022",
      "snippet": "The FIFA World Cup Qatar 2022\u2122 will be played from 20 November to 18 December. 32 teams will compete across 64 matches in the 22nd edition of the ...",
      "snippet_highlighted_words": [
        "World Cup",
        "matches"
      ],
      "about_this_result": {
        "source": {
          "description": "FIFA is the international governing body of association football, beach football and futsal. It was founded in 1904 to oversee international competition among the national associations of Belgium, Denmark, France, Germany, the Netherlands, Spain, Sweden and Switzerland.",
          "source_info_link": "https://www.fifa.com/tournaments/mens/worldcup/qatar2022",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df9b9e19299c5c9a00e289c3f87321e7827b90fd32f06b1d1cbe27d1749d9ae4e7e.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.fifa.com/tournaments/mens/worldcup/qatar2022&tbm=ilp&ilps=ADNMCi0g_HFJxNzUkZvU4hQSa5z5h5qocA",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi0g_HFJxNzUkZvU4hQSa5z5h5qocA&q=About+https%3A%2F%2Fwww.fifa.com%2Ftournaments%2Fmens%2Fworldcup%2Fqatar2022",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:3P8EH28p0NwJ:https://www.fifa.com/tournaments/mens/worldcup/qatar2022&cd=11&hl=en&ct=clnk&gl=us",
      "missing": [
        "summarize"
      ],
      "must_include": {
        "word": "summarize",
        "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=%22summarize%22+the+outcome+of+world+cup+games+in+the+last+two+days&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q5t4CegQIIRAB"
      }
    },
    {
      "position": 3,
      "title": "Pulisic Scores First World Cup Goal - US Soccer",
      "link": "https://www.ussoccer.com/stories/2022/11/fifa-world-cup-2022-usmnt-1-iran-0-match-report-stats-standings",
      "displayed_link": "https://www.ussoccer.com \u203a stories \u203a 2022/11 \u203a fifa-wo...",
      "date": "4 days ago",
      "snippet": "Needing a victory to advance, forward Christian Pulisic scored the game-winner in the 38th minute off an assist from defender Sergi\u00f1o Dest. With ...",
      "snippet_highlighted_words": [
        "game",
        "winner"
      ],
      "about_this_result": {
        "source": {
          "description": "The United States Soccer Federation, commonly referred to as U.S. Soccer, is a 501 nonprofit organization and the official governing body of the sport of soccer in the United States.",
          "source_info_link": "https://www.ussoccer.com/stories/2022/11/fifa-world-cup-2022-usmnt-1-iran-0-match-report-stats-standings",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df9da0e38907a969fe65eee19a71af9f62d860574cd01959e06c3f3bb14212c8a29.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.ussoccer.com/stories/2022/11/fifa-world-cup-2022-usmnt-1-iran-0-match-report-stats-standings&tbm=ilp&ilps=ADNMCi2_3qoB-CMgKzqGywmkZpx9CPo7wA",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi2_3qoB-CMgKzqGywmkZpx9CPo7wA&q=About+https%3A%2F%2Fwww.ussoccer.com%2Fstories%2F2022%2F11%2Ffifa-world-cup-2022-usmnt-1-iran-0-match-report-stats-standings",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:UXrPByvbaKoJ:https://www.ussoccer.com/stories/2022/11/fifa-world-cup-2022-usmnt-1-iran-0-match-report-stats-standings&cd=12&hl=en&ct=clnk&gl=us"
    },
    {
      "position": 4,
      "title": "The FIFA World Cup in Qatar, explained - The Washington Post",
      "link": "https://www.washingtonpost.com/sports/2022/11/15/fifa-world-cup/",
      "displayed_link": "https://www.washingtonpost.com \u203a sports \u203a 2022/11/15",
      "date": "Nov 15, 2022",
      "snippet": "The 2022 World Cup will be played in Qatar, where matches start Nov. 20 and run through the Dec. 18 final. The group stage concludes Dec.",
      "snippet_highlighted_words": [
        "World Cup",
        "matches",
        "final"
      ],
      "about_this_result": {
        "source": {
          "description": "The Washington Post is an American daily newspaper published in Washington, D.C. It is the most widely circulated newspaper within the Washington metropolitan area and has a large national audience. Daily broadsheet editions are printed for D.C., Maryland, and Virginia.\nThe Post was founded in 1877.",
          "source_info_link": "https://www.washingtonpost.com/sports/2022/11/15/fifa-world-cup/",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df969ef2da900277f38b2303eb1d48224db86aa0d51971b9a97ac56811dbbecc79c.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.washingtonpost.com/sports/2022/11/15/fifa-world-cup/&tbm=ilp&ilps=ADNMCi1UVS9dl-NdU914XUR5WjmUCQUYuQ",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi1UVS9dl-NdU914XUR5WjmUCQUYuQ&q=About+https%3A%2F%2Fwww.washingtonpost.com%2Fsports%2F2022%2F11%2F15%2Ffifa-world-cup%2F",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:MUb_f6ux5QAJ:https://www.washingtonpost.com/sports/2022/11/15/fifa-world-cup/&cd=13&hl=en&ct=clnk&gl=us"
    },
    {
      "position": 5,
      "title": "Qatar 2022: The World Cup That Changed Everything",
      "link": "https://www.nytimes.com/2022/11/19/sports/soccer/world-cup-qatar-2022.html",
      "displayed_link": "https://www.nytimes.com \u203a Sports \u203a Soccer",
      "date": "Nov 19, 2022",
      "snippet": "Over the two weeks that follow, four games will be played on most days. The tournament ends with the final on Dec. 18. Is a winter World Cup ...",
      "snippet_highlighted_words": [
        "two",
        "games",
        "days",
        "final",
        "World Cup"
      ],
      "about_this_result": {
        "source": {
          "description": "The New York Times is an American daily newspaper based in New York City with a worldwide readership reported in 2020 to be a declining 840,000 paid print subscribers, and a growing 6 million paid digital subscribers. It also is a producer of popular podcasts such as the Daily.",
          "source_info_link": "https://www.nytimes.com/2022/11/19/sports/soccer/world-cup-qatar-2022.html",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df9c48f83e309f471cbfc1c5cfc3651d9da558a8732b00de326eb57ba089e044578.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.nytimes.com/2022/11/19/sports/soccer/world-cup-qatar-2022.html&tbm=ilp&ilps=ADNMCi13KooxFwphdtN16z8KEkg2s4d3ag",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi13KooxFwphdtN16z8KEkg2s4d3ag&q=About+https%3A%2F%2Fwww.nytimes.com%2F2022%2F11%2F19%2Fsports%2Fsoccer%2Fworld-cup-qatar-2022.html",
      "related_results": [
        {
          "position": 1,
          "title": "Answering Your Questions About the 2022 World Cup",
          "link": "https://www.nytimes.com/article/world-cup-qatar-faq.html",
          "displayed_link": "https://www.nytimes.com \u203a Sports \u203a Soccer",
          "date": "5 hours ago",
          "snippet": "Over the two weeks that follow, four games will be played on most days. The tournament ends with the final on Dec. 18. Is a winter World Cup ...",
          "snippet_highlighted_words": [
            "two",
            "games",
            "days",
            "final",
            "World Cup"
          ],
          "about_this_result": {
            "source": {
              "description": "The New York Times is an American daily newspaper based in New York City with a worldwide readership reported in 2020 to be a declining 840,000 paid print subscribers, and a growing 6 million paid digital subscribers. It also is a producer of popular podcasts such as the Daily.",
              "source_info_link": "https://www.nytimes.com/article/world-cup-qatar-faq.html",
              "security": "secure",
              "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df9824e4558a8a8eb4d3ff1fbfca885551e1dac52d8d2af7de0cc58fe596e3b93de2a26da0a2a3abb27f4b4b51e663653ca20bb39f773bdb36a.png"
            }
          },
          "about_page_link": "https://www.google.com/search?q=About+https://www.nytimes.com/article/world-cup-qatar-faq.html&tbm=ilp&ilps=ADNMCi3yfJs_BTGTfYYixQNRQugyFjzSAQ",
          "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi3yfJs_BTGTfYYixQNRQugyFjzSAQ&q=About+https%3A%2F%2Fwww.nytimes.com%2Farticle%2Fworld-cup-qatar-faq.html"
        }
      ]
    },
    {
      "position": 6,
      "title": "2022 FIFA World Cup Qatar knockout bracket, fixtures - ESPN",
      "link": "https://www.espn.com/soccer/fifa-world-cup/story/4627307/2022-world-cup-finals-bracket-and-fixtures-schedule",
      "displayed_link": "https://www.espn.com \u203a soccer \u203a fifa-world-cup \u203a story",
      "snippet": "FIFA World Cup fixtures and results ; Wednesday, Nov. 23 ; Group F: Morocco 0-0 Croatia (Al Bayt Stadium) ; Group E: Germany 1-2 Japan (Khalifa International ...",
      "snippet_highlighted_words": [
        "World Cup",
        "results",
        "2"
      ],
      "about_this_result": {
        "source": {
          "description": "ESPN is an American international basic cable sports channel owned by ESPN Inc., owned jointly by The Walt Disney Company and Hearst Communications. The company was founded in 1979 by Bill Rasmussen along with his son Scott Rasmussen and Ed Eagan.",
          "source_info_link": "https://www.espn.com/soccer/fifa-world-cup/story/4627307/2022-world-cup-finals-bracket-and-fixtures-schedule",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df9357ff8117be54b41d8b3f716b98c46b047e62ae01f7fc497b9a56c3f7fe6410e.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.espn.com/soccer/fifa-world-cup/story/4627307/2022-world-cup-finals-bracket-and-fixtures-schedule&tbm=ilp&ilps=ADNMCi1R1mzjhr-hgGLUCelTNU_13BJHdg",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi1R1mzjhr-hgGLUCelTNU_13BJHdg&q=About+https%3A%2F%2Fwww.espn.com%2Fsoccer%2Ffifa-world-cup%2Fstory%2F4627307%2F2022-world-cup-finals-bracket-and-fixtures-schedule",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:NW1Db4PZKOEJ:https://www.espn.com/soccer/fifa-world-cup/story/4627307/2022-world-cup-finals-bracket-and-fixtures-schedule&cd=16&hl=en&ct=clnk&gl=us",
      "missing": [
        "days"
      ],
      "must_include": {
        "word": "days",
        "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+%22days%22&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q5t4CegQIRxAB"
      }
    },
    {
      "position": 7,
      "title": "2022 FIFA World Cup Qatar: What to expect | AP News",
      "link": "https://apnews.com/article/2022-world-cup-qatar-guide-88a1ff6f5776aae3fc4f16400a5a8a51",
      "displayed_link": "https://apnews.com \u203a article \u203a 2022-world-cup-qatar-gu...",
      "date": "Nov 14, 2022",
      "snippet": "Spain vs. Germany, Nov. 27. Surely there can't have been many bigger group-stage matches than this at a World Cup? Two recent champions, ...",
      "snippet_highlighted_words": [
        "matches",
        "World Cup",
        "Two recent"
      ],
      "about_this_result": {
        "source": {
          "description": "The Associated Press is an American non-profit news agency headquartered in New York City. Founded in 1846, it operates as a cooperative, unincorporated association. It produces news reports that are distributed to its members, U.S. newspapers and broadcasters.",
          "source_info_link": "https://apnews.com/article/2022-world-cup-qatar-guide-88a1ff6f5776aae3fc4f16400a5a8a51",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df986660b9b99db1bfcd4e4bc84787dd0e743b6c43166cfb92693e12f6dc3964b7f.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://apnews.com/article/2022-world-cup-qatar-guide-88a1ff6f5776aae3fc4f16400a5a8a51&tbm=ilp&ilps=ADNMCi2LwvLAKgF9xRX3X7akfZddI1F4LQ",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi2LwvLAKgF9xRX3X7akfZddI1F4LQ&q=About+https%3A%2F%2Fapnews.com%2Farticle%2F2022-world-cup-qatar-guide-88a1ff6f5776aae3fc4f16400a5a8a51",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:7hUN5y-B17IJ:https://apnews.com/article/2022-world-cup-qatar-guide-88a1ff6f5776aae3fc4f16400a5a8a51&cd=17&hl=en&ct=clnk&gl=us",
      "missing": [
        "summarize"
      ],
      "must_include": {
        "word": "summarize",
        "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=%22summarize%22+the+outcome+of+world+cup+games+in+the+last+two+days&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q5t4CegQISBAB"
      }
    },
    {
      "position": 8,
      "title": "World Cup 2022 key events: Winners and losers on day 2 in ...",
      "link": "https://www.aljazeera.com/news/2022/11/22/world-cup-2022-key-events-at-a-glance-day-2",
      "displayed_link": "https://www.aljazeera.com \u203a news \u203a 2022/11/22 \u203a worl...",
      "date": "Nov 22, 2022",
      "snippet": "England trounced Iran, the Netherlands edged Senegal 2-0, and Wales tied with USA on Day 2 of the World Cup.",
      "snippet_highlighted_words": [
        "2",
        "Day 2",
        "World Cup"
      ],
      "about_this_result": {
        "source": {
          "description": "aljazeera.com was first indexed by Google more than 10 years ago",
          "source_info_link": "https://www.aljazeera.com/news/2022/11/22/world-cup-2022-key-events-at-a-glance-day-2",
          "security": "secure",
          "icon": "https://serpapi.com/searches/638bc233d5ecf4de2dc0ff46/images/94a4d69e67e235bb08faa64321f72df970325e4bb056bb36afe3a91bc55e551d55d434b58472fba75ef652fd268ee841.png"
        }
      },
      "about_page_link": "https://www.google.com/search?q=About+https://www.aljazeera.com/news/2022/11/22/world-cup-2022-key-events-at-a-glance-day-2&tbm=ilp&ilps=ADNMCi16sE03XEqCZiarJ6zrY-7JeMaqaA",
      "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&ilps=ADNMCi16sE03XEqCZiarJ6zrY-7JeMaqaA&q=About+https%3A%2F%2Fwww.aljazeera.com%2Fnews%2F2022%2F11%2F22%2Fworld-cup-2022-key-events-at-a-glance-day-2",
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:Q0ZrJdws5EEJ:https://www.aljazeera.com/news/2022/11/22/world-cup-2022-key-events-at-a-glance-day-2&cd=18&hl=en&ct=clnk&gl=us",
      "missing": [
        "summarize"
      ],
      "must_include": {
        "word": "summarize",
        "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=%22summarize%22+the+outcome+of+world+cup+games+in+the+last+two+days&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q5t4CegQISRAB"
      }
    }
  ],
  "related_searches": [
    {
      "query": "football world cup qualifiers 2022",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=Football+World+Cup+qualifiers+2022&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg9EAE"
    },
    {
      "query": "days to world cup 2022",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=Days+to+World+Cup+2022&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg8EAE"
    },
    {
      "query": "who won the world cup 2022",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=Who+won+the+World+Cup+2022&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg6EAE"
    },
    {
      "query": "world cup countdown",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=World+Cup+countdown&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg7EAE"
    },
    {
      "query": "how long does world cup last",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=How+long+does+World+Cup+last&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg5EAE"
    },
    {
      "query": "world cup match",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=World+Cup+match&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg3EAE"
    },
    {
      "query": "world cup finals groups",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=World+Cup+finals+groups&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg4EAE"
    },
    {
      "query": "world cup knockout stage 2022",
      "link": "https://www.google.com/search?ucbcb=1&gl=us&hl=en&q=World+Cup+knockout+stage+2022&sa=X&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q1QJ6BAg2EAE"
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=10&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8NMDegQIBBAW",
    "other_pages": {
      "2": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=10&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAE",
      "3": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=20&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAG",
      "4": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=30&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAI",
      "5": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=40&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAK",
      "6": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=50&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAM",
      "7": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=60&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAO",
      "8": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=70&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAQ",
      "9": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=80&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAS",
      "10": "https://www.google.com/search?q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&ucbcb=1&gl=us&hl=en&ei=NMKLY8f5Nsn6wQOg_4D4AQ&start=90&sa=N&ved=2ahUKEwjH4-7gtN77AhVJfXAKHaA_AB8Q8tMDegQIBBAU"
    }
  },
  "serpapi_pagination": {
    "current": 1,
    "next_link": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=10",
    "next": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=10",
    "other_pages": {
      "2": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=10",
      "3": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=20",
      "4": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=30",
      "5": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=40",
      "6": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=50",
      "7": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=60",
      "8": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=70",
      "9": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=80",
      "10": "https://serpapi.com/search.json?device=desktop&engine=google&gl=us&google_domain=google.com&hl=en&q=summarize+the+outcome+of+world+cup+games+in+the+last+two+days&start=90"
    }
  }
}
  return json_string

def parse_response(query, response_dict):
  textual_response = f"Search results for `{query}`:\n"
  if 'related_questions' in response_dict:
    textual_response += "Related Questions:\n"
    for related_question in response_dict['related_questions']:
      textual_response += f"""
        Q: {related_question['question']}
        Snippet: {related_question.get('snippet', 'NA')}
        Date: {related_question.get('date', 'NA')}
        Link: {related_question.get('link', 'NA')}\n
        """
      if 'rich_list' in related_question:
        textual_response += "List of info:\n"
        for rich_list_item in related_question['rich_list']:
          textual_response += f"""{rich_list_item['title']},"""

  if 'organic_results' in response_dict:
    textual_response += "Organic Results:\n"
    for organic_result in response_dict['organic_results']:
      textual_response += f"""
        Title: {organic_result.get('title', 'NA')}
        Date: {organic_result.get('date', 'NA')}
        Snippet: {organic_result.get('snippet', 'NA')}

        Link: {organic_result.get('link', 'NA')}\n
        """
  if 'knowledge_graph' in response_dict:
    textual_response += f"Knowledge Graph: {json.dumps(response_dict['knowledge_graph'])}"
  return textual_response

if __name__ == "__main__":
  q = "summarize the outcome of world cup games in the last two days"
  response = googleSearch(q)
  print(parse_response(q, response))


