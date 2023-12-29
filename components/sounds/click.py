import os
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QGuiApplication


def button_clicked(instance):
    # Lounge looped music
    print('CLICKED SOUND')
    instance.media_player = QMediaPlayer(instance)
    instance.media_player.setAudioOutput(QAudioOutput(instance))
    file_url = QUrl.fromLocalFile(os.path.join(
        'Music', 'mixkit-modern-technology-select-3124.wav'))
    instance.media_player.setSource(file_url)
    # instance.media_player.mediaStatusChanged.connect(
    #     instance.handle_media_status)
    instance.media_player.play()
