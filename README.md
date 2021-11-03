# 4chan downloader
****

<div align=center>
    <h1>4chan downloader</h1>
    <b>Downloads all images from a 4chan board. I know, I am addicted to downloads.</b><br><br>
    <a href="https://github.com/r4v10l1/4chan_downloader/network/members"><img src="https://img.shields.io/github/forks/r4v10l1/4chan_downloader.svg?style=for-the-badge&logo=4chan&color=67c634&logoColor=67c634" alt="Forks"></a>
      <a href="https://github.com/r4v10l1/4chan_downloader/stargazers"><img src="https://img.shields.io/github/stars/r4v10l1/4chan_downloader.svg?style=for-the-badge&logo=4chan&color=67c634&logoColor=67c634" alt="Stars"></a>
</div>

#

⚠️ If you download a lot of images, you might get banned! I am not responsible at all. ⚠️

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
