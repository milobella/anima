FROM python:3.8
LABEL maintainer="celian.garcia1@gmail.com"

# Some arguments used for labelling
ARG BUILD_DATE
ARG VCS_REF
ARG BUILD_VERSION
ARG SSH_RSA_KEY
ARG PROJECT_NAME
ARG MODULE_NAME
ARG MODULE_DESCRIPTION

# Labels.
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="$PROJECT_NAME::$MODULE_NAME"
LABEL org.label-schema.description=$MODULE_DESCRIPTION
LABEL org.label-schema.url="https://www.$PROJECT_NAME.com/"
LABEL org.label-schema.vcs-url="https://github.com/$PROJECT_NAME/$MODULE_NAME"
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.version=$BUILD_VERSION
LABEL org.label-schema.docker.cmd="docker run -it $DOCKER_IMAGE:$BUILD_VERSION"

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

# run command
CMD ["anima_launcher"]
