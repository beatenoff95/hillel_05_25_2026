import argparse
import csv
import json
import logging
import sys
from pathlib import Path
from urllib.request import urlretrieve
from xml.etree import ElementTree


SECOND_NAME = "vyshnevskyi"
SOURCE_BASE_URL = (
    "https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test"
)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
IDEAS_DIR = PROJECT_ROOT / "ideas_for_test"

CSV_FILES = ("r-m-c.csv", "random-michaels.csv")
JSON_FILES = (
    "localizations_en.json",
    "localizations_ru.json",
    "login.json",
    "swagger.json",
)
XML_FILE = "groups.xml"


def download_file_if_missing(local_path: Path, source_url: str) -> None:
    if local_path.exists():
        return

    local_path.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(source_url, local_path)


def prepare_test_files() -> None:
    for file_name in CSV_FILES:
        download_file_if_missing(
            IDEAS_DIR / "work_with_csv" / file_name,
            f"{SOURCE_BASE_URL}/work_with_csv/{file_name}",
        )

    for file_name in JSON_FILES:
        download_file_if_missing(
            IDEAS_DIR / "work_with_json" / file_name,
            f"{SOURCE_BASE_URL}/work_with_json/{file_name}",
        )

    download_file_if_missing(
        IDEAS_DIR / "work_with_xml" / XML_FILE,
        f"{SOURCE_BASE_URL}/work_with_xml/{XML_FILE}",
    )


def read_csv_rows(csv_path: Path) -> tuple[list[str], list[list[str]]]:
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        sample = csv_file.read(2048)
        csv_file.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        reader = csv.reader(csv_file, dialect)
        header = next(reader)
        return header, [row for row in reader]


def remove_csv_duplicates(csv_paths: list[Path], result_path: Path) -> int:
    unique_rows = []
    seen_rows = set()
    result_header = None

    for csv_path in csv_paths:
        header, rows = read_csv_rows(csv_path)
        if result_header is None:
            result_header = header

        for row in rows:
            row_key = tuple(row)
            if row_key in seen_rows:
                continue

            seen_rows.add(row_key)
            unique_rows.append(row)

    result_path.parent.mkdir(parents=True, exist_ok=True)
    with result_path.open("w", newline="", encoding="utf-8") as result_file:
        writer = csv.writer(result_file)
        writer.writerow(result_header)
        writer.writerows(unique_rows)

    return len(unique_rows)


def setup_file_logger(logger_name: str, log_path: Path) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.ERROR)
    logger.handlers.clear()

    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    handler.setLevel(logging.ERROR)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False

    return logger


def validate_json_files(json_dir: Path, log_path: Path) -> list[Path]:
    logger = setup_file_logger("json_validator", log_path)
    invalid_files = []

    for json_path in sorted(json_dir.glob("*.json")):
        try:
            with json_path.open(encoding="utf-8") as json_file:
                json.load(json_file)
        except json.JSONDecodeError as error:
            invalid_files.append(json_path)
            logger.error(
                "Invalid JSON file %s: line %s, column %s - %s",
                json_path,
                error.lineno,
                error.colno,
                error.msg,
            )

    return invalid_files


def setup_console_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False

    return logger


def find_incoming_by_group_number(xml_path: Path, group_number: str) -> str | None:
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.findtext("number")
        if number == group_number:
            return group.findtext("timingExbytes/incoming")

    return None


def log_group_incoming(xml_path: Path, group_number: str) -> None:
    logger = setup_console_logger("xml_groups")
    incoming = find_incoming_by_group_number(xml_path, group_number)

    if incoming is None:
        logger.info("Group %s does not have timingExbytes/incoming", group_number)
    else:
        logger.info("Group %s timingExbytes/incoming: %s", group_number, incoming)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Homework 10 tasks.")
    parser.add_argument(
        "--group-number",
        default="2",
        help="group/number value for XML search. Default: 2",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prepare_test_files()

    csv_dir = IDEAS_DIR / "work_with_csv"
    json_dir = IDEAS_DIR / "work_with_json"
    xml_path = IDEAS_DIR / "work_with_xml" / XML_FILE

    csv_paths = [csv_dir / file_name for file_name in CSV_FILES]
    result_path = PROJECT_ROOT / f"result_{SECOND_NAME}.csv"
    remove_csv_duplicates(csv_paths, result_path)

    log_path = PROJECT_ROOT / f"json__{SECOND_NAME}.log"
    validate_json_files(json_dir, log_path)

    log_group_incoming(xml_path, args.group_number)


if __name__ == "__main__":
    main()
