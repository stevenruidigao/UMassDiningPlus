#!/bin/bash

gofmt -w *.go && go get && go build && ./umassdiningplus.tech
