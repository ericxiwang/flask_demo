BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "BUG_ATTACHMENT" (
	"id"	INTEGER NOT NULL UNIQUE,
	"bug_id"	INTEGER,
	"bug_attachment_link"	TEXT,
	"bug_attachment_name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "BUG_COMMENT" (
	"id"	INTEGER,
	"bug_id"	INTEGER,
	"bug_comment"	TEXT,
	"bug_commenter"	TEXT,
	"bug_comment_datetime"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "BUG_HISTORY" (
	"id"	INTEGER NOT NULL UNIQUE,
	"bug_id"	INTEGER,
	"bug_history_status"	TEXT,
	"bug_history_datetime"	TEXT,
	"bug_history_submitter"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "BUG_INFO" (
	"id"	INTEGER UNIQUE,
	"bug_title"	TEXT,
	"bug_desc"	TEXT,
	"bug_level"	INTEGER NOT NULL,
	"bug_assignee"	TEXT NOT NULL,
	"bug_status"	TEXT NOT NULL,
	"bug_category"	TEXT,
	"bug_keywords"	TEXT,
	"bug_datetime"	TEXT,
	"bug_project"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "PROJECT_INFO" (
	"id"	INTEGER NOT NULL UNIQUE,
	"project_name"	TEXT NOT NULL,
	"project_desc"	TEXT,
	"project_owner"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TICKET_HISTORY" (
	"id"	INTEGER NOT NULL UNIQUE,
	"ticket_current_status"	TEXT,
	"ticket_editor"	TEXT,
	"ticket_edit_datetime"	TEXT,
	"ticket_comment"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TICKET_INFO" (
	"id"	INTEGER NOT NULL UNIQUE,
	"ticket_title"	TEXT,
	"ticket_type"	TEXT,
	"ticket_description"	TEXT,
	"ticket_submitter"	TEXT,
	"ticket_datetime"	TEXT,
	"ticket_assignee"	TEXT,
	"ticket_status"	TEXT,
	"ticket_scope"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "USER_INFO" (
	"id"	INTEGER,
	"user_name"	TEXT,
	"email"	TEXT,
	"user_password"	TEXT,
	"group_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "BUG_INFO" VALUES (1,'bug-001','login failed',1,'dev_engineer@test.com','new','frontend','login','Tue Sep 30 2025','frontend api');
INSERT INTO "BUG_INFO" VALUES (2,'bug-002','dashboard stuck',2,'dev_engineer@test.com','assigned','frontend','dashboard','Tue Sep 30 2025','frontend api');
INSERT INTO "BUG_INFO" VALUES (3,'bug-003','memory leak',3,'dev_engineer@test.com','inprogress','backend','sys,os','Tue Sep 30 2025','backend api');
INSERT INTO "BUG_INFO" VALUES (4,'bug-004','OOM',4,'qa_engineer@test.com','review','image','sys,os','Tue Sep 30 2025','backend api');
INSERT INTO "BUG_INFO" VALUES (5,'bug-005','page loading slow',5,'admin@admin.com','fixed','image','frontend','Tue Sep 30 2025','frontend api');
INSERT INTO "BUG_INFO" VALUES (6,'bug-006','load balance issue',1,'admin@admin.com','new','backend','frontend','Tue Sep 30 2025','devops');
INSERT INTO "BUG_INFO" VALUES (7,'bug-007','nginx config issue',2,'admin@admin.com','inprogress','frontend','frontend','Tue Sep 30 2025','devops');
INSERT INTO "BUG_INFO" VALUES (8,'bug-008','database connection issue',3,'qa_engineer@test.com','review','frontend','frontend','Tue Sep 30 2025','devops');
INSERT INTO "BUG_INFO" VALUES (9,'bug-009','dashboard css issue',4,'admin@admin.com','new','frontend','frontend','Tue Sep 30 2025','frontend api');
INSERT INTO "BUG_INFO" VALUES (10,'bug-010','bug-test-desc-010',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','backend api');
INSERT INTO "BUG_INFO" VALUES (75,'bug-011','bug-test-desc-011',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','frontend api');
INSERT INTO "BUG_INFO" VALUES (76,'bug-012','bug-test-desc-012',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','backend api');
INSERT INTO "BUG_INFO" VALUES (77,'bug-013','bug-test-desc-013',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','backend api');
INSERT INTO "BUG_INFO" VALUES (78,'bug-014','bug-test-desc-014',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','devops');
INSERT INTO "BUG_INFO" VALUES (79,'bug-015','bug-test-desc-015',5,'dev_engineer@test.com','new','frontend','frontend','Tue Sep 30 2025','devops');
INSERT INTO "PROJECT_INFO" VALUES (1,'frontend api','React project','admin@admin.com');
INSERT INTO "PROJECT_INFO" VALUES (2,'backend api','Flask project','admin@admin.com');
INSERT INTO "PROJECT_INFO" VALUES (3,'devops','devops manifest','admin@admin.com');
INSERT INTO "TICKET_INFO" VALUES (1,'new-ticket-001','task','login page html optimize','admin','Fri Sep 21 2025','dev_engineer@test.com','new','firewall');
INSERT INTO "TICKET_INFO" VALUES (2,'new-ticket-002','task','sys load speed up','admin','Fri Sep 25 2025','dev_engineer@test.com','new','bigdata');
INSERT INTO "TICKET_INFO" VALUES (3,'new-ticket-003','task','new feature, for storage backup in vm','admin','Fri Sep 26 2025','dev_engineer@test.com','new','iaas');
INSERT INTO "TICKET_INFO" VALUES (4,'new-ticket-004','task','CSS error','admin','Fri Sep 26 2025','qa_engineer@test.com','new','saas');
INSERT INTO "TICKET_INFO" VALUES (5,'new-ticket-005','task','work with system backup feature','admin','Fri Sep 26 2025','qa_engineer@test.com','new','bigdata');
INSERT INTO "TICKET_INFO" VALUES (6,'new-ticket-006','task','upgrade kubeadm,kubectl etc','admin','Fri Sep 26 2025','admin@admin.com','new','saas');
INSERT INTO "TICKET_INFO" VALUES (7,'new-ticket-007','task','add rtmp plugin to nginx service','admin','Fri Sep 26 2025','DEV001','new','saas');
INSERT INTO "TICKET_INFO" VALUES (8,'new-ticket-008','task','refine kafka partiation and topic','admin','Fri Sep 26 2025','DEV001','new','saas');
INSERT INTO "TICKET_INFO" VALUES (10,'inprogress-ticket-001','task','inprogress-ticket-001-desc
','admin','Fri Sep 26 2025','admin@admin.com','inprogress',NULL);
INSERT INTO "TICKET_INFO" VALUES (14,'inprogress-ticket-002','task','inprogress-ticket-002-desc','admin','Fri Sep 26 2025','admin@admin.com','inprogress',NULL);
INSERT INTO "TICKET_INFO" VALUES (15,'inprogress-ticket-003','task','back end api needed','admin','Fri Sep 26 2025','admin@admin.com','inprogress',NULL);
INSERT INTO "TICKET_INFO" VALUES (16,'inprogress-ticket-004','task','need diagram to represent whole tasks status','admin','Fri Sep 26 2025','admin@admin.com','inprogress',NULL);
INSERT INTO "TICKET_INFO" VALUES (17,'inprogress-ticket-005','task','setup redis for cache server','admin','Mon Sep 19 2025','admin@admin.com','inprogress',NULL);
INSERT INTO "TICKET_INFO" VALUES (18,'review-ticket-001','task','bug data datagrid page ','admin','Mon Sep 19 2025','admin@admin.com','review',NULL);
INSERT INTO "TICKET_INFO" VALUES (112,'review-ticket-002','task','gui-new-ticket-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','review',NULL);
INSERT INTO "TICKET_INFO" VALUES (113,'review-ticket-003','task','gui-new-ticket-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','review',NULL);
INSERT INTO "TICKET_INFO" VALUES (114,'review-ticket-004','task','gui-new-ticket-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','review',NULL);
INSERT INTO "TICKET_INFO" VALUES (115,'review-ticket-005','task','gui-new-ticket-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','review',NULL);
INSERT INTO "TICKET_INFO" VALUES (117,'done-ticket-001','task','done-ticket-001-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','done',NULL);
INSERT INTO "TICKET_INFO" VALUES (118,'done-ticket-002','task','done-ticket-002-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','done',NULL);
INSERT INTO "TICKET_INFO" VALUES (119,'done-ticket-003','task','done-ticket-003-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','done',NULL);
INSERT INTO "TICKET_INFO" VALUES (120,'done-ticket-004','task','done-ticket-004-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','done',NULL);
INSERT INTO "TICKET_INFO" VALUES (121,'done-ticket-005','task','done-ticket-005-desc','admin','Tue Nov 25 2025','qa_engineer@test.com','done',NULL);
INSERT INTO "USER_INFO" VALUES (1,'QA001','qa_engineer@test.com','1234',1);
INSERT INTO "USER_INFO" VALUES (2,'admin','admin@admin.com','1234',3);
INSERT INTO "USER_INFO" VALUES (3,'manager','manager@gmail.com','1234',1);
INSERT INTO "USER_INFO" VALUES (4,'DEV001','dev_engineer@test.com','1234',1);
COMMIT;
