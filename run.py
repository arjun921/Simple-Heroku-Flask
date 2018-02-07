from app import app
import os

os.environ["PUSHBULLET_KEY"] = "o.pweWh6uDSBNVJgd74d0XB39Fn0JZHw5p"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    os.system("pb push \"Starting arjun921 at port {}\"".format(port))
    app.run(host='0.0.0.0', port=port)
