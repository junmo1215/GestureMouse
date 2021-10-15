# coding = UTF8

from GUI import CircleDemo

def main():
    circle_demo = CircleDemo()
    circle_demo.show()

    while True:
        cmd = input(">>> ")
        if cmd == "q":
            break

        try:
            if cmd == "d":
                circle_demo.set_down()
            elif cmd == "u":
                circle_demo.set_up()
            elif cmd.startswith("p"):
                arr = cmd.split(" ")
                x, y = int(arr[1]), int(arr[2])
                circle_demo.set_position(x, y)
        except Exception as ex:
            print("ex:", ex)

if __name__ == "__main__":
    main()
