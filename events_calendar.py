class Event:
    def __init__(self, start, end, summary):
        self.start = start
        self.end = end
        self.summary = summary

    def __repr__(self):
        return f"Event(start={self.start}, end={self.end}, summary={self.summary})"

def extract_event_info(event):
    return Event(event["start"]["dateTime"], event["end"]["dateTime"], event["summary"])

def extrac_data(data):
    data = data.split("T")
    data_correct = data[0].split('-')
    data_correct = data_correct[2] + '/' + data_correct[1] + '/' + data_correct[0]

    time_correct = data[1].split('-')[0]

    return data_correct, time_correct