from processor import save_article

article = {
    "title":"PICIP Phase 5 Alert Test",
    "content":"The government announced a major investment while a crisis threatens national security.",
    "url":"https://test.local/phase5"
}

save_article(
    article,
    source_id=1
)
