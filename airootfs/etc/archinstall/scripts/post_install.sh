#!/bin/bash
set -e

# Add Flathub remote
flatpak remote-add --if-not-exists flathub \
    https://dl.flathub.org/repo/flathub.flatpakrepo

echo "FlowOS post-install complete."