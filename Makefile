run-dummy:
	docker run ninjeneer/probe-dummy

run-nmap:
	docker run --env-file probenmap/.env ninjeneer/probe-nmap


build-nmap:
	docker build -f probenmap/Dockerfile . -t ninjeneer/probe-nmap

build-dummy:
	docker build -f probedummy/Dockerfile . -t ninjeneer/probe-dummy