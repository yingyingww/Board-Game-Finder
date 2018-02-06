DROP TABLE IF EXISTS boardgames;
CREATE TABLE boardgames (
  rank real,
  game_id real,
  game_name text,
  min_players real,
  max_players real,
  avg_time real,
  min_time real,
  max_time real,
  pub_year real,
  avg_rating real,
  geek_rating real,
  num_votes real,
  image_url text,
  min_age real,
  mechanic text,
  owned real,
  category text,
  designer text,
  weight real
);
