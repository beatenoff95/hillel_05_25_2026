import logging
from datetime import datetime, timedelta
from pathlib import Path


TARGET_KEY = "Key TSTFEED0300|7E3E|0400"
TIMESTAMP_MARKER = "Timestamp "
TIME_FORMAT = "%H:%M:%S"

CURRENT_DIR = Path(__file__).resolve().parent
SOURCE_LOG_PATH = CURRENT_DIR / "hblog.txt"
RESULT_LOG_PATH = CURRENT_DIR / "hb_test.log"


def get_target_lines(log_path: Path, target_key: str = TARGET_KEY) -> list[str]:
    with log_path.open(encoding="utf-8") as log_file:
        return [line.strip() for line in log_file if target_key in line]


def extract_timestamp(log_line: str) -> datetime:
    timestamp_start = log_line.find(TIMESTAMP_MARKER)
    if timestamp_start == -1:
        raise ValueError(f"Timestamp marker was not found in line: {log_line}")

    timestamp_start += len(TIMESTAMP_MARKER)
    timestamp_text = log_line[timestamp_start:timestamp_start + 8]
    return datetime.strptime(timestamp_text, TIME_FORMAT)


def get_heartbeat_seconds(current_time: datetime, next_time: datetime) -> int:
    heartbeat = current_time - next_time
    if heartbeat.total_seconds() < 0:
        heartbeat += timedelta(days=1)

    return int(heartbeat.total_seconds())


def setup_heartbeat_logger(result_log_path: Path) -> logging.Logger:
    logger = logging.getLogger("heartbeat_analyzer")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    handler = logging.FileHandler(result_log_path, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False

    return logger


def analyze_heartbeat(
    source_log_path: Path = SOURCE_LOG_PATH,
    result_log_path: Path = RESULT_LOG_PATH,
) -> Path:
    logger = setup_heartbeat_logger(result_log_path)
    filtered_lines = get_target_lines(source_log_path)

    for current_line, next_line in zip(filtered_lines, filtered_lines[1:]):
        current_time = extract_timestamp(current_line)
        next_time = extract_timestamp(next_line)
        heartbeat_seconds = get_heartbeat_seconds(current_time, next_time)

        message = (
            f"heartbeat={heartbeat_seconds}s, "
            f"current_timestamp={current_time.strftime(TIME_FORMAT)}, "
            f"next_timestamp={next_time.strftime(TIME_FORMAT)}"
        )

        if 31 < heartbeat_seconds < 33:
            logger.warning(message)
        elif heartbeat_seconds >= 33:
            logger.error(message)

    return result_log_path


if __name__ == "__main__":
    created_log = analyze_heartbeat()
    print(f"Heartbeat analysis was written to {created_log}")
