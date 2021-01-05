from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Friend"


@app.route("/sms", methods=['POST'])
def whatsapp_reply():
    """ Respond to incoming calls with a single SMS message"""

    # Request
    msg = request.form.get('Body')

    # Response
    response = MessagingResponse()
    response.message("Server said: {}".format(msg))

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)