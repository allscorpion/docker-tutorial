FROM debian:stable-slim

COPY docker-tutorial /bin/goserver
ENV PORT=8991
CMD ["/bin/goserver"]