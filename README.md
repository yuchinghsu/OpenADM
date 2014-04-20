OmniUI
------
A generalized web UI for various SDN controllers

##Introduction##
OmniUI is a debugging and performance evaluation tool for Software-Defined Network. It provides graphical user interface to illustrate information of flows, devices and statistic data. Features of OmniUI includes:

- Compatible with various controller
- Forwarding path of specific flow
- Topology view with traffic information
- Statistic data of specific flow
- Statistic data of specific port/link
- Dynamic flow migration

##Installation##
- Install controller adapter
    * Please refer to `/adapter/<controller>/README.md`
- Install web UI
    1. Install a web server (e.g. Apache)
    2. Simply copy `/webui` into root directory of website
- Install MongoDB 
    * Please refer to [Install MongoDB](http://docs.mongodb.org/manual/installation/)
- Modify the config file
    * `core/config.json`: Update `dbip`, `user` and `password` in both UIPusher and DbCollection section
    
    if you are access webui from outside localhost (optional)
    * `core/core.py`: Update `Access-Control-Allow-Origin`
    * `webui/js/omniui.js`: Update IP in `function loadJSONP()` and `function sendFlow()`
