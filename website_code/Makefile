
# start server on port 8000
dev:
	source activate web && \
	pelican --listen

clean:
	./develop_server.sh stop && \
	rm -rf __pycache__/

publish:
	cd output/
	git commit 