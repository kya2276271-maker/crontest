from datetime import datetime, timezone

def main():
    now = datetime.now(timezone.utc).astimezone()
    print("✅ Scheduled run OK")
    print("Local time:", now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

if __name__ == "__main__":
    main()
