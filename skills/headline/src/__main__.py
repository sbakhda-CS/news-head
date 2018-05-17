from cortex_client import InputMessage, OutputMessage
from news import news

def main(params):
    # Parse the function params
    msg = InputMessage.from_params(params)

    # Get agency and n
    source = msg.payload.get('source')
    n = msg.payload.get('n')


    top_head = news(source.lower(), n)

    # Compute and create output
    return OutputMessage.create().with_payload({'route':'headline','top_head': top_head}).to_params()



