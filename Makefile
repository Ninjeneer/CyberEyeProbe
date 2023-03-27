run-dummy:
	docker run --env-file probedummy/.env ninjeneer/vuln-scanner-probe:probe-dummy

run-nmap:
	docker run --env-file probenmap/.env ninjeneer/vuln-scanner-probe:probe-nmap


build-nmap:
	docker build -f probenmap/Dockerfile . -t ninjeneer/vuln-scanner-probe:probe-nmap

build-dummy:
	docker build -f probedummy/Dockerfile . -t ninjeneer/vuln-scanner-probe:probe-dummy