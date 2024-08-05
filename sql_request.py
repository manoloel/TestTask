"""
SELECT article.id, title, article.text
FROM article LEFT JOIN comment
    ON comment.article_id = article.id
WHERE comment.article_id IS NULL
"""