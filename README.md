# Niah Security Inc.

[![N|Solid](http://cyberthreatinfo.expert/static/logo.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Niah is open source vulnerability scanner. Confidently scan for vulnerablities in your source code, container image, virtual machine or physical servers.


  - Develop using open source...with confidence
  - Develop using open source...with confidence
  - Develop using open source...with confidence

# New Features!

  - Dependancies Vulnerabilites Scanner
  - Platform Vulnerability Scanner
  - Application Vulnerability Scanner

You can also:
  - Import the project from GitHub and scan vulnerabilities for dependancies
  - View Details Reports on Niah.io Portal
  - Manage bill of materials and 

### Installation from pip

```sh
$ pip install niah
```

### Installation from source

```sh
$ git clone https://github.com/umasolution/niah_scanner.git
cd niah_scanner
python setup.py install
```

### Development

Usage 1:
```sh
$ niah --help 
$ usage: niah [-h] [-v] {scan,auth,watch,connector} ...

positional arguments:
  {scan,auth,watch,connector}

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

Usage 2:
```sh
$ niah scan --help
usage: niah scan [-h] [--connector <type> <name> <repo name> <branch name>]
                 [-r REPORTPATH] [-n PROJECTNAME] [-up UPLOAD] [-l LABEL]
                 {system,application,dependancies} ...

positional arguments:
  {system,application,dependancies}

optional arguments:
  -h, --help            show this help message and exit
  --connector <type> <name> <repo name> <branch name>
                        Need four arguments : <connectory type> <connector
                        name> <repo name> <branch name> Example : niah scan
                        dependancies github conn1 repo1 branch1 (If you need
                        to pull specific branch) niah scan dependancies github
                        conn1 repo1 '' (If you need to pull latest available
                        code)
  -r REPORTPATH, --reportpath REPORTPATH
                        Report path where you need to store.
  -n PROJECTNAME, --projectname PROJECTNAME
                        Project name.
  -up UPLOAD, --upload UPLOAD
                        Upload report yes/no
  -l LABEL, --label LABEL
                        Project label
```

Usage 3:
```sh
$ niah scan dependancies --help
usage: niah scan dependancies [-h] [-lang LANG] [-t TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -lang LANG, --lang LANG
                        select dependancies `python/composer/npm/maven` which
                        you need to scan.
  -t TARGET, --target TARGET
                        Target scan folder
```

Example - Scan System Packages:
```sh
$ niah scan system
```

Example - Scan Installed Applications:
```sh
$ niah scan application
```
Example - Scan Dependancies:
```sh
$ niah scan dependancies
```

### Todos

 - Docker Container Scanner

License
----

MIT

**niah.io!**

