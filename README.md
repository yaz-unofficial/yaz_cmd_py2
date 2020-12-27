# yaz_cmd_py2
## Requires 
* `python2`
* [http://zoom.z3950.org/bind/python/](http://zoom.z3950.org/bind/python/)
  * [https://pypi.org/project/PyZ3950/](https://pypi.org/project/PyZ3950/) is already included and slightly fixed
  * python2 -m venv venv
  * `pip install ply`

* needs libyaz from yaz toolkit
  * [https://www.indexdata.com/resources/software/yaz/](https://www.indexdata.com/resources/software/yaz/)
  * [http://ftp.indexdata.dk/pub/yaz/yaz-5.27.1.tar.gz](http://ftp.indexdata.dk/pub/yaz/yaz-5.27.1.tar.gz)
    * `./buildconf.sh`
    * `./configure`
    * `make`
    * `sudo make install`
  * or
    * `./buildconf.sh`
    * `./configure --prefix=$HOME/myapps`
    * `make`
    * `make install`
    * ...
    * Add `export PATH="$HOME/myapps/bin:$PATH"` to `.bashrc`
    * (Reload file with `source ~/.bashrc`

## Usage
`python yaz_cmd_py2.py <host> <port> <databaseName> <user> <password> <syntax> <query>`  
`python yaz_cmd_py2.py --test <number_from_1-5>`  
Syntax is either `mab`or `usmarc`  
Query in ccl format  
