# docker-python-chromedriver

Python with Chromedriver, for running automated tests for https://www.caru-care.com/

## Image includes
 - Python (Debian or Alpine based)
 - Google Chrome
 - Chromedriver
 - Selenium (in some versions)
 - Xvfb (in some versions)

## Quick Try

```bash
mkdir pt
```
```bash
git clone https://github.com/st-mn/docker-python-chromedriver.git && cd docker-python-chromedriver
```
```bash
virtualenv venv && source venv/bin/activate
```
```bash
docker run -it -w /usr/workspace -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:latest bash
```
```bash
pip install selenium && python test_script.py
```

## Sample test cases

https://github.com/st-mn/docker-python-chromedriver/blob/master/test_script.py 


