run:
	@docker-compose -f docker/compose/docker-compose.yml up -d

kill:
	@docker-compose -f docker/compose/docker-compose.yml kill

rm: kill
	@docker-compose -f docker/compose/docker-compose.yml rm -f -a

restart: rm run
	

