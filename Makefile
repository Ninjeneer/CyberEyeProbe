new:
	chmod +x create_probe.sh
	./create_probe.sh

run-dummy:
	docker run --env-file probedummy/.env ninjeneer/vuln-scanner-probe:probe-dummy

run-nmap:
	docker run --env-file probenmap/.env ninjeneer/vuln-scanner-probe:probe-nmap

run-nikto:
	docker run --env-file probenikto/.env ninjeneer/vuln-scanner-probe:probe-nikto




build-nmap:
	docker build -f probenmap/Dockerfile . -t ninjeneer/vuln-scanner-probe:probe-nmap

build-dummy:
	docker build -f probedummy/Dockerfile . -t ninjeneer/vuln-scanner-probe:probe-dummy

build-nikto:
	docker build -f probenikto/Dockerfile . -t ninjeneer/vuln-scanner-probe:probe-nikto