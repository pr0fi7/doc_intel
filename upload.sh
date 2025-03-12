rsync -avz -progress -r -e ssh app rocky:/home/troople/API_DOCUMENT_INTELLIGENCE/
rsync -az -progress -r -e ssh docker-compose.yml rocky:/home/troople/API_DOCUMENT_INTELLIGENCE/
rsync -az -progress -r -e ssh Dockerfile rocky:/home/troople/API_DOCUMENT_INTELLIGENCE/
rsync -az -progress -r -e ssh app/requirements.txt rocky:/home/troople/API_DOCUMENT_INTELLIGENCE/