import os
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import keyring
from tqdm import tqdm  # Progress bar

# Authenticate with Spotify API
CLIENT_ID = keyring.get_password("spotify_api", "client_id")
CLIENT_SECRET = keyring.get_password("spotify_api", "client_secret")

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Spotify API credentials not found. "
                     "Check keyring or environment variables.")

try:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print("Authenticated with Spotify API.")
except Exception as e:
    raise RuntimeError(f"Authentication failed: {e}")

output_file = "spotify_tracks_unique.csv"

# Define popularity bins
popularity_bins = [(i, i + 10) for i in range(0, 100, 10)]
songs_per_bin = 1000
tracks_per_request = 50  # Max per search API request
batch_size = 100  # Max per audio features request
requests_per_bin = songs_per_bin // tracks_per_request

# Full expected columns
expected_columns = [
    "id", "name", "popularity", "duration_ms", "explicit", "artists",
    "id_artists", "release_date", "danceability", "energy", "key",
    "loudness", "mode", "speechiness", "acousticness", "instrumentalness",
    "liveness", "valence", "tempo", "time_signature"
]

# Data storage
all_tracks = set()

def get_tracks_with_popularity(min_pop, max_pop):
    """Fetch unique tracks within a given popularity range using pagination & filters."""
    track_data = []
    track_ids = set()  # Store unique IDs for this batch

    print(f"\n🔍 Fetching {songs_per_bin} unique songs in popularity range {min_pop}-{max_pop}...")

    for _ in tqdm(range(songs_per_bin // tracks_per_request), desc=f"Fetching Tracks ({min_pop}-{max_pop})"):
        try:
            query = f"popularity:{min_pop}-{max_pop}"
            results = sp.search(q=query, type='track', limit=tracks_per_request)

            for item in results['tracks']['items']:
                track_id = item['id']
                if track_id in all_tracks:  # Skip duplicates
                    continue

                name = item['name']
                popularity = item['popularity']
                duration_ms = item['duration_ms']
                explicit = item['explicit']
                release_date = item['album']['release_date']
                artists = ", ".join([artist['name'] for artist in item['artists']])
                id_artists = ", ".join([artist['id'] for artist in item['artists']])

                track_ids.add(track_id)
                track_data.append(
                    [track_id, name, popularity, duration_ms, explicit, artists, id_artists, release_date])
                all_tracks.add(track_id)  # Store to avoid duplicates

            time.sleep(0.1)  # Prevent rate limits

        except Exception as e:
            print(f"⚠️ Error fetching tracks: {e}")
            time.sleep(5)

    print(f"✅ Collected {len(track_data)} unique tracks in range {min_pop}-{max_pop}.\n")
    return track_data, track_ids


# Loop through popularity bins
for min_pop, max_pop in popularity_bins:
    track_data, track_ids = get_tracks_with_popularity(min_pop, max_pop)

    # Merge track metadata with audio features
    track_list = []
    for track in track_data:
        track_id = track[0]
        track_list.append(track)

    # Convert batch to DataFrame
    df = pd.DataFrame(track_list, columns=expected_columns)

    # Drop missing columns dynamically
    df = df.dropna(axis=1, how="all")

    # Print missing columns (for debugging)
    missing_cols = [col for col in expected_columns if col not in df.columns]
    if missing_cols:
        print(f"⚠️ Missing Columns: {missing_cols}")

    # Save to CSV
    if not os.path.exists(output_file):
        df.to_csv(output_file, index=False)  # First batch: Write with header
        print(f"📂 First batch saved to '{output_file}'")
    else:
        df.to_csv(output_file, index=False, mode='a', header=False)  # Append new data
        print(f"📂 Batch for popularity {min_pop}-{max_pop} appended to '{output_file}'")

print("🎉 Data collection complete! ✅")
