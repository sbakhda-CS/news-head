from cortex_client import InputMessage, OutputMessage


# example of routing: cnbc route
def main(params):
    # Parse the function params
    msg = InputMessage.from_params(params)

    # Get source and n
    source = 'cnbc'
    n = msg.payload.get('n')

    # get api token from properties
    api = msg.properties.get('token')

    # get the top headlines using the news api
    top_head = news(source.lower(), n, api)

    # Compute and create output
    return OutputMessage.create().with_payload({'route':'cnbc','top_head': top_head,'api':api}).to_params()

# News Function - Data Source
import requests, json

# source: news source from news api
# n: number of top articles from source
# api: api token for the website newsapi.org
def news(source, n, api):

    url = ('https://newsapi.org/v2/top-headlines?'
           'sources='+source+
           '&pageSize='+str(n)+
           '&apiKey='+api)
    response = requests.get(url).json()

    # return an array of n article titles and urls
    return [json.dumps({'title':art['title'], 'url':art['url']}) for art in response['articles']]