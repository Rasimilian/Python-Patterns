from patterns.structural.three_tier.three_tier import UI


def main():
    gui = UI()
    gui.show_objects()
    gui.show_object_by_id([1, 2])


if __name__ == "__main__":
    main()
