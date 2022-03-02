# your program imports #
import time
########################

import snowflake

options = {
    'just_run':False,   # if true, runs snowflake discretly - without logging and saving data
    'save_data':True,   # if true, snowflake will save your peers data in database
    'get_loc':True,     # if true, snowflake will not get peers country and region
    'log':True          # if true, snowflake will print every log
}

# runs snowflake concurrently in another thread while your main program runs
snowflake.start_run(options)

for i in range(10):
    print('stuff')
    time.sleep(1)

while True:
    pass
