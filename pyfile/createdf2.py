import random
import os
def create_log_file(filename: str, lines: int):
    status =['SUCCESS', 'FAILED', 'SUCCESS', 'PENDING', 'SUCCESS']
    err_codes=["ERR_TIMEOUT", "ERR_AUTH_FAILED", "ERR_CONN_DROP", "ERR_INSUFFICIENT_FUNDS"]

    with open(filename, "w") as f:
        for i in range (1, lines):
            tx_id = f"TXN{10000+i}"
            stat = random.choice(status)
            if stat == "FAILED":
                err = random.choice(err_codes)
                f.write(f"{tx_id}, {stat}, {err}\n")
            else:
                f.write(f"{tx_id}, {stat}, NONE\n")
    print("Log file creation successful" + '='*40)

if __name__ == "__main__":
    log_filename = "/home/deepak/projects/practice/practice/datafile/practice_logfile.log"
    create_log_file(log_filename, lines=70)


