from cortex_client import InputMessage, OutputMessage

def main(params):

    msg = InputMessage.from_params(params)

    n = msg.payload.get('n')

    top_head = news('cnn', n)

    # Compute and create output
    return OutputMessage.create().with_payload({'route':'cnn', 'top_head': top_head}).to_params()

import requests, json

# source: news source from news api
# n: number of top articles from source
def news(source, n, api='d641992dd1f544d28409176c74802ac4'):

    url = ('https://newsapi.org/v2/top-headlines?'
           'sources='+source+
           '&pageSize='+str(n)+
           '&apiKey='+api)
    response = requests.get(url).json()

    return [json.dumps({'title':art['title'], 'url':art['url']}) for art in response['articles']]