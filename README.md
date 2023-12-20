# ConnectX Project 🚀
ConnectX it's an chat application, the project it's made in PyQt6 framework.

*The code is open source and free to use under the license attached in this repository* 

Tags:
- fastapi 🚄
- uvicorn 🐍
- PyQt6 🐉
- Qt
- Python 🐉
- sqlalchemy 🗃️
- Chat Application

## How to Get Started 🌟
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`. 📦
3. Run the `main.py` script. 🏃
4. Enjoy 🌐

## Features ✨
- The features are listed here.
## Authors✨
@AESMatias & @emonkey0
# Next things to do 🚀

### Improve the memory optimization:

### Modularize the code and solve the problem of hight cohesion and low coupling:

### Design:
- We need to add the option that allows maximise or just shrink the windows dimensions.

### Security: message inputs, endpoints, etc...
- We need to ensure that the two sockets (to send and recibe messages) for each user connected were absolute closed through de server (maybe using a periodic func), because if this isn't done, we're having a big vulnerability breach that allows the users collapse the RAM used by the server, blowing up the entire server.

### Chat:
- When a new message income, we need to refresh the two instances> the pixmap and the animated label with the new picture that has been changed from our own account session.
- If the user scrolls up, then we need to calculate the current height
dinamically obtained through a function, thus allowing them to scrolls up the
chat history, because currently there's a func that scrolls the whole chat down
every 15 seconds.

# Attributions and acknowledgments:
Settings icon: <a href="https://www.flaticon.com/free-icons/settings" title="settings icons">Settings icons created by Freepik - Flaticon</a>

Volume icon: <a href="https://www.flaticon.com/free-icons/speaker" title="speaker icons">Speaker icons created by Pixel perfect - Flaticon</a>

Volume icon muted: <a href="https://www.flaticon.com/free-icons/mute" title="mute icons">Mute icons created by Pixel perfect - Flaticon</a>

Send message icon: <a href="https://www.flaticon.com/free-icons/send" title="send icons">Send icons created by kmg design - Flaticon</a>

Undo (back) icon: <a href="https://www.flaticon.com/free-icons/back-button" title="back button icons">Back button icons created by icon_small - Flaticon</a>

Wallpaper at Edit Profile Frame: Photo by <a href="https://unsplash.com/@the_real_napster?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Dominik Lange</a> on <a href="https://unsplash.com/photos/blue-parrot-standing-on-brown-tree-branch-Lej_oqHljbk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

Wallpaper at The initial Frame: Photo by <a href="https://unsplash.com/@choys_?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Conny Schneider</a> on <a href="https://unsplash.com/photos/a-blue-abstract-background-with-lines-and-dots-pREq0ns_p_E?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  