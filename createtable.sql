DROP TABLE IF EXISTS board-game-data;
CREATE TABLE board-game-data (
  rank int,
  game_id real,
  game_name text,
  min_players int,
  max_players int,
  avg_time real,
  min_time real,
  max_time real,
  pub_year int,
  avg_rating real,
  geek_rating real,
  num_votes int,
  image_url text,
  min_age int,
  mechanic text,
  owned int,
  category text,
  designer text,
  weight real
);
