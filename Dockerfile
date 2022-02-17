FROM python:3.8-slim-buster
RUN pip install mkdocs
WORKDIR ./docs .
CMD ["mkdocs", "serve", "-a 0.0.0.0:8000"]