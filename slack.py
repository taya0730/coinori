from flask import request
from flask_restx import Resource, Api, Namespace, fields
import config
import requests

errorText = "오류 발생"
successText = "정상 동작"


Slack = Namespace(
    name="Slack API",
    description="Slack을 사용하기 위해 사용하는 API.",
)

slack_fields = Slack.model('Slack Message', {  # Model 객체 생성
    # 'data': fields.String(description='a Todo', required=True, example="what to do")
    'channel': fields.String(description='slack channel id', required=False, example="코이노리-upbit id"),
    'message': fields.String(description='slack message', required=True, example="input message")
})

# slack_fields_with_id = Slack.inherit('slack_fields With ID', slack_fields, {
#     'todo_id': fields.Integer(description='a Todo ID')
# })
#test

@Slack.route('/send-msg')
# @Slack.doc(params={'channel_name': '코이노리-upbit'})
class SendMsg(Resource):
    @Slack.expect(slack_fields) # 주입
    # @Slack.response(200, 'Success', slack_fields_with_id)
    @Slack.response(500, 'Failed')
    def post(self):
        channel_name = request.json.get('channel')
        msg = request.json.get('message')
        token = config.slack_token
        # channel_name = "코이노리-upbit"
        response = self.post_message(token, channel_name, msg)
        if(response.status_code == 200) : 
            result = successText
        return {
            'channel_name': channel_name,
            'sendText': msg,
            'result': result
        }


    def post_message(self, token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text}
        )
        return response