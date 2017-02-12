#!/usr/bin/env bash

workon Warmy

celery worker -A swicher --loglevel=info

