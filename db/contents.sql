CREATE TABLE IF NOT EXISTS contents
(
    video_id        INTEGER NOT NULL,
    duration        INTEGER NOT NULL,
    content         TEXT,
    paragraph_start INTEGER,
    start_time      INTEGER NOT NULL,
    PRIMARY KEY (video_id, start_time)
);