# start server on http://localhost:8000/
dev:
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