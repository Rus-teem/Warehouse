/*
  Анализ активности реферальных партнёров.
  Собирает статистику по дням: количество реферальщиков, пользователей,
  корреляцию, количество партнёров с контрактами и сумму выводов.
*/

WITH prtn AS (
    SELECT id
    FROM accounts
    WHERE registration_type_id = 1
)
SELECT
    oppp.day,
    oppp.count_prtn AS "Количество реферальщиков",
    oppp.count_user AS "Количество пользователей",
    ABS(oppp.count_prtn - AVG(oppp.count_prtn)) AS lol,
    corr(oppp.count_prtn, oppp.count_user) AS lol2,
    count_user / oppp.count_prtn AS "Количество пользователей на одного партнера",
    love.withcontr AS "Количество реф с контрактом",
    love.withcontr / oppp.count_prtn AS "Доля с контрактами",
    amount_prtn.coun_prtn_money AS "Количество партнеров, снявших деньги",
    ABS(amount_prtn.prtn_money) AS "Сумма вывода партнера"
FROM (
    SELECT
        to_char(created_at, 'YYYY-MM') AS day,
        COUNT(DISTINCT inviter_id) AS count_prtn,
        COUNT(id) AS count_user
    FROM accounts
    WHERE inviter_id IN (SELECT id FROM prtn)
      AND created_at > '2021-01-01'
    GROUP BY 1
) AS oppp
JOIN (
    SELECT
        to_char(pc.created_at, 'YYYY-MM') AS day,
        COUNT(c.account_id) AS withcontr
    FROM contractors AS pc
    JOIN contracts AS c ON (pc.id = c.contractor_id)
    WHERE c.account_id IN (SELECT id FROM prtn)
      AND pc.created_at > '2021-01-01'
    GROUP BY 1
) AS love ON (love.day = oppp.day)
JOIN (
    SELECT
        to_char(created_at, 'YYYY-MM') AS day,
        COUNT(account_id) AS coun_prtn_money,
        SUM(amount) AS prtn_money
    FROM transactions
    WHERE amount < 0
      AND type_string = 'Withdrawal'
      AND account_id IN (SELECT id FROM prtn)
      AND created_at > '2021-01-01'
    GROUP BY 1
) AS amount_prtn ON (amount_prtn.day = oppp.day)
GROUP BY
    oppp.day,
    oppp.count_prtn,
    oppp.count_user,
    love.withcontr,
    amount_prtn.coun_prtn_money,
    amount_prtn.prtn_money;
