SELECT
    ROUND(
        COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Activity a
WHERE event_date = (
    SELECT DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
    FROM Activity
    WHERE player_id = a.player_id
);