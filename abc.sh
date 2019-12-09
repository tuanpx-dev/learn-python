#!/usr/bin/env bash


# Author : Tuan
# Copyright (c) Alright
# Script run test

HELLO="Xin chào, "
HELLO=$(printf "%s %s" "$HELLO" "$(whoami)" "!")
DAY="Hôm nay là ngày "
DAY=$(printf "%s %s" "$DAY" "$(date)")
echo ${HELLO}
echo ${DAY}
