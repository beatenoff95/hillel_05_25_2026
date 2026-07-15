import logging
from unittest import TestCase, main


def log_event(username: str, status: str):
    """
    Logs a login event.

    status:
    * success - logged as info
    * expired - logged as warning
    * failed - logged as error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename="login_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


class TestLogEvent(TestCase):
    def test_success_status_logs_info_message(self):
        with self.assertLogs("log_event", level="INFO") as log_records:
            log_event("alice", "success")

        self.assertEqual(
            log_records.output,
            ["INFO:log_event:Login event - Username: alice, Status: success"],
        )

    def test_expired_status_logs_warning_message(self):
        with self.assertLogs("log_event", level="WARNING") as log_records:
            log_event("bob", "expired")

        self.assertEqual(
            log_records.output,
            ["WARNING:log_event:Login event - Username: bob, Status: expired"],
        )

    def test_failed_status_logs_error_message(self):
        with self.assertLogs("log_event", level="ERROR") as log_records:
            log_event("charlie", "failed")

        self.assertEqual(
            log_records.output,
            ["ERROR:log_event:Login event - Username: charlie, Status: failed"],
        )

    def test_unknown_status_logs_error_message(self):
        with self.assertLogs("log_event", level="ERROR") as log_records:
            log_event("diana", "blocked")

        self.assertEqual(
            log_records.output,
            ["ERROR:log_event:Login event - Username: diana, Status: blocked"],
        )

    def test_success_status_does_not_log_warning_or_error(self):
        with self.assertLogs("log_event", level="INFO") as log_records:
            log_event("eve", "success")

        self.assertEqual(len(log_records.records), 1)
        self.assertEqual(log_records.records[0].levelno, logging.INFO)


if __name__ == "__main__":
    main()
