from cortex_client import InputMessage, OutputMessage
from news import news

def main(params):

    msg = InputMessage.from_params(params)

    n = msg.payload.get('n')

    top_head = news('cnn', n)

    # Compute and create output
    return OutputMessage.create().with_payload({'route':'cnn', 'top_head': top_head}).to_params()
