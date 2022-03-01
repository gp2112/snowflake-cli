# snowflake-cli
Snowflake is a system to defeat internet censorship, made by [Tor Project](https://www.torproject.org).

The system works by volunteers who run the snowflake extension on browser.

Now, with this script, you can host on a server too, without the need to use a browser with GUI and install an extension.

## Requirements

` pip install -r requirements.txt `

- Google Chrome 98
- [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/)
- Add Chromedriver to path (or to /usr/bin on linux)

## Running

` $ python snowflake.py `

### Options: 
```options
--no-persist - Run without storing peer's data
--no-location - Doesn't get IPs locations
```

## Features

You can watch all peers that conects with you live, store this data with the peer's location to further analisys.

## Database Tables Schema

### peers

- timestamp (int)
- ip (text)
- country (text)
- region (text)
