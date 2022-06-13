import snowflakecli
import sys

def main():
    op = {}
    op['just_run'] = '--just-run' in sys.argv
    op['save_data'] = not op['just_run'] and '--no-persist' not in sys.argv #saves peer's data in database
    op['get_loc'] = not op['just_run'] and '--no-location' not in sys.argv # check peer's location using ip-api.com
    op['log'] = not op['just_run'] and '--no-logging' not in sys.argv
    
    snowflakecli.run(**op)

if __name__ == '__main__':
    main()
