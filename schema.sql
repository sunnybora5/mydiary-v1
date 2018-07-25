create table entries(
  id serial not null primary key,
  title varchar not null,
  body text not null,
  created_at timestamp not null default now(),
  updated_at timestamp default current_timestamp
);

create table users(
  id serial not null primary key,
  name varchar not null,
  email varchar not null,
  password varchar not null,
  created_at timestamp not null default now(),
  updated_at timestamp default current_timestamp
);
