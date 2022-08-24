include .env


start:
	docker compose up -d

stop:
	docker compose down

init-db:
	psql 'postgresql://$(DATABASE_USER):$(DATABASE_PASSWORD)@localhost:5432/$(DATABASE_NAME)' < ./backend/trivia.psql
