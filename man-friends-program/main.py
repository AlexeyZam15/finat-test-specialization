import traceback

from app import App


def main():
    app = App("man-friends.clv")
    input_mode = True
    while input_mode:
        try:
            input_mode = app.start()
        except IOError:
            traceback.print_exc()
            input_mode = False
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
