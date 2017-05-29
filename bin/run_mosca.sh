#!/usr/bin/env bash
mosca -v --http-port 3000 --http-bundle | bunyan
