import argparse

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required = True)
    args = parser.parse_args(argv)
    print("args.name:", args.name)
    return 0
    
if __name__ == "__main__":
    raise SystemExit(main())