#!/bin/bash

cd ./blue
docker build --tag openterprise/blue:latest . &
cd ../green
docker build --tag openterprise/green:latest . &
cd ../orange
docker build --tag openterprise/orange:latest . &
cd ../red
docker build --tag openterprise/red:latest . &
cd ../yellow
docker build --tag openterprise/yellow:latest . &
cd ../purple
docker build --tag openterprise/purple:latest . &
cd ../brown
docker build --tag openterprise/brown:latest . &
