
# start server on port 8000
dev:
	source activate web && \
	pelican --listen --autoreload --relative-urls

clean:
	./develop_server.sh stop && \
	rm -rf __pycache__/

publish:
	source activate web && \
	pelican && \
	cd output/ && \
	git add -A && \
	git commit && \
	git push