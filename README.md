# spotify-applescript

Set a time and be awaken with your Spotify at the time. You could get up with Spotify at the morning.

### How to use

Pass the time you want to be awakened as an argument vector to `run.py`.

Ex.

```bash
python3 ~/git/spotify-applescript/run.py 08 00
```

You should use a "24-hour clock" to set the time to PM.

```bash
python3 ~/git/spotify-applescript/run.py 20 30
```

Above example sets 8:30 PM. 

You can also use `once.py`.

### Terminal Output

```
2022-04-17T21:33:19 : Run after 2 seconds...
2022-04-17T21:33:21 : 0
```

`0` means the AppleScript exit code.

```
~ ❯ python3 ~/git/spotify-applescript/run.py 21 3
2022-04-17T21:35:51 : Run after 2 seconds...
2022-04-17T21:35:53 : Not this time
```

`run.py ` logs one line each day. You can see the next log at the next day.

`once.py` executes the command once then be terminated.

### The AppleScript

The script's content below:

```
tell application "Spotify"
	play
end tell
```
