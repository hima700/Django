#!/bin/bash

# This script adds seed data
# https://en.wikipedia.org/wiki/Database_seeding

./manage.py loaddata greetings/seeds.yaml
