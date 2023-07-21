#!/usr/bin/python3
import sys

def parse_line(line):
    try:
        _, _, _, status_code, file_size = line.split()[0:5]
        status_code = int(status_code)
        file_size = int(file_size)
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None

def print_statistics(total_file_size, status_counts):
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_file_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is None:
                continue

            total_file_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
