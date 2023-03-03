SELECT a.owner_id,c.owner_name, count(distinct b.category_id) AS different_category_count
FROM article a
JOIN category_article_mapping b
ON a.article_id = b.article_id;
JOIN owner c
ON b.owner_id = c.owner_id
GROUP BY a.owner_id
ORDER BY different_category_count DESC