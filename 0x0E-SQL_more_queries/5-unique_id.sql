-- Creates table unique_id where id has unique value
-- Database passed as argument in mysql
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
