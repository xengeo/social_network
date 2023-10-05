-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email, username) VALUES ('bob@test.com', 'bob');
INSERT INTO users (email, username) VALUES ('fred@test.com', 'fred');
INSERT INTO users (email, username) VALUES ('sarah@test.com', 'sarah');
INSERT INTO users (email, username) VALUES ('maria@test.com', 'maria');

INSERT INTO posts (title, content, views, user_id) VALUES ('bob_title_1', 'Bob Contents 1', 5, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('bob_title_2', 'bob Contents 2', 2, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('sarah_title_1', 'Sarah Contents 1', 10, 3);