/*
  Анализ удержания пригласивших (инвайтеров) по месяцам.
  CTE inviters_results собирает статистику по инвайтерам и их приглашённым.
  Внешний запрос считает: количество инвайтеров, удержание (curn_percent),
  новых инвайтеров и общее количество приглашённых.
*/

WITH inviters_results AS (
    SELECT
        to_char(a.created_at, 'YYYY-MM') AS date,
        inviter.id AS inviter_id,
        count(a.id) AS accounts
    FROM
        (
            SELECT id
            FROM accounts
            WHERE registration_type_id = 1
              AND created_at >= '2018-01-01'
        ) AS inviter
        JOIN accounts AS a ON (a.inviter_id = inviter.id)
    WHERE a.created_at >= '2018-01-01'
    GROUP BY date, inviter.id
    ORDER BY 1 ASC
)
SELECT
    date,
    inviters,
    curn_inviter_count,
    round(
        curn_inviter_count :: numeric / (
            inviters + curn_inviter_count - new_inviter_count
        ) * 100, 2
    ) AS curn_percent,
    new_inviter_count
FROM (
    SELECT
        date,
        count(inviter_id) AS inviters,
        SUM(accounts) AS accounts
    FROM inviters_results
    GROUP BY date
) AS t1
LEFT JOIN (
    SELECT
        COALESCE(
            to_char((d1.date || '-01') :: date + '1 month' :: interval, 'YYYY-MM'),
            d2.date
        ) AS date,
        SUM(CASE WHEN d2.date IS NULL THEN 1 END) AS curn_inviter_count,
        array_remove(array_agg(DISTINCT CASE WHEN d2.date IS NULL THEN d1.inviter_id END), NULL) AS curn_inviter_ids,
        SUM(CASE WHEN d1.date IS NULL THEN 1 END) AS new_inviter_count,
        array_remove(array_agg(DISTINCT CASE WHEN d1.date IS NULL THEN d2.inviter_id END), NULL) AS new_inviter_ids
    FROM inviters_results AS d1
    FULL OUTER JOIN inviters_results AS d2
        ON (d1.inviter_id = d2.inviter_id
            AND to_char((d1.date || '-01') :: date + '1 month' :: interval, 'YYYY-MM') = d2.date)
    GROUP BY 1
) AS t2 USING (date)
ORDER BY date;
