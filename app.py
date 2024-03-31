from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Playlist stored here
playlist = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def add_song():
    url = request.form.get('url')
    # Extract video id from url and add to playlist
    video_id = url.split('=')[1]
    playlist.append(video_id)
    return "Media added!", 200

@app.route('/skip', methods=['POST'])
def skip_song():
    if playlist:
        # Remove the current song from the playlist
        skipped_element = playlist.pop(0)
        return f"Skipped {skipped_element}", 200
    return "Playlist is empty", 400


@app.route('/player')
def player():
    # Get the first song in the playlist
    video_id = playlist.pop(0) if playlist else None
    # Store the next song ID in a global variable
    global next_video_id
    next_video_id = playlist[0] if playlist else None
    # Specify the refresh time in seconds (e.g., 60 seconds)
    refresh_time = 60
    return render_template('player.html', video_id=video_id, refresh_time=refresh_time)




if __name__ == '__main__':
    app.run(debug=True)
