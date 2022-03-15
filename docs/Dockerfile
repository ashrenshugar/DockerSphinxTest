FROM tk0miya/sphinx-base

WORKDIR /docs
ADD requirements.txt /docs
RUN pip3 install -r requirements.txt
CMD make html
