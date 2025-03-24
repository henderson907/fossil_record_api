DROP DATABASE IF EXISTS fossils;

CREATE DATABASE fossils;
USE fossils;

CREATE TABLE fossil
(
	id INT AUTO_INCREMENT,
	species VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    discovered_on DATE NOT NULL,
    discovered_by VARCHAR(255) NOT NULL,
    fossil_type VARCHAR(255),
    complete BOOLEAN DEFAULT FALSE,
    period VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO fossil (species, country, discovered_on, discovered_by, fossil_type, complete, period)
VALUES
("Velociraptor mongoliensis", "Mongolia", "1923-08-11", "Peter Kaisen", "skull", TRUE, "Cretaceous"),
("Albertosaurus sarcophagus", "Canada", "1884-06-09", "Joseph Burr Tyrrell", "skull", FALSE, "Cretaceous"),
("Stegosaurus armatus", "United States of America", "1850-04-15", "Arthur Lakes", "vertebrae", FALSE, "Jurassic"),
("Parasaurolophus tubicen", "United States of America", "1921-12-07", "Charles Sternberg", "skull", FALSE, "Cretaceous"),
("Pachycephalosaurus wyomingensis", "United States of America", "1854-02-22", "Ferdinand Vandeveer Hayden", "squamosal bone", FALSE, "Cretaceous"),
("Caihong juji", "China", "2014-02-01", "Yang Jun", "skeleton", TRUE, "Jurassic"),
("Coelophysis bauri", "United States of America", "1887-11-23", "Edward Drinker Cope", "skeleton", FALSE, "Triassic"),
("Eoraptor lunensis", "Argentina", "1991-09-21", "Ricardo Martinez", "Tooth", TRUE, "Triassic"),
("Dilophosaurus wetherilli", "United States of America", "1942-07-22", "Charles Camp", "skeleton", FALSE, "Jurassic"),
("Hesperonyx martinhotomasorum", "Portugal", "2021-05-12", "Carla Alexandra Tomas", "metatarsal bone", True, "Jurassic");

