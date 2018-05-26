from com.obytech.pychat.dtos.message import Message
from datetime import datetime

messages = []


def add_message(msg: Message):
    messages.append(msg)


def get_messages(recipient_id, from_timestamp: int):
    msgs = get_from_message_index(from_timestamp)
    return list((a_msg for a_msg in msgs if a_msg.dest == recipient_id))


def get_from_message_index(timestamp: int):
    # TODO impl approximate bin search
    # start, end = 0, len(messages)
    # if end == 0:
    #     return 0
    #
    # while start < end:
    #     mid = start + (end - start) / 2
    #     msg_time = messages[mid].sent_on
    #     if msg_time <= timestamp:
    #         start = mid + 1
    #     else:
    #         end = mid - 1
    #
    # return mid
    output = []
    for msg in messages:
        if msg.sent_on > datetime.fromtimestamp(timestamp):
            output.append(msg)

    return output
