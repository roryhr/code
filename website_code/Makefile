# start server on http://localhost:8000/
dev:
	source activate py39 && pelican --listen --autoreload --relative-urls

publish:
	source activate py39 && \
	pelican && \
	cd output/ && \
	git add -A && \
	git commit && \
	git push