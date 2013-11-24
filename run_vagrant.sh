#!/bin/bash

vagrant up
ssh vagrant@10.13.37.2 -i ~/.vagrant.d/insecure_private_key "/vagrant/files/run_dev.sh"
