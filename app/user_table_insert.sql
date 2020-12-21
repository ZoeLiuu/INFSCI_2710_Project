drop table user;

CREATE TABLE `user`(
`user_id` varchar(64) NOT NULL,
`username` varchar(20) NOT NULL unique,
`user_type` varchar(64) NOT NULL,
`password_hash` varchar(128) NOT NULL,
primary key(`username`));




insert into user(user_id, username, user_type,password_hash)
values ("DT1013066794", "demo_doctor_1", "doctor","pbkdf2:sha256:150000$kbUR6pm0$8f985a44918310e39f7f5647ebcd89a679823338a312306428f3336391124d7c" ),
("DT1003914227", "demo_doctor_2", "doctor", "pbkdf2:sha256:150000$vBUWqoSl$5444761fc34d7249ae9437fe606e6f8148b362f36089f107b35d94fcf773c7de'"),
("P56544020", "demo_patient_1", "patient", "pbkdf2:sha256:150000$EnUyE0D2$418a45c1036643153d579d813470c10ec1b726d672834f63e5e97fef750e8660"  ),
("P71774482", "demo_patient_2", "patient", "pbkdf2:sha256:150000$wpx0UiQi$b932da13ac6db1035a3c615c9d1dbefaafb7a5e68f3ee21548747c2635994f36" ),
("PC165750", "demo_pharmacy_1", "pharmacy", "pbkdf2:sha256:150000$ukh4bcPB$31e988fe950daa94800008641249f58c4189a1470e12ade66d4d6dd5b56ee0a1" ),
("PC301085", "demo_pharmacy_2", "pharmacy", "pbkdf2:sha256:150000$lW9i3PFA$489eb3604ac1c9577d25b9321c0547e5452c9e4a770475199d23962f028debf4" ),
("PP200053", "demo_plant_1", "plant", "pbkdf2:sha256:150000$xOUtxSUL$1654877418564ecbad06d27d1f3350117dbd857ba9ad4c2a79ef690f2b79cba0" ),
("PP323961", "demo_plant_2", "plant", "pbkdf2:sha256:150000$KPfMVOQK$3a388349cac235015c4c334f3c74cc605e90ffb6cd151b4503fab3846067f051" );

#generate_password_hash('doctor_pass_1')
#generate_password_hash('doctor_pass_2')
#generate_password_hash('patient_pass_1')
#generate_password_hash('patient_pass_2')
#generate_password_hash('pharmacy_pass_1')
#generate_password_hash('pharmacy_pass_2')
#generate_password_hash('plant_pass_1')
#generate_password_hash('plant_pass_2')
