# 4chan downloader
**Downloads all images from a 4chan board. I know, I am addicted to downloads.**

⚠️ If you download a lot of images, you might get banned! I am not responsible at all. A VPN is recommended. ⚠️

# 

### Installing

``` shell
https://github.com/r4v10l1/4chan_downloader
cd 4chan_downloader
python -m pip install -r requirements.txt
python3 4chan_downloader.py
```

### Configuration

* You can edit the `debugPrint` variable to print some extra stuff.
* You can edit the `useTorProxy` variable to enable the use of a proxy during the requests. If you enable this, you will need to have tor open and the port it will use will be **9150**.
* You can edit the `sessionMode` variable to store the cookies.

### Logs

The script writes the following information into a log (`4chan_debug.log`):
* When the user starts the program.
* When the user stops the program.
* When the script detects an error.
