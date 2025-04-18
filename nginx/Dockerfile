FROM nginx:1.25

# Remove the default configuration file
RUN rm /etc/nginx/conf.d/default.conf
# Copy the custom configuration file
COPY htmx_book.conf /etc/nginx/conf.d/
