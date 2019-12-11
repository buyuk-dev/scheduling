import argparse
import instance


def validate(instance_path, solution_path):
    inst = instance.Instance.from_file(instance_path)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", help="scheduling instance file")
    parser.add_argument("--solution", help="scheduling file")
    args = parser.parse_args()

    if validate(args.instance, args.solution):
        print("OK")
    else:
        print("NOT OK")
