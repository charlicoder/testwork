# Dockerfile for React app
FROM node:18

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the project
COPY . .

# Start the React app
CMD ["yarn", "start"]
