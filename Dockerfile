# Start with the Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to the root user to install Docker and Docker Compose
USER root

# Install Docker
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Add Jenkins user to the Docker group, using existing group if necessary
RUN if getent group docker; then \
        usermod -aG docker jenkins; \
    else \
        groupadd -g 999 docker && \
        usermod -aG docker jenkins; \
    fi

# Switch back to the Jenkins user
USER jenkins
