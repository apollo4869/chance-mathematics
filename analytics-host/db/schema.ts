import {sqliteTable, integer, text, index, uniqueIndex} from 'drizzle-orm/sqlite-core';
export const visits=sqliteTable('reading_visits',{
  id:text('id').primaryKey(),day:text('day').notNull(),chapter:integer('chapter').notNull(),locale:text('locale').notNull(),
  visitorDay:text('visitor_day').notNull(),source:text('source').notNull(),started:integer('started_ms').notNull(),last:integer('last_ms').notNull(),
  seq:integer('seq').notNull().default(0),active:integer('active_ms').notNull().default(0),progress:integer('progress').notNull().default(0),
  next:integer('next_clicked').notNull().default(0),interest:text('interest'),
},t=>[index('visits_day_chapter').on(t.day,t.chapter),index('visits_visitor_started').on(t.visitorDay,t.started)]);
export const transitions=sqliteTable('reading_transitions',{
  from:text('from_visit').notNull(),to:text('to_visit').notNull(),day:text('day').notNull(),fromChapter:integer('from_chapter').notNull(),toChapter:integer('to_chapter').notNull(),source:text('source').notNull(),
},t=>[uniqueIndex('transition_once').on(t.from,t.toChapter),index('transitions_day').on(t.day)]);
export const owner=sqliteTable('analytics_owner',{id:integer('id').primaryKey(),subject:text('subject').notNull()});
export const maintenance=sqliteTable('analytics_maintenance',{id:integer('id').primaryKey(),lastDay:text('last_day').notNull()});
