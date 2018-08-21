#!/usr/bin/env bash

sudo apt-get install supervisor
sudo netstat -tlpn | grep 800 #Check that the chosen port is already in use.
