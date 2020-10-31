import logging


def input_def():
    logging.info('The user is about to make his input')
    user_input = input("User input: ")
    logging.warning('Users says: {}'.format(user_input))

    try:
        user_input = int(user_input)
        print(user_input)
    except ValueError:
        print("Please type an integer")
        logging.exception('An exception has occurred!')
        logging.critical('{} is not a number'.format(user_input))


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                        filename='my_log.log',
                        level=logging.DEBUG,
                        datefmt='%d/%m/%Y %H:%M:%S')
    logging.debug('inside main: before input_def() starts ---')
    input_def()
    logging.debug('inside main: after input_def() starts ---')
