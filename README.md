# docker-python-chromedriver

Python with Chromedriver, for running automated tests for https://www.caru-care.com/

## Quick Try

```bash
mkdir pt
```
```bash
git clone https://github.com/st-mn/docker-python-chromedriver.git && cd docker-python-chromedriver
```
```bash
cd docker-python-chromedriver
```
```bash
docker run -it -w /usr/workspace -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:latest bash
```
```bash
pip install selenium
```
```bash
python test_script.py
```


## Image includes
 - Python (Debian or Alpine based)
 - Google Chrome
 - Chromedriver
 - Selenium (in some versions)
 - Xvfb (in some versions)


