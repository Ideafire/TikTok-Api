from gevent import monkey
monkey.patch_all()

from flask import Flask
from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
custom_verifyFp = "verify_kqv2svy0_gQARqKRo_fV40_4EW1_Bob0_RGCkXxCbfYTz"

app = Flask(__name__)

@app.route('/tiktok/<tiktok_id>', methods=['GET'])
def tiktok(tiktok_id):
    tiktok_video = api.get_tiktok_by_id(tiktok_id, custom_verifyFp=custom_verifyFp)
    return tiktok_video

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
