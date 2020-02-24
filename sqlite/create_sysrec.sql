CREATE TABLE IF NOT EXISTS environments (
	environment TEXT PRIMARY KEY,
	create_date REAL NOT NULL,
	status TEXT NOT NULL
	);
	
INSERT INTO environments
	(environment, create_date, status) 
	VALUES 
		("DEV", julianday('now'), "ACTIVE"),
		("PRODQA", julianday('now'), "ACTIVE"),
		("PRODMIE", julianday('now'), "ACTIVE"),
		("PROD", julianday('now'), "ACTIVE");


CREATE TABLE IF NOT EXISTS tiers (
	tier TEXT PRIMARY KEY,
	create_date REAL NOT NULL,
	status TEXT NOT NULL
	);

INSERT INTO tiers
	(tier, create_date, status) 
VALUES 
	("META", julianday('now'), "ACTIVE"),
	("MID", julianday('now'), "ACTIVE"),
	("COMPUTE", julianday('now'), "ACTIVE"),
	("LASR", julianday('now'), "ACTIVE"),
	("UTIL", julianday('now'), "ACTIVE")
	;

CREATE TABLE IF NOT EXISTS hosts (
	hostname TEXT PRIMARY KEY,
	tier TEXT NOT NULL,
	environment TEXT NOT NULL,
	role TEXT,
	status TEXT NOT NULL,
	application_install_status TEXT NOT NULL,
	discovery_date REAL NOT NULL,
	last_update_date REAL NOT NULL
	);
	
INSERT INTO hosts
	(hostname, tier, environment, status, application_install_status, discovery_date, last_update_date)
VALUES
	("devtestmeta1", "META", "DEV", "ACTIVE", "NOT_INSTALLED", julianday('now'), julianday('now'));
	
	
INSERT INTO hosts
	(hostname, tier, environment, status, application_install_status, discovery_date, last_update_date)
VALUES
	("devtestmeta2", "META", "PRODQA", "ACTIVE", "NOT_INSTALLED", julianday('now'), julianday('now'));
	
	