import re


class RedactPhoneNumbers:
    def __init__(self, stream):
        self.stream = stream

    def write(self, text):
        # Regular expression to match phone numbers
        phone_regex = r"(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
        redacted_text = re.sub(phone_regex, "****", text)
        self.stream.write(redacted_text)

    def flush(self):
        self.stream.flush()


class RedactEmails:
    def __init__(self, stream):
        self.stream = stream

    def write(self, text):
        # Regular expression to match email addresses
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        redacted_text = re.sub(email_regex, "****", text)
        self.stream.write(redacted_text)

    def flush(self):
        self.stream.flush()
