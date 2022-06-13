# snowflake-cli
Snowflake is a system to defeat internet censorship, made by [Tor Project](https://www.torproject.org).

The system works by volunteers who run the snowflake extension on browser.

Now, with this script, you can host a snowflake relay in another program or run it in CLI mode in a server!

## Requirements

- Google Chrome 98
- [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/)
- Add Chromedriver to path (or to /usr/bin on linux)

## Install

```bash
cd snowflake-cli
pip install .
```

## Running snowflake in your program:

It's possible to import snowflake in your program's python code to host snowflake cuncurrently!
This is very nice because you can allow users of your software to donate their bandwidth to snowflake's network :)

```python
import snowflakecli

options = {
  'just_run':False, # if true, runs snowflake discretly - without logging and saving data
  'save_data':True, # if true, snowflake will save your peers data in database
  'get_loc':True,   # if true, snowflake will not get peers country and region
  'log':True        # if true, snowflake will print every log
}

# runs snowflake concurrently in another thread while your main program runs
snowflakecli.start_run(options) 

```

## Running (cli mode)

` $ snowflakecli [OPTIONS]`

### Options: 
```
--just-run   - Just run snowflake with all options below
--no-persist - Run without storing peer's data
--no-location - Doesn't get IPs locations
--no-logging  - Doesn't print anything (just the starting log)
```
## Features

You can watch all peers that conects with you live, store this data with the peer's location to further analisys.

## Database Tables Schema

### peers

- timestamp (int)
- ip (text)
- country (text)
- region (text)
