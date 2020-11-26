build-MecabFunction:
	$(eval MecabVer := mecab-0.996)
	$(eval IpadicVer := mecab-ipadic-2.7.0-20070801)

	# Download MeCab
	curl -L -o $(MecabVer).tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
	curl -L -o $(IpadicVer).tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
	tar -zxvf $(MecabVer).tar.gz
	tar -zxvf $(IpadicVer).tar.gz

	# Install MeCab
	cd ./$(MecabVer); \
	./configure --prefix=/var/task --with-charset=utf8; \
	make && make install
	# Install MeCab dic
	cd ./$(IpadicVer); \
	./configure --prefix=/var/task --with-charset=utf8 --with-mecab-config=/var/task/bin/mecab-config; \
	make && make install

	# Copy installed MeCab
	cp -r /var/task/* $(ARTIFACTS_DIR)

	# Copy Python files
	cp *.py $(ARTIFACTS_DIR)
	cp requirements.txt $(ARTIFACTS_DIR)
	python -m pip install -r requirements.txt -t $(ARTIFACTS_DIR)
	rm -rf $(ARTIFACTS_DIR)/bin
