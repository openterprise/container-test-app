#!/bin/bash

cd ./blue
docker push openterprise/blue:latest &
cd ../green
docker push openterprise/green:latest &
cd ../orange
docker push openterprise/orange:latest &
cd ../red
docker push openterprise/red:latest &
cd ../yellow
docker push openterprise/yellow:latest &

