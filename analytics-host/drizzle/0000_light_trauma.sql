CREATE TABLE `analytics_maintenance` (
	`id` integer PRIMARY KEY NOT NULL,
	`last_day` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `analytics_owner` (
	`id` integer PRIMARY KEY NOT NULL,
	`subject` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `reading_transitions` (
	`from_visit` text NOT NULL,
	`to_visit` text NOT NULL,
	`day` text NOT NULL,
	`from_chapter` integer NOT NULL,
	`to_chapter` integer NOT NULL,
	`source` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `transition_once` ON `reading_transitions` (`from_visit`,`to_chapter`);--> statement-breakpoint
CREATE INDEX `transitions_day` ON `reading_transitions` (`day`);--> statement-breakpoint
CREATE TABLE `reading_visits` (
	`id` text PRIMARY KEY NOT NULL,
	`day` text NOT NULL,
	`chapter` integer NOT NULL,
	`locale` text NOT NULL,
	`visitor_day` text NOT NULL,
	`source` text NOT NULL,
	`started_ms` integer NOT NULL,
	`last_ms` integer NOT NULL,
	`seq` integer DEFAULT 0 NOT NULL,
	`active_ms` integer DEFAULT 0 NOT NULL,
	`progress` integer DEFAULT 0 NOT NULL,
	`next_clicked` integer DEFAULT 0 NOT NULL,
	`interest` text
);
--> statement-breakpoint
CREATE INDEX `visits_day_chapter` ON `reading_visits` (`day`,`chapter`);--> statement-breakpoint
CREATE INDEX `visits_visitor_started` ON `reading_visits` (`visitor_day`,`started_ms`);