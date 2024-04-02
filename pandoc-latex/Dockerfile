# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND noninteractive

# Install basic tools
RUN apt update -y \
    && apt install -y \
    curl \
    locales \
    && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

# Install Pandoc (version: 3.1.12.3), [Installing Pandoc - Linux](https://pandoc.org/installing.html#linux)
RUN cd /tmp \
    && curl -L -o pandoc-3.1.12.3-1-amd64.deb https://github.com/jgm/pandoc/releases/download/3.1.12.3/pandoc-3.1.12.3-1-amd64.deb \
    && dpkg -i pandoc-3.1.12.3-1-amd64.deb

# Install TeX Live: official LaTeX distribution, [TeX Live - Quick install for Unix](https://www.tug.org/texlive/quickinstall.html)
# `--scheme=small` corresponds to the BasicTeX variant of MacTeX.
RUN cd /tmp \
    && curl -L -o install-tl-unx.tar.gz https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
    && mkdir -p install-tl-unx
    && tar -xvzf install-tl-unx.tar.gz -C install-tl-unx \
    && cd install-tl-* \
    && perl ./install-tl --no-interaction --scheme=small

# Finally, prepend `/usr/local/texlive/YYYY/bin/PLATFORM` to your PATH.
ENV PATH="/usr/local/texlive/2024/bin/x86_64-linux/:${PATH}"

# Install LaTeX library via `tlmgr` in need.
RUN tlmgr install collection-fontsrecommended