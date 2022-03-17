FROM python:slim
LABEL maintainer="Sphinx Team <https://www.sphinx-doc.org/>"

WORKDIR /docs
RUN apt-get update \
    && apt-get install --no-install-recommends -y --fix-missing \
    graphviz \
    imagemagick \
    make \
    \
    latexmk \
    lmodern \
    fonts-freefont-otf \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-luatex \
    texlive-xetex \
    xindy \
    tex-gyre \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir -U pip
RUN python3 -m pip install --no-cache-dir Sphinx==4.4.0 Pillow
RUN python3 -m pip install --no-cache-dir myst-parser
RUN python3 -m pip install --no-cache-dir sphinxcontrib-svg2pdfconverter[CairoSVG]

CMD ["make", "latexpdf"]