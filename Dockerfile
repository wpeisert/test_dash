FROM wpeisert/dash

COPY ./app/* /app/

EXPOSE 8050

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
