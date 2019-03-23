# A docker base image based on Node.js 8
FROM node:8

# Set app working directory
WORKDIR /usr/src/app

# Install app dependencies
# Copy package.json AND package-lock.json and then run npm install
COPY package*.json ./
RUN npm install

# Copy the node.js app to the working directory
COPY app.js ./

RUN echo "This runs during the build process..." 

# Set the default execution command for this container
CMD node app.js
