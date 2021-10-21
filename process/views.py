from ingest.serializers import ScanSerializer
from ingest.models import Scan
from scanner.consts import Consts
from datetime import datetime, timedelta
import time


# Consts
TIME_BETWEEN_PROCESSES_IN_SECONDS = 5
TIME_BETWEEN_PROCESS_AND_DELETE_IN_SECONDS = 60
TIME_LIMITATION_IN_MINUTES = 20


def process_scans():
    while(True):
        delete_scans_over_time_limit()
        time.sleep(TIME_BETWEEN_PROCESS_AND_DELETE_IN_SECONDS)
        update_scan_statuses()


def update_scan_statuses():
    try:
        accepted_scans_ids = list(Scan.objects.filter(status = Consts.ACCEPTED).values('id'))
        for scan_id in accepted_scans_ids:
            Scan.objects.filter(id = scan_id).update(status = Consts.RUNNING)
        time.sleep(TIME_BETWEEN_PROCESSES_IN_SECONDS)
        running_scans_ids = list(Scan.objects.filter(status = Consts.RUNNING).values('id'))
        for scan_id in running_scans_ids:
            Scan.objects.filter(id = scan_id).update(status = Consts.COMPLETE)
        return f"Status updates succeeded"
    except Exception as ex:
        return f"Status updates failed with exception: {ex}"


def delete_scans_over_time_limit():
    try:
        scans = Scan.objects.filter(creation_time_lte = timedelta(minutes = TIME_LIMITATION_IN_MINUTES))
        scans.delete()
        return f"Delete scans over time limitation succeeded"
    except Exception as ex:
        return f"Delete scans over time limitation failed with exception: {ex}"

