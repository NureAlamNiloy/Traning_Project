import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    test_internet_speed()
