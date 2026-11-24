"""Write one honest, funny error message to /output/entry.txt."""

LINE = "The server ran out of memory and forgot what you asked for. Nothing was saved. Try again before it forgets this message too."

# The gate accepts 1-200 characters of non-blank UTF-8 text, one line.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert LINE == LINE.strip(), "entry must be a single line with no padding"
assert "\n" not in LINE, "entry must be a single line"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
